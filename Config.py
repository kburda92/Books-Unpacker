import configparser
import os.path

class Config:
    def __init__(self):
        self._config_path = "config.ini"
        self.__init_file()

    def __init_file(self):
        self._config = configparser.ConfigParser()
        if not os.path.isfile(self._config_path):
            with open(self._config_path, 'w') as ini_file:
                self._config.add_section('Paths')
                self._config.set('Paths', 'Source', 'C:/')
                self._config.set('Paths', 'Dest', 'D:/')
                self._config.write(ini_file)
        self._config.read('config.ini')

    def save(self):
        with open(self._config_path, 'w') as ini_file:
            self._config.write(ini_file)

    @property
    def source_path(self):
        return self._config.get('Paths','Source')

    @source_path.setter
    def source_path(self, value):
        self._config.set('Paths', 'Source', value)

    @property
    def dest_path(self):
        return self._config.get('Paths', 'Dest')

    @dest_path.setter
    def dest_path(self, value):
        self._config.set('Paths', 'Dest', value)
