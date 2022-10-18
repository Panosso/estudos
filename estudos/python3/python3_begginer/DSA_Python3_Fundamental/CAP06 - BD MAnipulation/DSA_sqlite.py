from sqlite3 import connect
from random import randint
from math import ceil

def examples():
    print("Examples SQL Lite DSA")

    con = connect("school.db")
    print(type(con))

    cur = con.cursor()

    sql_create_products = """create table if not exists products
                            (id integer primary key, 
                            title varchar(100),
                            category varchar(140))"""

    cur.execute(sql_create_products)

    cur.execute("Select * from products")

    products = list(cur.fetchall())

    list_prod_id = [i for i in range(1, 101)]

    if len(products) == 0:

        list_prod_name = ["Meia", "Sapato", "Calca", "Pijama", "Camisa", "Tenis"]

        list_prod_category = ["Roupa"]

        prod = randint(0,len(list_prod_name)-1)

        for i in list_prod_id:
            cur.execute(f"insert into products(id, title, category) values ('{i}', '{list_prod_name[prod]}', '{list_prod_category[0]}');")
            con.commit()

    quantidade_pagina = 20
    quantidade_total_pagina = ceil(len(products) / quantidade_pagina)
    pagina = randint(1, quantidade_total_pagina)
    item_inicial = pagina * 20
    item_final = item_inicial + 20
    print("Numero da Pagina: " + str(pagina))
    print("Qtd. Pagina: " + str(quantidade_total_pagina))
    print("Item Inicial: " + str(item_inicial))
    print("Item Final: " + str(item_final))
    print(products[item_inicial:item_final])
