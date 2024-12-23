import jwt
from time import sleep
from datetime import datetime, timedelta, timezone

def create_jwt_token(payload):
    
    secret_key = 'supersecretkey'
    algorith = 'HS256'
    token = jwt.encode(payload, secret_key, algorith)
    return token

def validate_token(token):
    secret_key = 'supersecretkey'
    algorith = 'HS256'
    try:
        decoded_payload = jwt.decode(token, secret_key, algorith)
        return decoded_payload
    except jwt.ExpiredSignatureError as expired:
        raise f'Token Expirado: {expired}'
    except jwt.InvalidTokenError as invalid:
        raise f'Token Invalido: {invalid}'
    except Exception as e:
        raise f'{e}'
    
def main():
    
    payload = {
        'sub': '4242',
        'name': 'Pedro',
        'nick': 'PedroPan',
        'role': 'admin',
        'Hehe': 'waka',
        'exp': datetime.now(timezone.utc) + timedelta(seconds=20)
    }

    token = create_jwt_token(payload)

    sleep(5)

    a = validate_token(token)

    if a:
        print('Deu certo')

    print(token)
    print(a)

if __name__ == '__main__':
    main()