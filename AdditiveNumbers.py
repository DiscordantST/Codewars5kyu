def find_additive_numbers(num):
    for k in range(2, len(num)):
        for j in range(1, k):
            if k-j > 1 and num[j] == '0':
                continue
            a, b = j, k
            out = [num[:a], num[a:b]]
            while b < len(num):
                x = int(out[-2]) + int(out[-1])
                a, b = b, b + len(str(x))
                y = int(num[a:b])
                if x != y:
                    break
                out.append(str(y))
            else:
                return out
    return []
