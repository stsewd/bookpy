def get_text_from_file(file_name):
    with open(file_name, mode='r') as file:
        return file.read()
