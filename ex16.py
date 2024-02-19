# Import from sys the argv module
from sys import argv

# Those args is input from the terminal
script, fileName = argv

# Print in f-string triple single quotes the script name and the file name
print(f'''
    Run The script {script},
    And write the {fileName}.     
''')

# Open the txt in write mode
text = open(fileName, "w")

# Print in f-string what user inputs
print(f'write some thing in to the {fileName}: ')

# The input for the user store in line1
line1 = input('> ')

# With the write method write in to txt 
text.write(line1)

# Open the txt in read mode
text = open(fileName, "r")

# Print the all the file
print(f'read the file \n{text.read()}')

# Print some string
print("Now take those byte of the record")

# Open the txt in write mode
text = open(fileName, "w")

# This method delete all the previous writes
text.truncate()

# Print in f-string what user inputs
print(f'write again in to the {fileName}: ')

# The input for the user store in line2
line2 = input('> ')

# With the write method write in to txt 
text.write(line2)

# write in to txt the escape sequences 
text.write("\n")

# write in to txt the string 2024
text.write("2024")

# Open the txt in read mode
text = open(fileName, "r")

# Print the all the file
print(f'read the file \n{text.read()}')

# this method close the file 
text.close()