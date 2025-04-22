from PySide6.QtCore import QObject, Signal
import models.DataManager as mng

class Model(QObject):
    CURRENT_PATH = 'D:\\python\\data\\'
    FILE_NAME = '-DAY.csv'

    def __init__(self):
        super().__init__()
        self._currency_list = 'USD/JPY'

    # Viewへファイル読込み異常を通知するSignal
    invalid_file_load = Signal(str)

    @property
    def currency_list(self):
        return self._currency_list

    @currency_list.setter
    def currency_list(self, value: str):
        self._currency_list = value

    def _make_judge(self, year):
        file_path = self.CURRENT_PATH + self.currency_list.replace('/', '') + self.FILE_NAME

        manager = mng.DataManager(self.currency_list, file_path)
        #if manager.LoadFile() == True:
        if manager.LoadWeb(year) == True:
            manager.Judge()
        else:
            self.invalid_file_load.emit(file_path)

    def _make_chart(self, year, interval):
        file_path = self.CURRENT_PATH + self.currency_list.replace('/', '') + self.FILE_NAME

        manager = mng.DataManager(self.currency_list, file_path)
        if manager.LoadWeb(year) == True:
            manager.MakeSecretChart(interval)
        else:
            self.invalid_file_load.emit(file_path)

    def button_start(self, judge, chart, year, interval):
        if judge == True:
            self._make_judge(year)

        if chart == True:
            self._make_chart(year, interval)

