require_relative "livro.rb"
require_relative "estoque"
#nao é necessario importar o contador.rb porque o estoque ja requer ele,
# portanto ele ja é chamado pelo estoque.

algoritmo = Livro.new("Algoritmos", 100, 1992, true, "Pearl", "Livro")
arquitetura = Livro.new("Arquitetura de software", 70, 2011, true, "Potate", "Livro")
pragmatico = Livro.new("Pogramador pragmatico", 100, 1999, true, "Alura", "Livro")
ruby = Livro.new("Pogramador Ruby", 100, 2004, true, "MeuPau", "Livro")
revista_ruby = Livro.new("Revista Ruby", 100, 2004, true, "MeuPau", "Resvista")

estoque = Estoque.new

#Método para adicionar mais de um elemento no array
#Essa combinacao '<<' é um método da classe Array, assim como temos estoque_csv como um método da classe estoque
#A classe Array possui o método '<<'

#Crio um estoque, adiciono um livro com o comando << que está na classe estoque, dentro da classe estoque
# eu tenho uma variavel que chama livros e ela extende o modelo Contador, quando chamado o método '<<' de
# estoque, ele adiciona um livro com o comando '@livros << livro', quando utilizado esse '<<' será executado
# o método '<<' do modelo estoque

estoque << algoritmo << algoritmo << algoritmo << arquitetura << arquitetura << pragmatico << ruby << arquitetura << ruby << ruby
estoque << revista_ruby
estoque << revista_ruby

estoque.vendas ruby
estoque.vendas ruby
estoque.vendas ruby
estoque.vendas algoritmo
estoque.vendas algoritmo
estoque.vendas revista_ruby
puts estoque.livro_que_mais_vendeu_por_titulo.titulo
puts estoque.revista_que_mais_vendeu_por_titulo.titulo
