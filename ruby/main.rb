require_relative 'jogo_forca/jogo_forca'
require_relative 'maior_menor/maior_menor'
require_relative 'fogefoge/fogefoge'

puts "Digite qual jogo deseja abrir:\n\n"
puts "1 - Maior Menor:\n\n"
puts "2 - Jogo da Forca:\n\n"
puts "3 - Jogo Foge Foge:\n\n"
jogo = gets.to_i

case jogo

	when 1
		puts "\n\n\n\n\n\n\n\n\n\n\n\n"
		jogo_maior_menor
		
	when 2
		puts "\n\n\n\n\n\n\n\n\n\n\n\n"
		jogo_da_forca
		
	when 3
		puts "\n\n\n\n\n\n\n\n\n\n\n\n"
		jogo_fogefoge

end
