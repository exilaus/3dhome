#!/usr/bin/pythonRoot
import cgi, os,sys 


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
tocken = form.getvalue('token')
file = open("/home/pi/3dhome/ducktoken","w")
file.write(tocken)
file.close()
print "<br><br><br><br><br><br><center><h1>Token updated need wait 5min</h1></center>"
print "<br><br><br><br><br><br><center><h2>Remember to create dns record on site</h2></center>"
print "</body>"