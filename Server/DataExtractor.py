from DataReceiver import DataReceiver
from MessageID import MessageID
import ConnectionManager
import Messages

class DataExtractor(DataReceiver):

    def handleData(self, data) -> None:
        print("New data Received", data)
        separatedData = data.split("::")
        print("Raw data: ",separatedData)
        print("config file: ",separatedData[1:])
        messageId = MessageID(int(separatedData[0]))
        message = Messages.messageIdSwitch[messageId](separatedData[1:])

dataExtractor = DataExtractor()
ConnectionManager.connManager.registerReceiver(dataExtractor)