﻿#!python
import cgi
a = 3+4+5
b = a/3
print("content-type:text/html; charset=UTF-8\n")
print(b)

print("""<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.html">WEB</a></h1>
<ol>
  <li><a href="1.html">HTML</a></li>
  <li><a href="2.html">CSS</a></li>
  <li><a href="3.html">JavaScript</a></li>
  <li><a href="ss.py?id=HTML">python</a></li>
  <li><a href="form.html">CSS</a></li>
  <li><a href="구원.html">JavaScript</a></li>
  <li><a href="묵상.html">python</a></li>
  <li><a href="분노.html">CSS</a></li>
  <li><a href="시편1~2편.html">JavaScript</a></li>
  <li><a href="시편3~4편.html">python</a></li>
  <li><a href="시편5~6편.html">JavaScript</a></li>
  <li><a href="zzz.html">python</a></li>
  <li><a href="home_text.html">python</a></li>
</ol>
<h2>WEB</h2>
<h2>엄청 고맙다 덕분에 서버가 뭔지 알게 됨</h2>
<p>
  The World Wide Web (abbreviated WWW or the Web) is an information space where documents and other web resources are identified by Uniform Resource Locators (URLs), interlinked by hypertext links, and can be accessed via the Internet.[1] English scientist Tim Berners-Lee invented the World Wide Web in 1989. He wrote the first web browser computer program in 1990 while employed at CERN in Switzerland.[2][3] The Web browser was released outside of CERN in 1991, first to other research institutions starting in January 1991 and to the general public on the Internet in August 1991. </p>
</body>
</html>
""")

print("zzzzzzzzzzzzzzzzzzzzz")
print(d)
