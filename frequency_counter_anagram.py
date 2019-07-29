def validAnagram(a,b):
    if len(a) != len(b):
        return "false"

    dict_a = {}
    # dict_b = {}

    for letter in a:
        if letter not in dict_a:
            dict_a[letter] = 1
        else:
            dict_a[letter] += 1

    # for letter in b:
    #     if letter not in dict_b:
    #         dict_b[letter] = 1
    #     else:
    #         dict_b[letter] += 1

    # for key in dict_a:
    #     if key not in dict_b:
    #         return "false"
    #
    #     if dict_a[key] != dict_b[key]:
    #         return "false"
    #
    #     return "true"

    for index in range(len(b)):
        letter = b[index]
        if letter not in dict_a:
            return "false"

        if dict_a[letter] > 0:
            dict_a[letter] -= 1
        else:
            return "false"




# validAnagram('','')
validAnagram('aaz','zza')
# validAnagram('anagram','nagaram')
# validAnagram('rat','car')
