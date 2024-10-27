require_relative "contador"

class Estoque
	
	attr_reader :livros
	
	def initialize
	
		@livros = []
		@vendas = []
		#Essa linha mostra que a class livro tera os métodos do contador
		@livros.extend Contador
	end

	def quantidade_de_vendas_por(produto, &campo)
		puts "aqui tbm"
		#o Array será percorrido e para cada elemento atribuido a variavel venda
		# será verificado o titulo da venda com o titulo do produto
		@vendas.count {|venda| campo.call(venda) == campo.call(produto)}
	
	end

	def revista_que_mais_vendeu_por_ano
	
		que_mais_vendeu_por("revista", &:ano_lancamento)
	
	end

	def revista_que_mais_vendeu_por_titulo
	
		que_mais_vendeu_por("revista", &:titulo)
	
	end
	
	def revista_que_mais_vendeu_por_editora
	
		que_mais_vendeu_por("revista", &:editora)
	
	end

	def livro_que_mais_vendeu_por_ano
	
		que_mais_vendeu_por("livro", &:ano_lancamento)
	
	end

	def livro_que_mais_vendeu_por_titulo
		
		que_mais_vendeu_por("livro", &:titulo)
	
	end
	
	def livro_que_mais_vendeu_por_editora
	
		que_mais_vendeu_por("livro", &:editora)
	
	end

	def que_mais_vendeu_por(tipo, &campo)
		
		#<=> Comparacao
		@vendas.select { | l | l.tipo == tipo}.sort {|v1,v2| quantidade_de_vendas_por(v1, &campo) <=> quantidade_de_vendas_por(v2, &campo)}.last

	end

	def exporta_csv
		@livros.each do |livro|
			livro.to_csv
		end
	end

	def <<(livro)
		@livros << livro if livro
		self
	end

	def vendas livro
		#Método delete de um array é usado para remover do array, o elemento passado como parametro
		@livros.delete livro
		@vendas << livro
	
	end
	
	def maximo
		
		@livros.maximo
		
	end

	def mais_baratos_que(valor)
			
			#select: equivalente ao filter em python, ele retorna um novo array com os valores que satisfazem
			# a condicao, no caso a condicao 'livro.preco <= valor'
			# Esse return ja serve como return da funcao
			@livros.select do |livro|
				livro.preco <= valor
			end
	end
	
	def total
	
		@livros.size
	
	end
	
	def tenho_no_estoque
	
		livros.each do |livro|
		
			puts livro.imprime_infos
		
		end
	
	end

	def livro_para_newsletter(livro)

		if livro.ano_lancamento < 1999
		
			puts "Liquidacao"
			puts livro.titulo
			puts livro.preco
			puts livro.reimpreesao?
		
		end

	end
	
end
