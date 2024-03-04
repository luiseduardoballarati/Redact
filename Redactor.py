string = "The quick brown fox jumps over the lazy dog!"

redact_list = ["Fox", "jumps", "dog"]

def redact(string, redact_list):

    new_list = []
    new_redact_list = []
    rmv = []

    for index, letter in enumerate(string):
        if letter.isalpha() or letter == " ":
            pass
        else:
            string = string.replace(letter, "")
            rmv.append([index, letter])

    for re in redact_list:
        new_redact_list.append(re.capitalize())

    string_splitted = string.split(" ")
    for st in string_splitted:
        if st in redact_list or st in new_redact_list:
            new_list.append("*"*len(st))
        else:
            new_list.append(st)

    res = ' '.join(new_list)

    for r in rmv:
        res = res[:r[0]] + r[1] + res[r[0]:]

    return res

print(redact(string, redact_list))