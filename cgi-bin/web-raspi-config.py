#!/usr/bin/pythonRoot

import cgi, os,
import cgitb; cgitb.enable()
#add other module you need

# or other class and def you need :)
class Unbuffered:
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)



#take value from html page
timezone = form.getvalue('timezone')
keyboard = form.getvalue('keyboard')
locale   = form.getvalue('locale')
wifiname = form.getvalue('wifiname')
wifipass = form.getvalue('wifipass')


# todo prepare items for use

# convert timezone from zone number to text value

if timezone == '-12' : timezone = 'Europe/London'
if timezone == '-11' : timezone = 'Europe/London'
if timezone == '-10' : timezone = 'Europe/London'
if timezone == '-9'  : timezone = 'Europe/London'
if timezone == '-8'  : timezone = 'Europe/London'
if timezone == '-7'  : timezone = 'Europe/London'
if timezone == '-6'  : timezone = 'Europe/London'
if timezone == '-5'  : timezone = 'Europe/London'
if timezone == '-4'  : timezone = 'Europe/London'
if timezone == '-3'  : timezone = 'Europe/London'
if timezone == '-2'  : timezone = 'Europe/London'
if timezone == '-1'  : timezone = 'Europe/London'
if timezone == '0'   : timezone = 'Europe/London'
if timezone == '+1'  : timezone = 'Europe/London'
if timezone == '+2'  : timezone = 'Europe/London'
if timezone == '+3'  : timezone = 'Europe/London'
if timezone == '+4'  : timezone = 'Europe/London'
if timezone == '+5'  : timezone = 'Europe/London'
if timezone == '+6'  : timezone = 'Europe/London'
if timezone == '+7'  : timezone = 'Europe/London'
if timezone == '+8'  : timezone = 'Europe/London'
if timezone == '+9'  : timezone = 'Europe/London'
if timezone == '+10' : timezone = 'Europe/London'
if timezone == '+11' : timezone = 'Europe/London'
if timezone == '+12' : timezone = 'Europe/London'

#now can manipulate or manage variable this python script

#
# all search/replace comment out until know more
#

################## update timezone  #####################
#if timezone != 'Europe/London' :
#search-replace 
# Read in the file
#  filedata = None
#  with file = open('/etc/timezone', 'r') :
#    filedata = file.read()

# Replace the target string
#  filedata.replace('Europe/London', timezone)

# Write the file out again
#  with file = open('/etc/timezone', 'w') :
#    file.write(filedata)

################## update keyboard  #####################
# todo: only update if needed
#search-replace 
# Read in the file
#filedata = None
#with file = open('/etc/default/keyboard', 'r') :
#  filedata = file.read()

# Replace the target string
#filedata.replace('???', keyboard)

# Write the file out again
#with file = open('/etc/default/keyboard', 'w') :
#  file.write(filedata)

################## update locale  #####################
# todo: only update if needed
#search-replace 
# Read in the file
#filedata = None
#with file = open('/etc/default/locale', 'r') :
#  filedata = file.read()

# Replace the target string
#filedata.replace('???', locale)

# Write the file out again
#with file = open('/etc/default/locale', 'w') :
#  file.write(filedata)

################## update wifi name  #####################
################## update wifi password  #################
#if wifiname != '' and wifipass != '' :
#search-replace 
# Read in the file
#  filedata = None
#  with file = open('/etc/network/interfaces', 'r') :
#    filedata = file.read()

# Replace the target string
#  filedata.replace('<SSID>', wifiname)
#  filedata.replace('<WPA Password>', wifipass)

# Write the file out again
#  with file = open('/etc/network/interfaces', 'w') :
#    file.write(filedata)


################## comment out web cgi python at boot  #####################
################## uncomment 5dprint for launch at boot  ###################
#search-replace 
# Read in the file
#filedata = None
#with file = open('/etc/rc.local', 'r') :
#  filedata = file.read()

# Replace the target string
#filedata.replace('python -m CGIHTTPServer', '#python -m CGIHTTPServer')
#filedata.replace('#5dprint', '5dprint')

# Write the file out again
#with file = open('/etc/rc.local', 'w') :
#  file.write(filedata)


##############################  finish up   ###################################

#config-done web page

sys.stdout=Unbuffered(sys.stdout)
print "Content-Type: text/html;charset=utf-8\r\n\r\n"
print "<html><head><title>Configuration Done</title></head>"
print "<body><br><br><center>"
print "Congratulations! The basic configuration is complete.<br><br>"
print "Please reboot your Pi for the changes to take effect.<br><br>"
print "If you wish to further customize your Pi,<br>use a SSH client program to connect to the Pi and run raspi-config."
print "<br><br><br><br><small>"
print "Details: On future boots, the Pi will automatically logon with the default username and connect to your wifi network.  Only SSH and 5DPrint will be automatically launched at boot up."
print "</small></center></body></html>"