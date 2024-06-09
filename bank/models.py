from django.db import models


class User(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=128)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.username


class Transaction(models.Model):
    sender = models.ForeignKey(
        User, related_name='sent_transactions', on_delete=models.CASCADE)
    receiver = models.ForeignKey(
        User, related_name='received_transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} -> {self.receiver} : {self.amount}'
