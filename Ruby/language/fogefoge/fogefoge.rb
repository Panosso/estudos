require_relative "fogefoge_ui"
require_relative "heroi"

def le_mapa(numero)

	arquivo = "fogefoge/mapa#{numero}.txt"
	texto = File.read arquivo
	mapa = texto.split "\n"
	mapa
end

def colisao

	puts "colidi"

end

def soma_vetor vetor1, vetor2

	[vetor1[0] + vetor2[0], vetor1[1] + vetor2[1]]

end

def	posicoes_validas_fantasmas mapa, novo_mapa, posicao

	posicoes = []
	
	cima = [-1, 0]
	baixo = [+1, 0]
	esquerda = [0, -1]
	direita = [0, +1]	
	
	movimentos_possiveis = [cima, baixo, esquerda, direita]

	movimentos_possiveis.each do |movimento|
	
		nova_posicao = soma_vetor(posicao, movimento)
		
		if posicao_valida(mapa, nova_posicao) && posicao_valida(novo_mapa, nova_posicao)
	
			posicoes << nova_posicao
	
		end
	
	end

	posicoes

end

def move_fantasma mapa, novo_mapa, linha, coluna

	posicoes = posicoes_validas_fantasmas mapa, novo_mapa, [linha, coluna]
	return if posicoes.empty?
	
	#Desomentar para teste
	posicao = posicoes[rand(posicoes.size)]
	#posicao = posicoes[0]
	mapa[linha][coluna] = " "
	novo_mapa[posicao[0]][posicao[1]] = "F"
	

end

def copia_mapa mapa

	#Join: O parametro passado servira como uma 'cola' para cada elemento do array, ou seja, teremos o Elemento1ColaElemento2Cola...
	#tr: traduz o primeiro elemento no segundo, ou seja, onde tiver algum "F" ele será substituido por " "
	novo_mapa = mapa.join("\n").tr("F", " ").split "\n"
	novo_mapa

end

def encontra_fantasma mapa

	caractere_fantasma = "F"
	
	new_map = copia_mapa mapa
	
	mapa.each_with_index do |linha_atual, linha|
	
		#Convertendo a linha para um array com o comando chars e entao usado o each_with_index
		linha_atual.chars.each_with_index do |caractere_atual, coluna|
		
			eh_fantasma = caractere_atual.include? caractere_fantasma
			if eh_fantasma
			
				move_fantasma mapa, new_map, linha, coluna
			
			end
		
		end
	
	end
	new_map
end

def encontra_jogador mapa
	#Funcao que localiza e retorna a posicao linha x coluna do heroi
	caractere_heroi = "H"
	#Idiomatismo
	#mapa.each: Percorre todos os caracteres 
	#mapa.each_with_index: Vai percorrer todas as linhas do mapa e retornada a linha, 
	# por exemplo X H X e o index dele no exemplo a index será 1, fazendo 
	# um laço no arquivo inteiro
	mapa.each_with_index do |linha_atual, linha|
		#O método index retorna nil caso nao contenha o caractere passado como parametro
		coluna_do_heroi = linha_atual.index caractere_heroi
		#Pode ser retirado a parte != nil, pois o if verifica se tem algo, caso tenha ele entra no if
		if coluna_do_heroi != nil
			
			jogador = Heroi.new
			jogador.linha = linha
			jogador.coluna = coluna_do_heroi
			
			return jogador
				
		end	
	end
	nil
end

def posicao_valida mapa, nova_posicao

	if nova_posicao[0] < 0 || nova_posicao[1] < 0
		return false
	end

	if nova_posicao[0] >= mapa.size || nova_posicao[1] >= mapa[0].size
		return false
	end

	if mapa[nova_posicao[0]][nova_posicao[1]] == "X" || mapa[nova_posicao[0]][nova_posicao[1]] == "F"
		return false
	end


	true

end

def jogador_perdeu mapa

	perdeu = !(encontra_jogador mapa)

end

def explode mapa, posicao, quantidade_explodir
	#3 formas de sair da recurssao
	#if quantidade_explodir == 0
	#	return
	#end
	return if quantidade_explodir == 0
	#return unless quantidade_explodir > 0
	
	if mapa[posicao.linha][posicao.coluna] == "X"
		return
	end
	
	posicao.remove_mapa mapa
	explode mapa, posicao.cima, quantidade_explodir - 1
	explode mapa, posicao.baixo, quantidade_explodir - 1
	explode mapa, posicao.direita, quantidade_explodir - 1
	explode mapa, posicao.esquerda, quantidade_explodir - 1
end

def joga_foge(nome)
	
	puts "Digite o mapa a ser jogado"
	numero = gets.strip.to_i
	mapa = le_mapa numero

	while true

		desenha_mapa mapa
		direcao = pede_movimento
		heroi = encontra_jogador mapa
		nova_posicao = heroi.movimentacao direcao
				
		if !posicao_valida mapa, nova_posicao.to_array
			next
		end
				
		heroi.remove_mapa mapa
		if mapa[nova_posicao.linha][nova_posicao.coluna] == "*"
			explode mapa, nova_posicao, 4
		end
		
		nova_posicao.coloca_mapa mapa
		
		mapa = encontra_fantasma mapa
		
		if jogador_perdeu mapa
			fim_de_jogo
			break
		end
				
	end

end

def jogo_fogefoge

	nome = boas_vindas_foge
	joga_foge nome

end
