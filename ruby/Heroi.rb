#Heroi.rp
#Criacao de classe
class Heroi

	#Permite que os atributos possam ser lidas fora da classe e alterado tbm.
	# é passado para classe 2 simbolos, um com o nome linha e um com o nome coluna
	# attr_write: apenas consegui escrever e nao ler
	# attr_reader: apenas consegui ler e nao escrever
	attr_accessor :linha, :coluna

	def movimentacao direcao

		#self: Refencia o proprio objeto, portanto nessa linha ele está duplicando o heroi evitando assim
		# o erro de enderecamento de array, o self é opcional portanto a linha abaixo pode ser escrita como
		# heroi = dup
		novo_heroi = self.dup
	
		#Criado um dicionario onde a string W tem o valor array [-1,0]
		movimento = {"W" => [-1,0],
		"S" => [+1,0],
		"A" => [0,-1],
		"D" => [0,+1]
		}
	
		movimento_heroi = movimento[direcao]
		novo_heroi.linha += movimento_heroi[0]
		novo_heroi.coluna += movimento_heroi[1]
		novo_heroi
	
	end

	def to_array
		#Retorna a linha e a coluna em formato de um array para uma funcao que dependa de um array
		[linha, coluna]
	
	end

	#Quando colocamos o @ antes do atributo, ele está acessando(pois foid dado acesso com attr_acessor)
	# o atributo com o nome após o @, portanto é possível alterar o valor do artibuto sem problema.

	def remove_mapa mapa
		puts "Tirando do mapa"
		puts "*************************"
		puts @linha
		puts @coluna
		puts "*************************"
		mapa[@linha][@coluna] = " "
	end
	
	def coloca_mapa mapa
		puts "Colocando no Mapa"
		puts "*************************"
		puts @linha
		puts @coluna
		puts "*************************"
		mapa[@linha][@coluna] = "H"
	end

	def direita
		movimentacao "D"
	end

	def esquerda
		movimentacao "A"
	end

	def cima
		movimentacao "W"
	end

	def baixo
		movimentacao "S"
	end

end