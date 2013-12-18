#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from subprocess import Popen


def oneString(_string_):
    pattern = re.compile('(?s)\n\s*')
    __foo = pattern.sub('', _string_)
    pattern = re.compile('\{\s*\}')
    return pattern.sub('', __foo)
    

def compressCSS(code):
    p = re.compile('(?s)/\*.*?\*/')
    code = p.sub('', code)
    p = re.compile('(?s)[^}](.*?\})')
    ms = p.findall(code)
    foo = ''
    for m in ms:
        foo += oneString(m) + '\n'
    return foo


FILES = [
    {
        'directory': '/home/admin/radomir.biz/mysite/static/css_new/',
        'outputFile': 'radomir_style.min.css',
        'files': [
            'nybble_style.css',
            'style.css'
        ]
    }
]

if __name__ == '__main__':
    print 'Begin combining files...'
    codeToCompress = ''
    for FILE in FILES:
        for cssFile in FILE['files']:
            _fullPath = FILE['directory'] + cssFile
            print 'Reading file - ' + _fullPath
            codeToCompress += open(_fullPath, 'r').read()
        fullPath = FILE['directory'] + FILE['outputFile']
        print 'Creating ouput file - ' + fullPath
        outputFile = open(fullPath, 'w')
        outputFile.write(compressCSS(codeToCompress))