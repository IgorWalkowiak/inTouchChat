from DataSwitch import DataSwitch
from ConnectionManager import ConnectionManager

dataSwitch = DataSwitch()
connManager = ConnectionManager()
connManager.registerReceiver(dataSwitch)