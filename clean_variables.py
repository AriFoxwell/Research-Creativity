# Python 3 Scratch to read python and c files and output a cleaned file with all likely variables
# Specific requirements were to clean for the rest of the variables manually

source_file = input("Enter file location: ")
dest_file = input("Enter output file destination: ")

# open the source file, count number of lines, close it
file = open(source_file, "r")
num_lines = sum(1 for line in file)
file.close()

# open the source and destination files
file = open(source_file, "r")
output = open(dest_file, "w+")

# function to find common places for variables in Python code
def python_var(s):
    if "# " in s:
        return False
    elif "=" in s:
        return True
    elif "for " in s:
        return True
    elif " for " in s:
        return True
    elif "\tfor" in s:
        return True
    elif " as " in s:
        return True
    elif "def " in s:
        return True

# function to find common places for variables in java and c family code
def java_var(s):
    if "DEFINE" in s:
        return True
    elif "int" in s:
        return True
    elif "char" in s:
        return True
    elif "string" in s:
        return True
    elif "String" in s:
        return True
    elif "float" in s:
        return True
    elif "double" in s:
        return True
    elif "long" in s:
        return True
    elif "boolean" in s:
        return True
    elif "byte" in s:
        return True
    elif "short" in s:
        return True
    elif "static" in s:
        return True
    elif "public" in s:
        return True
    elif "private" in s:
        return True

# iterate through the lines of the files
# if that line is likely to have a variable, write it to the output
for i in range(0, num_lines):
    s = file.readline()
    if python_var(s) is True:
        x = str(i) + " " + s
        output.write(x)
    elif java_var(s):
        x = str(i) + " " + s
        output.write(x)
        
# close both files
file.close()
output.close()

exit(0)
