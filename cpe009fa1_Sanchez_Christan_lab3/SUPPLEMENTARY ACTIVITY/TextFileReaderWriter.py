# TextFileReaderWriter.py

class TextFileReaderWriter:
    def read(self, filepath):
        """Reads the content of a text file and returns it as a string."""
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        return content

    def write(self, filepath, data):
        """Writes the given data to a text file, overwriting any existing content."""
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(data)
