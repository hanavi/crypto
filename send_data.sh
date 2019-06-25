#!/bin/bash


CRYPTO=/home/james/.local/bin/crypto
TMPFILE=$(mktemp /tmp/crypto.XXXXXX)
TMPIMG=$(mktemp --suffix .png /tmp/crypto.XXXXXX)
MUTT_CONFIG=fetchmail
MUTT='/usr/bin/neomutt'


$CRYPTO > $TMPFILE

convert -units PixelsPerInch -density 150 -size 750x550 xc:white -font \
    "FreeMono-Bold" -pointsize 12 -fill black \
    -annotate +15+15 "@$TMPFILE" $TMPIMG

echo  "crypto update" |MUTT_CONFIG=fetchmail $MUTT mymedia -a $TMPIMG


rm $TMPIMG
rm $TMPFILE
