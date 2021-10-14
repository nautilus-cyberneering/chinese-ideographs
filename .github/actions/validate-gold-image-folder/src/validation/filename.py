class Filename():
    def __init__(self, filename):
        self.parse(filename)

    def parse(self, filename):
        self.filename = filename
        self.artwork_id, char, rest = filename.partition("-")
        self.purpose_code, char, rest = rest.partition(".")
        self.transformacion_code, char, rest = rest.partition(".")
        self.type_code, char, rest = rest.partition(".")
        self.extension, char, rest = rest.partition(".")

    def __str__(self):
        return self.filename
