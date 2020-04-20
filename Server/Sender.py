import ConnectionManager


def send(target, data):
    ConnectionManager.connManager.sendTo(target, data)