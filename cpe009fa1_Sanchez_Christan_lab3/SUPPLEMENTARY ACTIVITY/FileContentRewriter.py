# Example usage
from TextFileReaderWriter import TextFileReaderWriter

# Create an instance of TextFileReaderWriter
file_rw = TextFileReaderWriter()

# Write data to a text file
file_rw.write('example.txt', 'Hello World, I am Christan Sanchez.')

# Read data from the text file
content = file_rw.read('example.txt')
print(content)
