def scramble(s1, s2):
    for i in set(s2):
        if s2.count(i) > s1.count(i):
            return False
    else:
        return True

