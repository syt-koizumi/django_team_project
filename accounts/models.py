from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# 一般ユーザーおよびスーパーユーザーを作成するクラス
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            password=password
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        # is_staffとis_superuserの追加
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


# カスタムユーザーモデルを指定するクラス
#　PermissionsMixinの継承
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('ユーザー名', max_length=100,
                                unique=True,
                                error_messages={
                                    'unique': ("同一のユーザー名が既に登録されています"),
                                }, )
    email = models.EmailField('メールアドレス', unique=True, )
    age = models.PositiveIntegerField('年齢', default=0)
    is_admin = models.BooleanField('管理者', default=False)
    is_active = models.BooleanField('有効', default=False)
    is_staff = models.BooleanField('有効', default=False)
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.username