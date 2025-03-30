1.Read a File and Handle Errors
Problem Statement:
1. The program attempts to open and read a text file named `sample.txt`.
2. It prints the content of the file line by line.
3. If the file does not exist, it handles the error gracefully and displays an appropriate message.

How It Works:
1. The program opens the file `sample.txt` in read mode.
2. It reads and prints the content of the file line by line.
3. If the file doesn't exist, the program will catch the `FileNotFoundError` and display an error message indicating that the file is missing.

Output:

- If the file `sample.txt` exists and contains the following:
- 
Reading file content:
Line1"This is a sample text.
Line2:It contains multiple lines.

- If the file `sample.txt` doesn't exists:
Error: The file 'sample.txt' was not found.


2.Write and Append Data to a File

This repository contains a Python program that demonstrates basic file handling operations. The program performs the following tasks:
1. Takes user input and writes it to a file named `output.txt`.
2. Appends additional data to the same file.
3. Reads and displays the final content of the file.

Problem Statement:
1. The program first takes a user input and writes it to `output.txt`.
2. Then, it appends additional user input to the same file.
3. Finally, it reads and displays the content of the file after writing and appending the data.

How It Works:
1. Step 1: The program opens `output.txt` in write mode (`"w"`) and writes the first user input to the file.
2. Step 2: The program then opens the same file in append mode (`"a"`) and appends additional text provided by the user.
3. Step 3: The program opens the file in read mode (`"r"`) and displays the final content of the file.

Output:
Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.
Enter additional text to append: Learning file handling in Python.
Data successfully appended.
Final content of output.txt:
Hello, Python!
Learning file handling in Python.

