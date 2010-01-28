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
            ugeseddel += '<a href="%s">%s</a> ' % ("u42/view_python_file.py?filename=" + weekdir + "/" + pyfile, pyfile)
        for imgfile in glob.glob("*.jpg"):
            shutil.copy(imgfile, destdir)
            ugeseddel += '<a href="%s">%s</a> ' % (imgfile, pyfile)
        ugeseddel += "</p>"

        os.chdir("..")

files["Ugesedler"] = ugeseddel
files["Praktisk"] = """
<p>Undervisningen foregår tirsdag og torsdag, kl 8-12, i lokale 18.1.59,<br>
med en kombination af forelæsninger og øvelser.<br>
Første undervisningsgang er torsdag d. 3/9-2009.<br>
Til øvelserne skal I medbringe bærbar computer.<br>
</p>

<h3><a name="TOC-Kontaktinformation"></a>Kontaktinformation</h3>
Spørgsmål, afleveringer, kommentarer, etc.<br>
sendes til <a href="mailto:grundat@kommunikationogit.dk">grundat@kommunikationogit.dk</a>, <br>
der er en fælles email for underviserne på kurset:<br>
Rasmus J. og Johan.

<p>Rasmus kan også fanges på kontor 24.5.48, almindeligvis tirsdag, onsdag og torsdag, men aftal helst per mail inden, for ikke at gå forgæves.

"""
files["Undervisningsmaterialer"] = """<h2>Litteratur</h2>
Til den grundlæggende programmering anvendes:
<ul>
    <li>Lærebogen "<a href="http://www.greenteapress.com/thinkpython/thinkCSpy/thinkCSpy.pdf">How to Think Like a Computer Scientist</a>" af Allen Downey et al. (Da den oprindelige lærebog ikke kunne skaffes er udvalgte uddrag af denne tidligere lagt her på siden. Selve bogen erstatter disse uddrag. </li>
    <li>Som supplement anvendes også tutorials fra <a href="http://www.tutorialspoint.com/python/">http://www.tutorialspoint.com/python/</a>: Python basics</li>
    <li>Dele af den officielle Python dokumentation fra <a href="http://docs.python.org/">http://docs.python.org/</a>.
</ul>

Litteraturen for anden halvdel af kurset er ved at blive fastlagt<br>
<h2>Software</h2>

Til introduktionen til Python og billeder anvendes JES, der kan hentes fra: <a href="http://coweb.cc.gatech.edu/mediaComp-plan/26" rel="nofollow">http://coweb.cc.gatech.edu/mediaComp-plan/26</a>.<br>
<br>
Senere hen i forløbet bliver følgende relevante:<br>
<ul><li><a href="http://www.python.org/download/releases/2.6.2/" rel="nofollow">http://www.python.org/download/releases/2.6.2/</a><br>
</li>
<li><a href="http://ipython.scipy.org/moin/Download" rel="nofollow">http://ipython.scipy.org/moin/Download</a></li>
<li>En ssh-klient til at forbinde til web-serveren - følger automatisk med OS-X og nyere linux, på windows-platformen kan <a href="http://www.chiark.greenend.org.uk/%7Esgtatham/putty/download.html" rel="nofollow">http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html</a> anvendes.</li>
<li>Versionsstyringssoftware, svn</li>
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
<td style="width: 641px; height: 24px;">Klasser og objekter.<br>
</td>
</tr>
<tr>
<td style="width: 71px; height: 24px;">Uge 40</td>
<td style="width: 641px; height: 24px;">Rustur</td>
</tr>
<tr>
<td style="width: 71px; height: 22px;">Uge 41</td>
<td style="width: 641px; height: 22px;">Webapplikationer, CGI. Strukturerede data, html, xml<br>
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
<td style="width: 641px; height: 24px;">
I gang med anden del af kurset: Data og algoritmer. <br>
Søgning og sortering, beregningskompleksitet og konstruktion af algoritmer - divide and conqueor.<br>
</td>
</tr>
<tr>
<td style="width: 71px; height: 57px;">Uge 45</td>
<td style="width: 641px; height: 57px;">Efterårsferie.
Der kommer ekstra studerende fra IT og Kognition til kurset. <br>
</td>
</tr>
<tr>
<td style="width: 71px; height: 24px;">Uge 46</td>
<td style="width: 641px; height: 24px;">Repetition omkring webapplikationer, samt introduktion til algoritmer og datastrukturer<br>
</td>
</tr>
<tr>
<td style="width: 71px; height: 24px;">Uge 47</td>
<td style="width: 641px; height: 24px;">Mere om objekter og klasser<br>
</td>
</tr>
<tr>
<td style="width: 71px; height: 24px;">Uge 48</td>
<td style="width: 641px; height: 24px;">Introduktion til træer og grafer<br>
</td>
</tr>
<tr>
<td style="width: 71px; height: 24px;">Uge 49</td>
<td style="width: 641px; height: 24px;">Grafer<br>
</td>
</tr>
<tr>
<td style="width: 71px; height: 24px;">Uge 50</td>
<td style="width: 641px; height: 24px;">Repetition, spørgetime, sidste undervisningsgang er 8/12 Eksamen: Ugeopgave 10/12-17/12 <br>
</td>
</tr>

</tbody>
</table>
"""
make_pages(files)
os.chdir(destdir)
shutil.copy("Ugesedler.html", "index.html")
