try:
    with open("sample.txt", "r") as file:
        print("Reading file content:")
        reading_file=file.read()
        line_number = 1
        for line in file:
            print(f"Line{line_number}:{reading_file}")
            line_number += 1
        
except FileNotFoundError:
   print("Error: The file 'sample.txt' was not found.")
