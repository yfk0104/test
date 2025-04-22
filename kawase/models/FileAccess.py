from datetime import date, datetime
from os.path import dirname, basename
import models.AbstractAccess as base
import csv

class FileAccess(base.AbstractAccess):
    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def __del__(self) -> None:
        pass

    def importData(self):
        try:
            with open(self.file_path, encoding='utf8', newline='') as f:
                try:
                    csvreader = csv.reader(f)
                    header = next(csvreader)  # 見出し行は別扱い
                    content = [[row[0], float(row[3])] for row in csvreader]
                    return content
                except:
                    return None
        except:
            return None

    def save_judge_file(self, wb):
        path = dirname(self.file_path)
        wb.save(path + '\\judge.xlsx')

    def save_chart_file(self, wb):
        path = dirname(self.file_path)
        wb.save(path + '\\chart.xlsx')

