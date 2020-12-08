class Dono:
    def __init__(self, nome, total_vendas, cnpj):
        self.nome = nome
        self.total_vendas = total_vendas
        self.cnpj = cnpj

    def set_total_vendas(self, vendas):
        self.total_vendas += vendas

    def get_nome(self):
        return self.nome

    def get_total_vendas(self):
        return self.total_vendas

    def get_cnpj(self):
        return self.cnpj


class Profissional:
    def __init__(self, nome, profissao):
        self.nome = nome
        self.comissao = 0
        self.profissao = profissao

    def get_profissao(self):
        return self.profissao

    def get_comissao(self):
        return self.comissao

    def get_nome(self):
        return self.nome

    def set_comissao(self, comissao):
        self.comissao += comissao


lista_profissionais = []
lista_dono = [Dono("João Pedro Santos de Mello", 0, "77.777.777/7777-77")]


def relatorio_profissioais():
    for profissional in lista_profissionais:
        print("Nome: ", profissional.get_nome(), "\nProfissão: ", profissional.get_profissao(), "\nComissão: ",
              profissional.get_comissao())


def profissionais_disponiveis():
    for indice, profissional in enumerate(lista_profissionais):
        print("Número: ", indice, "\nProfissional: ", profissional.get_nome())


def relatorio_dono():
    for relatorio in lista_dono:
        print("Nome: ", relatorio.get_nome(), "\nTotal de vendas: R$", relatorio.total_vendas,
              "\nCNPJ: ", relatorio.get_cnpj())


def cadastro_profissional():
    nome = input("Qual o nome do profissional? ")
    profissao = input("Qual a profissão dele? ")
    profissional = Profissional(nome, profissao)
    lista_profissionais.append(profissional)


def venda_profissional():
    profissionais_disponiveis()
    indice = int(input("Escolha pelo número: "))
    escolha = lista_profissionais[indice]
    dono = lista_dono[0]
    servico = int(input("Qual o valor serviço que o profissinal vendeu? "))
    if escolha.get_profissao() == 'cabeleireiro':
        escolha.set_comissao(servico * 0.75)
        dono.set_total_vendas(servico * 0.25)
    if escolha.get_profissao() == 'manicure':
        escolha.set_comissao(servico * 0.60)
        dono.set_total_vendas(servico * 0.40)



while True:
    escolha = input("""
    Menu
0-	Finalizar o Programa
1-	Cadastrar profissional
2-	Venda profissional
3-	Relatório de profissionais
4-	Relatório do dono

Escolha: """)

    if escolha == '0':
        print("Programa finalizado!")
        break
    if escolha == '1':
        cadastro_profissional()
    if escolha == '2':
        venda_profissional()
    if escolha == '3':
        relatorio_profissioais()
    if escolha == '4':
        relatorio_dono()
