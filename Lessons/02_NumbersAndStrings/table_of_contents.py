# Write a program that will generate a table of contents line like this:
# Chapter title ...... N, where N is the page number.
# The table of contents line must be 40 characters long,
# There must be a space between the chapter title and periods.
# There must also be a space between the dots and the page number.

import sys
# chapter = sys.argv[1]
# page = sys.argv[2]
chapter = 'Chapter one '
page = ' 17'


print(chapter + page.rjust((38 - len(chapter + page)), '.'))