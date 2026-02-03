# Read a File and Handle Errors

try:
    print("Reading file content: ")
    with open("sample.txt", "rt") as fh:
        Line1 = fh.readline().strip()
        Line2 = fh.readline().strip()
        print(f'Line 1: {Line1}')
        print(f"Line 2: {Line2}")
        fh.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")





