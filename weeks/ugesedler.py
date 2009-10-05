#!/usr/bin/env python
# -*- coding: utf-8 -*-

# WARNING:
# THIS FILE IS JUST AN UGLY QUICK AND DIRTY HACK(tm)

import os
import shutil
import glob

destdir = "/home/www/grundat.kommunikationogit.dk/"
if not os.path.exists(destdir):
        os.makedirs(destdir)

def make_pages(pages):

    template = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
    <head>
        <!-- THIS IS AN UGLY HACK TO QUICKLY GET IT ONLINE, DO NOT USE THIS AS AN EXAMPLE -->
        <title>%s - Grundl&aelig;ggende Datalogi - Kommunikation og IT</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <style>
        html {
            font-family: sans-serif;
        }
        </style>
    </head>
    <body>
    <table border=0 padding=1em><tr><td valign="top">
        <h1>&nbsp;</h1>
        %s
    </td><td width="3%%"></td><td>
        <h1>%s</h1>
        %s
    </td><td width="3%%"></td>
    </tr></table>

    </body>
</html>"""
    menu = "<ul>"
    for name in pages:
        menu += '<li><a href="%s.html">%s</a></li>' % (name, name)
    menu += "</ul>"

    for name in pages:
        file(destdir + "/" + name + ".html", "w").write(
                template % (name, menu, name, pages[name]))


files = {}

ugeseddel = ""

def paragraph(name, content):
    return "<p>" + name + ": " + content + "</p>"

for week in range(53, 34, -1):
    dir = "week" + str(week)
    if os.path.exists(dir):
        os.chdir(dir)

        ugeseddel += "<h2>Uge " + str(week) + "</h2>"

        ugeseddel += "<p>Slides/noter: "
        for texfile in glob.glob("*.tex"):
            for _ in range(3): # repeat to get cross-references right
                os.system("pdflatex " + texfile);
            pdffile = texfile.replace(".tex", ".pdf")
            shutil.copy(pdffile, destdir)
            ugeseddel += '<a href="%s">%s</a> ' % (pdffile, pdffile)
        ugeseddel += "</p>"

        if os.path.exists("thisweek.html"):
            ugeseddel += file("thisweek.html").read()

        weekdir = "u" + str(week)
        if not os.path.exists(destdir + "/" + weekdir):
            os.makedirs(destdir + "/" + weekdir)
        ugeseddel += "<p>Eksempler: "
        for pyfile in glob.glob("*.py"):
            shutil.copy(pyfile, destdir + "/"+ weekdir)
            ugeseddel += '<a href="%s">%s</a> ' % ("u41/view_python_file.py?filename=" + weekdir + "/" + pyfile, pyfile)
        for imgfile in glob.glob("*.jpg"):
            shutil.copy(imgfile, destdir)
            ugeseddel += '<a href="%s">%s</a> ' % (imgfile, pyfile)
        ugeseddel += "</p>"

        os.chdir("..")

files["Ugesedler"] = ugeseddel
files["Praktisk"] = """Undervisningen foregår tirsdag og torsdag, kl 8-12, i lokale 18.1.59,<br>
med en kombination af forelæsninger og øvelser.<br>
Første undervisningsgang er torsdag d. 3/9-2009.<br>
Til øvelserne skal I medbringe bærbar computer.<br>
<br>
I første del af kurset anvendes bogen<br>
<span>"Introduction to Computing and Programming in Python, A Multimedia Approach"</span> <br>
af Mark Guzdial, 2. udgave. <br>
<br>
Lærebogen er forsinket<br>
- endnu ikke kommet til bogladen,<br>
så foreløbigt anvendes noter.<br>
<h3><a name="TOC-Undervisningsmaterialer"></a></h3>
<h3><a name="TOC-Kontaktinformation"></a>Kontaktinformation</h3>
Spørgsmål, afleveringer, kommentarer, etc.<br>
sendes til <a href="mailto:grundat@kommunikationogit.dk">grundat@kommunikationogit.dk</a>, <br>
der er en fælles email for underviserne på kurset:<br>
Rasmus J. og Johan.
"""
files["Undervisningsmaterialer"] = """<h2>Litteratur</h2>
I første del af kurset anvendes: <a href="http://www.greenteapress.com/thinkpython/thinkCSpy/thinkCSpy.pdf" rel="nofollow">http://www.greenteapress.com/thinkpython/thinkCSpy/thinkCSpy.pdf</a> (da den&nbsp; oprindelige lærebog ikke ser ud til at ankomme)<br>
<br>
Herudover anvendes også uddrag af <br>
<ul><li>"How To Think Like a Computer Scientist, Learning with Python" af Allan Downey, Jeffry Elkner og Chris Meyers. <a href="http://www.greenteapress.com/thinkpython/" rel="nofollow">http://www.greenteapress.com/thinkpython/</a></li>
<li>Den officielle python dokumentation på: <a href="http://docs.python.org" rel="nofollow">http://docs.python.org</a><br>
</li>
<ul><li><a href="http://docs.python.org/library/doctest.html" rel="nofollow">http://docs.python.org/library/doctest.html</a></li></ul></ul>
<div>
<div><br>
Litteraturen for anden halvdel af kurset er ved at blive fastlagt<br>
<div>
<h2>Software</h2>
Til introduktionen til Python og billeder anvendes JES, der kan hentes fra: <a href="http://coweb.cc.gatech.edu/mediaComp-plan/26" rel="nofollow">http://coweb.cc.gatech.edu/mediaComp-plan/26</a>.<br>
<br>
Senere hen i forløbet bliver følgende relevante:<br>
<ul><li><a href="http://www.python.org/download/releases/2.6.2/" rel="nofollow">http://www.python.org/download/releases/2.6.2/</a><br>
</li>
<li><a href="http://ipython.scipy.org/moin/Download" rel="nofollow">http://ipython.scipy.org/moin/Download</a></li>
<li>En ssh-klient til at forbinde til web-serveren - følger automatisk med OS-X og nyere linux, på windows-platformen kan <a href="http://www.chiark.greenend.org.uk/%7Esgtatham/putty/download.html" rel="nofollow">http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html</a> anvendes.</li>
<li>Versionsstyringssoftware, git <a href="http://git-scm.com/" rel="nofollow">http://git-scm.com/</a><br>
</li></ul>
<br>
<br>
</div>
</div>
</div>
"""
files["Semesterplan"] = """<table border="0">
<tbody>
<tr>
<td style="width: 71px; height: 22px;">Uge 35</td>
<td style="width: 641px; height: 22px;">Introuge<br>
</td>
</tr>
<tr>
<td style="width: 71px; height: 76px;">Uge 36<br>
</td>
<td style="width: 641px; height: 76px;">I gang med programmering, introduktion til: definition af funktioner, billeder, billedkoordinatsystemer,
farverepræsentation, kald af indbyggede funktioner, for-løkker over
billeder, variable, dokumentation/kommentarer, repræsentation af data
(binære tal, tekst som tal). Disse uddybes også i de kommende uger<br>
</td>
</tr>
<tr>
<td style="width: 71px; height: 38px;">Uge 37</td>
<td style="width: 641px; height: 38px;">Betingelser, if, while, problemløsning, læseteknik og tilgang til noter, debugging, introduktion til lister.<br>
</td>
</tr>
<tr>
<td style="width: 71px; height: 57px;">Uge 38</td>
<td style="width: 641px; height: 57px;">Lister og hashtabeller. Skift til idle. At bruge og finde biblioteksfunktioner, problemløsning - at gå fra idé til program, at læse kode / code review. Afprøvning, mere om docstrings. Smagsprøve på rekursion. Introduktion til kommandoprompt. <br>
</td>
</tr>
<tr>
<td style="width: 71px; height: 24px;">Uge 39</td>
<td style="width: 641px; height: 24px;">Klasser og objekter. Introduktion til versionsstyring. <br>
</td>
</tr>
<tr>
<td style="width: 71px; height: 24px;">Uge 40</td>
<td style="width: 641px; height: 24px;">Rustur</td>
</tr>
<tr>
<td style="width: 71px; height: 22px;">Uge 41</td>
<td style="width: 641px; height: 22px;">Webapplikationer, CGI. Strukturerede data, html, xml, DOM, LaTeX.<br>
</td>
</tr>
<tr>
<td style="width: 71px; height: 24px;">Uge 42</td>
<td style="width: 641px; height: 24px;">Databaser, SQL. 3-tier model.<br>
</td>
</tr>
<tr>
<td style="width: 71px; height: 38px;">Uge 43</td>
<td style="width: 641px; height: 38px;">Hvorledes de samme principper går igen i forskellige sprog, JavaScript, syntaks vs. semantik. <br>
</td>
</tr>
<tr>
<td style="width: 71px; height: 24px;">Uge 44</td>
<td style="width: 641px; height: 24px;">Repetition og opsamling. Buffer<br>
</td>
</tr>
<tr>
<td style="width: 71px; height: 57px;">Uge 45</td>
<td style="width: 641px; height: 57px;">I gang med anden del af kurset: Data og algoritmer. <br>
Der kommer ekstra studerende fra IT og Kognition til kurset. <br>
Søgning og sortering, beregningskompleksitet og konstruktion af algoritmer - divide and conqueor.<br>
</td>
</tr>
<tr>
<td style="width: 71px; height: 24px;">Uge 46</td>
<td style="width: 641px; height: 24px;">Stakke, træer, hobe/prioritetskøer, hashtabeller<br>
</td>
</tr>
<tr>
<td style="width: 71px; height: 24px;">Uge 47</td>
<td style="width: 641px; height: 24px;">Maskinmodeller, beregnelighed. Cache. Genopfriskning om representation af data. Grådige algoritmer. Evt. entropi og kodning.<br>
</td>
</tr>
<tr>
<td style="width: 71px; height: 24px;">Uge 48</td>
<td style="width: 641px; height: 24px;">Introduktion til grafer og grafalgoritmer, repræsentation, DAGs, shortest path, lidt om centralitet.<br>
</td>
</tr>
<tr>
<td style="width: 71px; height: 24px;">Uge 49</td>
<td style="width: 641px; height: 24px;">Repetition og opsamling. Buffer<br>
</td>
</tr>
<tr>
<td style="width: 71px; height: 24px;">Uge 50</td>
<td style="width: 641px; height: 24px;">Eksamen: Ugeopgave 10/12-17/12 eller 11/12-18/12<br>
</td>
</tr>

</tbody>
</table>
"""
make_pages(files)
os.chdir(destdir)
shutil.copy("Ugesedler.html", "index.html")
