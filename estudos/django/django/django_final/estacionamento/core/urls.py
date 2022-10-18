from django.urls import path, include

from .views import (home,
                    cadastro_pessoas,
                    cadastro_novo,
                    update_pessoa,
                    cadastro_veiculos,
                    update_veiculo,
                    delete_veiculo,
                    rot_hora,
                    rot_mes,
                    novo_veiculo,
                    mov_rot_hora,
                    mov_rot_mes,
                    parametros_gerais,
                    cor_nova,
                    update_cor,
                    categoria_nova,
                    update_categoria,
                    marca_nova,
                    update_marca,
                    )

urlpatterns = [
    path('', home, name="core_home"),


    #Cadastros e listagem de pessoas cadastradas
    path('cadastros', cadastro_pessoas, name="pessoas"),
    path('cadastros_novo', cadastro_novo, name="pessoas_novo"),
    path('cadastro/<int:id_cadastro>', update_pessoa, name="att_pessoa"),

    #Cadastro e lista de carros cadastrados
    path('veiculos', cadastro_veiculos, name="veiculos"),
    path('veiculo_novo', novo_veiculo, name="veiculo_novo"),
    path('veiculo_novo/<int:id_veiculo>', update_veiculo, name='att_veiculo'),
    path('veiculo_deletar/<int:id_veiculo>', delete_veiculo, name='del_veiculo'),

    # Cadastro e lista de movimentações por hora cadastradas
    path('rothora', rot_hora, name="rotativos_hora"),
    path('mov_rot_hora', mov_rot_hora, name="mov_rot_hora"),

    # Cadastro e lista de movimentações por mes cadastradas
    path('rotmes', rot_mes, name="rotativos_mes"),
    path('mov_rot_mes', mov_rot_mes, name="mov_rot_mes"),

    #Parametros Gerais
    path('parametros', parametros_gerais, name="parametros_gerais"),

    # Cor
    path('cores_novas', cor_nova, name="cor_nova"),
    path('cor_update/<int:id_cor>', update_cor, name="att_cor"),

    #Categoria
    path('categoria_novas', categoria_nova, name="categoria_nova"),
    path('categoria_update/<int:id_categoria>', update_categoria, name="att_categoria"),

    # #Marca
    path('marca_novas', marca_nova, name="marca_nova"),
    path('marca_update/<int:id_marca>', update_marca, name="att_marca"),

]
