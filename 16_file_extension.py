#Write a Python program to accept a filename from the user and print the extension of that.


filename = input("Enter the filename with extension : ")

print(f"File extension is .{filename.split('.')[1]}")