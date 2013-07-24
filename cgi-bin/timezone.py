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
      setTimeout("goBack()", 5000);
      }
      window.onload=timer;
      </script>
      </head><body>
      <h2>Configuration</h2>"""

form = cgi.FieldStorage()
passa = form.getvalue('timezone')


c = subprocess.Popen("sudo cp /usr/share/zoneinfo/Etc/%s /etc/localtime" % passa, shell=True)
c = subprocess.Popen("sudo echo Etc/%s > /etc/timezone" % passa, shell=True)

print "<br><br><br><br><br><br><center><h1>Timezone updated need restart</h1></center>"
print "</body>"