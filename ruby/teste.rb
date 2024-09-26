arrai = ["Sociedade do anel", "Sociedade do anel" ,"2 torres" ,"retorno do rei", "gil de ham", "silmarillion", "O Hobbit"]

total = arrai.count {|venda| venda == "Sociedade do anel"}

puts total

#bemvindo = -> (nome){
#	puts "Bem vindo #{nome}"
#}
#
#minhafuncao = bemvindo
#minhafuncao.("Pedro")
#minhafuncao.call "Pedro"
#minhafuncao.call("Pedro")
#
#
#a = ["XXXXXXXXX", "X H     X", "XPX XXX X", "X X X   X", "X   X X X", "  X     X", " XXX XX X", "  X     X", "X   X X X", "XXXF  F X", "XXX XXX X", "XXX XXX X", "XXX     X"]
#b = a.clone
#
#b[0] = 7
#
#puts a
#puts b
#
#
#palavra = "Programador teste de with"
#
#mapa = File.read "mapa1.txt"
#puts mapa

#palavra.each_char do |n| 
#
#	puts "Linha N: #{n}"
#
#end

#palavra.chars.each_with_index do |caractere_atual, coluna|
#
#	puts "#{caractere_atual}, #{coluna}"
#
#end
#
#total = palavra.count "r"
#
#puts total
#
#for i in palavra.chars
#
#	puts palavra[i]
#	
#end
#
#e = 0
#
#while e < 6
#
#	puts e
#	e+=1
#	if e == 2
#		next
#	end
#end
