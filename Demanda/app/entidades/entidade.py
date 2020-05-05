class Produtos():
    def __init__(self, nome, marca, tamanho, quantidade, tipo):
        self.__nome = nome,
        self.__marca = marca,
        self.__tamanho = tamanho,
        self.__quantidade = quantidade,
        self.__tipo = tipo

        @property
        def nome(self):
            return self.__nome

        @nome.setter
        def nome(self, nome):
            self.__nome = nome

        @property
        def marca(self):
            return self.__marca

        @marca.setter
        def marca(self, marca):
            self.__marca = marca

        
        @property
        def tamanho(self):
            return self.__tamanho

        @tamanho.setter
        def tamanho(self, tamanho):
            self.__tamanho = tamanho


        @property
        def quantidade(self):
            return self.__quantidade

        @quantidade.setter
        def quantidade(self, quantidade):
            self.__quantidade = quantidade

        
        @property
        def tipo(self):
            return self.__tipo

        @tipo.setter
        def tipo(self, tipo):
            self.__tipo = tipo
