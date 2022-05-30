
def substring(string):

    string_splitada = str.split(string)

    if string_splitada[0] in string:
        return string_splitada[0]

    return -1


print(substring("hello world"))
