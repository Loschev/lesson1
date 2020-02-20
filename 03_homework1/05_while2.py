"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""
dict_of_questions = {
    'Как дела?': 'Хорошо!',
    'Что делаешь?': 'Программирую',
    'Вопрос': 'Ответ'
}


def ask_user_dict():
    while True:
        question = input('Введите ваш вопрос:\n')
        if question in dict_of_questions:
            print(dict_of_questions[f'{question}'])


if __name__ == "__main__":
    ask_user_dict()
