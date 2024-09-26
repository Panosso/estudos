module Contador

	attr_reader :maximo

	def <<(livro)
		#Push adiciona o elemento em um Array
		push(livro)
		#Esse size é do objeto livro que é um array, em Ruby o self pode ser ignorado
		# portanto na comparacao eu nao preciso digitar o self, portanto nela eu tenho
		# maximo < self.size
		if maximo.nil? || maximo < size
			@maximo = size
		end
		self
	end
	
	

end
