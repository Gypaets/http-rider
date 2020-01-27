# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/base_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1077, 723)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.lst_http_requests = ApiCallsListView(self.splitter)
        self.lst_http_requests.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.lst_http_requests.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.lst_http_requests.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.lst_http_requests.setObjectName("lst_http_requests")
        self.frame_request_response = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_request_response.sizePolicy().hasHeightForWidth())
        self.frame_request_response.setSizePolicy(sizePolicy)
        self.frame_request_response.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_request_response.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_request_response.setLineWidth(1)
        self.frame_request_response.setObjectName("frame_request_response")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_request_response)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cmb_http_method = QtWidgets.QComboBox(self.frame_request_response)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cmb_http_method.setFont(font)
        self.cmb_http_method.setObjectName("cmb_http_method")
        self.cmb_http_method.addItem("")
        self.cmb_http_method.addItem("")
        self.cmb_http_method.addItem("")
        self.cmb_http_method.addItem("")
        self.cmb_http_method.addItem("")
        self.cmb_http_method.addItem("")
        self.cmb_http_method.addItem("")
        self.horizontalLayout.addWidget(self.cmb_http_method)
        self.txt_http_url = CompletionLineEdit(self.frame_request_response)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.txt_http_url.setFont(font)
        self.txt_http_url.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txt_http_url.setObjectName("txt_http_url")
        self.horizontalLayout.addWidget(self.txt_http_url)
        self.btn_send_request = QtWidgets.QPushButton(self.frame_request_response)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_send_request.setFont(font)
        self.btn_send_request.setObjectName("btn_send_request")
        self.horizontalLayout.addWidget(self.btn_send_request)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.frame_request_response)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_description = QtWidgets.QWidget()
        self.tab_description.setObjectName("tab_description")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_description)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txt_api_title = QtWidgets.QLineEdit(self.tab_description)
        self.txt_api_title.setObjectName("txt_api_title")
        self.verticalLayout_2.addWidget(self.txt_api_title)
        self.txt_api_description = QtWidgets.QPlainTextEdit(self.tab_description)
        self.txt_api_description.setObjectName("txt_api_description")
        self.verticalLayout_2.addWidget(self.txt_api_description)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab_description, "")
        self.tab_headers = QtWidgets.QWidget()
        self.tab_headers.setObjectName("tab_headers")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_headers)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lst_request_headers = QtWidgets.QListWidget(self.tab_headers)
        self.lst_request_headers.setObjectName("lst_request_headers")
        self.horizontalLayout_3.addWidget(self.lst_request_headers)
        self.tabWidget.addTab(self.tab_headers, "")
        self.tab_queryparams = QtWidgets.QWidget()
        self.tab_queryparams.setObjectName("tab_queryparams")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_queryparams)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lst_request_params = QtWidgets.QListWidget(self.tab_queryparams)
        self.lst_request_params.setObjectName("lst_request_params")
        self.horizontalLayout_5.addWidget(self.lst_request_params)
        self.tabWidget.addTab(self.tab_queryparams, "")
        self.tab_formparams = QtWidgets.QWidget()
        self.tab_formparams.setObjectName("tab_formparams")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.tab_formparams)
        self.horizontalLayout_14.setContentsMargins(12, -1, 12, 12)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.lst_form_params = QtWidgets.QListWidget(self.tab_formparams)
        self.lst_form_params.setObjectName("lst_form_params")
        self.horizontalLayout_14.addWidget(self.lst_form_params)
        self.tabWidget.addTab(self.tab_formparams, "")
        self.tab_request_body = QtWidgets.QWidget()
        self.tab_request_body.setObjectName("tab_request_body")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_request_body)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.txt_request_body = CompletionPlainTextEdit(self.tab_request_body)
        self.txt_request_body.setObjectName("txt_request_body")
        self.verticalLayout_4.addWidget(self.txt_request_body)
        self.tabWidget.addTab(self.tab_request_body, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.chk_mock_response_enabled = QtWidgets.QCheckBox(self.tab_7)
        self.chk_mock_response_enabled.setObjectName("chk_mock_response_enabled")
        self.horizontalLayout_16.addWidget(self.chk_mock_response_enabled)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem)
        self.txt_mocked_response_code = QtWidgets.QLineEdit(self.tab_7)
        self.txt_mocked_response_code.setText("")
        self.txt_mocked_response_code.setObjectName("txt_mocked_response_code")
        self.horizontalLayout_16.addWidget(self.txt_mocked_response_code)
        self.verticalLayout_6.addLayout(self.horizontalLayout_16)
        self.lst_mocked_response_headers = QtWidgets.QListWidget(self.tab_7)
        self.lst_mocked_response_headers.setObjectName("lst_mocked_response_headers")
        self.verticalLayout_6.addWidget(self.lst_mocked_response_headers)
        self.txt_mocked_response_body = CompletionPlainTextEdit(self.tab_7)
        self.txt_mocked_response_body.setPlaceholderText("")
        self.txt_mocked_response_body.setObjectName("txt_mocked_response_body")
        self.verticalLayout_6.addWidget(self.txt_mocked_response_body)
        self.tabWidget.addTab(self.tab_7, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.tags_layout = QtWidgets.QHBoxLayout()
        self.tags_layout.setObjectName("tags_layout")
        self.btn_add_tag = QtWidgets.QToolButton(self.frame_request_response)
        self.btn_add_tag.setObjectName("btn_add_tag")
        self.tags_layout.addWidget(self.btn_add_tag)
        self.verticalLayout.addLayout(self.tags_layout)
        self.line = QtWidgets.QFrame(self.frame_request_response)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_request_response)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.btn_open_assertions_dialog = QtWidgets.QToolButton(self.frame_request_response)
        self.btn_open_assertions_dialog.setObjectName("btn_open_assertions_dialog")
        self.horizontalLayout_4.addWidget(self.btn_open_assertions_dialog)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.list_assertion_results = QtWidgets.QListWidget(self.frame_request_response)
        self.list_assertion_results.setObjectName("list_assertion_results")
        self.verticalLayout.addWidget(self.list_assertion_results)
        self.frame_exchange = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_exchange.sizePolicy().hasHeightForWidth())
        self.frame_exchange.setSizePolicy(sizePolicy)
        self.frame_exchange.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_exchange.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_exchange.setObjectName("frame_exchange")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_exchange)
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lbl_request_time = QtWidgets.QLabel(self.frame_exchange)
        self.lbl_request_time.setObjectName("lbl_request_time")
        self.horizontalLayout_6.addWidget(self.lbl_request_time)
        self.btn_share_preview = QtWidgets.QToolButton(self.frame_exchange)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/share-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btn_share_preview.setIcon(icon)
        self.btn_share_preview.setObjectName("btn_share_preview")
        self.horizontalLayout_6.addWidget(self.btn_share_preview)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.tabWidget_3 = QtWidgets.QTabWidget(self.frame_exchange)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab_8)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.txt_raw_request = QtWidgets.QPlainTextEdit(self.tab_8)
        self.txt_raw_request.setReadOnly(True)
        self.txt_raw_request.setObjectName("txt_raw_request")
        self.horizontalLayout_7.addWidget(self.txt_raw_request)
        self.tabWidget_3.addTab(self.tab_8, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.tbl_exchange_request_headers = QtWidgets.QTreeWidget(self.tab)
        self.tbl_exchange_request_headers.setObjectName("tbl_exchange_request_headers")
        self.tbl_exchange_request_headers.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        self.tbl_exchange_request_headers.headerItem().setTextAlignment(1, QtCore.Qt.AlignCenter)
        self.horizontalLayout_12.addWidget(self.tbl_exchange_request_headers)
        self.tabWidget_3.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.tbl_exchange_request_params = QtWidgets.QTreeWidget(self.tab_2)
        self.tbl_exchange_request_params.setObjectName("tbl_exchange_request_params")
        self.tbl_exchange_request_params.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        self.tbl_exchange_request_params.headerItem().setTextAlignment(1, QtCore.Qt.AlignCenter)
        self.horizontalLayout_13.addWidget(self.tbl_exchange_request_params)
        self.tabWidget_3.addTab(self.tab_2, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.tab_6)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.tbl_exchange_form_params = QtWidgets.QTreeWidget(self.tab_6)
        self.tbl_exchange_form_params.setObjectName("tbl_exchange_form_params")
        self.tbl_exchange_form_params.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        self.tbl_exchange_form_params.headerItem().setTextAlignment(1, QtCore.Qt.AlignCenter)
        self.horizontalLayout_15.addWidget(self.tbl_exchange_form_params)
        self.tabWidget_3.addTab(self.tab_6, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.txt_exchange_request_body = QtWidgets.QTextEdit(self.tab_3)
        self.txt_exchange_request_body.setAcceptDrops(False)
        self.txt_exchange_request_body.setReadOnly(True)
        self.txt_exchange_request_body.setObjectName("txt_exchange_request_body")
        self.horizontalLayout_11.addWidget(self.txt_exchange_request_body)
        self.tabWidget_3.addTab(self.tab_3, "")
        self.verticalLayout_5.addWidget(self.tabWidget_3)
        self.tabWidget_4 = QtWidgets.QTabWidget(self.frame_exchange)
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.tab_9)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.txt_raw_response = QtWidgets.QPlainTextEdit(self.tab_9)
        self.txt_raw_response.setReadOnly(True)
        self.txt_raw_response.setObjectName("txt_raw_response")
        self.horizontalLayout_18.addWidget(self.txt_raw_response)
        self.tabWidget_4.addTab(self.tab_9, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.tbl_response_headers = QtWidgets.QTreeWidget(self.tab_4)
        self.tbl_response_headers.setObjectName("tbl_response_headers")
        self.tbl_response_headers.headerItem().setTextAlignment(0, QtCore.Qt.AlignCenter)
        self.tbl_response_headers.headerItem().setTextAlignment(1, QtCore.Qt.AlignCenter)
        self.horizontalLayout_10.addWidget(self.tbl_response_headers)
        self.tabWidget_4.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.txt_response_body = QtWidgets.QTextEdit(self.tab_5)
        self.txt_response_body.setAcceptDrops(False)
        self.txt_response_body.setReadOnly(True)
        self.txt_response_body.setObjectName("txt_response_body")
        self.horizontalLayout_9.addWidget(self.txt_response_body)
        self.tabWidget_4.addTab(self.tab_5, "")
        self.verticalLayout_5.addWidget(self.tabWidget_4)
        self.horizontalLayout_2.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "::::"))
        self.cmb_http_method.setItemText(0, _translate("MainWindow", "GET"))
        self.cmb_http_method.setItemText(1, _translate("MainWindow", "POST"))
        self.cmb_http_method.setItemText(2, _translate("MainWindow", "PATCH"))
        self.cmb_http_method.setItemText(3, _translate("MainWindow", "PUT"))
        self.cmb_http_method.setItemText(4, _translate("MainWindow", "DELETE"))
        self.cmb_http_method.setItemText(5, _translate("MainWindow", "OPTIONS"))
        self.cmb_http_method.setItemText(6, _translate("MainWindow", "HEAD"))
        self.txt_http_url.setText(_translate("MainWindow", "https://httpbin.org/get"))
        self.btn_send_request.setText(_translate("MainWindow", "Send"))
        self.txt_api_title.setPlaceholderText(_translate("MainWindow", "Untitled request"))
        self.txt_api_description.setPlaceholderText(_translate("MainWindow", "Request description ..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_description), _translate("MainWindow", "Description"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_headers), _translate("MainWindow", "Headers"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_queryparams), _translate("MainWindow", "Query Params"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_formparams), _translate("MainWindow", "Form Params"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_request_body), _translate("MainWindow", "Request Body"))
        self.chk_mock_response_enabled.setText(_translate("MainWindow", "Enabled"))
        self.txt_mocked_response_code.setPlaceholderText(_translate("MainWindow", "200"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Mocked Response"))
        self.btn_add_tag.setText(_translate("MainWindow", "+"))
        self.label.setText(_translate("MainWindow", "Assertions"))
        self.btn_open_assertions_dialog.setText(_translate("MainWindow", "Setup"))
        self.lbl_request_time.setText(_translate("MainWindow", "request time"))
        self.btn_share_preview.setText(_translate("MainWindow", "..."))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), _translate("MainWindow", "Raw"))
        self.tbl_exchange_request_headers.headerItem().setText(0, _translate("MainWindow", "Name"))
        self.tbl_exchange_request_headers.headerItem().setText(1, _translate("MainWindow", "Value"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab), _translate("MainWindow", "Headers"))
        self.tbl_exchange_request_params.headerItem().setText(0, _translate("MainWindow", "Name"))
        self.tbl_exchange_request_params.headerItem().setText(1, _translate("MainWindow", "Value"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_2), _translate("MainWindow", "Params"))
        self.tbl_exchange_form_params.headerItem().setText(0, _translate("MainWindow", "Name"))
        self.tbl_exchange_form_params.headerItem().setText(1, _translate("MainWindow", "Value"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), _translate("MainWindow", "Form"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), _translate("MainWindow", "Body"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_9), _translate("MainWindow", "Raw"))
        self.tbl_response_headers.headerItem().setText(0, _translate("MainWindow", "Name"))
        self.tbl_response_headers.headerItem().setText(1, _translate("MainWindow", "Value"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_4), _translate("MainWindow", "Headers"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_5), _translate("MainWindow", "Body"))
from ..widgets.api_calls_list_view import ApiCallsListView
from ..widgets.completion_line_edit import CompletionLineEdit
from ..widgets.completion_plain_text import CompletionPlainTextEdit
