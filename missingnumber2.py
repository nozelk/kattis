def find(s):
    SUM, SUM2 = 0, 0
    count = 1
    while s:
        SUM += count
        num_str = str(count)
        if s.startswith(num_str):
            SUM2 += count
            s = s[len(num_str):]
        else:
            return count
        count += 1
    return count



def find2(s):
    SUM, SUM2 = 0, 0
    count = 1
    while s:
        SUM += count
        if count < 10:
            if len(s) < 1:
                break
            number = int(s[0])
            s = s[1:]
        else:
            if len(s) < 2:
                break
            number = int(s[0] + s[1])
            s = s[2:]
            
        SUM2 += number

        if SUM != SUM2:
            return count
        count += 1
    return count



n = int(input())
s = input()
print(find(s), find2(s))