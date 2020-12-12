def dist(str1,str2):
    len1 = len(str1)
    len2 = len(str2)

    if str1 == str2:
        return 0
    
    working_string = ""
    static_string = ""
    if len1 > len2:
        working_string = str2
        static_string = str1
    else:
        working_string = str1
        static_string = str2

    min_dist = 0

    if len(working_string) == 0:
        return len(static_string)

    if len1 != len2:
        if working_string[0] == static_string[0]:
            return dist(working_string[1:],static_string[1:])
        else:
            return min(1 + dist(working_string, static_string[1:]), 1+dist(working_string[1:],static_string[1:]))
    else:
        if working_string[0] == static_string[0]:
            return dist(working_string[1:], static_string[1:])
        else:
            return 1 + dist(working_string[1:], static_string[1:])

    return min_dist    


if __name__ == "__main__":
    print(dist("kitten", "sitting"))
    assert dist("kitten", "sitting") == 3
    print(dist("abc", "abcd"))
    assert dist("abc", "abcd") == 1
    print(dist("bobby", "bobi"))
    assert dist("bobby", "bobi") == 2