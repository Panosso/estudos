#jogo_forca.rb
require_relative 'ui'
require_relative 'rank'

def escolhe_palavra_secreta

	avisa_escolhendo_palavra
	-Primeiro jeito de ler a palavra secreta.
	---------------------------------------------------------------
	-texto = File.read("dicionario.txt")						  -
	-todas_palavras = texto.split "\n"							  -
	-numero_escolhido = rand(todas_palavras.size)				  -
	-palavra_secreta = todas_palavras[numero_escolhido].downcase  -
	---------------------------------------------------------------

	#Segundo jeito e melhor aplicado
	arquivo = File.new("dicionario.txt")
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

def joga(nome)

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
		pontos_totais += joga nome
		avisa_pontos_totais pontos_totais


		if le_rank[1].to_i < pontos_totais
			salvar_rank nome, pontos_totais
		end

		if nao_quer_jogar
			break
		end
	end
end

#rank.rb
def salvar_rank nome, pontos_totais

	conteudo = "#{nome}\n#{pontos_totais}"
	File.write "rank.txt", conteudo

end

def le_rank

	conteudo = File.read "rank.txt"
	jogadores = conteudo.split "\n"
	jogadores

end

#ui.rb

def avisa_escolhendo_palavra
	puts "Escolhendo palavra secreta..."
end

def avisa_palavra_escolhida(palavra_secreta)

	puts "Palavra secreta com #{palavra_secreta.size} letras, boa sorte!!!"
	puts "Palavra secreta é #{palavra_secreta}"

end

def boas_vindas

	puts "****************************"
	puts "*Bem vindo ao jogo da forca*"
	puts "****************************"
	puts "Qual seu nome"
	nome = gets.strip
	puts "\n\n\n\n\n\n"
	puts "Começaremos o jogo para você #{nome}"
	nome

end

def cabecalho_de_tentativas(erros, chutes, chutes_certos, mascara)

	puts "\n\n\n\n"
	puts "Palavra secreta: #{mascara}"
	puts "Erros até agora: #{erros}"
	puts "Chutes até agora: #{chutes}"
	puts "Chutes certos até agora: #{chutes_certos}"
	puts "\n\n\n\n"

end

def pede_chute

	puts "Digite uma letra ou uma palavra"
	chute = gets.strip
	puts "Será que acertou? Você chutou #{chute}"
	chute

end

def nao_quer_jogar

	puts "Deseja jogar novamente? (S/N)"
	quero_jogar = gets.strip
	nao_quer_jogar = quero_jogar.upcase == "N"
	nao_quer_jogar
end

def pede_um_chute(chutes, erros, chutes_certos, mascara)
		cabecalho_de_tentativas erros, chutes, chutes_certos, mascara
		loop do
			chute = pede_chute
			if chutes.include? chute
			
				puts "Voce ja chutou #{chute}"
				
			else
				return chute
			end
		end
end

def mascarando_palavra chutes, palavra_secreta

	mascara = ""

	for letra in palavra_secreta.chars
	
		if chutes.include? letra

			mascara << letra
	
		else
		
			mascara << "_"
		
		end
		
	end
	
	mascara

end

def avisa_pontos_totais pontos

	puts "Voce possui #{pontos}"

end

def salvar_rank nome, pontos_totais

	conteudo = "#{nome}\n#{pontos_totais}"
	File.write "rank.txt", conteudo

end

def le_rank

	conteudo = File.read "rank.txt"
	jogadores = conteudo.split "\n"
	jogadores

end

def campeao_atual dados

	puts "Nosso campeao atual é #{dados[0]} com #{dados[1]} pontos"

end

#main.rb
require_relative 'jogo_forca'

jogo_da_forca

#dicionario.txt
# 8
# alura
# casa do código
# caelum
# programador
# code smell
# desenvolvedor
# refatorar
# software

#rank.txt
# Pedro
# 300