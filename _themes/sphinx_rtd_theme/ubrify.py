#!/usr/bin/env python

"""
This modifies the CSS for our color scheme -- it is run
as part of make -- DO NOT CHECK IN THE MODIFIED CSS
"""
import os

directory = os.path.dirname(os.path.realpath(__file__))
cssfile = os.path.join(directory, "static", "css", "theme.css")

original = open(cssfile).read()

# replace blues with oranges
#  3091d1 -- center blue -- 
new = original.replace("2980b9", "df5a0c")
new = new.replace("3091d1", "f26512")

#  9b59b6 -- purple?
new = new.replace("9b59b6", "df5a0c")

# replace their gray with ours
new = new.replace("343131", "4f555b")

with open(cssfile,"w") as f:
    f.write(new)

