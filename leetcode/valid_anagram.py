def isAnagram_1(s: str, t: str) -> bool:
    """
    Runtime: 84 ms
    Runtime beats 6.15 % of python3 submissions.
    """
    return sorted(s) == sorted(t)


def isAnagram_2(s: str, t: str) -> bool:
    """
    Runtime: 72 ms
    Runtime beats 8.52 % of python3 submissions.
    """

    if len(s) != len(t):
        return False

    def counter(s):
        count = {}
        for i in range(len(s)):
            if s[i] in count:
                count[s[i]] += 1
            else:
                count[s[i]] = 1

        return count

    s_count = counter(s)
    t_count = counter(t)

    for key in s_count:
        if s_count[key] != t_count.get(key, 0):
            return False
    return True


def isAnagram_3(s: str, t: str) -> bool:
    """
    Runtime: 60 ms
    Runtime beats 19.26 % of python3 submissions.
    """
    count = [0] * 26
    if len(s) != len(t):
        return False

    for i in range(len(s)):

        count[ord(s[i]) - 97] += 1
        count[ord(t[i]) - 97] -= 1

    for x in count:
        if x != 0:
            return False
    return True


def isAnagram_4(s: str, t: str) -> bool:
    """
    <<NOT MINE METHOD>>
    Runtime: 44 ms
    Runtime beats 75.86 % of python3 submissions.
    """
    s_dict = {}
    t_dict = {}
    if s == t:
        return True
    for i in s:
        try:
            s_dict[i] += 1
        except:
            s_dict[i] = 1
    for j in t:
        try:
            t_dict[j] += 1
        except:
            t_dict[j] = 1

    if len(s_dict) != len(t_dict):
        return False
    return t_dict == s_dict


from collections import Counter
def isAnagram_4(s: str, t: str) -> bool:
    """
    FASTEST ==>
    Runtime: 32 ms
    Runtime beats 98.19 % of python3 submissions.
    """
    return Counter(s) == Counter(t)


# Driver Code Starts
if __name__ == "__main__":
    s = input()
    t = input()

    print(isAnagram_1(s, t))

    print(isAnagram_2(s, t))

    print(isAnagram_3(s, t))
    
    print(isAnagram_4(s, t))