class ISBNNotFoundError(Exception):
    def __init__(self, file_name):
        Exception.__init__(self, "Any valid ISBN has been found in " + "''" + file_name + "'")
