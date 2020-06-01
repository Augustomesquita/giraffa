from collections import namedtuple


def get_data_with_pagination():
    data = []
    limit_result = 100
    for offset in range(0, 1000, limit_result):
        data.append(offset)
    return data


def get_character():
    character = {
        "life": 500,
        "mana": 200,
        "equipaments": {
            "helmet": "Royal Helmet",
            "armor": "Demom Armor"
        }
    }

    character.update({"life": 1500})
    character["life"] = 2000
    return character


def get_input_number():
    try:
        return int(input("Enter a number: "))
    except ValueError:
        print("Invalid input number. Try again.")
        return get_input_number()


def input_file_content(file_name):
    text_file = open(file_name, "w")
    text_content = [
        prepare_text("this is my sample"),
        prepare_text("of text file"),
        prepare_text("in python."),
        prepare_text("my mission here is open,"),
        prepare_text("write and read this thing."),
    ]
    text_file.writelines(text_content)
    text_file.close()


def prepare_text(text):
    return "\n" + text


def output_file_content(file_name):
    text_file = open(file_name, "r")
    print(text_file.read())
    text_file.seek(0)

    for text in text_file.readlines():
        print(text)

    text_file.close()


def get_cards():
    ranks = [str(rank) for rank in range(2, 11)] + list("JQKA")
    suits = "paus ouros copas espadas".split()

    Card = namedtuple("Card", ["suit",  "rank"])
    cards = [Card(suit=suit, rank=rank) for suit in suits for rank in ranks]
    return cards
