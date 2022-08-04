from gerenciador__funcoes import leia_int, leia_lista, leia_str


class Clientes:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def cadastrar_nome(self, nome):
        arquivo = open('nomes.txt', 'a')
        arquivo.write(nome)
        arquivo.close()

    def telefone(self, telefone):
        arquivo = open('telefones.txt', 'a')
        telefone = leia_int('Telefone: ')
        self.telefone = str(telefone)
        arquivo.write(telefone)
        arquivo.close()
        return telefone



# cadastrar_nascimento = leia_int('Nascimento: ')
# cadastrar_nascimento = str(cadastrar_nascimento)
#
#
# arquivo.write(cadastrar_nascimento)
# arquivo.close()
