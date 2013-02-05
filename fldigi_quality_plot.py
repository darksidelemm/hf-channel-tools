#!/usr/bin/env python

# 	FLDIGI Channel Quality Grapher
#
#	This program plots the modem signal quality value, as reported by fldigi.
#	Information is collected from fldigi using its XMLRPC interface:
#	http://www.w1hkj.com/FldigiHelp-3.21/xmlrpc-control.html
# 	
# 	Copyright (C) 2013 Mark Jessop <mark.jessop@adelaide.edu.au>
# 
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
# 
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
# 
#     For a full copy of the GNU General Public License, 
#     see <http://www.gnu.org/licenses/>.
#
#

from xmlrpclib import ServerProxy, Error
import socket,sys,time

# Open a connection to the fldigi XMLRPC server
fldigi = ServerProxy("http://localhost:7362")

# Check the connection is working by requesting the program name
try:
	fldigi.fldigi.name()
except socket.error as v:
	print "ERROR:",v
	print "Is fldigi running?"
	sys.exit(1)


while True:
	current_time = time.strftime("%Y-%m-%d-%H%M%S: ",time.gmtime())
	current_quality = fldigi.modem.get_quality();
	print current_time + str(current_quality)
	time.sleep(0.25)