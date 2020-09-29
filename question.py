# Given a string, find a substring based on the following conditions: * The substring must be the longest one of all the possible substring
#  in the given string. * There must not be any repeating characters in the substring. * If there is more than one substring satisfying the
#   above two conditions, then print the substring which occurs first. * If there is no substring satisfying all the aforementioned conditions
#    then print -1.

def duplicate(string):
    new_str = []
    new_chars = []
    for i in range(0,len(string)):
        if i == 0:
            new_str += string[0]
        else:
            if string[i] not in new_str:
                new_str += string[i]
    new_chars.append("".join(new_str))
    return new_chars
string = 'Saathi'
same = duplicate(string)
print("Older String:",string)
print("The new string:",same[0])
