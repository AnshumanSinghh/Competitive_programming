
"""
    My runtime beats 83.39 % of python3 submissions (as per leetcode).
"""
def backspace_string(s: str, t: str) -> bool:

    def back_space(strs: str) -> str:
        s1 = []
        for i in range(len(strs)):

            if strs[i] != "#":
                s1.append(strs[i])

            elif strs[i] == "#" and len(s1) != 0:
                s1.pop()

        return s1

    a = back_space(s)
    b = back_space(t)

    print(a, b)
    return a == b


# Driver Code Starts
if __name__ == "__main__":

    s = input()

    t = input()

    print(backspace_string(s, t))
