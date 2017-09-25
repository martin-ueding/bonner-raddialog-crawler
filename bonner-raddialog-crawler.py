#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright © 2017 Martin Ueding <dev@martin-ueding.de>
# Licensed under the MIT/Expat license.

import argparse
import re
import os

from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET
import yaml


def parse_comment(tag):
    meta = tag.select('div.submitted')[0]

    date = re.search(r'(\d+\. \w+. \d+)', meta.text).group(1)
    time = re.search(r'(\d+:\d+)', meta.text).group(1)
    author = meta.select('span.username')[0].text

    body = tag.select('div.content-wrapper > div.comment-body')[0]

    title = tag.select('a.permalink')[0].text
    paragraphs = body.select('div.field-name-comment-body p')

    return dict(
        date=date,
        time=time,
        author=author,
        title=title,
        text=[p.text for p in paragraphs],
    )


def parse_post(url):
    r = requests.get(url)

    with open('out.html', 'w') as f:
        f.write(r.text)

    m = re.search(r'"lat":([\d.]+),"lon":([\d.]+)', r.text)
    if m:
        lat, lon = map(float, m.groups())

    soup = BeautifulSoup(r.text, 'html.parser')

    s = soup.select('p.user-and-date')[0]

    date = re.search(r'(\d{2}\.\d{2}\.\d{4})', s.text).group(1)
    author = s.select('span.username')[0].text

    paragraphs = soup.select('div.node-main-content p')

    m = re.search(r'(\d+)', soup.select('div.rate-info')[0].text)
    if m:
        votes = int(m.group(1))

    tags_next = soup.select('a.proposal-next')
    if len(tags_next) > 0:
        next_ = 'https://www.raddialog.bonn.de' + tags_next[0]['href']
    else:
        next_ = None

    title = soup.select('h2.node-title')[0].text

    top_comments = soup.select('#comments > div.comment-wrapper')
    comments = []
    for top_comment in top_comments:
        parsed = parse_comment(top_comment)

        sub_comments = top_comment.select('div.all-replies div.indented')
        sub_parsed = list(map(parse_comment, sub_comments))

        parsed['answers'] = sub_parsed
        comments.append(parsed)

    return dict(
        date=date,
        author=author,
        text=[p.text for p in paragraphs],
        lat=lat,
        lon=lon,
        url=url,
        title=title,
        votes=votes,
        next=next_,
        comments=comments,
    )


def main():
    options = _parse_args()

    url = 'https://www.raddialog.bonn.de/dialoge/bonner-rad-dialog/fahrbahnbelag-bei-naesse-extrem-rutschig'

    storage = 'posts.yml'
    
    if os.path.isfile(storage):
        with open(storage) as f:
            posts = yaml.load(f)
    else:
        posts = {}

    while True:
        print(url)
        parsed = parse_post(url)
        posts[url] = parsed
        url = parsed['next']

        with open(storage, 'w') as f:
            yaml.dump(posts, f)


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
