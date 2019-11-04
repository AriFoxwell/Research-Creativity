# Python 3 Scratch to count the number of variables after cleaned and output the average length
# Specific requirements were to clean for the variables manually and enter the data manually

# Specific file format:
#  (sof)var1(\n)
#       var2(\n)
#       var3 (eof)

source_file = input("Enter the cleaned file location: ")

# open the file to count the number of lines with witch to average/iterate through
file = open(source_file, "r")
num_lines = sum(1 for line in file)
file.close()

file = open(source_file, "r")

# x holds the number of characters
x = 0

# iterate through the file and sum up the number of characters
for i in range(0, num_lines):
    s = file.readline()
    x += len(s)-1

# print it to the console for manual input of the data
print("For ", num_lines, " words, ", x, " chars, the avg is ", x/num_lines)

file.close()

exit(0)
