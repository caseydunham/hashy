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
    hashy.py [-h] [--version] [-hash hash] file

    hash a file

    positional arguments:
        file        file to compute hash

    optional arguments:
       -h, --help  show this help message and exit
       --version   print version information
       -hash hash  hash algorithm to use. can be one of ('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512')

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
