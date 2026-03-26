from rest_framework.exceptions import AuthenticationFailed, APIException

from django.contrib.auth.hashers import check_password, make_password

from accounts.models import User
from companies.models import Enterprise, Employee


class AuthenticationService:
    def sign_in(self, email: str = None, password: str = None) -> User | None:

        user = User.objects.filter(email=email)

        if not user.exists():
            raise AuthenticationFailed("Invalid email")
        
        user = user.first()

        if not check_password(password=password, encoded=user.password):
            raise AuthenticationFailed("Invalid password")

        return user
    
    def sign_up(self, 
                name: str = None, 
                email: str = None, 
                password: str = None, 
                type_account: str = None, 
                company_id: int = None) -> User | None:
        
        if not name or name == "":
            raise APIException("Name is required")
        
        if not email or email == "":
            raise APIException("Email is required")
        
        if not password or password == "":
            raise APIException("Password is required")
        
        user = User

        if User.objects.filter(email=email).exists():
            raise APIException("Email already exists")
        
        password_hashed = make_password(password)

        created_user = User.objects.create(
            name=name,
            email=email,
            password=password_hashed,
            is_owner=True if type_account == "owner" else False)
        
        if type_account == "owner":
            created_enterprise = Enterprise.objects.create(name=f"{name}'s company", user=created_user)

        if type_account == "employee":
            Employee.objects.create(user=created_user.id, enterprise=created_enterprise.id)

        return created_user