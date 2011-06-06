# TDL
A simple library for downloading datastreams from the Tufts Digital Library.

## Using TDL

Basic usage of TDL:

    >>> from tdl import digitalobject
    >>> do = digitalobject.load("tufts:UA024.001.003.00001.00010")
    >>> do
    <tdl.digitalobject.Image4DS instance at 0x1004d7f38>
    >>> dir(do)
    ['__doc__', '__init__', '__module__', 'advanced', 'archival', 'basic', 'dc', 'thumb']
    >>> do.basic.url
    'http://repository01.lib.tufts.edu:8080/fedora/objects/tufts:UA024.001.003.00001.00010/datastreams/Basic.jpg/content'
    >>> do.basic.download("/path/to/filename.jpg")


 