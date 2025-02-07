from modelos .avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"{self._nome} | {self._categoria}"

    def listar_restaurantes():
        print(f"{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}")
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante._ativo}")

    @property
    def ativo(self):
        return "⌧" if self._ativo else "☐"

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return "-"
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quandidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quandidade_de_notas, 1)
        return media

    # def adicionar_bebida_no_cardapio(self,bebida):
    #     self._cardapio.append(bebida)
    #
    # def adicionar_prato_no_cardapio(self,prato):
    #     self._cardapio.append(prato)

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f"Cardapio do restaurante {self._nome}\n")
        for i,item in enumerate(self._cardapio,start=1):
            if hasattr(item, "descricao"):
                mensagem_prato = f"{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}"
                print(mensagem_prato)
            else:
                mensagem_bebida = f"{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}"
                print(mensagem_bebida)

