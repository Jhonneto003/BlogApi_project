from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self,email,username, password,**extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        
        email=self.normalize_email(email)
        user=self.model(email=email,password=password,username=username,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,username,password, **extra_fields):
      
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email=email, password=password,username=username,**extra_fields)
