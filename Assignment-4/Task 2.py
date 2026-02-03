# Write and Append Data to a File

Text = input("Enter text to write to the file: ")
with open("output.txt", "wt") as fh:
    fh.write(Text + "\n")

print("Data successfully written to output.txt.\n")

Append_text = input("Enter additional text to append: ")
with open("output.txt", "at") as fh:
    fh.write(Append_text + "\n")

print("Data successfully appended.\n")

print("Final content of output.txt:")
with open("output.txt", "rt") as fh :
    for line in fh:
        print(line.strip())