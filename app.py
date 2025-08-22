from modelos.biblioteca import Biblioteca
from modelos.itens.livro import Livro
from modelos.itens.revista import Revista

def main():
    # Definição de objetos de Bibliotecas
    biblioteca_cidade = Biblioteca("Biblioteca Municipal", True)
    # biblioteca_cidade.alterna_estado()
    biblioteca_cidade.receber_avaliacao("Filipe Vieira", 10.0)
    biblioteca_shopping = Biblioteca("Biblioteca do Shopping", False)
    # biblioteca_shopping.alterna_estado()
    biblioteca_shopping.receber_avaliacao("João Silva", 8.5)
    # Biblioteca.listar_bibliotecas()
    
    # Definição de objetos de livros e revistas
    livro1 = Livro("1984", "George Orwell", 30.0, "084-3245")
    livro2 = Livro("Brave New World", "Aldous Huxley", 25.0, "123-4567")
    revista1 = Revista("National Geographic", "John Doe", 15.0, "Quinta")
    
    livro1.aplicar_desconto()
    revista1.aplicar_desconto()
    
    biblioteca_cidade.adicionar_item(livro1)
    biblioteca_cidade.adicionar_item(livro2)
    biblioteca_cidade.adicionar_item(revista1)
    
    biblioteca_cidade.exibir_itens()
    
    # print(vars(livro1))
    # print(vars(revista1))

if __name__ == "__main__":
    main()