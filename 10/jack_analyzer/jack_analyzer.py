#!/usr/bin/python
# -*- coding: utf-8 -*-

from constants import *
from jack_tokenizer import JackTokenizer
from code_writer import CodeWriter
import glob
import argparse
import os.path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, help='source file or directory')

    args = parser.parse_args()
    path = args.path

    if path.endswith(".jack"):  # file
        compile(path)

    else:  # directory
        if path.endswith("/"):
            path = path[:-1]
        files = glob.glob("%s/*" % path)
        for filepath in files:
            if filepath.endswith(".jack"):
                compile(filepath)


def compile(filepath):
    with JackTokenizer(filepath) as tokenizer:
        print "====%s====" % filepath


if __name__ == '__main__':
    main()
