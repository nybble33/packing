#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from subprocess import Popen

def oneString(_string_):
    pattern = re.compile('(?s)\n\s*')
    __foo = pattern.sub('', _string_)
    pattern = re.compile('\s*')
    return pattern.sub('', __foo)

def compressCSS(filename):
    code = filename.read()
    p = re.compile('(?s)/\*.*?\*/')
    code = p.sub('', code)
    p = re.compile('(?s)[^}](.*?\})')
    ms = p.findall(code)
    for m in ms:
        print '-------------------'
        print m
        print oneString(m)
    print '--- end parsing'


FILES = [
    {
        'directory': '/home/admin/radomir.biz/mysite/static/css_new/',
        'outputFile': 'nybble_style.min.css',
        'files': [
            'nybble_style.css'
        ]
    }
]

if __name__ == '__main__':
    print 'Begin combining files...'
    for FILE in FILES:
        fullPath = FILE['directory'] + FILE['outputFile']+'.tmp'
        print 'Creating ouput file - ' + fullPath
        outputFile = open(fullPath, 'w')
        for jsFile in FILE['files']:
            _fullPath = FILE['directory'] + jsFile
            print 'Reading file - ' + _fullPath
            code = open(_fullPath, 'r').read()
            outputFile.write(code)
        outputFile.close()
        outputFile = open(fullPath, 'r')
        compressCSS(outputFile)