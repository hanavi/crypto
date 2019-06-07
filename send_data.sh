#!/bin/bash

convert -size 380x260 xc:white -font "FreeMono" -pointsize 12 -fill black  \
    -annotate +15+15 "@-" image.png


