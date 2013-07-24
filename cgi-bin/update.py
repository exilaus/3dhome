#!/usr/bin/pythonRoot
import cgi, os,sys 
import subprocess
import urllib2

print """Content-Type: text/html;charset=utf-8\r\n\r\n\r\n\r\n\r\n       
      <html>
      <head>
      <title>Update</title><link rel="stylesheet" type="text/css" href="/WEB/style.css">
      <script type="text/javascript">
      function goBack() {
      javascript: history.go(-2);
      }
      function timer() {
      setTimeout("goBack()", 35000);
      }
      window.onload=timer;
      </script>
      </head><body>
      <h2>Update</h2><center><table><tr><td>"""

url = 'http://exilaus.byethost15.com/3dhome/update.txt' # write the url here

response = urllib2.urlopen(url)
for line in response:
    print line.rstrip()
    print "<br>"
    c = subprocess.Popen(line.rstrip(), shell=True)

print "</td></tr></table></center><br><br><br><br><br><br><center><h1>Update complete. Please wait...</h1></center>"
print "</body>"