def pig_it(text):
    simple_list = text.split()
    suffix = 'ay'
    simple_list_reverse = []
    for i in simple_list:
        for j in range(len(i)):
            if j == 0:
                if i[j].isalpha():
                    simple_list_reverse.append(i[j + 1:] + i[j] + suffix + " ")
                else:
                    simple_list_reverse.append(i[j])
    return ("".join(simple_list_reverse).strip())