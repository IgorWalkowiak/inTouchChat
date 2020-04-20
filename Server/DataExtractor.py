from DataReceiver import DataReceiver
from MessageID import MessageID
from MessageExecutor import MessageExecutor
import Messages

class DataExtractor(DataReceiver):

    def handleData(self, fromPort, data) -> None:
        separatedData = data.split("::")
        messageId = MessageID(int(separatedData[0]))
        message = Messages.messageIdSwitch[messageId](separatedData[1:])
        message.fromPort = fromPort
        MessageExecutor.execute(message)


