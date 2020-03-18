from MessageID import MessageID

class RegisterMessage:
    messageId = MessageID.REGISTER
    def __init__(self, config):
        self.nickName = config[0]

class ListUserMessage:
    messageId = MessageID.LIST_USER
    def __init__(self,config):
        self.fromId = config[0]

class SendToMessage:
    messageId = MessageID.SEND_TO
    def __init__(self, config):
        self.fromId = config[0]
        self.toId = config[1]
        self.content = config[2]