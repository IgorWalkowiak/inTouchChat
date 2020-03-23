from DataReceiver import DataReceiver
from MessageID import MessageID
from MessageExecutor import MessageExecutor
import ConnectionManager
import Messages

class DataExtractor(DataReceiver):

    def handleData(self, fromPort, data) -> None:
        separatedData = data.split("::")
        print("from port",fromPort)
        print("New raw data: ",separatedData)
        print("config file: ",separatedData[1:])
        messageId = MessageID(int(separatedData[0]))
        message = Messages.messageIdSwitch[messageId](separatedData[1:])
        message.fromPort = fromPort
        MessageExecutor.execute(message)


dataExtractor = DataExtractor()
ConnectionManager.connManager.registerReceiver(dataExtractor)