from sys import argv

script, file_name = argv

print("We're going to erase %r." % file_name)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("Your choice? ")

print("Opening the file...")
target = open(file_name, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("All finally, we close it.")
target.close()