hashy [![endorse](http://api.coderwall.com/caseydunham/endorse.png)](http://coderwall.com/caseydunham) 
==

hashy is a simple wrapper around the python (version 2.7.1 and higher) hashlib module to compute file hashes.   
currently supports:
 
 * md5 
 * sha1
 * sha224 
 * sha256
 * sha384
 * sha512


Usage 
==
    hashy.py [-h] [--version] [-hash hash] 'pattern'

    hash a file

    positional arguments:
        pattern        file glob pattern to compute hashes of (in single quotes)

    optional arguments:
       -h, --help  show this help message and exit
       --version   print version information
       -hash hash  hash algorithm to use. can be one of ('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512')

The pattern field can be any valid file python glob pattern. Needs to be surrounded in ' (single quotes)

Example Output
==

When run, hashy will produce a list of all the files it has hashed to stdout.

    $ python hashy.py '*'
    sha256 a717b635ea745e4536a0b3b07c8a580c23ea5e2c362820c3389c0de8e59f2e41 hashy.py
    sha256 d1d068fb37633c2001d10a72e5cb54840b3a6e2f02e60fcca2b95cd5ff8c0a18 README.md


License
==

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
