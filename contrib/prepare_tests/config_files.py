#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import argparse
import glob
import os


def to_json(fobj):
    text = json.load(fobj)
    return json.dumps(text, indent=4, sort_keys=True, separators=(',', ': ')) + '\n'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Test files")
    parser.add_argument('-c', '--config', help='Path to the config files.')
    args = parser.parse_args()

    config_file_path = args.config

    for f in glob.glob(os.path.join(config_file_path, '*.conf')):
        with open(f, 'r+') as f:
            clean = to_json(f)
            f.seek(0)
            f.write(clean)
