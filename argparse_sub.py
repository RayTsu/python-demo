#!/usr/bin/env python

# -*- coding: utf-8 -*-
 
import argparse
 
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()
query_parser = subparsers.add_parser(
    "query", help="Show objects in different version of Kubernetes.")
parser.add_argument("square", help="display a square of a given number", type=int)
args = parser.parse_args()
print(args.square**2)
