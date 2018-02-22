from sys import argv

script, filename = argv

txt = open(filename)

print("Here is your file %r: " % filename)
print(txt.read())

print("Type the file name again: ")
file_name = input("> ")

text = open(file_name)

print(text.read())