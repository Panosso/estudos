from time import sleep

def login():
    with st.container(border=True):
        st.markdown('Bem vindo a tela de login')
        usuarios = le_todos_usuarios()
        usuarios = {usuario.nome: usuario for usuario in usuarios}
        nome_usuario = st.selectbox('Selecione o usuario', 
                                    list(usuarios.keys()))
        
        senha = st.text_input(
            'Digite sua senha',
            type='password'
            )
        #4322211
        if st.button('Logar'):
            usuario = usuarios[nome_usuario]

            if usuario.verificar_senha(senha):
                st.success('Login efetuado com sucesso')
                st.session_state['usuario'] = usuario
                st.session_state['logado'] = True
                sleep(5)
                st.rerun()
            else:
                st.error('Senha incorreta')

def main():
    if not 'logado' in st.session_state:
        st.session_state['logado'] = False

    if not st.session_state['logado']:
        login()

    else:
        st.markdown('Bem vindo ao site.')

if __name__ == '__main__':
    main()