from datetime import datetime
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

    def __init__(self, codigo=None, nome=None, data_estreia=None, data_saida=None, duracao=None):
        self.codigo = codigo
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
    def __init__(self, codigo=None, sala=None, filme=None, data=None, hora_inicio=None, capacidade=0):
        self.codigo = codigo
        self.sala = sala
        self.filme = filme
        self.data = data
        self.hora_inicio = hora_inicio
        self.assentos = {numero: 0 for numero in range(1, capacidade + 1)}

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

def cadastrar_valor_ingresso(tipo_sala, valor_ingresso):
    if valor_ingresso <= 0 or not isinstance(valor_ingresso, int):
        return False
    tipo_sala[tipo_sala] = valor_ingresso
    return True

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
            return "Data invalida."
    except ValueError:
        return "Data invalida."

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

def cadastrar_sessao(numero_sala, codigo_filme, data_sessao, hora_inicio):
    if (type(numero_sala) is not int or type(codigo_filme) is not int or
            type(hora_inicio) is not int or not 0 <= hora_inicio <= 23 or
            not isinstance(data_sessao, str)):
        return None

    try:
        datetime.strptime(data_sessao, "%d/%m/%Y")
    except ValueError:
        return None

    sala = next((sala for sala in salas if sala.numero == numero_sala), None)
    if sala is None:
        return None

    for sessao in sessoes:
        if (sessao.sala == numero_sala and sessao.data == data_sessao and
                sessao.hora_inicio == hora_inicio):
            return None

    codigo = len(sessoes) + 1
    sessao = Sessao(codigo, numero_sala, codigo_filme, data_sessao,
                    hora_inicio, sala.capacidade)
    sessoes.append(sessao)
    return sessao