#Criando uma funcao
def da_boas_vindas
	
	puts "Olá bem-vindo"
	puts "Qual o seu nome?"
	nome = gets.strip
	puts "\n\n\n\n\n\n\n\n"
	puts "Vamos começar o game " + nome
	nome

end

def pede_dificuldade
	puts "Qual vai ser a dificuldade, IZI, MED, FODA?"
	gets.strip.upcase
end


def sorteia_numero_secreto(dificuldade)

	retorno = []
	case dificuldade
	when "IZI"
		maximo = 30
	
	when "MED"
		maximo = 100
		
	when "FODA"
		maximo = 200
	
	end

	#Aqui ele gera do 0 até o 199, somando mais 1 ele pode ir até o 200
	sorteio = rand(maximo) + 1
	#return numero_secreto
	#Em ruby, ele adimite a ultima linha como return, sendo assim não é necessário digitar o return.
	retorno[0] = sorteio
	retorno[1] = maximo
	retorno

end

def chute_jogador(tentativa, limite_chute, maximo)

	puts "Tentativa #{tentativa} de #{limite_chute.to_s}"
	puts "Digite um numero entre 1 e #{maximo}"
	chute = gets
	puts "Voce digitou #{chute}"
	chute.to_i

end

def verifica_acerto(numero_secreto, chute)

	if numero_secreto == chute
	
		puts "Acertou"
		return true
		
	else
		
		puts "Errou"
		
		if chute.to_i > numero_secreto
		
			puts "O número chutado é maior"
		
		else
		
			puts "O número chutado é menor"
		
		end
		
		false

	end	

end

def joga(nome, dificuldade)

	dados = sorteia_numero_secreto(dificuldade)
	numero_secreto = dados[0]
	maximo = dados[1]
	
	puts "\n\n\n\n\n\n\n\n"
	
	inicio = 1
	fim = 5
	chutes = []
	pts_jogador = 1000
	puts numero_secreto
	
	for tentativas in inicio..fim
	
		chute = chute_jogador(tentativas, fim, maximo)
	
		chutes << chute
	
		if nome == "Pedro"
		
			puts "Acertou"
			break
		end
	
		pts_jogador -= ((chute - numero_secreto).abs/2.0)
	
		puts "Números já chutados: #{chutes}"
		puts "Pontuação atual do jogador: #{pts_jogador}"
	
		break if verifica_acerto(numero_secreto, chute) 
		
	end

end

def quer_jogar

	puts "Deseja continuar jogando? S/N"
	gets.strip.upcase

end

def jogo_maior_menor

	continuar = "S"

	while continuar == 'S'
	
		nome = da_boas_vindas
		dificuldade = pede_dificuldade
		joga nome, dificuldade
		continuar = quer_jogar
	
	
	end
end
