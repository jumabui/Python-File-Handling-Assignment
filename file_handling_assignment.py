try:
    # File Creation
    with open("my_file.txt", "w") as file:
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Another line of text\n")
    print("File 'my_file.txt' created and initial content written.")

    # File Reading and Display
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print("Contents of my_file.txt:")
        print(contents)

    # File Appending
    with open("my_file.txt", "a") as file:
        file.write("Additional line 1\n")
        file.write("67890\n")
        file.write("Yet another line of text\n")
    print("Additional content appended to 'my_file.txt'.")

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied to access the file.")

finally:
    print("Execution completed.")
