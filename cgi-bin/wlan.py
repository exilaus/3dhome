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
ssid = form.getvalue('ssid')
key = form.getvalue('key')
file = open("/etc/wpa_supplicant/wpa_supplicant.conf","w")
file.write('network={\n')
file.write('ssid="%s"\n' % ssid)
file.write('proto=RSN\n')
file.write('key_mgmt=WPA-PSK\n')
file.write('pairwise=CCMP TKIP\n')
file.write('group=CCMP TKIP\n')
file.write('psk="%s"\n' % key)
file.write('}')
file.close()
print "<br><br><br><br><br><br><center><h1>Wifi configured need restart</h1></center>"
print "</body>"