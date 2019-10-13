import attr
from pygments.lexers.testing import GherkinLexer
from typing import List

from ..core.core_settings import app_settings
from ..exporters import *
from ..model.app_data import ApiCall, HttpExchange, ApiTestCase, AssertionDataSource, ProjectInfo


def gen_tags(tags: List):
    return " ".join([f"@{t}" for t in tags])


def gen_given(api_call: ApiCall, last_exchange: HttpExchange):
    first_statement = True
    statements = []
    test_tags = gen_tags(api_call.tags)
    if test_tags:
        statements.append(f"{test_tags}")

    statements.append(f"Scenario: {api_call.title}")
    for hk, hv in last_exchange.request.headers.items():
        if first_statement:

            statements.append(f"    Given I set {hk} header to {hv}")
            first_statement = False
        else:
            statements.append(f"    And I set {hk} header to {hv}")

    request_body = last_exchange.request.request_body
    if request_body:
        if first_statement:
            statements.append(f"    Given I set body to {request_body}")
            first_statement = False
        else:
            statements.append(f"    And I set body to {request_body}")

    if not statements:
        return ""

    return "\n".join(statements)


def apickli_http_method(http_method: str):
    table = {
        "post": f"{http_method} to",
        "options": f"request {http_method} for",
    }
    return table.get(http_method.lower(), http_method)


def gen_when(project_info: ProjectInfo, api_call: ApiCall, last_exchange: HttpExchange):
    http_relative_uri = extract_uri(last_exchange.request.http_url, project_info.servers)
    method_conversion = apickli_http_method(last_exchange.request.http_method)
    statements = [
        f"    When I {method_conversion} {http_relative_uri}"
    ]
    return "\n".join(statements)


def gen_then(api_call: ApiCall, last_exchange: HttpExchange, api_test_case: ApiTestCase):
    statements = [
        f"    Then response code should be {last_exchange.response.http_status_code}"
    ]

    for a in api_test_case.assertions:
        if a.data_from == AssertionDataSource.RESPONSE_HEADER.value:
            statements.append(f"    And response header {a.selector} should {converter(a)}")

        if a.data_from == AssertionDataSource.RESPONSE_BODY.value:
            statements.append(f"    And response path {a.selector} should {converter(a)}")

    for a in api_test_case.assertions:
        if a.data_from == AssertionDataSource.RESPONSE_HEADER.value:
            statements.append(f"    And I store the value of response header {a.selector} as {a.var_name}")

        if a.data_from == AssertionDataSource.RESPONSE_BODY.value:
            statements.append(f"    And I store the value of body path {a.selector} as {a.var_name}")

    return "\n".join(statements)


def converter(assertion):
    return "exist" if assertion.expected_value == "Not Null" else f"be {assertion.expected_value}"


@attr.s
class ApickliExporter:
    name: str = "Apickli Tests"
    output_ext: str = "text"

    def export_data(self, api_calls: List[ApiCall]):
        test_file_header = """
## See https://github.com/namuan/apickli_functional_tests for starting up a new project. 

## The following feature definitions should go in tests/Functional.feature file.           

Feature: Validating API requests
    As a user, I want to validate that all the user scenarios are correct
"""
        project_info = app_settings.app_data_reader.get_or_create_project_info()

        output = [
            self.__export_api_call(project_info, api_call)
            for api_call in api_calls
        ]

        return highlight(test_file_header, GherkinLexer(), HtmlFormatter()) + "<br/>".join(output)

    def __export_api_call(self, project_info, api_call):
        last_exchange = app_settings.app_data_cache.get_last_exchange(api_call.id)
        api_test_case = app_settings.app_data_cache.get_api_test_case(api_call.id)
        doc = f"""# {api_call.title}
# 
{gen_given(api_call, last_exchange)}
{gen_when(project_info, api_call, last_exchange)}
{gen_then(api_call, last_exchange, api_test_case)}
"""
        return highlight(doc, GherkinLexer(), HtmlFormatter())


exporter = ApickliExporter()
