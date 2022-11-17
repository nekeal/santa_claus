from rest_framework import serializers

from santa_claus.accounts.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
        )
