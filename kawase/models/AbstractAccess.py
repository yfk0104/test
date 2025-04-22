# 処理対象となるデータをインポートするクラス

from abc import ABC, ABCMeta, abstractmethod

class AbstractAccess(metaclass=ABCMeta):

    def __init__(self) -> None:
        pass

    def __del__(self) -> None:
        pass

    @abstractmethod
    def importData() -> None:
        pass
