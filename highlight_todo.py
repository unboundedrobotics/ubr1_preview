#!/usr/bin/env python

"""
This modifies the CSS for our color scheme -- it is run
as part of make -- DO NOT CHECK IN THE MODIFIED CSS
"""

import os

directory = os.path.dirname(os.path.realpath(__file__))
directory = os.path.join(directory, "_build", "html")

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f) and f.endswith(".html"):
        original = open(f).read()
        new = original.replace("TODO", "<span style=\"background:yellow\">TODO</span>")
        with open(f, "w") as w:
            w.write(new)
