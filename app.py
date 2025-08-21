from modelos.biblioteca import Biblioteca

def main():
    biblioteca_cidade = Biblioteca("Biblioteca Municipal", True)
    biblioteca_cidade.alterna_estado()
    biblioteca_shopping = Biblioteca("Biblioteca do Shopping", False)
    biblioteca_shopping.alterna_estado()
    Biblioteca.listar_bibliotecas()

if __name__ == "__main__":
    main()