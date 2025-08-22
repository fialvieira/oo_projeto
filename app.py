from modelos.biblioteca import Biblioteca

def main():
    biblioteca_cidade = Biblioteca("Biblioteca Municipal", True)
    # biblioteca_cidade.alterna_estado()
    biblioteca_cidade.receber_avaliacao("Filipe Vieira", 10.0)
    biblioteca_shopping = Biblioteca("Biblioteca do Shopping", False)
    # biblioteca_shopping.alterna_estado()
    biblioteca_shopping.receber_avaliacao("João Silva", 8.5)
    Biblioteca.listar_bibliotecas()

if __name__ == "__main__":
    main()