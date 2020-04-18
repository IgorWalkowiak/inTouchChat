import DataExtractor
import ConnectionManager

dataExtractor = DataExtractor.DataExtractor()
ConnectionManager.connManager.registerReceiver(dataExtractor)