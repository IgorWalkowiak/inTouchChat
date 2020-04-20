import ChatGUI as gui
import Requests
import ConnectionManager
import threading
import time
import copy

usersToId = {}
nickname = input("nick")

def userRefresher():
    while True:
        print("refreshing!")
        Requests.listUsers()
        time.sleep(2.5)

def messageSentTo(toNickName, text):
    global usersToId
    myId = usersToId[nickname]
    toId = usersToId[toNickName]
    Requests.sendTo(myId, toId, text)



Requests.register(nickname)
chatGui = gui.ChatGUI(600,600,nickname, messageSentTo)

def availableUserHandler(message):
    global usersToId
    global nickname
    print("availableUserHandler")
    usersToId = copy.deepcopy(message)
    usersList = list(usersToId.keys())
    usersList.remove(nickname)
    if usersList:
        chatGui.updateAvailableUsers(usersList)

def newMessageFrom(fromId, text):
    global usersToId
    for user, userId in usersToId.items():
        if userId == fromId:
            chatGui.newMessageFrom(text, user)



Requests.availableUserResponseHandler = availableUserHandler
Requests.newMessageFrom = newMessageFrom

refresher = threading.Thread(target=userRefresher)
refresher.start()
gui.mainWindow.mainloop()


print("listuje")
