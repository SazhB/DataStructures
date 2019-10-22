def main():

    _end = '*'

    
    def make_trie(*words):

        trie = dict()

        for word in words:
            # creates a temp dict
            # temp dict is inherited root
            temp_dict = trie

            for letter in word:
                # updates temporary dict and adds current
                # letter and a sub-dictionary
                temp_dict = temp_dict.setdefault(letter, {})


            temp_dict[_end] = _end
        return trie


    trie = make_trie('hi', 'hello', 'whatsup')
    print(trie)


if "__name__" == "__main__":
    main()
