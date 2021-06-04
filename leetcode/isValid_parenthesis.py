def isValid(s: str) -> bool:
    ans = []
    top = ""
    for x in s:
        empty = len(ans)
        if empty != 0:
            top = ans[-1]
        if x == "{" or x == "[" or x == "(":
            ans.append(x)

        elif x == "}" and top == "{" and empty != 0:
            ans.pop()

        elif x == "]" and top == "[" and empty != 0:
            ans.pop()

        elif x == ")" and top == "(" and empty != 0:
            ans.pop()
        else:
            ans.append(x)
    return (len(ans) == 0)

print(isValid(input()))
