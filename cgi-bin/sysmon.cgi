#!/usr/bin/env python
import psutil
import cgi, os,sys 
def memoryUsage():
  #print '<small>%sMemory</small>' % (int(psutil.virtual_memory().percent))
  print '<center><small><b>Memory :</b></small></center><div xmlns="http://www.w3.org/1999/xhtml" style="left:10px;width:180px; position:relative; border:1px solid #999999">'
  print ('<div style="background-color:#CCCCCC; width:'),
  print ("%s%%" % int(100-psutil.virtual_memory().percent)),
  print ('; height:15px;left:10px">')
  print '<div style="position:absolute; left:0px; top:0; text-align:center; width:100%; color:#000000"><small>'
  print (psutil.virtual_memory().available/1024)/1024;
  print ' MB / '
  print (psutil.virtual_memory().total/1024)/1024;
  print' MB ('
  print psutil.virtual_memory().percent;
  print '% used)</small></div></div></div><br>'

def CpuUsage():
  print '<center><small><b>CPU :</b></small></center><div xmlns="http://www.w3.org/1999/xhtml" style="left:10px;width:180px; position:relative; border:1px solid #999999">'
  print ('<div style="background-color:#CCCCCC; width:'),
  print ("%s%%" % int(100-psutil.cpu_percent())),
  print ('; height:15px;left:10px">')
  print '<div style="position:absolute; left:0; top:0; text-align:center; width:100%; color:#000000"><small>'
  print 100-psutil.cpu_percent();
  print '% idle</small></div></div></div><br>'

def DiskUsage():
  print '<center><small><b>SD-CARD :</b></small></center><div xmlns="http://www.w3.org/1999/xhtml" style="left:10px;width:180px; position:relative; border:1px solid #999999">'
  print ('<div style="background-color:#CCCCCC; width:'),
  print ("%s%%" % int(psutil.disk_usage('/').percent)),
  print ('; height:15px;left:10px">')
  print '<div style="position:absolute; left:0; top:0; text-align:center; width:100%; color:#000000"><small>'
  print (psutil.disk_usage('/').free/1024)/1024
  print 'MB/'
  print psutil.disk_usage('/').percent;
  print '% free</small></div></div></div><br>'

print "Content-Type: text/html;charset=utf-8\r\n\r\n\r\n\r\n\r\n"        
print "<html>"
print "<head>"
print "<title>sysmon</title>"
print '<script type="text/JavaScript">'
print '<!--'
print 'function AutoRefresh( t ) {'
print '	setTimeout("location.reload(true);", t);'
print '}'
print '//   -->'
print '</script>'
print "<link rel=""stylesheet"" type=""text/css"" href=""../WEB/style.css"">"
print '</head>'
print '<body onload="JavaScript:AutoRefresh(5000);">'
memoryUsage()
CpuUsage()
DiskUsage()
print '</body>'
