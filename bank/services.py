from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from .models import User, Transaction


class UserService:
    @staticmethod
    def user_exists(username):
        """Check if a user exists."""
        try:
            return User.objects.filter(username=username).exists()
        except Exception as e:
            return f"Error occurred: {e}", 400

    @staticmethod
    def is_email_used(email):
        """Check if an email is already in use."""
        try:
            return User.objects.filter(email=email).exists()
        except Exception as e:
            return f"Error occurred: {e}", 400

    @staticmethod
    @transaction.atomic
    def register_user(username, email, password, balance=0.0):
        """Register a new user."""
        try:
            User.objects.create(username=username, email=email,
                                password_hash=password, balance=balance)
            return "User registered successfully", 200
        except Exception as e:
            return f"Error occurred while registering user: {e}", 400

    @staticmethod
    def authenticate_user(username, password):
        """Authenticate user."""
        try:
            user = User.objects.get(username=username, password_hash=password)
            return True if user else False
        except ObjectDoesNotExist:
            return False

    @staticmethod
    def get_user_balance(username):
        """Get user's balance."""
        try:
            user = User.objects.get(username=username)
            return user.balance
        except ObjectDoesNotExist:
            return -1

    @staticmethod
    @transaction.atomic
    def update_user_balance(username, new_balance):
        """Update user's balance."""
        try:
            user = User.objects.get(username=username)
            user.balance = new_balance
            user.save()
            return "Balance updated successfully", 200
        except Exception as e:
            return f"Error occurred while updating user balance: {e}", 400

    @staticmethod
    def get_user_transactions(username):
        """Get user's transactions."""
        try:
            user = User.objects.get(username=username)
            transactions = Transaction.objects.filter(
                sender=user) | Transaction.objects.filter(receiver=user)
            return transactions
        except ObjectDoesNotExist:
            return None  # User not found
        except Exception as e:
            return f"Error occurred while getting user transactions: {e}"

    @staticmethod
    @transaction.atomic
    def add_transaction(sender_username, receiver_username, amount):
        """Add a transaction."""
        try:
            sender = User.objects.get(username=sender_username)
            receiver = User.objects.get(username=receiver_username)
            Transaction.objects.create(
                sender=sender, receiver=receiver, amount=amount)
            return "Transaction added successfully", 200
        except Exception as e:
            return f"Error occurred while adding transaction: {e}", 400
