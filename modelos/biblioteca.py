from modelos.avaliacao import Avaliacao


# Classe Biblioteca
class Biblioteca:
    bibliotecas = []

    # Método construtor para inicializar os atributos do objeto
    def __init__(self, nome="", ativo=False) -> None:
        self.nome = nome
        self._ativo = ativo  # Atributo privado, com _propriedade
        self._avaliacao = []
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
