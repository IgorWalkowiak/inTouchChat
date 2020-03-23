import random

class UserDatebase:
    idToNickName = {}
    idToPort = {}
    lastIdCounter = 0

    def register(self, nickName, port):
        if nickName in self.idToNickName.values():
            raise NameError('Nickname already in base!')
        elif port in self.idToPort.values():
            raise NameError('Two users connected from one port!')
        else:
            self.lastIdCounter = self.lastIdCounter+1
            self.idToPort[self.lastIdCounter] = port
            print("REJESTRACJA:", self.idToPort)
            self.idToNickName[self.lastIdCounter] = nickName
            return self.lastIdCounter

userDatabase = UserDatebase()
