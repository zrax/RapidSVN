#!/usr/bin/python
# ====================================================================
# Copyright (c) 2002-2008 The RapidSvn Group.  All rights reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program (in the file GPL.txt.  
# If not, see <http://www.gnu.org/licenses/>.
#
# This software consists of voluntary contributions made by many
# individuals.  For exact contribution history, see the revision
# history and logs, available at http://rapidsvn.tigris.org/.
# ====================================================================
import sys
import os
import os.path
import re
import array

USAGE="""png2c - Embed a PNG in a C header file (like XPM)
Usage: png2c [file ..] Convert all the file <file.png> to <file.png.h>"""

if len(sys.argv) < 2:
  print USAGE
  os.exit(1)

r=re.compile("^([a-zA-Z._][a-zA-Z._0-9]*)[.][pP][nN][gG]$")
for path in sys.argv[1:]:
  filename=os.path.basename(path)
  m=r.match(filename)
  # Allow only filenames that make sense
  # as C variable names
  if not(m):
    print "Skipped file (unsuitable filename): " + filename
    continue

  # Read PNG file as character array
  bytes=array.array('B', open(path, "rb").read())
  count=len(bytes)

  # Create the C header
  text="/* %s - %d bytes */\n" \
    "static const unsigned char %s_png[] = {\n" % (filename, count, m.group(1))

  # Iterate the characters, we want
  # lines like:
  #   0x01, 0x02, .... (8 values per line maximum)
  i=0
  count=len(bytes)
  for byte in bytes:
    # Every new line starts with two whitespaces
    if (i % 8) == 0:
      text += "  "
    # Then the hex data (up to 8 values per line)
    text+="0x%02x" % (byte)
    # Separate all but the last values 
    if (i+1) < count:
      text += ", "
    if (i % 8) == 7:
      text += '\n'
    i+=1
      
  # Now conclude the C source
  text += "};\n/* End Of File */\n"

  open(path + ".h", 'w').write(text)
