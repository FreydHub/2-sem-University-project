import sys

from BackEnd import json_reader
from ui_main import Ui_MainWindow

from scroll_area_class import WrapLabel
from qt_window_transparency import WindowEffect
from BackEnd.synth_recog import SynthRecognition

from PySide2 import QtWidgets
from PySide2.QtGui import QIcon, QColor
from PySide2.QtWidgets import QMainWindow, QSizeGrip, QApplication
from PySide2.QtCore import QThread, Qt, QPropertyAnimation, QEasingCurve, QTimer


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.clickPosition = None
        self.animation = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.thread_vosk = QThread()
        self.SynthRecognition_obj = SynthRecognition()
        self.SynthRecognition_obj.send_text_signal.connect(self.add_message)
        self.thread_vosk.started.connect(self.SynthRecognition_obj.run)
        self.SynthRecognition_obj.moveToThread(self.thread_vosk)
        self.thread_vosk.start()

        self.ui.label_page_name.setText('')
        self.ui.scrollArea.verticalScrollBar().rangeChanged.connect(
            lambda: self.ui.scrollArea.verticalScrollBar().setValue(self.ui.scrollArea.verticalScrollBar().maximum()))
        self.ui.scrollArea.setWidgetResizable(True)
        self.ui.verticalLayout_16.addStretch()
        self.ui.scrollArea.verticalScrollBar().setValue(self.ui.scrollArea.verticalScrollBar().maximum())
        self.ui.scrollArea.horizontalScrollBar().setValue(self.ui.scrollArea.horizontalScrollBar().maximum())
        self.ui.label_page_name.setText('Ксю')
        self.ui.line_api.setText(self.SynthRecognition_obj.open_api_key)
        self.ui.line_secret_api.setText(self.SynthRecognition_obj.secret_api_key)

        self.window_effect = WindowEffect()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.window_effect.setAeroEffect(int(self.winId()))
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(10)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(37, 37, 37))
        self.setGraphicsEffect(self.shadow)

        self.setWindowIcon(QIcon(':/icons/icons/icon.ico'))
        self.setWindowTitle('Ксю')

        self.ui.btn_minus.clicked.connect(lambda: self.showMinimized())
        self.ui.btn_close.clicked.connect(lambda: self.close())
        self.ui.btn_exit_in_menu.clicked.connect(lambda: self.close())
        self.ui.btn_resize.clicked.connect(lambda: self.restore_or_maximize_window())
        QSizeGrip(self.ui.frame_resize_grip)

        self.ui.btn_menu.clicked.connect(lambda: self.toggle_menu(50, True))

        self.ui.btn_page_chat.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_chat))
        self.ui.btn_page_chat.clicked.connect(lambda: self.toggle_menu(50, True))
        self.ui.btn_page_chat.clicked.connect(lambda: self.ui.label_page_name.setText('Ксю'))
        self.ui.btn_page_chat.clicked.connect(lambda: self.ui.frame_top_menus.setStyleSheet('''
                                                #frame_top_menus *{background-color: transparent;}
                                                #frame_top_menus *:hover{background-color: rgba(240, 240, 240, 90);}
                                                #btn_page_chat{background-color: rgba(240, 240, 240, 90);}'''))

        self.ui.btn_page_settings.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings))
        self.ui.btn_page_settings.clicked.connect(lambda: self.toggle_menu(50, True))
        self.ui.btn_page_settings.clicked.connect(lambda: self.ui.label_page_name.setText('Настройки'))
        self.ui.btn_update.clicked.connect(lambda: self.refresh_api())
        self.ui.comboBox.activated[str].connect(lambda: self.change_voice())
        self.ui.btn_page_settings.clicked.connect(lambda: self.ui.frame_top_menus.setStyleSheet('''
                                                    #frame_top_menus *{background-color: transparent;}
                                                    #frame_top_menus *:hover{background-color: rgba(240, 240, 240, 90);}
                                                    #btn_page_settings{background-color: rgba(240, 240, 240, 90);}'''))

        self.ui.btn_page_info.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_info))
        self.ui.btn_page_info.clicked.connect(lambda: self.toggle_menu(50, True))
        self.ui.btn_page_info.clicked.connect(lambda: self.ui.label_page_name.setText('О нас'))
        self.ui.btn_page_info.clicked.connect(lambda: self.ui.frame_top_menus.setStyleSheet('''
                                                    #frame_top_menus *{background-color: transparent;}
                                                    #frame_top_menus *:hover{background-color: rgba(240, 240, 240, 90);}
                                                    #btn_page_info{background-color: rgba(240, 240, 240, 90);}'''))

        self.ui.btn_send.clicked.connect(lambda: self.correct_and_add_message())
        self.ui.btn_send.clicked.connect(lambda: self.ui.line_chat.setFocus())
        self.ui.line_chat.returnPressed.connect(lambda: self.correct_and_add_message())
        self.ui.line_chat.textChanged.connect(lambda: self.ui.btn_send.setEnabled(bool(self.ui.line_chat.text())))

        QTimer.singleShot(2000, lambda: self.check_connection(not_starter=False))

        def moveWindow(e):
            if not self.isMaximized():
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()

        self.ui.frame_top.mouseMoveEvent = moveWindow

    # Сохранение перед выходом
    def closeEvent(self, e):
        print('bye')
        self.save_before_exit()
        self.SynthRecognition_obj.stop()
        self.thread_vosk.exit()
        self.thread_vosk.wait()
        e.accept()

    # Отслеживание курсора
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    # Свернуть и развернуть окно
    def restore_or_maximize_window(self):
        if self.isMaximized():
            # self.ui.verticalLayout.setContentsMargins(5, 5, 5, 5)
            self.showNormal()
            self.ui.btn_resize.setIcon(QIcon(u':/icons/icons/chevron-up.svg'))
        else:
            self.ui.verticalLayout.setContentsMargins(0, 0, 0, 0)
            self.showMaximized()
            self.ui.btn_resize.setIcon(QIcon(u':/icons/icons/chevron-down.svg'))

    # Свернуть и развернуть меню
    def toggle_menu(self, max_width, enable):
        if enable:

            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            max_extend = max_width
            standard = 0

            # SET MAX WIDTH
            if width == 0:
                width_extended = max_extend
            else:
                width_extended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(width_extended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    # вернуть и развернуть уведомление
    def toggle_pop_up(self, max_height, btn=False, recursion=False, enable=True, warning=True, text=''):
        if enable:
            self.ui.btn_update.setEnabled(btn)
            self.ui.label_pop_up.setStyleSheet('''
                        #label_pop_up {{
                            border-bottom-right-radius: 7px;
                            border-bottom-left-radius: 7px;
                            background: {};
                            color: {};
                        }}	

                    '''.format('rgba(236, 29, 0, 190)' if warning else '#a2e2e9', 'white' if warning else '#222A35'))
            if text != '':
                self.ui.label_pop_up.setText(text)
            # GET WIDTH
            height = self.ui.frame_notification.height()
            max_extend = max_height
            standard = 0

            # SET MAX WIDTH
            if height == 0:
                height_extended = max_extend
            else:
                height_extended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_notification, b"minimumHeight")
            self.animation.setDuration(400)
            self.animation.setStartValue(height)
            self.animation.setEndValue(height_extended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
            if not recursion:
                QTimer.singleShot(3000,
                                  lambda: self.toggle_pop_up(max_height=30, btn=True, recursion=True, warning=warning))

    # Удалить пробелы в начале и в конце сообщения пользователя
    def correct_and_add_message(self):
        # Check the message before add to the label
        message = self.ui.line_chat.text()
        if not message.isspace() and message != '':
            message = " ".join(message.split())
            self.add_message(message, user_sent=True)
            self.ui.line_chat.clear()
            self.SynthRecognition_obj.user_text = message
            print('added')

    # Добавить нарисованное сообщение (QTextEdit)
    def add_message(self, text, user_sent=False):
        if text[-3:] == '#%&':
            text = text.replace(text[-3:], '')
            user_sent = True
        message = WrapLabel(text)
        message.setStyleSheet('''
            WrapLabel {{
                border-radius: 17px;
                background: #dee1e4;
                border-{}-{}-radius: 0px;
                color: #2b5865;
            }}
        '''.format(
            'bottom' if user_sent else 'top',
            'right' if user_sent else 'left')
        )
        self.ui.scrollArea.messages.append(message)
        self.ui.verticalLayout_16.addWidget(message,
                                            alignment=Qt.AlignRight if user_sent else Qt.AlignLeft)
        self.ui.scrollArea.resizeEvent(self.ui.verticalLayout_16.update())

    # Изменить текущий голос
    def change_voice(self):
        self.SynthRecognition_obj.set_voice(self.ui.comboBox.currentText())
        print(self.SynthRecognition_obj.voice)

    # Пинг
    def check_connection(self, not_starter=True):
        voice_list = self.SynthRecognition_obj.get_voices_list()
        self.ui.comboBox.clear()
        if voice_list is None:
            if not_starter:
                self.toggle_pop_up(max_height=30, text='Не удалось получить список голосов')
            return

        if voice_list[0] == 'auth error':
            if not_starter:
                self.toggle_pop_up(max_height=30, text='Ошибка авторизации')
        elif voice_list[0] == 'connection error':
            if not_starter:
                self.toggle_pop_up(max_height=30, text='Ошибка подключения')
        elif voice_list[0] == 'unknown error':
            if not_starter:
                self.toggle_pop_up(max_height=30, text='Внутренняя ошибка')
        else:
            if not_starter:
                self.toggle_pop_up(max_height=30, warning=False, text='API ключи обновлены')
                self.add_message('API ключи обновлены')
            current_voice = self.SynthRecognition_obj.voice
            for i in range(len(voice_list)):
                self.ui.comboBox.addItem(voice_list[i])
                if voice_list[i] == current_voice:
                    current_voice = i
            if type(current_voice) == int:
                self.ui.comboBox.setCurrentIndex(current_voice)
            else:
                self.SynthRecognition_obj.voice = 'alyona'
                self.ui.comboBox.setCurrentIndex(0)

    # Сохранить конфиг перед выходом
    def save_before_exit(self):
        json_reader.save_new_config(self.SynthRecognition_obj.open_api_key,
                                    self.SynthRecognition_obj.secret_api_key,
                                    self.SynthRecognition_obj.voice)

    # Обновить API в системе
    def refresh_api(self):
        if len(self.ui.line_api.text()) == 44 and len(self.ui.line_secret_api.text()) == 44:
            self.SynthRecognition_obj.update_api(self.ui.line_api.text(), self.ui.line_secret_api.text())
            self.check_connection()
        else:
            self.toggle_pop_up(max_height=30, text='Ошибка авторизации')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
