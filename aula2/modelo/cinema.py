import datetime
#Eduardo Gobbi Jorge | NUSP: 5980278
#Marcelo Olivetti França Neri de Almeida | NUSP: 15474654
#Rafael Romanello Rezende | NUSP: 15485490
#Vinícius Akira Durante Tahara | NUSP: 12547002


###listas
filmes = []
salas = []
sessoes = []

###dictionary
tipo_sala = {}

class Filme:

    def __init__(self, nome=None, data_estreia=None, data_saida=None, duracao=None):
#        self.codigo
        self.nome = nome
        self.data_estreia = data_estreia
        self.data_saida = data_saida
        self.duracao = duracao
        



class Sala:

    def __init__(self, numero=None, capacidade=None, tipo=None):
        self.numero = numero
        self.capacidade = capacidade
        self.tipo = tipo

class Sessao:
    def __init__(self, sala=None, filme=None, data=None, hora_inicio=None):
#        self.codigo
        self.sala = sala
        self.filme = filme
        self.data = data
        self.hora_inicio = hora_inicio
#        self.assentos

#metodos

def cadastrar_filme(nome, data_estreia, data_saida, duracao):
    try:
        datetime.strptime(data_estreia, "%d/%m/%Y")
        datetime.strptime(data_saida, "%d/%m/%Y")
    except ValueError:
        return None

    codigo = len(filmes) + 1
    filme = Filme(codigo, nome, data_estreia, data_saida, duracao)
    filmes.append(filme)
    return filme


def cadastrar_sala(numero, capacidade, tipo_sala):
    if numero <= 0 or capacidade <= 0:
        return None

    for sala_existente in salas:
        if sala_existente.numero == numero:
            return None

    sala = Sala(numero, capacidade, tipo_sala)
    salas.append(sala)
    return sala

def listar_filmes_por_data(data):
    try:
        data_convertida = datetime.strptime(data, "%d/%m/%Y")

        if data_convertida.strftime("%d/%m/%Y") != data:
            return "Data Inválida"
    except ValueError:
        return "Data Inválida"

    resultado = []

    for sessao in sessoes:
        if sessao.data == data and 0 in sessao.assentos:
            valor_ingresso = tipo_sala[sessao.sala.tipo]

            linha = (
                f"{sessao.codigo}: {sessao.filme.nome}, "
                f"sala {sessao.sala.numero} ({sessao.sala.tipo}), "
                f"{sessao.hora_inicio}h, {valor_ingresso} reais."
            )

            resultado.append(linha)

    if not resultado:
        return "Nenhum filme no dia escolhido."

    return "\n".join(resultado)



           