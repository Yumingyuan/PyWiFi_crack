from pywifi import *
import time

if __name__=="__main__":
	wifi=PyWiFi()
	ifaces=wifi.interfaces()[0]
	ifaces.scan()
	results=ifaces.scan_results()
	for result in results:
		print(result.bssid,result.ssid)
