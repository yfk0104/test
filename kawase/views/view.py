#表示用コード
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Slot
from models.model import Model
from controllers.controller import Controller
from views.Ui_Kawase import Ui_MainWindow
import models.Define as define

class View(QMainWindow):
    def __init__(self, model :Model, controller :Controller):
        super().__init__()
        self._model = model
        self._controller = controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        # UiMainViewの通貨選択通知Signalを、ViewのSlotに接続
        self._ui.currency_list.currentIndexChanged.connect(self.change_currency_list)

        # UiMainViewの開始ボタンクリック通知Signalを、ControllerのSlotに接続
        self._ui.button_start.clicked.connect(self.button_start)

        # Controllerの不正な入力値通知Signalを、ViewのSlotに接続
        self._controller.invalid_currency_list.connect(self.invalid_currency_list)

        # Modelのファイル読込み異常通知Signalを、ViewのSlotに接続
        self._model.invalid_file_load.connect(self.invalid_file_load)

    # Uiの通貨選択通知を受信
    @Slot()
    def change_currency_list(self):
        self._controller.change_currency_list(self._ui.currency_list.currentText())

    # 開始ボタン通知を受信
    @Slot()
    def button_start(self):
        judge = False
        chart = False
        interval = 0.0
        year = 0

        if self._ui.checkBox_judge.isChecked() == True:
            judge = True

        if self._ui.checkBox_chart.isChecked() == True:
            chart = True
            try:
                float(self._ui.lineEdit_interval.text())
            except ValueError:
                msg = '「チャートの間隔」には数値を入力してください。' 
                QMessageBox.information(None, "My message", msg, QMessageBox.Yes)
                return
            else:
                interval = float(self._ui.lineEdit_interval.text())

        if self._ui.lineEdit_Year.text().isdecimal() == True:
            year = int(self._ui.lineEdit_Year.text())
        else:
            msg = '「データ取得年数」には数値を入力してください。' 
            QMessageBox.information(None, "My message", msg, QMessageBox.Yes)
            return

        self._controller.button_start(judge, chart, year, interval)

        msg = self._model.CURRENT_PATH + 'に保存しました。' 
        QMessageBox.information(None, "My message", msg, QMessageBox.Yes)

    # Controllerの不正な入力値通知を受信
    @Slot()
    def invalid_currency_list(self):
        self._ui.currency_list.	setCurrentIndex(1)

    # modelのファイル読込み異常通知を受信
    @Slot()
    def invalid_file_load(self, value: str):
        msg = 'ファイルの読み込みに失敗しました。\n(' + value + ')' 
        QMessageBox.information(None, "My message", msg, QMessageBox.Yes)
