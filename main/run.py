from flask import Flask
from random import choice
import string

app = Flask(__name__)


@app.route('/senhas')
def gerador_de_senha():
    values = string.ascii_lowercase + string.digits + string.punctuation
    key = ''
    for i in range(8):
        key += choice(values)

    return key


# def random_letters():
#     tamanho = 5
#     values = string.ascii_lowercase
#     senha = ''
#     for i in range(tamanho):
#         senha += choice(values)
#     return senha
#
# def random_numbers():
#     tamanho = 3
#     numbers = string.digits
#     key_numbers = ''
#     for i in range(tamanho):
#         key_numbers += choice(numbers)
#     return key_numbers
#
# def random_punctuation():
#     tamanho = 3
#     punctuations = string.punctuation
#     key_pontuaction = ''
#     for i in range(tamanho):
#         key_pontuaction += choice(punctuations)
#     return key_pontuaction


if __name__ == '__main__':
    app.run()
