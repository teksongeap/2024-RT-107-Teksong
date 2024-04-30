user_input = input("Enter a word: ")
print("Length of word:", len(user_input))
print("Upper:", user_input.upper(), "Lower:", user_input.lower())
user_input0 = input("Enter a character: ")
count = 0
for c in user_input:
    if c == user_input0:
        count += 1
print("Character appeared this many times:", count)
user_input1 = input("Enter a substring: ")
print("Substring occurred this many times:", user_input.count(user_input1))
print("Reversed:", user_input[::-1])
starting_index = int(input("Input starting index: "))
ending_index = int(input("Input ending index: "))
print("Sliced word:", user_input[starting_index:ending_index])
user_input2 = input("Enter a character to replace: ")
user_input3 = input("Enter replacement character: ")
print("Replaced:", user_input.replace(user_input2, user_input3))
user_input4 = input("Enter a second word: ")
print("Concatenated: " + user_input + user_input4)
palindrome = False
if user_input[::-1] == user_input:
    palindrome = True
print("Is a palindrome?: ", palindrome)
print("Is a valid Python identifier?: ", user_input.isidentifier())
