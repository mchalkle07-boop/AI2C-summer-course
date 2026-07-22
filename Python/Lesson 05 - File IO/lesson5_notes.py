## Hands-On #1

### Exercise 0: Environment Set-up

# Clone the repository at `https://github.com/shafe123/AI2C-python-files.git`.

# in terminal run git clone 'website address'

# ### Exercise 1: Get Current Working Directory

# **Goal**: Use Python to print the current working directory.

# ✅ *Check*: Run the script and confirm it prints the full path of your working directory.

import os
from pathlib import Path

# print(Path.cwd())

### Exercise 2: Change Directory

# **Goal**: Change into a directory named `projects`.

# ✅ *Check*: Ensure that you are now in the `projects` directory. Create it first if it doesn't exist.

# create the folder if it doesn't already exist
# Path("projects").mkdir(exist_ok=True)

# # move into the projects folder, the directory we just created
# os.chdir("projects")

# # check where we are, show new location
# print(Path.cwd())

# ### Exercise 3: List Directory Contents

# **Goal**: List all files and directories in the current directory.

# ✅ *Check*: Compare the output to the `ls` command in your terminal.

# Path(".") means current directory, .iterdir looks at everything inside the current folder 
# for item in Path(".").iterdir():
#     if item.is_dir():
#         # item.name prints only the name, not the full path
#         print("DIR:", item.name)
#     else:
#         print("FILE: ", item.name)

# ### Exercise 4: Create a Directory

# **Goal**: Create a directory named `data`.

# ✅ *Check*: Verify the directory exists using `pathlib` or by checking in your terminal.
# create directory named 'data'
# Path("data").mkdir(exist_ok=True)
# # print CWD current working directory, current location
# print(Path.cwd())

# ### Exercise 5: Create Nested Directories

# **Goal**: Create nested directories `a/b/c` in one call.

# ✅ *Check*: Use `pathlib` to confirm creation.
# writing a / b / c creates nested, parents=True creates any missing parent folders
# Path("a/b/c").mkdir(parents=True, exist_ok=True)

# print("Nested folders a/b/c created successfully.")

# ### Exercise 6: Remove a File

# **Goal**: Delete a file named `temp.txt`.

# ✅ *Check*: Use `pathlib` to validate that the file no longer exists.

# This creates the txt file, in current directory AI2C-PYTHON-FILES
# Path("tmp.txt").write_text("This is a temp file, meant to be deleted")   # This is what to write in the txt file

# This deletes the tmp.txt file with .unlink
# Path("tmp.txt").unlink()

# print("tmp.txt has been deleted")

# ### Exercise 7: Remove an Empty Directory

# **Goal**: Delete an empty directory named `old_data`.

# ✅ *Check*: If the directory is not empty, this will raise an error. Try clearing it first.

# This deletes the old_data directory/folder
# Path("old_data").rmdir()

# print("old_data directory has been deleted.")

# ### Exercise 8: Rename a File

# **Goal**: Rename `example.txt` to `renamed_example.txt`.

# ✅ *Check*: Confirm the new name exists and the old one doesn't.
# .rename is used to do just that
# Path("old_data").rename("renamed_example.txt")

# print("File has been renamed.")

# ### Exercise 9: Check File or Directory Type

# **Goal**: Determine whether `target` is a file or directory.

# ✅ *Check*: Create a test file or directory and run the script to see the correct output.

# target = Path('target')    #must use '   ' 
# # create the directory
# # target.mkdir(exist_ok=True)
# # if loop to determine if the target is a file or directory
# if target.is_file():
#     print("It's a file.")
# elif target.is_dir():
#     print("It's a directory.")
# else:
#     print("It doesn't exist")

# ## Hands-On #2

# This series of exercises helps you understand how to create, read, append, and handle files in Python using both built-in `open()` and the `pathlib` module.


# ### Exercise 10: Create and Write to a File

# **Goal**: Create a file called `log.txt` and write a single line to it.

# ✅ *Check*: Open `log.txt` and verify the line was written.

# This is easiest, but requires "from pathlib import Path"
# Path("log.txt").write_text("This the first log entry.\n")

# OR

# with open("log.txt", "w") as f:    # with open, opens the file and closes when done  # 'w' means write mode, will create or overwrite the file
#     f.write("This is the first log.\n")     # write text on one line


# ### Exercise 11: Read the File

# **Goal**: Read and print the contents of `log.txt`.

# ✅ *Check*: Ensure the output matches the line you wrote previously.

# content = Path("log.txt").read_text()
# print(content)

# OR

# with open("log.txt", 'r') as f:
#     content = f.read()
#     print(content)
# ### Exercise 12: Append a Line to the File

# **Goal**: Add another line to `log.txt` without removing the original content.

# ✅ *Check*: Re-read the file and confirm both lines are present.

# ---

# ### Exercise 13: Write Multiple Lines

# **Goal**: Write multiple lines to a new file using a list.

# ✅ *Check*: Open `multi.txt` and confirm all three lines are present.

# ---

# ### Exercise 14: Read a File Line by Line

# **Goal**: Read `multi.txt` and print each line one at a time.

# ✅ *Check*: Each line should print without extra blank lines.

# ---

# ### Exercise 15: Count Lines in a File

# **Goal**: Count how many lines are in `multi.txt`.

# ✅ *Check*: The count should be 3 if using the previous file.

# ---

# ### Exercise 16: Read a File Safely

# **Goal**: Try reading a file that may not exist and handle the error.

# ✅ *Check*: Make sure the program doesn't crash if the file is missing.

# ---

# ### Exercise 17: Use `pathlib` to Read/Write

# **Goal**: Use `pathlib.Path` instead of `open()`.

# ✅ *Check*: The file should contain the message, and it should print to the screen.


# ## Stretch Goals

# **Goal**: Print the size and last modified time of `data.csv`.

# ✅ *Check*: Match file size with `ls -l` and modification time with `stat` in the terminal.

# **Goal**: Gain a deeper understanding of os and Pathlib.

# Create a short listing of the overlapping features of os and Pathlib.  Why might one prefer one module over the other?


# Manipulating files:

# #OPEN
# with open('input.txt', 'r') as file:        
#     lines = file.readlines()
#     for line in lines:
#         print(line)
# #WHAT TO WRITE
# text_to_write = [
#     "This is a new line of text.\n"
#     "Here is another line.\n"
#     "And yet another line.\n"
# ]
# #WRITE
# with open("output.txt", "w") as file:
#     for text in text_to_write:
#         file.write(text)

# both in one line:
# with open('input.txt', 'r') as input, open('output.txt', 'w') as output:
#     for line in input:
#         output.write()

# write a script to write 100 random integers on new lines


import random

# 1. Create and write 5 random numbers to the file
with open('integers.txt', 'w') as file:
    for _ in range(50, 100):
        file.write(str(random.randint(1, 100)) + '\n')

# 2. Read the numbers back from the file
with open('integers.txt', 'r') as file:
    lines = file.readlines()

# 3. Use the first number as the starting point
minimum = float(lines[0])
maximum = float(lines[0])
total_sum = 0

# 4. Find min, max, and sum
for line in lines:
    number = float(line)
    total_sum += number
    
    if number < minimum:
        minimum = number
    if number > maximum:
        maximum = number

# 5. Calculate the true average
average = total_sum / len(lines)

print("Maximum:", maximum)
print("Minimum:", minimum)
print("Average:", average)





# for line in range(100):
#     random_num = random.randit(50, 100)
#     file.write(str(random_num)) + \n
# write one that reads the file above finds min value, max value, and average