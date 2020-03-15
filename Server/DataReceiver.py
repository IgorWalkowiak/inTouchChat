from abc import ABC, abstractmethod


class DataReceiver(ABC):

    @abstractmethod
    def handleData(data) -> None:
        pass
