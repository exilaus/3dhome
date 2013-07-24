#!/usr/bin/pythonRoot
import cgi, os,sys 
import subprocess

print """Content-Type: text/html;charset=utf-8\r\n\r\n\r\n\r\n\r\n       
      <html>
      <head>
      <title>Configuration</title><link rel="stylesheet" type="text/css" href="/WEB/style.css">
      <script type="text/javascript">
      function goBack() {
      javascript: history.go(-1);
      }
      function timer() {
      setTimeout("goBack()", 5000);
      }
      window.onload=timer;
      </script>
      </head><body>
      <h2>Configuration</h2>"""

form = cgi.FieldStorage()
passa = form.getvalue('password')

log = open('/home/pi/3dhome/cryptpass', 'w')
c = subprocess.Popen("openssl passwd -crypt %s" % passa, stdout=log, stderr=log, shell=True)
log.close()

print "<br><br><br><br><br><br><center><h1><h1>Password updated need restart</h1></center>"
print "</body>"