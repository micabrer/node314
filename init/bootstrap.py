#!/usr/bin/env python2.7

"""
node314 Bootstrap and Remote Maintenance Script
Version 0.1
Author: Mike C.
"""

import subprocess
import sys

def checkWireless(essids):

	print >>sys.stdout, "Starting wireless search..."
	for ap in essids:

		print >>sys.stdout, "Scanning for " + ap + "..."
		
		try:

			retcode = subprocess.call("iwlist wlan0 scan | grep -i " + ap, shell=True)
			if retcode != 0:
				print >>sys.stdout, ap + " not in range."
				ap = None
			elif retcode == 0:
				print >>sys.stdout, ap + " in range. Attempting connection..."
				return ap
		except OSError as e:
			
			print >>sys.stdout, "Scan failed. Reason: " + e


	return ap

def associateWireless(activeAP):

	#print >>sys.stdout, "Starting WPA_Supplicant for " + 
	
	




essids = ['1blizzard', '1Scratch_N', '1scratch_G', 'test2']

activeAP=checkWireless(essids)

if activeAP == None:
	print >>sys.stdout, "No APs in range. Closing."
else:
	print >>sys.stdout, "Active AP is: " + activeAP
