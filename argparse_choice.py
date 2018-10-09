#!/usr/bin/env python

# -*- coding: utf-8 -*-
 
import argparse
 
parser = argparse.ArgumentParser()
 
parser.add_argument("--square", "-s", help="display a square of a given number", type=int)
parser.add_argument("--cubic", "-c", help="display a cubic of a given number", type=int)
 
args = parser.parse_args()
 
if args.square:
    print(args.square**2)
 
if args.cubic:
    print(args.cubic**3)
