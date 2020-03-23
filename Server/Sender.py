import ConnectionManager


def send(target, data):
    print("sending: ", data)
    ConnectionManager.connManager.sendTo(target, data)