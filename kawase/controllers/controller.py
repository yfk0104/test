from PySide6.QtCore import QObject, Signal, Slot
from models.model import Model

class Controller(QObject):
    # Viewへ入力値が不正であることを通知するSignal
    invalid_currency_list = Signal()

    def __init__(self, model :Model):
        super().__init__()
        self._model = model

    def change_currency_list(self, value: str):
        if len(value) != 0:
            self._model.currency_list = value
        else:
            self._model.currency_list = 'USD/JPY'
            self.invalid_currency_list.emit()

    # 開始ボタンクリック時に実行
    @Slot()
    def button_start(self, judge, chart, year, interval):
        self._model.button_start(judge, chart, year, interval)
