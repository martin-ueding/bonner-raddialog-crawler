#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright © 2017 Martin Ueding <dev@martin-ueding.de>
# Licensed under the MIT/Expat license.

import argparse
import csv

import yaml


def main():
    options = _parse_args()

    with open('posts2.yml') as f:
        data = yaml.load(f)

    with open('posts.csv', 'w') as f:
        writer = csv.writer(f)

        writer.writerow([
            'author',
            'title',
            'date',
            'votes',
            'lat',
            'lon',
            'num comments',
            'url',
            'category',
        ])

        for url, post in sorted(data.items()):
            writer.writerow([
                post.get('author'),
                post.get('title'),
                post.get('date'),
                post.get('votes'),
                post.get('lat'),
                post.get('lon'),
                len(post.get('comments')),
                post.get('url'),
                post.get('category', None),
            ])


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
