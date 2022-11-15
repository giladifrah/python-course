def get_file_name(reprompt=False):
    if reprompt:
        print("Please enter a file name : ")
    file_name = input("Destination file name : ")
    return file_name or get_file_name(True)


file_name = get_file_name()

print(f"Please Enter your content. Entering an empty Line will write the content to {file_name}:\n")


with open(file_name, 'w') as f:
    eof = False
    lines = []

    while not eof:
        line = input()
        if line.strip():
            lines.append(f"{line}\n")
        else:
            eof = True

    f.writelines(lines)
    print(f"Lines written to {file_name}")
