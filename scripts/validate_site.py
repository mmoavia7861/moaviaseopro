#!/usr/bin/env python3
"""Dependency-free static HTML/site checks. Exit nonzero if any check fails."""
import re
import json
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote

ROOT=Path(__file__).resolve().parents[1]
FILES=sorted(ROOT.rglob('*.html'))
ISSUES=[]

class Parser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links=[]; self.h1=0; self.titles=[]; self.canonicals=[]
        self.schema=[]; self.in_script=False; self.in_title=False; self.buf=''
    def handle_starttag(self, tag, attrs):
        d=dict(attrs)
        if tag=='h1': self.h1 += 1
        if tag=='title': self.in_title=True; self.buf=''
        if tag=='script' and d.get('type')=='application/ld+json':self.in_script=True;self.buf=''
        if tag=='link' and d.get('rel')=='canonical':self.canonicals.append(d.get('href'))
        for attr in ('href','src'):
            if tag in ('a','link','script','img') and attr in d: self.links.append(d[attr])
        if tag=='img' and not d.get('alt'):ISSUES.append('image missing alt')
    def handle_data(self,data):
        if self.in_script or self.in_title:self.buf +=data
    def handle_endtag(self,tag):
        if tag=='title':self.titles.append(self.buf.strip());self.in_title=False
        if tag=='script' and self.in_script:
            self.schema.append(json.loads(self.buf));self.in_script=False

for file in FILES:
    relative=file.relative_to(ROOT)
    try:
        parser=Parser();parser.feed(file.read_text(encoding='utf-8'))
        if parser.h1!=1: ISSUES.append(f'{relative}: expected 1 H1, got {parser.h1}')
        if not parser.titles or not parser.titles[0]:ISSUES.append(f'{relative}: no title')
        if len(parser.canonicals)!=1:ISSUES.append(f'{relative}: not exactly 1 canonical')
        if not parser.schema:ISSUES.append(f'{relative}: missing JSON-LD')
        for link in parser.links:
            if link.startswith(('https://','http://','mailto:','tel:','#','data:')):continue
            link=unquote(urlparse(link).path)
            if link and not (file.parent/link).exists():ISSUES.append(f'{relative}: missing link {link}')
        if file.name in ('seo.html','web-development.html','meta-ads.html','google-ads.html'):
            types=[x.get('@type') for x in parser.schema[0].get('@graph',[])]
            if 'Service' not in types or 'FAQPage' not in types:
                ISSUES.append(f'{relative}: missing Service/FAQ schema')
    except Exception as exc:ISSUES.append(f'{relative}: {exc}')

try:
    sitemap=ET.fromstring((ROOT/'sitemap.xml').read_text(encoding='utf-8'))
    entries=sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
    if len(entries)!=len(FILES):ISSUES.append(f'sitemap URLs {len(entries)} != HTML files {len(FILES)}')
except Exception as exc:ISSUES.append(f'sitemap: {exc}')

if ISSUES:
    print('FAILED:')
    for issue in ISSUES:print(' -',issue)
    sys.exit(1)
print(f'PASS: {len(FILES)} HTML pages, JSON-LD, 1 H1/page, internal links, sitemap')
