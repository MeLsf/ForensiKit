

class FileWriter:
    _instance = None

    def __new__(cls, filename):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.file = open(filename, 'a')
        return cls._instance

    def __del__(self):
        self.file.close()

    def write_to_file(self, text):
        self.file.write(text)
