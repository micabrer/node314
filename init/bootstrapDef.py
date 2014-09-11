# Bootsrap definitions file
# Author: Michael Cabrera

import subprocess
import sys

def checkWireless(ssid):

	"""
	Check for access point in range
	Return 0 if success
	Return 1 if not in range
	Return 2 if other error
	"""
	print >>sys.stdout, "Scanning for " + ssid + "..."
	
	args=['iwlist', 'wlan0', 'scan', '|', 'grep ']
	process = subprocess.Popen(args[0], args[1], args[2], args[3], args[4], ssid)

	if process.returncode != 0:
		print >>sys.stdout, ssid + " not in range."
		print >> sys.stdout, process.pid
		return 1

	elif process.returncode == 0:
		print >>sys.stdout, ssid + " in range."
		return 0

	return 2


def associateWireless(ssid):

	print >>sys.stdout, "Attempting association with " + ssid

	retcode = subprocess.call("wpa_supplicant -d wext -B -c /etc/node314/wpa_supplicant/" + ssid, shell=True)
	if retcode !=0:
		print >>sys.stdout, "Failed to associate with " + ssid + "."
		return 1
	elif retcode == 0:
		print >>sys.stdout, "Associated with " + ssid + "."

