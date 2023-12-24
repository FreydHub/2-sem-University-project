# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainRVFpHt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from scroll_area_class import ScrollAreaClass

import icons_rc


class Ui_MainWindow(object):
    def __init__(self):
            self.verticalLayout_5 = None

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QSize(600, 400))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"/* ALL */\n"
                                 "*{\n"
                                 "	border: none;\n"
                                 "	background-color: transparent;\n"
                                 "	color: #222A35;\n"
                                 "}\n"
                                 "#label_page_name{\n"
                                 "	color: #f0f0f0;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "/* GLOBAL BACKGROUND*/\n"
                                 "#Content, #Top_Bar{\n"
                                 "	background-color: rgba(115, 166, 188, 90);\n"
                                 "}\n"
                                 "#frame_pages{\n"
                                 "	background-color: #f0f0f0;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "/* WINDOW BUTTONS */\n"
                                 "#frame_window_btns *:hover{\n"
                                 "	background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.511, y2:1, stop:0 rgba(240, 240, 240, 90), stop:1 rgba(240, 240, 240, 0));\n"
                                 "}\n"
                                 "#btn_close:hover{\n"
                                 "	background-color: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.523, y2:1, stop:0 rgba(236, 29, 0, 190), stop:1 rgba(236, 29, 0, 0));\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "/* MENU BUTTONS */\n"
                                 "#frame_top_menus *, #frame_toggle {\n"
                                 "	background-color: rgba(240, 240, 240, 0);\n"
                                 "	border-radius: 0px;\n"
                                 "}\n"
                                 "#frame_top_menus *:hover, #frame_toggle:hover {\n"
                                 "	background-color: rgba(240, 240, 240, 90);\n"
                                 "	border-radius: 0px;\n"
                                 "}\n"
                                 "#btn_exit_in_menu:hover{\n"
                                 "	ba"
                                 "ckground-color: rgba(236, 29, 0, 190);\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "/* CHAT*/\n"
                                 "#frame_chat_input{\n"
                                 "	border-top: 1px solid  rgba(115, 166, 188, 90);\n"
                                 "}\n"
                                 "#btn_send:enabled{\n"
                                 "	background-color: #a2e2e9;\n"
                                 "	border-radius: 17px;\n"
                                 "	border-top-right-radius: 7px;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "/* SETTINGS */\n"
                                 "#frame_line_api *{\n"
                                 "	border: 1px solid rgba(115, 166, 188, 90);\n"
                                 "}\n"
                                 "#separator{\n"
                                 "	background-color: rgba(115, 166, 188, 90);\n"
                                 "}\n"
                                 "#btn_update:enabled{\n"
                                 "	background-color: #a2e2e9;\n"
                                 "	border-radius: 17px;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "/* COMBOBOX AREA */\n"
                                 "QComboBox{\n"
                                 "	background-color: #f0f0f0;\n"
                                 "	border: 1px solid rgba(115, 166, 188, 90);\n"
                                 "}\n"
                                 "QComboBox:down-arrow {\n"
                                 "	border: none; \n"
                                 "	background: transparent;\n"
                                 "}\n"
                                 "QComboBox:drop-down {\n"
                                 "	width:40px;\n"
                                 "	height:50px;\n"
                                 "	border: none;\n"
                                 "	subcontrol-position: right center;\n"
                                 "	subcontrol-origin: padding;\n"
                                 "}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(50, 50))
        self.frame_toggle.setStyleSheet(u"")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_menu = QPushButton(self.frame_toggle)
        self.btn_menu.setObjectName(u"btn_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_menu.sizePolicy().hasHeightForWidth())
        self.btn_menu.setSizePolicy(sizePolicy)
        self.btn_menu.setMinimumSize(QSize(50, 40))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_menu.setFont(font)
        self.btn_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.btn_menu)

        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setStyleSheet(u"")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 0, 0, 0)
        self.label_page_name = QLabel(self.frame_top)
        self.label_page_name.setObjectName(u"label_page_name")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.label_page_name.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_page_name, 0, Qt.AlignLeft)

        self.frame_notification = QFrame(self.frame_top)
        self.frame_notification.setObjectName(u"frame_notification")
        self.frame_notification.setMinimumSize(QSize(0, 0))
        self.frame_notification.setFrameShape(QFrame.StyledPanel)
        self.frame_notification.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_notification)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_pop_up = QLabel(self.frame_notification)
        self.label_pop_up.setObjectName(u"label_pop_up")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_pop_up.sizePolicy().hasHeightForWidth())
        self.label_pop_up.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        self.label_pop_up.setFont(font2)
        self.label_pop_up.setAlignment(Qt.AlignCenter)
        self.label_pop_up.setMargin(5)

        self.verticalLayout_13.addWidget(self.label_pop_up)

        self.horizontalLayout_4.addWidget(self.frame_notification, 0, Qt.AlignHCenter | Qt.AlignTop)

        self.frame_window_btns = QFrame(self.frame_top)
        self.frame_window_btns.setObjectName(u"frame_window_btns")
        self.frame_window_btns.setStyleSheet(u"")
        self.frame_window_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_window_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_window_btns)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minus = QPushButton(self.frame_window_btns)
        self.btn_minus.setObjectName(u"btn_minus")
        self.btn_minus.setMinimumSize(QSize(40, 30))
        self.btn_minus.setMaximumSize(QSize(40, 30))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minus.setIcon(icon1)
        self.btn_minus.setIconSize(QSize(23, 23))

        self.horizontalLayout_5.addWidget(self.btn_minus)

        self.btn_resize = QPushButton(self.frame_window_btns)
        self.btn_resize.setObjectName(u"btn_resize")
        self.btn_resize.setMinimumSize(QSize(40, 30))
        self.btn_resize.setMaximumSize(QSize(40, 30))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/chevron-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_resize.setIcon(icon2)
        self.btn_resize.setIconSize(QSize(23, 23))

        self.horizontalLayout_5.addWidget(self.btn_resize)

        self.btn_close = QPushButton(self.frame_window_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(40, 30))
        self.btn_close.setMaximumSize(QSize(40, 30))
        self.btn_close.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon3)
        self.btn_close.setIconSize(QSize(23, 23))

        self.horizontalLayout_5.addWidget(self.btn_close)

        self.horizontalLayout_4.addWidget(self.frame_window_btns, 0, Qt.AlignRight | Qt.AlignTop)

        self.horizontalLayout.addWidget(self.frame_top)

        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(50, 0))
        self.frame_left_menu.setMaximumSize(QSize(50, 16777215))
        self.frame_left_menu.setStyleSheet(u"")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_top_menus.sizePolicy().hasHeightForWidth())
        self.frame_top_menus.setSizePolicy(sizePolicy2)
        self.frame_top_menus.setMinimumSize(QSize(0, 0))
        self.frame_top_menus.setStyleSheet(u"")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_page_chat = QPushButton(self.frame_top_menus)
        self.btn_page_chat.setObjectName(u"btn_page_chat")
        sizePolicy3 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_page_chat.sizePolicy().hasHeightForWidth())
        self.btn_page_chat.setSizePolicy(sizePolicy3)
        self.btn_page_chat.setMinimumSize(QSize(50, 50))
        self.btn_page_chat.setMaximumSize(QSize(50, 50))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setWeight(50)
        self.btn_page_chat.setFont(font3)
        self.btn_page_chat.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_chat.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/message-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_chat.setIcon(icon4)
        self.btn_page_chat.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.btn_page_chat)

        self.btn_page_settings = QPushButton(self.frame_top_menus)
        self.btn_page_settings.setObjectName(u"btn_page_settings")
        sizePolicy3.setHeightForWidth(self.btn_page_settings.sizePolicy().hasHeightForWidth())
        self.btn_page_settings.setSizePolicy(sizePolicy3)
        self.btn_page_settings.setMinimumSize(QSize(50, 50))
        self.btn_page_settings.setMaximumSize(QSize(50, 50))
        self.btn_page_settings.setFont(font3)
        self.btn_page_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_settings.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_settings.setIcon(icon5)
        self.btn_page_settings.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.btn_page_settings)

        self.btn_page_info = QPushButton(self.frame_top_menus)
        self.btn_page_info.setObjectName(u"btn_page_info")
        sizePolicy3.setHeightForWidth(self.btn_page_info.sizePolicy().hasHeightForWidth())
        self.btn_page_info.setSizePolicy(sizePolicy3)
        self.btn_page_info.setMinimumSize(QSize(50, 50))
        self.btn_page_info.setMaximumSize(QSize(50, 50))
        self.btn_page_info.setFont(font3)
        self.btn_page_info.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page_info.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_info.setIcon(icon6)
        self.btn_page_info.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.btn_page_info)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.btn_exit_in_menu = QPushButton(self.frame_top_menus)
        self.btn_exit_in_menu.setObjectName(u"btn_exit_in_menu")
        self.btn_exit_in_menu.setMinimumSize(QSize(50, 50))
        self.btn_exit_in_menu.setMaximumSize(QSize(50, 50))
        self.btn_exit_in_menu.setFont(font2)
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exit_in_menu.setIcon(icon7)
        self.btn_exit_in_menu.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.btn_exit_in_menu, 0, Qt.AlignHCenter | Qt.AlignBottom)

        self.verticalLayout_3.addWidget(self.frame_top_menus)

        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setStyleSheet(u"")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.page_chat = QWidget()
        self.page_chat.setObjectName(u"page_chat")
        self.page_chat.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.page_chat)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_list_chat = QFrame(self.page_chat)
        self.frame_list_chat.setObjectName(u"frame_list_chat")
        self.frame_list_chat.setFrameShape(QFrame.StyledPanel)
        self.frame_list_chat.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_list_chat)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = ScrollAreaClass(self.frame_list_chat)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"/* VERTICAL SCROLLBAR */\n"
                                      "QScrollBar:vertical {\n"
                                      "	border: none;\n"
                                      "    background: rgba(115, 166, 188, 70);\n"
                                      "    width: 12px;\n"
                                      "	border-radius: 4px;\n"
                                      "	margin: 2 2 2 2;\n"
                                      " }\n"
                                      "\n"
                                      "\n"
                                      "/*  HANDLE BAR VERTICAL */\n"
                                      "QScrollBar::handle:vertical {	\n"
                                      "    background: rgba(115, 166, 188, 90);\n"
                                      "	min-height: 70px;\n"
                                      "	border-radius: 4px;\n"
                                      "}\n"
                                      "QScrollBar::handle:vertical:hover{	\n"
                                      "    background: rgba(115, 166, 188, 170);\n"
                                      "	min-height: 70px;\n"
                                      "	border-radius: 4px;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "/* BTN TOP - SCROLLBAR */\n"
                                      "QScrollBar::sub-line:vertical {\n"
                                      "	border: none;\n"
                                      "	background-color: none;\n"
                                      "	height: 0px;\n"
                                      "}\n"
                                      "\n"
                                      "/* BTN BOTTOM - SCROLLBAR */\n"
                                      "QScrollBar::add-line:vertical {\n"
                                      "	border: none;\n"
                                      "	background-color: none;\n"
                                      "	height: 0px;\n"
                                      "}\n"
                                      "\n"
                                      "/* RESET ARROW */\n"
                                      "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                      "	background: none;\n"
                                      "	height: 0px;\n"
                                      "}\n"
                                      "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                      "	background:"
                                      " none;\n"
                                      "	height: 0px;\n"
                                      "}\n"
                                      "")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 550, 305))
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_16.setSpacing(12)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_8.addWidget(self.scrollArea)

        self.verticalLayout_7.addWidget(self.frame_list_chat)

        self.frame_chat_input = QFrame(self.page_chat)
        self.frame_chat_input.setObjectName(u"frame_chat_input")
        self.frame_chat_input.setStyleSheet(u"")
        self.frame_chat_input.setFrameShape(QFrame.StyledPanel)
        self.frame_chat_input.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_chat_input)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 0)
        self.line_chat = QLineEdit(self.frame_chat_input)
        self.line_chat.setObjectName(u"line_chat")
        self.line_chat.setMinimumSize(QSize(0, 30))
        self.line_chat.setMaximumSize(QSize(16777215, 30))
        self.line_chat.setFont(font2)
        self.line_chat.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.line_chat)

        self.btn_send = QPushButton(self.frame_chat_input)
        self.btn_send.setObjectName(u"btn_send")
        self.btn_send.setEnabled(False)
        self.btn_send.setMinimumSize(QSize(35, 35))
        self.btn_send.setMaximumSize(QSize(35, 35))
        self.btn_send.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_send.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/send.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_send.setIcon(icon8)
        self.btn_send.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.btn_send)

        self.verticalLayout_7.addWidget(self.frame_chat_input)

        self.stackedWidget.addWidget(self.page_chat)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.page_settings.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.page_settings)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_settings = QFrame(self.page_settings)
        self.frame_settings.setObjectName(u"frame_settings")
        self.frame_settings.setFrameShape(QFrame.StyledPanel)
        self.frame_settings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_settings)
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(9, 9, 9, 0)
        self.label_main_settings = QLabel(self.frame_settings)
        self.label_main_settings.setObjectName(u"label_main_settings")
        self.label_main_settings.setFont(font2)

        self.verticalLayout_14.addWidget(self.label_main_settings)

        self.frame_silent_mode = QFrame(self.frame_settings)
        self.frame_silent_mode.setObjectName(u"frame_silent_mode")
        self.frame_silent_mode.setFrameShape(QFrame.StyledPanel)
        self.frame_silent_mode.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_silent_mode)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_silent_mode = QLabel(self.frame_silent_mode)
        self.label_silent_mode.setObjectName(u"label_silent_mode")
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setWeight(50)
        self.label_silent_mode.setFont(font4)

        self.horizontalLayout_6.addWidget(self.label_silent_mode)

        self.comboBox = QComboBox(self.frame_silent_mode)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy4)
        self.comboBox.setMinimumSize(QSize(0, 25))
        self.comboBox.setMaximumSize(QSize(250, 16777215))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(10)
        self.comboBox.setFont(font5)
        self.comboBox.setMaxVisibleItems(30)
        self.comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_6.addWidget(self.comboBox, 0, Qt.AlignRight)

        self.verticalLayout_14.addWidget(self.frame_silent_mode)

        self.separator = QFrame(self.frame_settings)
        self.separator.setObjectName(u"separator")
        self.separator.setMinimumSize(QSize(0, 1))
        self.separator.setMaximumSize(QSize(16777215, 1))
        self.separator.setFrameShape(QFrame.HLine)
        self.separator.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.separator)

        self.label_connection_settings = QLabel(self.frame_settings)
        self.label_connection_settings.setObjectName(u"label_connection_settings")
        self.label_connection_settings.setFont(font2)

        self.verticalLayout_14.addWidget(self.label_connection_settings)

        self.frame_keys = QFrame(self.frame_settings)
        self.frame_keys.setObjectName(u"frame_keys")
        self.frame_keys.setFrameShape(QFrame.StyledPanel)
        self.frame_keys.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_keys)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_api = QFrame(self.frame_keys)
        self.frame_api.setObjectName(u"frame_api")
        self.frame_api.setFrameShape(QFrame.StyledPanel)
        self.frame_api.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_api)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_label_api = QFrame(self.frame_api)
        self.frame_label_api.setObjectName(u"frame_label_api")
        self.frame_label_api.setFrameShape(QFrame.StyledPanel)
        self.frame_label_api.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_label_api)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_api = QLabel(self.frame_label_api)
        self.label_api.setObjectName(u"label_api")
        self.label_api.setFont(font5)

        self.verticalLayout_12.addWidget(self.label_api, 0, Qt.AlignLeft)

        self.label_secret_api = QLabel(self.frame_label_api)
        self.label_secret_api.setObjectName(u"label_secret_api")
        self.label_secret_api.setFont(font5)

        self.verticalLayout_12.addWidget(self.label_secret_api)

        self.horizontalLayout_7.addWidget(self.frame_label_api)

        self.frame_line_api = QFrame(self.frame_api)
        self.frame_line_api.setObjectName(u"frame_line_api")
        self.frame_line_api.setFrameShape(QFrame.StyledPanel)
        self.frame_line_api.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_line_api)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.line_api = QLineEdit(self.frame_line_api)
        self.line_api.setObjectName(u"line_api")
        self.line_api.setMinimumSize(QSize(0, 25))
        self.line_api.setMaximumSize(QSize(16777215, 25))
        self.line_api.setFont(font5)

        self.verticalLayout_11.addWidget(self.line_api)

        self.line_secret_api = QLineEdit(self.frame_line_api)
        self.line_secret_api.setObjectName(u"line_secret_api")
        self.line_secret_api.setMinimumSize(QSize(0, 25))
        self.line_secret_api.setMaximumSize(QSize(16777215, 25))
        self.line_secret_api.setFont(font5)

        self.verticalLayout_11.addWidget(self.line_secret_api)

        self.horizontalLayout_7.addWidget(self.frame_line_api)

        self.verticalLayout_10.addWidget(self.frame_api, 0, Qt.AlignTop)

        self.frame_update = QFrame(self.frame_keys)
        self.frame_update.setObjectName(u"frame_update")
        self.frame_update.setFrameShape(QFrame.StyledPanel)
        self.frame_update.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_update)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_update = QPushButton(self.frame_update)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setMinimumSize(QSize(145, 35))
        self.btn_update.setMaximumSize(QSize(145, 35))
        self.btn_update.setFont(font5)
        self.btn_update.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_update.setIcon(icon9)
        self.btn_update.setIconSize(QSize(25, 25))

        self.horizontalLayout_9.addWidget(self.btn_update)

        self.verticalLayout_10.addWidget(self.frame_update, 0, Qt.AlignRight)

        self.verticalLayout_14.addWidget(self.frame_keys)

        self.verticalLayout_6.addWidget(self.frame_settings, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.page_settings)
        self.page_info = QWidget()
        self.page_info.setObjectName(u"page_info")
        self.verticalLayout_5 = QVBoxLayout(self.page_info)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_info = QFrame(self.page_info)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setFrameShape(QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_info)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, -1, -1, 0)
        self.text_info = QTextBrowser(self.frame_info)
        self.text_info.setObjectName(u"text_info")
        self.text_info.setFont(font2)
        self.text_info.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.text_info.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_15.addWidget(self.text_info)

        self.verticalLayout_5.addWidget(self.frame_info)

        self.stackedWidget.addWidget(self.page_info)

        self.verticalLayout_9.addWidget(self.stackedWidget)

        self.frame_resize_grip = QFrame(self.frame_pages)
        self.frame_resize_grip.setObjectName(u"frame_resize_grip")
        self.frame_resize_grip.setMinimumSize(QSize(9, 9))
        self.frame_resize_grip.setMaximumSize(QSize(9, 9))
        self.frame_resize_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_resize_grip.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.frame_resize_grip, 0, Qt.AlignRight | Qt.AlignBottom)

        self.horizontalLayout_2.addWidget(self.frame_pages)

        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(-1)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_menu.setText("")
        self.label_page_name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_pop_up.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_minus.setText("")
        self.btn_resize.setText("")
        self.btn_close.setText("")
        self.btn_page_chat.setText("")
        self.btn_page_settings.setText("")
        self.btn_page_info.setText("")
        self.btn_exit_in_menu.setText("")
        self.line_chat.setText("")
        self.line_chat.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                     u"\u041d\u0430\u043f\u0438\u0448\u0438\u0442\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 . . .",
                                                                     None))
        # if QT_CONFIG(tooltip)
        self.btn_send.setToolTip(
            QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        # endif // QT_CONFIG(tooltip)
        self.btn_send.setText("")
        self.label_main_settings.setText(
            QCoreApplication.translate("MainWindow", u"\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435", None))
        self.label_silent_mode.setText(QCoreApplication.translate("MainWindow",
                                                                  u"  \u0413\u043e\u043b\u043e\u0441 \u0430\u0441\u0441\u0438\u0441\u0442\u0435\u043d\u0442\u0430 (\u0433\u043e\u043b\u043e\u0441 : \u043c\u043e\u0434\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440)",
                                                                  None))
        self.comboBox.setCurrentText("")
        self.comboBox.setPlaceholderText("")
        self.label_connection_settings.setText(QCoreApplication.translate("MainWindow",
                                                                          u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435",
                                                                          None))
        self.label_api.setText(QCoreApplication.translate("MainWindow",
                                                          u"  \u041e\u0442\u043a\u0440\u044b\u0442\u044b\u0439 API \u043a\u043b\u044e\u0447",
                                                          None))
        self.label_secret_api.setText(QCoreApplication.translate("MainWindow",
                                                                 u"  \u0421\u0435\u043a\u0440\u0435\u0442\u043d\u044b\u0439 API \u043a\u043b\u044e\u0447",
                                                                 None))
        self.btn_update.setText(QCoreApplication.translate("MainWindow",
                                                           u" \u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u043a\u043b\u044e\u0447\u0438",
                                                           None))
        self.text_info.setHtml(QCoreApplication.translate("MainWindow",
                                                          u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                          "p, li { white-space: pre-wrap; }\n"
                                                          "</style></head><body style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                          "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Зима Григорий - дизайнер ( Blender )<br>"
                                                          "Таушанкова Лиза - дизайнер<br>"
                                                          "Коршунов Егор - backend<br>"
                                                          "Шарапов Галим - backend</span></p>\n", None))

        self.text_info.setPlaceholderText("")
    # retranslateUi
