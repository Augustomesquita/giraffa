class Playlist:

    def __init__(self, nome, musicas):
        self.__nome = nome
        self.__musicas = musicas

    @property
    def teste(self):
        print("PASSOU NO GET")
        return self.__nome

    @teste.setter
    def teste(self, teste):
        print("PASSOU NO SET")
        self.__nome = teste

    def __len__(self):
        return len(self.__musicas)

    def __getitem__(self, item):
        return self.__musicas[item]
