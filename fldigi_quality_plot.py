#!/usr/bin/env python

#    FLDIGI Channel Quality Grapher
#
#    This program plots the modem signal quality value, as reported by fldigi.
#    Information is collected from fldigi using its XMLRPC interface:
#    http://www.w1hkj.com/FldigiHelp-3.21/xmlrpc-control.html
#    
#    Copyright (C) 2013 Mark Jessop <mark.jessop@adelaide.edu.au>
# 
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
# 
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
#      GNU General Public License for more details.
# 
#      For a full copy of the GNU General Public License, 
#      see <http://www.gnu.org/licenses/>.
#
#

from xmlrpclib import ServerProxy, Error
import socket,sys,time
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np

# Open a connection to the fldigi XMLRPC server
fldigi = ServerProxy("http://localhost:7362")

# Check the connection is working by requesting the program name
try:
    fldigi.fldigi.name()
except socket.error as v:
    print "ERROR:",v
    print "Is fldigi running?"
    sys.exit(1)


# Setup plot
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

data = []

line, = plt.plot([], [], 'r-')


def draw_new_data(i, data, line, *args):
    current_quality = fldigi.modem.get_quality()
    data.append(current_quality)
    #Trim to 100 elements    
    data = data[-100:]
    xscale = np.arange(len(data))
    line.set_data([xscale,data])
    ax.axis([0,xscale[-1],min(data),max(data)])
    return line,


ani = anim.FuncAnimation(fig,draw_new_data,fargs=(data,line),interval=200)
plt.show()
