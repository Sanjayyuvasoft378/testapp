from django.apps import AppConfig


class TestappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'testapp'



# def validate(self, attrs):
#         password = attrs.get('password')
#         confirmPassword = attrs.get('confirmPassword')
#         if password != confirmPassword:
#             raise serializers.ValidationError("password and confirm password does not match")
#         return attrs