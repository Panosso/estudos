def boas_vindas_foge

	puts "Bem-vindo ao foge foge"
	puts "Digite o seu nome: "
	nome = gets.strip
	puts "\n\n\n\n"
	puts "Comecaremos o game pra voce #{nome}"
	nome	

end


def desenha_mapa mapa

	puts mapa

end

def pede_movimento

	puts "Para onde quer ir?"
	movimento = gets.strip.upcase

end

def fim_de_jogo
	
	puts "\n\n\n\n\n\n\n\n\n"
	puts "Voce perdeu."
	puts "\n\n\n\n\n\n\n\n\n"
	
end
