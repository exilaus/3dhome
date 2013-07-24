#!/usr/bin/env python
import cgi, os,sys 


print """Content-Type: text/html;charset=utf-8\r\n\r\n\r\n\r\n\r\n       
      <html>
      <head>
      <title>Configuration</title><link rel="stylesheet" type="text/css" href="/WEB/style.css">
    <script type="text/javascript" src="/WEB/jquery.min.js"></script>
    <!--[if IE 7]>
    <style type="text/css">
        #vtab > ul > li.selected{
            border-right: 1px solid #fff !important;
        }
        #vtab > ul > li {
            border-right: 1px solid #ddd !important;
        }
        #vtab > div { 
            z-index: -1 !important;
            left:1px;
        }
    </style>
    <![endif]-->
    <style type="text/css">

  
    </style>

    <script type="text/javascript">
        $(function() {
            var $items = $('#vtab>ul>li');
            $items.mouseover(function() {
                $items.removeClass('selected');
                $(this).addClass('selected');

                var index = $items.index($(this));
                $('#vtab>div').hide().eq(index).show();
            }).eq(1).mouseover();
        });
    </script>
      </head><body>
      <h2>Configuration</h2>
      <div id="vtab">
      <ul>
         <li class="flag"></li>
         <li class="trunk"></li>
      </ul><div>
      <table><tr><td><li>Hostname:</li>
      <form id=formhost name=formhost method=post action='hostname.py'><input type=""text"" id='hostname' name='hostname' value='"""

in_file = open("/etc/hostname","r")
text = in_file.read()
in_file.close()

print text,
print "'/><input type=submit name=b1 id=b1 value=Submit /></form><br><li>DuckDNS token:</li><form id=dns name=dns method=post action='ducktoken.py'><input name='token' id='token' type=""text"" value='"
in_file = open("/home/pi/3dhome/ducktoken","r")
text = in_file.read()
in_file.close()

print text,
print "' /><input type=submit name=b3 id=b3 value=Submit /></form><br><li>Webaccess password:</li><form id=crypt name=crypt method=post action='webaccess.py'><input type=""text"" name='password' id='password' value='' /><input type=submit name=b5 id=b5 value=Submit /></form><br>"
print "<li>SSID & KEY:</li><form id=wlan name=wlan method=post action='wlan.py'><input type=""text"" name='ssid' id='ssid' value='SSID'/><input type=""text"" name='key' id='key' value='KEY'/><input type=submit name=b6 id=b6 value=Submit /></form><br>"
print """</td></tr></table></div><div><form id=time name=time method=post action='timezone.py'>
      <table width="830px" border="0"><tbody><tr><td colspan=5><li>Timezone:</li><td></tr><tr><td width="4%">
      <input type="radio" name="timezone" value="GMT-12"></td><td width="4%">
      <input type="radio" name="timezone" value="GMT-11"></td><td width="4%">
      <input type="radio" name="timezone" value="GMT-10"></td><td width="4%">
      <input type="radio" name="timezone" value="GMT-9"></td><td width="4%">
      <input type="radio" name="timezone" value="GMT-8"></td><td width="4%">
      <input type="radio" name="timezone" value="GMT-7"></td><td width="4%">
      <input type="radio" name="timezone" value="GMT-6"></td><td width="4%">
      <input type="radio" name="timezone" value="GMT-5"></td><td width="4%">
      <input type="radio" name="timezone" value="GMT-4"></td><td width="4%">
      <input type="radio" name="timezone" value="GMT-3"></td><td width="4%">
      <input type="radio" name="timezone" value="GMT-2"></td><td width="4%">
      <input type="radio" name="timezone" value="GMT-1"></td><td width="4%">
      <input type="radio" name="timezone" value="GMT0" checked="checked"></td><td width="4%">
      <input type="radio" name="timezone" value="GMT+1"></td><td width="4%">
      <input type="radio" name="timezone" value="GMT+2"></td><td width="4%">
      <input type="radio" name="timezone" value="GMT+3"></td><td width="4%">
      <input type="radio" name="timezone" value="GMT+4"></td><td width="4%">
      <input type="radio" name="timezone" value="GMT+5"></td><td width="4%">
      <input type="radio" name="timezone" value="GMT+6"></td><td width="4%">
      <input type="radio" name="timezone" value="GMT+7"></td><td width="4%">
      <input type="radio" name="timezone" value="GMT+8"></td><td width="4%">
      <input type="radio" name="timezone" value="GMT+9"></td><td width="4%">
      <input type="radio" name="timezone" value="GMT+10"></td><td width="4%">
      <input type="radio" name="timezone" value="GMT+11"></td><td width="4%">
      <input type="radio" name="timezone" value="GMT+12"></td></tr><tr align="center">    
      <td colspan="25"><img src="/img/timezone.jpg" alt=></td></tr><tr><td align="center" colspan=25><input type=submit name=b7 id=b7 value=Submit /></td></tr></tbody></table></form>"""

print "</div></div></body>"