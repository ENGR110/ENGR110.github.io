def remove_comments(f):
    lines2 = []
    for ln in f:
        good_chars = ""
        for i in range(len(ln)):
                if ln[i] == '/' and ln[i+1] == '/':
                    break
                else:
                    good_chars += ln[i]
        if len(good_chars):
            lines2.append(good_chars)
    return lines2

def remove_whitespace(f):
    lines2 = []
    for ln in f:
        good_chars = ""
        for ch in ln:
                if ch != ' ' and ch != '\n':
                        good_chars += ch
        if len(good_chars):
            lines2.append(good_chars)
    return lines2

def remove_whitespace_file(filename):
    lines2 = []
    with open(filename) as f:
        for ln in f:
            good_chars = ""
            for ch in ln:
                    if ch != ' ' and ch != '\n':
                            good_chars += ch
            lines2.append(good_chars)
    return lines2


if __name__ == "__main__":
    myfile = open("a.hack")
    print(remove_whitespace(myfile))
    myfile.seek(0)
    print(remove_comments(myfile))
    myfile.seek(0)
    print(remove_comments(remove_whitespace(myfile)))

    print("...")
    print(remove_whitespace_file("a.hack"))
