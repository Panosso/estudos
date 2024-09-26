class Livro

	attr_reader :titulo, :preco, :ano_lancamento, :reimpreesao, :editora, :tipo

	#Cronstrutor da classe, usado quando estamos criando um objeto
	def initialize(titulo, preco, ano_lancamento, reimpreesao, editora, tipo)

		@titulo = titulo
		@ano_lancamento = ano_lancamento
		@preco = calcula_preco_base(preco)
		@reimpreesao = reimpreesao
		@editora = editora
		@tipo = tipo
		
	end

	def chama_retorna_nome
	
		retorna_nome
	
	end

	def imprime_infos
	
		puts "Titulo: #{@titulo}, valor de R$#{preco} escrito em #{ano_lancamento}. Reimpresso: #{reimpreesao}"
	
	end

	def reimpreesao?
		@reimpreesao
	end

	def to_csv
		puts "#{@titulo}, #{@ano_lancamento}, #{@preco}"
	end


	#Todos os métodos e funcoes declaradas após essa palavra private
	# só poderam ser acessador pela classe e nao fora dela.
	private
	
	def calcula_preco_base(base)
		if @ano_lancamento < 2006
			if @reimpreesao

				base *= 0.9

			else

				base *= 0.95
			
			end
			
		elsif @ano_lancamento <=2010

			base *= 0.96
			
		else

			base

		end
	
	end
	
	def retorna_nome
	
		puts @titulo
	
	end

end
