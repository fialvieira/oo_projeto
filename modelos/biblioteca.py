class Biblioteca:
    def __init__(self, nome="", ativo=False) -> None:
        self.nome = nome
        self.ativo = ativo

    def __str__(self) -> str:
        return f"Biblioteca: {self.nome}\nAtivo: {"Sim" if self.ativo else "Não"}"

biblioteca_cidade = Biblioteca("Biblioteca Municipal", True)
biblioteca_shopping = Biblioteca("Biblioteca do Shopping", False)

bibliotecas = [biblioteca_cidade, biblioteca_shopping]

for biblioteca in bibliotecas:
    print(biblioteca)