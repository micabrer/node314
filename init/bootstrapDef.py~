# Bootsrap definitions file
# Author: Michael Cabrera



def checkWireless(ssid):

"""
Check for access point in range
Return 0 if success
Return 1 if not in range
Return 2 if other error
"""
	print >>sys.stdout, "Scanning for " + ssid + "..."
		
	try:

		retcode = subprocess.call("iwlist wlan0 scan | grep -i " + ssid, shell=True)
		if retcode != 0:
			print >>sys.stdout, ssid + " not in range."
			return 1
		elif retcode == 0:
			print >>sys.stdout, ssid + " in range."
			return 0

		except OSError as e:
			print >>sys.stdout, "Scan failed. Reason: " + e		
			return 2
	return 2


def associateWireless(ssid):

	print >>sys.stdout, "Attempting association with " + activessid

