# Project 3
# Name: Eeshan Mishra
# Instructor: S. Einakian
# Section: 05


# gets the 100 characters for the grid and the words that need to be searched using user input
# None --> list of strings, list of strings
def get_input():
    # Ask user to input 100 characters
    characters = input("Please entire 100 characters")
    # ask user to input the words that need to be searched
    words = input("Please enter a list of words separated by a space")
    # get a formatted grid and list of words by calling on a separate function that formats the input
    word, search_box = format_search(characters, words)
    return word, search_box


# formats the input from the text file into a word search
# string, string --> list of strings, list of strings
def format_search(characters, words):
    # takes the string of characters, splits them every ten characters, and stores it into a list (the grid)
    search_box = [characters[i: i + 10] for i in range(0, len(characters), 10)]
    # takes the list of words, splits them by every space, and stores them in a list
    word = words.split(" ")
    # removes the /n at the end of the list
    word[len(word)-1] = word[len(word)-1].strip()
    # returns the new list of words and the grid for the word search
    return word, search_box


# looks forward for each word in each row
# list of strings, list of strings --> Boolean, string, int, int
def word_forward(word, search_box):
    check = ""
    # sets the number of rows to 10
    for r in range(10):
        # sets the number of columns to 10
        for c in range(10):
            # check if the first letter of any word in the list is equal to any letter in the grid
            if search_box[r][c] == word[0]:
                # if the first letter of the word is present, set the letter equal to the empty initialized variable
                check += search_box[r][c]
                # check if the characters to the right of the first letter you found are equal to the rest of the
                # characters in the word
                for x in range(1, len(word)):
                    # while you check for the characters, check to make sure the word is within the range of ten columns
                    if c + x <= 9:
                        # if it is, and the characters in the grid match up with the characters in the word, then add
                        # the rest of the characters to the variable you added the first letter to
                        if search_box[r][c + x] == word[0 + x]:
                            check += search_box[r][c + x]
                            # if the entire word matches, return the boolean, the type of check you made, as well as the
                            # row and column where the word begins
                            if check == word:
                                return True, "(FORWARD) ", r, c
                        # if the letter don't match up, reset the value of the variable holding the characters
                        # after you check them and break
                        else:
                            check = ""
                            break
                    else:
                        break
            else:
                continue
    return False, "NOT FOUND", "A", "A"


# looks up for each word in each column
# list of strings, list of strings --> Boolean, string, int, int

# for this function, flip the grid to search column by column by switching the places for the  variables for r and c
# with each other from the last function
def word_up(word, search_box):
    check = ""
    # sets the number of columns to 10
    for c in range(10):
        # sets the number of rows to 10
        for r in range(10):
            # check if the first letter of any word in the list is equal to any letter in the grid
            if search_box[r][c] == word[0]:
                # if the first letter of the word is present, set the letter equal to the empty initialized variable
                check += search_box[r][c]
                # check if the characters to above the first letter you found are equal to the rest of the
                # characters in the word
                for x in range(1, len(word)):
                    # while you check for the characters, check to make sure the word is within the range of ten rows
                    if 0 <= r - x:
                        # if it is, and the characters in the grid match up with the characters in the word, then add
                        # the rest of the characters to the variable you added the first letter to
                        if search_box[r - x][c] == word[0 + x]:
                            check += search_box[r - x][c]
                            # if the entire word matches, return the boolean, the type of check you made, as well as the
                            # row and column where the word begins
                            if check == word:
                                return True, "(UP) ", r, c
                        # if the letter don't match up, reset the value of the variable holding the characters
                        # after you check them and break
                        else:
                            check = ""
                            break
                    else:
                        break
            else:
                continue
    return False, "NOT FOUND", "A", "A"


# looks backward for each word in each row
# list of strings, list of strings --> Boolean, string, int, int
def word_backward(word, search_box):
    check = ""
    # sets the number of rows to 10
    for r in range(10):
        # sets the number of columns to 10
        for c in range(10):
            # check if the first letter of any word in the list is equal to any letter in the grid
            if search_box[r][c] == word[0]:
                # if the first letter of the word is present, set the letter equal to the empty initialized variable
                check += search_box[r][c]
                # check if the characters to the left of the first letter you found are equal to the rest of the
                # characters in the word
                for x in range(1, len(word)):
                    # while you check for the characters, check to make sure the word is within the range of ten columns
                    if 0 <= c - x:
                        # if it is, and the characters in the grid match up with the characters in the word, then add
                        # the rest of the characters to the variable you added the first letter to
                        if search_box[r][c - x] == word[0 + x]:
                            check += search_box[r][c - x]
                            # if the entire word matches, return the boolean, the type of check you made, as well as the
                            # row and column where the word begins
                            if check == word:
                                return True, "(BACKWARD) ", r, c
                        # if the letter don't match up, reset the value of the variable holding the characters
                        # after you check them and break
                        else:
                            check = ""
                            break
                    else:
                        break
            else:
                continue
    return False, "NOT FOUND", "A", "A"


# looks down for each word in each column
# list of strings, list of strings --> Boolean, string, int, int

# for this function, flip the grid to search column by column by switching the places for the  variables for r and c
# with each other from the last function
def word_down(word, search_box):
    check = ""
    # sets the number of columns to 10
    for c in range(10):
        # sets the number of rows to 10
        for r in range(10):
            # check if the first letter of any word in the list is equal to any letter in the grid
            if search_box[r][c] == word[0]:
                # if the first letter of the word is present, set the letter equal to the empty initialized variable
                check += search_box[r][c]
                # check if the characters belowthe first letter you found are equal to the rest of the
                # characters in the word
                for x in range(1, len(word)):
                    # while you check for the characters, check to make sure the word is within the range of ten columns
                    if r + x <= 9:
                        # if it is, and the characters in the grid match up with the characters in the word, then add
                        # the rest of the characters to the variable you added the first letter to
                        if search_box[r + x][c] == word[0 + x]:
                            check += search_box[r + x][c]
                            # if the entire word matches, return the boolean, the type of check you made, as well as the
                            # row and column where the word begins
                            if check == word:
                                return True, "(DOWN) ", r, c
                        # if the letter don't match up, reset the value of the variable holding the characters
                        # after you check them and break
                        else:
                            check = ""
                            break
                    else:
                        break
            else:
                continue
    return False, "NOT FOUND", "A", "A"

# print(get_input())
