from os import *
from Utils import Format

class Book:
    def __init__(self, source):
        self._path = path.dirname(source)
        filenameext = path.splitext(path.basename(source))
        self._name = filenameext[0]
        self._ext = Format[filenameext[1][-3:].upper()]

    @property
    def path(self):
        return self._path

    @property
    def name(self):
        return self._name

    @property
    def ext(self):
        return self._ext