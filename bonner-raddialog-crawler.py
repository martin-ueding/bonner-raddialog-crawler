#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright © 2017 Martin Ueding <dev@martin-ueding.de>

import argparse
import re

from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET
import yaml


def parse_post(url):
    r = requests.get(url)

    with open('out.html', 'w') as f:
        f.write(r.text)

    m = re.search(r'"lat":([\d.]+),"lon":([\d.]+)', r.text)
    if m:
        lat, lon = map(float, m.groups())

    soup = BeautifulSoup(r.text, 'html.parser')
    #print(soup)

    s = soup.select('p.user-and-date')[0]

    m = re.search(r'(\d{2}\.\d{2}\.\d{4})', s.text)
    date = m.group(1)

    author = s.select('span.username')[0].text

    paragraphs = soup.select('div.node-main-content p')

    m = re.search(r'(\d+)', soup.select('div.rate-info')[0].text)
    if m:
        votes = int(m.group(1))

    next_ = 'https://www.raddialog.bonn.de' + soup.select('a.proposal-next')[0]['href']

    return dict(
        date=date,
        author=author,
        text=[p.text for p in paragraphs],
        lat=lat,
        lon=lon,
        url=url,
        votes=votes,
        next=next_,
    )


def main():
    options = _parse_args()

    url = 'https://www.raddialog.bonn.de/dialoge/bonner-rad-dialog/fahrbahnbelag-bei-naesse-extrem-rutschig'

    parsed = parse_post(url)

    print(yaml.dump(parsed))

    '''

      <p class="user-and-date inline">
                      von <span class="username">Miss Construction</span> am 24.09.2017               </p>

                      <div class="leftside node-main-content">

                      field field-name-body field-type-text-with-summary field-label-hidden
    '''


def _parse_args():
    '''
    Parses the command line arguments.

    :return: Namespace with arguments.
    :rtype: Namespace
    '''
    parser = argparse.ArgumentParser(description='')
    options = parser.parse_args()

    return options


if __name__ == '__main__':
    main()
