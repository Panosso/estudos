def salvar_rank nome, pontos_totais

	conteudo = "#{nome}\n#{pontos_totais}"
	File.write "jogo_forca/rank.txt", conteudo

end

def le_rank

	conteudo = File.read "jogo_forca/rank.txt"
	jogadores = conteudo.split "\n"
	jogadores

end
