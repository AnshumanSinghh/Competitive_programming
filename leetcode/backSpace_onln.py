def cleanStr(s):
    final_str = ""

    for each in s:
        if each == "#": final_str = final_str[:-1]
        
        else:final_str += each
            
    return final_str

def backspaceCompare(s, t):
    s = cleanStr(s)
    t = cleanStr(t)
    return s == t


if __name__ == "__main__":
    s = input()

    t = input()

    print(backspaceCompare(s, t))
