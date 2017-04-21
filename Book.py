from os import *
from Utils import Format

class Book:
    def __init__(self, source):
        self._path = path.dirname(source)
        filenameext = path.splitext(path.basename(source))
        self._name = filenameext[0]
        dot_ext = filenameext[1]
        self._ext = Format[dot_ext[dot_ext.rfind(".")+1:].upper()]

    @property
    def path(self):
        return self._path

    @property
    def name(self):
        return self._name

    @property
    def ext(self):
        return self._ext.name.lower()

    @property
    def full_name(self):
        return self._name + '.' + self._ext.name.lower()