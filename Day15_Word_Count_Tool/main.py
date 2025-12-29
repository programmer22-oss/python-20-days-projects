# file_name = "sample.txt"

# file_name = input("Enter the file name: ")

path_name = input("please enter the file path: ")

with open(path_name, "r") as file:
    lines = file.readlines()

line_count = len(lines)
word_count = 0

for line in lines:
    words = line.split()
    word_count += len(words)

print("📄 File Analysis")
print("Total Lines:", line_count)
print("Total Words:", word_count)
print("File Name:", file_name)