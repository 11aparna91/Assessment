def missingWords3(s, t):
    """
    this solution does not work for all test cases.
    
    inputs:
    s = string
    t = string
    output: 
    return
    each
    word
    """
    # missingWords = []
    
    new_s = s.split()
    new_t = t.split()
    missing = []
    j = 0

    for i in range(len(new_s)):
        if j <= len(new_t) - 1:
            if new_s[i] != new_t[j]:
                missing.append(new_s[i])
            else:
                j += 1

        if (j>=(len(new_t)-1) and new_s[i] != new_t[j-1]):
            missing.append(new_s[i])

    return missing

if _name_ == '_main_':
    
    s = 'I am using HackerRank to improve programming'
    t = 'am HackerRank to improve'
    print('Test s, t:')
    print(missingWords3(s, t))

    first = 'Python is an easy to learn powerful programming language It has efficient high-level data structures and a simple but effective approach to objectoriented programming Python elegant syntax and dynamic typing'
    second = 'Python is an easy to learn powerful programming language'
    print('Test first, second')
    print(missingWords3(first, second))
