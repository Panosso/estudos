from pathlib import Path

from sqlalchemy import create_engine, String, Boolean, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

#Pega o caminho atual do arquivo de execução, até a pasta onde ele está
pasta_atual = Path(__file__).parent
PATH_TO_BD = pasta_atual / 'bd_usuarios.sqlite'

#Representação da classe do SQLAlchemy.
class Base(DeclarativeBase):
    pass


class Usuario(Base):

    #nome da tabela
    __tablename__ = 'usuarios'

    #Campos
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(30))
    senha: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))
    acesso_gestor: Mapped[bool] = mapped_column(Boolean, default=False)

    #Caso seja utilizando o print em um objeto da tabela, esse será o retorno
    def __repr__(self):
        #Esse = que está no retorno, é um sinal que eu peço ao python para retorna a string + o valor, exemplo: Usuario: self.id=1, self.nome='Pedro'
        return f"Usuario: {self.id=}, {self.nome=}"
    
    def define_senha(self, senha):
        self.senha = generate_password_hash(senha)

    def verificar_senha(self, senha):
        return check_password_hash(self.senha, senha)

#Cria a engine
engine = create_engine(f"sqlite:///{PATH_TO_BD}")

#Cria o banco com as tabelas.
Base.metadata.create_all(bind=engine)

# CRUD ==================================
def cria_user(nome, senha, email, **kwargs):
    
    #Crio a sessão para a engine criada na linha 34
    with Session(bind=engine) as session:
        usuario = Usuario(
            nome = nome,
            email = email,
            **kwargs
        )
        usuario.define_senha(senha=senha)
        session.add(usuario)
        session.commit()

def le_todos_usuarios():
    with Session(bind=engine) as session:
        cmd_sql = select(Usuario)
        usuarios = session.execute(cmd_sql).fetchall()
        usuarios = [user[0] for user in usuarios]
        return usuarios

def le_user_por_nome(nome):
    with Session(bind=engine) as session:
        cmd_sql = select(Usuario).filter_by(nome = nome)
        usuario = session.execute(cmd_sql).fetchall()
        usuario = [user[0] for user in usuario]
        return usuario

def le_user_por_id(id):
    with Session(bind=engine) as session:
        cmd_sql = select(Usuario).filter_by(id = id)
        usuario = session.execute(cmd_sql).fetchall()
        usuario = [user[0] for user in usuario]
        return usuario


#Metodo mais legivel
# def modifica_usuario(id, nome = None, senha = None, email = None, acesso_gesto = None):
#     with Session(bind=engine) as session:
#         cmd_sql = select(Usuario).filter_by(id=id)
#         usuario = session.execute(cmd_sql).fetchall()
#         for usuario in usuario:
#             if nome:
#                 usuario[0].nome = nome
#             if senha:
#                 usuario[0].senha = senha
#             if email:
#                 usuario[0].email = email
#             if not acesso_gesto is None:
#                 usuario[0].acesso_gesto = acesso_gesto

#         session.commit()

#Metodo pythonico
def modifica_usuario(id, **kwargs):
    with Session(bind=engine) as session:
        cmd_sql = select(Usuario).filter_by(id=id)
        usuario = session.execute(cmd_sql).fetchall()
        for usuario in usuario:
            for key, value in kwargs.items():
                #Metodo especial de classe, modificando o elemento de uma instancia da uma classe, passando a classe, atributo e o valor a ser alterado
                if key == 'senha':
                    usuario[0].define_senha(value)
                else:
                    setattr(usuario[0], key, value)

        session.commit()


def deletar_usuario(id):
    with Session(bind=engine) as session:
        cmd_sql = select(Usuario).filter_by(id=id)
        usuarios = session.execute(cmd_sql).fetchall()
        for usuario in usuarios:
            session.delete(usuario[0])

        session.commit()

if __name__ == '__main__':

    # cria_user('Pedro', '1234', 'pedropanosso@gmail.com', acesso_gestor=1)
    # cria_user('Yago', '12345', 'yago@gmail.com', acesso_gestor=0)

    # all_user = le_todos_usuarios()
    # print(all_user)
    # usuario_0 = all_user[0]

    # print(usuario_0)
    # print(usuario_0.nome, usuario_0.senha, usuario_0.email)

    # usuario = le_user_por_nome('Pedro')[0]

    # print(usuario.nome, usuario.senha, usuario.email)

    # #Passando as informações para o kwarg, o resultado será mais ou menos esse:
    # #    kwargs = {'nome': 'Pedro12312321', 'senha' = '4322211'}
    # modifica_usuario(id=1, nome='Pedro12312321', senha='4322211')

    # user = le_user_por_id(1)

    # print(user)

    # deletar_usuario(4)

    # user = le_user_por_id(1)
    # print(user)
    # print(f"Senha informada é valida? {user[0].verificar_senha('43222211')}")

    # a = [deletar_usuario(i) for i in range(0, 100)]
    pass