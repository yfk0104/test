import models.FileAccess as file
import models.WebAccess as web
import models.JudgeFile as j
import models.SecretChart as secret

class DataManager:
    def __init__(self, selected_currency, file_path) -> None:
        self._selected_currency = selected_currency
        self._file_path = file_path
        self.faccess = file.FileAccess(self._file_path)

    def __del__(self) -> None:
        pass

    def LoadFile(self):
        self.csv_data = self.faccess.importData()
        if self.csv_data == None:
            return False
        else:
            return True

    def LoadWeb(self, year):
        access = web.WebAccess(year)
        self.csv_data = access.importData(self._selected_currency)
        if self.csv_data == None:
            return False
        else:
            return True

    def Judge(self):
        judge = j.JudgeFile(self.faccess, self.csv_data, self._selected_currency)
        judge.MakeFile()

    def MakeSecretChart(self, interval):
        st = secret.SecretChart(self.faccess, self.csv_data, self._selected_currency, interval)
        st.MakeFile()
