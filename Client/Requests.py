import ConnectionManager

userID = ""
availableUserResponseHandler = None
newMessageFrom = None

def newMessageHandler(message):
    parsedMessage = message.split("::")
    messageId = parsedMessage[0]
    if messageId == "1":
        userID = parsedMessage[1]
    if messageId == "2":
        parsedMessage = parsedMessage[1:]
        userToUserId = {}
        for user, userID in zip(parsedMessage[0::2], parsedMessage[1::2]):
            userToUserId[user] = userID
        availableUserResponseHandler(userToUserId)
    if messageId == "3":
        print(parsedMessage)
        fromId = parsedMessage[1]
        text = parsedMessage[2]
        newMessageFrom(fromId, text)


connManager = ConnectionManager.ConnectionManager(newMessageHandler)

def printer(a):
    print(a)


def register(nickName):
    connManager.send("1::"+nickName)

def listUsers():
    connManager.send("2::"+userID)

def sendTo(fromId, toId, message):
    readyMessage = "3::{}::{}::{}".format(fromId, toId, message)
    connManager.send(readyMessage)



