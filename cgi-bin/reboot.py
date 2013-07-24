#!/usr/bin/pythonRoot
import cgi, os,sys 
import subprocess

print """Content-Type: text/html;charset=utf-8\r\n\r\n\r\n\r\n\r\n       
      <html>
      <head>
      <title>Configuration</title><link rel="stylesheet" type="text/css" href="/WEB/style.css">
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
      <h2>Configuration</h2>"""

c = subprocess.Popen("shutdown -r now", shell=True)

print "<br><br><br><br><br><br><center><h1>Reboot now. Please wait...</h1></center>"
print "</body>"