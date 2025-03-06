variable "nome" {
    type = string
    default = "Mundo"
}

resource "exemplo" "meuRecurso" {
    nome = var.nome
    count = 3
}
