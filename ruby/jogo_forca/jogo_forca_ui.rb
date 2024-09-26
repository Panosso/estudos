
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

	conteudo = File.read "jogo_foca/rank.txt"
	jogadores = conteudo.split "\n"
	jogadores

end

def campeao_atual dados

	 puts "Nosso campeao atual é #{dados[0]} com #{dados[1]} pontos"

end











