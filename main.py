from random import choice

from flask import Flask, json
from markupsafe import escape
from modules import giraffa_tools as gt


app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/login')
def login():
    return json.dumps(gt.get_character())


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))


@app.route('/card')
def card():
    return json.dumps(choice(gt.get_cards()))


if __name__ == "__main__":
    # Test character
    my_character = gt.get_character()
    print(my_character.get("equipaments", "Not a key valid"))
    print(my_character)

    # Test data with pagination
    data = gt.get_data_with_pagination()
    print(data)

    # Test input number
    print(gt.get_input_number())

    # Test text file writing
    gt.input_file_content("text_file.txt")

    # Test text file reading
    gt.output_file_content("text_file.txt")

    #  Teste f-string to format a float output
    float_value = 10 / 3
    print(f'{float_value:7.2f}')

    uma_lista = [1, 2, 3]
    uma_tupla_ou_seja_imutavel = (1, 2, 3)
    um_set_ou_seja_valores_unicos = {1, 1, 1, 2, 2, 3, 4, 4}

    # Duck type testing
    print("uma_lista")
    print(uma_lista)

    print("uma_tupla_ou_seja_imutavel")
    print(uma_tupla_ou_seja_imutavel)

    print("um_set_ou_seja_valores_unicos")
    print(um_set_ou_seja_valores_unicos)

    print(
        "\n\nVarrendo um objeto que possui uma lista, apenas referenciado o "
        "proprio objetvo atraves do `Duck Typing` __getitem__"
        " e __len__, os quais nos permite indicar que nossa classe pode se comportar como uma lista")
    playlist = Playlist(nome="Tibia", musicas=["Rap", "Classic"])
    print(f"Tamanho da playlist: {len(playlist)}")
    for song in playlist:
        print(f"- {song}")


    # Test a simple Rest API
    app.run()

