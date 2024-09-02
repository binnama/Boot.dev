def filter_messages(messages):

    curse_word = "dang"
    clean_message = []
    dang_list = []

    for message in messages:
        # New lists
        new_message = []
        dang_counter = 0

        words = message.split()

        for word in words:
            if word == curse_word:
                words.remove(word)
                dang_counter += 1


        dang_list.append(dang_counter)
        new_message = " ".join(words)
        clean_message.append(new_message)


    return clean_message, dang_list
