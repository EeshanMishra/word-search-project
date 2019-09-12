# Project 3
# Name: Eeshan Mishra
# Instructor: S. Einakian
# Section: 05


from funcs import*


# calls on the functions in funcs.py
# None --> None
def main():
    # get the list of words and the list required ot make the crossword grid
    word, search_box = get_input()

    # print the formatted grid
    for u in range(len(search_box)):
        print(search_box[u])

    for i in range(len(word)):

        # call return values
        fboolean, fchecker, fr, fc = word_forward(word[i], search_box)

        uboolean, uchecker, ur, uc = word_up(word[i], search_box)

        bboolean, bchecker, br, bc = word_backward(word[i], search_box)

        dboolean, dchecker, dr, dc = word_down(word[i], search_box)

        # print info in the correct format based on the return values
        if fboolean:
            print(word[i] + ": " + str(fchecker) + "row: " + str(fr) + " column: " + str(fc))

        elif uboolean:
            print(word[i] + ": " + str(uchecker) + "row: " + str(ur) + " column: " + str(uc))

        elif bboolean:
            print(word[i] + ": " + str(bchecker) + "row: " + str(br) + " column: " + str(bc))

        elif dboolean:
            print(word[i] + ": " + str(dchecker) + "row: " + str(dr) + " column: " + str(dc))

        else:
            print(word[i] + ": word not found")


if __name__ == '__main__':
    main()


