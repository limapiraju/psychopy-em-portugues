import time

responses = [" " * 15 for i in range (30)]

def response_box(responses):

    # criando uma lista vazia de respostas
    word_list = list()
    
    for i in range(5): # i = 0
        temp_string = f"""
    {(i * 6) + 1}. {responses[(i * 6) + 0]}
    {(i * 6) + 2}. {responses[(i * 6) + 1]}
    {(i * 6) + 3}. {responses[(i * 6) + 2]}
    {(i * 6) + 4}. {responses[(i * 6) + 3]}
    {(i * 6) + 5}. {responses[(i * 6) + 4]}
    {(i * 6) + 6}. {responses[(i * 6) + 5]}
    """
        word_list.append(temp_string)

    return word_list

word_list = response_box(responses)

for sublist in word_list:
    print(sublist)
