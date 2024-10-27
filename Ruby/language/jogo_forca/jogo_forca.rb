#Jogo da forca
require_relative 'jogo_forca_ui'
require_relative 'rank_forca'

def escolhe_palavra_secreta

	avisa_escolhendo_palavra
	#Primeiro jeito de ler a palavra secreta.
	###############################################################
	#texto = File.read("dicionario.txt")						  #
	#todas_palavras = texto.split "\n"							  #
	#numero_escolhido = rand(todas_palavras.size)				  #
	#palavra_secreta = todas_palavras[numero_escolhido].downcase  #
	###############################################################

	#Segundo jeito e melhor aplicado
	arquivo = File.new("jogo_forca/dicionario.txt")
	#Retorna a primeira linha do arquivos
	quantidade_palavras = arquivo.gets.to_i
	numero_escolhido = rand(quantidade_palavras)
	for linha in 1..(numero_escolhido-1)
		puts "Linha descartada: #{linha}"
		arquivo.gets
	end
	palavra_secreta = arquivo.gets.strip.downcase
	arquivo.close
	avisa_palavra_escolhida palavra_secreta
	palavra_secreta

end

def joga_forca(nome)

	palavra_secreta = escolhe_palavra_secreta
	erros = 0
	chutes = []
	chutes_certos = []
	pontos = 0
	
	while erros < 5
		mascara = mascarando_palavra chutes, palavra_secreta
		chute = pede_um_chute(chutes, erros, chutes_certos, mascara)
		chutes << chute
		
		if chute.size == 1
	
			letra_procurada = chute[0]
			total_encontrado = palavra_secreta.count letra_procurada
			
			if total_encontrado != 0
			
				puts "A letra #{letra_procurada} foi encontrada #{total_encontrado} vezes."
				chutes_certos << chute
				
			else
			
				puts "A palavra não contem a letra #{letra_procurada}"
				erros += 1
			end
		
		else
		
			acertou = chute == palavra_secreta

			if acertou 
			
				puts "Parabens! Voce acertou"
				pontos += 100
				break
				
			else

				puts "Que pena errou."
				pontos -= 30
				erros +=1

			end
		
		end
		
	end
	
	puts "Você ganhou #{pontos} pontos"
	pontos

end

def jogo_da_forca

	nome = boas_vindas
	
	pontos_totais = 0
	
	campeao_atual le_rank
	
	loop do
		pontos_totais += joga_forca nome
		avisa_pontos_totais pontos_totais


		if le_rank[1].to_i < pontos_totais
			salvar_rank nome, pontos_totais
		end

		if nao_quer_jogar
			break
		end
	end
end

