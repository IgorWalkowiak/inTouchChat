from abc import ABC, abstractmethod


class DataReceiver(ABC):

    @abstractmethod
    def handleData(self, data) -> None:
        pass
