#!/usr/bin/env python3

import os, sys
import Functions

def key():
    return sys.argv[1]

def getValue(json, element):
    keys = element.split('.')
    rv = json
    for key in keys:
        rv = rv[key]
    if isinstance(rv, dict):
        rv = rv[Functions.osName()]
    return rv

print(getValue(Functions.config(), key()))
