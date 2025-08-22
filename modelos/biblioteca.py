from modelos.avaliacao import Avaliacao
from modelos.itens.item_biblioteca import ItemBiblioteca


# Classe Biblioteca
class Biblioteca:
    bibliotecas = []

    # Método construtor para inicializar os atributos do objeto
    def __init__(self, nome="", ativo=False) -> None:
        self.nome = nome
        self._ativo = ativo  # Atributo privado, com _propriedade
        self._avaliacao = []
        self._itens = []
        Biblioteca.bibliotecas.append(self)

    # Método __str__ é chamado quando usamos print() no objeto.
    # Ele deve retornar uma string que representa o objeto de forma legível.
    def __str__(self) -> str:
        return f"Biblioteca: {self.nome}\nAtivo: {"Sim" if self._ativo else "Não"}"

    # Método de classe
    @classmethod
    def listar_bibliotecas(cls):
        print(f"{'Nome da biblioteca'.ljust(25)} | {'Status'.ljust(25)} | {'Nota Média'}")
        for biblioteca in cls.bibliotecas:
            print(f"{biblioteca.nome.ljust(25)} | {str(biblioteca.ativo).ljust(25)} | {biblioteca.media_avaliacoes}")

    # Método set
    def alterna_estado(self):
        self._ativo = not self._ativo

    # Método get
    @property
    def ativo(self):
        return "ativada" if self._ativo else "desativada"

    # Método para atribuir avaliação para a biblioteca
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
        
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return "-"
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
        return round(soma / len(self._avaliacao), 1)

    # Adiciona item à biblioteca
    def adicionar_item(self, item: ItemBiblioteca):
        if not isinstance(item, ItemBiblioteca):
            raise TypeError("O item deve ser uma instância de ItemBiblioteca.")
        self._itens.append(item)
        
    # Exibir itens da biblioteca
    def exibir_itens(self):
        if not self._itens:
            print("Nenhum item cadastrado.")
            return
        print(f"Itens da Biblioteca {self.nome}\n")
        print(f"{'Título':<30} {'Autor':<20} {'Preço':<10} {'Edição/ISBN':<30} {'Tipo'}")
        for item in self._itens:
            print(f"{item._titulo:<30} {item._autor:<20} {item._preco:<10} {item._isbn if hasattr(item, '_isbn') else item._edicao:<30} {type(item).__name__}")