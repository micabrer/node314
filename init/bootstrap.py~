#!/usr/bin/env python2.7

"""
node314 Bootstrap and Remote Maintenance Script
Version 0.2
Author: Mike C.
"""

import subprocess
import sys
from bootstrapDef.py import checkWireless, associateWireless


essids = ['1blizzard', '1Scratch_N', '1scratch_G', 'test2']


for ssid in essids:

	inRange = checkWireless(ssid)
	

	if inRange == 0
		print >>sys.stdout, "Associate AP would run at this point"
	elif inRange == 1
		print >>sys.stdout, "Would skip to next AP, previous one not in range."
	elif inRange == 2
		print >>sys.stdout, "Unexpected error at this point. Unclear how to handle."
