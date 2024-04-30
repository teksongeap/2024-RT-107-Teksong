import random

wordlist = ["alpha", "bravo", "charlie", "darling", "engine"]
desiredwordlist = []
for i in range(len(wordlist)):
    desiredwordlist.append(random.choice(wordlist))
    
def check_wordlist():
    if wordlist == desiredwordlist:
        print("Wordlists match!")
        return True
    else:
        return False

def menu():
    print("Current list:", wordlist)
    print("Target list:", desiredwordlist)
    print("Make the lists match!")
    print("1. Append a word")
    print("1. Extend the list")
    print("3. Concatenate two elements")
    print("4. Traverse the list")
    print("5. Modify an element")
    print("6. Insert an element at index")
    print("7. Pop an element from the list")
    print("8. Remove a specific element")
    print("9. Sort the list in ascending or descending order")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        word = input("Enter a word: ")
        wordlist.append(word)
    elif choice == 2:
        userlist = input("Enter a space separated list: ").split()
        wordlist.extend(userlist)
    elif choice == 3:
        try:
            # Attempt to read indices from the user and modify the list
            index1 = int(input("Enter the index of the first element: "))
            index2 = int(input("Enter the index of the second element: "))

            # Add the element at index2 to the element at index1
            wordlist[index1] += wordlist[index2]
            # Remove the element at index2
            del wordlist[index2]
        except ValueError:
            # Handles cases where the input is not a valid integer
            print("Please enter a valid integer for indices.")
        except IndexError:
            # Handles cases where the input indices are out of the valid range
            print("Invalid index - make sure the indices are within the range of the list.")
    elif choice == 4:
        print("List elements:")
        for word in wordlist:
            print(word)
    elif choice == 5:
        index = int(input("Enter the index of the element to modify: "))
        if index >= 0 and index < len(wordlist):
            word = input("Enter the new word: ")
            wordlist[index] = word
        else:
            print("Invalid index")
    elif choice == 6:
        index = int(input("Enter the index to insert at: "))
        if index >= 0 and index <= len(wordlist):
            word = input("Enter the new word: ")
            wordlist.insert(index, word)
        else:
            print("Invalid index")
    elif choice == 7:
        if len(wordlist) > 0:
            print("Popped:", wordlist.pop())
        else:
            print("List is empty")
    elif choice == 8:
        word = input("Enter a word to remove: ")
        try:
            wordlist.remove(word)
        except ValueError:
            print("Word not found!")
    elif choice == 9:
        ascending = input("Sort in ascending order? (y/n) ").lower() == "y"
        wordlist.sort(reverse=not ascending)
    else:
        print("Invalid choice")

    return

while (check_wordlist() == False):        
    menu()


