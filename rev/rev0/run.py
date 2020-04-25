#!/usr/bin/env python3

import flagchecker

print("Enter Flag: ")
inp = input()
if flagchecker.CheckFlag(inp):
    print("Way to Go!")
else:
    print("Bad Boy!")