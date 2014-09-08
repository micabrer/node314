#!/usr/bin/env python2.7

"""
node314 Bootstrap and Remote Maintenance Script
Version 0.1
Author: Mike C.
"""

import subprocess


def checkWireless(ssids):

	print "Starting wireless search..."
	for ap in ssids:

		print "Scanning for " + ap + "..."
		
		subprocess.call("iwli


ssids = ['blizzard', 'strider', 'test1', 'test2']

checkWireless(ssids)

#linkUp = subprocess.call("ip link set wlan0 up")


#if (linkUp == 0)
#	print "Wlan0 is up!"









#print status
