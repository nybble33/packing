#!/usr/bin/python
# -*- coding: utf-8 -*-

from subprocess import Popen

FILES = [
    {
        'directory': '/home/admin/radomir.biz/mysite/static/js_new/',
        'outputFile': 'radomir.script.min.js',
        'files': [
            'script.js',
            'nybble_script.js',
            'jquery.flexslider-min.js',
            'jquery.carouFredSel-6.2.1.js',
            'fancybox/jquery.fancybox.pack.js'
        ]

    }
]

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
    
    cmd = 'java -jar compiler.jar --js %s --js_output_file %s%s' % (
                                fullPath,
                                FILE['directory'],
                                FILE['outputFile']
                                )
    print cmd
    Popen(cmd, shell=True)
    #Popen('rm %s' % fullPath, shell=True)
    
