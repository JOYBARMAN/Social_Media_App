from django.db.models import TextChoices


class UserType(TextChoices):
    AUTHOR = "AUTHOR", "Author"
    VISITOR = "VISITOR", "Visitor"
    UNDEFINED = "UNDEFINED", "Undefined"


class OtpType(TextChoices):
    REGISTRATION = "REGISTRATION", "Registration"
    LOGIN = "LOGIN", "Login"
    UNDEFINED = "UNDEFINED", "Undefined"
