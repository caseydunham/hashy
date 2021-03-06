"""
The MIT License

Copyright (c) 2011 Casey Dunham <casey.dunham@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

__version__ = '0.4.0'
__author__ = "Casey Dunham"
__license__ = 'MIT'

import os
import sys
import argparse
import hashlib
import glob

VERSION_STR = 'hashy ' + __version__
DEFAULT_ALGORITHM = 'sha256'

try:
    algorithms = repr(hashlib.algorithms)
except AttributeError, e:
    algorithms = repr(('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'))

BLOCK_SIZE = 1024

def hash(file, algorithm=DEFAULT_ALGORITHM):
    """ Read the file and return its hash """
    h = hashlib.new(algorithm)
    try:
        with open(file, 'rb') as f:
            while True:
                part = f.read(BLOCK_SIZE)
                if not part:
                    break
                h.update(part)
        return h.hexdigest()
    except IOError, reason:
        print reason
        return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='hash a file')
    parser.add_argument('--version', help='print version information', action='version', version=VERSION_STR)
    parser.add_argument('-verify', type=str, help='compute file hash and compare against passed in hash', metavar='verify')
    parser.add_argument('-hash', type=str, help='hash algorithm to use. can be one of ' + algorithms, metavar='hash',
        default=DEFAULT_ALGORITHM, choices=algorithms)
    parser.add_argument('file', type=str, help='file to compute hash')

    args = parser.parse_args()
    
    pattern = args.file
    if os.path.isdir(pattern):
        pattern = "%s/*" % args.file

    files = glob.glob(pattern)
    for f in files:
        h = hash(f, args.hash)
        if h:
            if args.verify:
                if h == args.verify:
                    print 'hashes match'
                else:
                    print 'hashes are not the same!'
            else:
                print '%s %s %s' % (args.hash, h, f)

