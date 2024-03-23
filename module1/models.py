from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    phonenumber = models.PositiveBigIntegerField()
    class Meta:
        db_table="RegisterForm"

    from django.db import models

class Feedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    phonenumber=models.PositiveBigIntegerField()
    feedback_text=models.CharField(max_length=100)
    class Meta:
        db_table="FeedbackForm"
