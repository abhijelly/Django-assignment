from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    """
    Renders the login page. Checks if the user exists in the database.
    """
    return HttpResponse("Enter email and password here to login")

def register(request):
    """
    Checks the user credentials against the existing User database with the email field using authenticate().
    If the user does not alreay exists in the dabase, redirect to `otp` page. Otherwise, render register page
    to display a message that the user already exists.  
    """
    return HttpResponse("New users register here")

def otp(request):
    """
    Generates a random OTP and sends to the email of the user. Depending on OTP validity, shows successful
    registeration or invalid OTP 
    """

    return HttpResponse("Enter OTP sent to your email address")
