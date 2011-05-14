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

import argparse
import hashlib

VERSION = '0.1'
VERSION_STR = 'hashy ' + VERSION
DEFAULT_ALGORITHM = 'sha256'

READ_SIZE = 1024

algorithms = repr(hashlib.algorithms)

def hash_file(hash, file):
    h = hashlib.new(args.hash)
    try:
        with open(file, 'rb') as f:
            while True:
                part = f.read(READ_SIZE)
                if not part:
                    break
                h.update(part)    
        return h.hexdigest()
    except IOError, reason:
        print reason
        return None
    
def parse_args():
    parser = argparse.ArgumentParser(description='hash a file')
    parser.add_argument('--version', help='print version information', action='version', version=VERSION_STR)
    parser.add_argument('-hash', type=str, help='hash algorithm to use. can be one of ' + algorithms, metavar='hash', 
	    default=DEFAULT_ALGORITHM, choices=hashlib.algorithms)
    parser.add_argument('file', type=str, help='file to compute hash')

    return parser.parse_args()
        
if __name__ == '__main__':
    args = parse_args()
    hash = hash_file(args.hash, args.file)
    if hash:
        print '%s:%s' % (args.hash, hash)
    
