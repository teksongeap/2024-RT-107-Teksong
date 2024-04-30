def merge_the_tools(string, k):
    # your code goes here
    # substring_size = len(string) // k
    # k_list = [string[i * substring_size:(i + 1) * substring_size] for i in range(k)]
    # for substring in k_list:
    #     seen = set()
    #     unique = ''
    #     for c in substring:
    #         if c not in seen:
    #             unique += c
    #             seen.add(c)
    #     print(unique)
    newstring = ""
    mystring = list(string)
    while len(mystring) != 0:
        for i in range(k):
            if mystring[i] in newstring:
                print("duplicate:", mystring[i])
                continue
            else:
                newstring+=mystring[i]
                print("added to newstring:", mystring[i])
        print("before deletion:", mystring)
        del mystring[0:k]
        
        print("newstring before clearing:", newstring)
        newstring = ""

string, k = input(), int(input())
merge_the_tools(string, k)