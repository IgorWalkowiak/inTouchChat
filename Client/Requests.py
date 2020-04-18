import ConnectionManager

userID = ""

class Responder:
    def __init__(self, availableUserHandler, userMessage):
        self.availableUserHandler = availableUserHandler
        self.userMessage = userMessage

    def newMessageHandler(self, message):
        parsedMessage = message.split("::")
        if parsedMessage[0] == "1":
            userID = parsedMessage[1]
        if parsedMessage[0] == "2":
            self.availableUserHandler(parsedMessage[1:])

def printer(a):
    print(a)

responder = Responder(printer,"b")
connManager = ConnectionManager.ConnectionManager(responder.newMessageHandler)

def register(nickName):
    connManager.send("1::"+nickName)

def listUsers():
    connManager.send("2::"+userID)

def sendTo(nickName, message):
    connManager.send("2::")



