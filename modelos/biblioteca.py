# Classe Biblioteca
class Biblioteca:
    bibliotecas = []

    def __init__(self, nome="", ativo=False) -> None:
        self.nome = nome
        self._ativo = ativo # Atributo privado, com _propriedade
        Biblioteca.bibliotecas.append(self)

    def __str__(self) -> str:
        return f"Biblioteca: {self.nome}\nAtivo: {"Sim" if self._ativo else "Não"}"

    def listar_bibliotecas():
        for biblioteca in Biblioteca.bibliotecas:
            print(f"{biblioteca.nome} | {biblioteca.ativo}")
    
    # Método set  
    def alterna_estado(self):
        self._ativo = not self._ativo
    
    # Método get
    @property
    def ativo(self):
        return "ativada" if self._ativo else "desativada"
    


biblioteca_cidade = Biblioteca("Biblioteca Municipal", True)
biblioteca_cidade.alterna_estado()
biblioteca_shopping = Biblioteca("Biblioteca do Shopping", False)
biblioteca_shopping.alterna_estado()

Biblioteca.listar_bibliotecas()