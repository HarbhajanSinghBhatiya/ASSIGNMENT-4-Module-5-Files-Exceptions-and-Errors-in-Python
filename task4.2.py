with open("output.txt", "w") as file:
    user_input = input("Enter text to write to the file: ")
    file.write(user_input + "\n") 
    print("\nData successfully written to output.txt.")

with open("output.txt", "a") as file:
    additional_data = input("Enter additional text to append: ")
    file.write(additional_data + "\n")
    print("\nData successfully appended.")

with open("output.txt", "r") as file:
    print("\nFinal content of output.txt:\n")
    print(file.read())
