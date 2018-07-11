#!/usr/bin/env python2

import argparse
import re
import string
import random
import gzip


# borrowed from http://stackoverflow.com/questions/2257441/ddg#2257449
def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


if __name__ == "__main__":

    argparser = argparse.ArgumentParser(description="Any Logfile Anonymiser, Replaces regex with uniq random characters")
    argparser.add_argument("-f", "--source-file", action="store", required="true", help="Input File")
    argparser.add_argument("-d", "--destination-file", action="store", required="true", help="Anonymised data output")
    argparser.add_argument("-r", "--replace-regex", action="store", required="true", help="Regex of source to replace")
    argparser.add_argument("-z", "--gzip", action="store_true", help="")
    args = argparser.parse_args()

    if args.gzip:
        print("Opening as GZIP")
        source = gzip.open(args.source_file, "r")
        destination = gzip.open(args.destination_file, "w")
    else:
        print("Opening as normal")
        source = open(args.source_file, "r")
        destination = open(args.destination_file, "w")
    replacements = {}

    for line in source:
        line = str(line)
        split = re.findall('{}'.format(args.replace_regex), line)
        if len(split) == 1:
            split = split[0]
        # print(split)
        if split:
            # "line" contains our pattern, and split contains
            if split in replacements:
                replace = replacements[split]
            else:
                replace = id_generator(len(split))
                replace = "/{}".format(replace[1:])
                replacements[split] = replace

            newline = line.replace(split, replace)
        else:
            newline = line
        destination.write(newline)
    source.close()
    destination.close()
