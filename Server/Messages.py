from MessageID import MessageID
from abc import ABC, abstractmethod
import UserDatabase
import Sender

class Message(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

class RegisterMessage(Message):
    messageId = MessageID.REGISTER
    def __init__(self, config):
        print("NEW",self.messageId)
        self.nickName = config[0]
    def execute(self) -> None:
        givenId = UserDatabase.userDatabase.register(self.nickName, self.fromPort)
        print(UserDatabase.userDatabase.idToNickName)
        response = self.prepareResponse(givenId)
        Sender.send(self.fromPort,response)
    def prepareResponse(self, givenId):
        return "1::"+str(givenId)

class ListUserMessage(Message):
    messageId = MessageID.LIST_USER
    def __init__(self,config):
        print("NEW",self.messageId)
        self.fromId = config[0]
    def execute(self) -> None:
        users = UserDatabase.userDatabase.idToNickName.values()
        response = self.prepareResponse(users)
        Sender.send(self.fromPort,response)
    def prepareResponse(self, users):
        reponse = "2"
        for user in users:
            print(user)
            reponse = reponse+"::"+user
        return reponse


class SendToMessage(Message):
    messageId = MessageID.SEND_TO
    def __init__(self, config):
        print("NEW",self.messageId)
        self.fromId = config[0]
        self.toId = config[1]
        self.content = config[2]
    def execute(self) -> None:
        print(self.messageId)
        print(self.toId)
        print(UserDatabase.userDatabase.idToPort)
        recipientPort = UserDatabase.userDatabase.idToPort[int(self.toId)]
        print("do kogo? ",recipientPort)
        response = self.prepareResponse()
        Sender.send(recipientPort, response)
    def prepareResponse(self):
        response="1::"+self.content
        return response

messageIdSwitch = {
    MessageID.REGISTER : RegisterMessage,
    MessageID.LIST_USER : ListUserMessage,
    MessageID.SEND_TO : SendToMessage
}