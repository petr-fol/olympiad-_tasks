def search_substr():
    with open("INPUT.txt", "r") as input_:
        str_ = input_.readline().strip()
        substr = input_.readline().strip()
        str_len = len(str_)
        substr_len = len(substr)
        difference = str_len - substr_len
        output_list = []

        for i_ in range(difference + 1):  # Используйте range() для итерации по индексам
            if substr == str_[i_:i_ + substr_len]:
                output_list.append(i_)

        with open('OUTPUT.txt', 'a') as output_:
            for i in output_list:
                output_.write(str(i) + " ")


# Вызываем функцию для выполнения кода
search_substr()

