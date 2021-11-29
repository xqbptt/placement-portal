from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib import messages
from .graph_helper import get_user
from .auth_helper import get_sign_in_flow, get_token_from_code, store_user, remove_user_and_token
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
import re


def sign_in(request):
  # Get the sign-in flow
  flow = get_sign_in_flow()
  # Save the expected flow so we can use it in the callback
  try:
    request.session['auth_flow'] = flow
  except Exception as e:
    print(e)
  # Redirect to the Azure sign-in page
  return HttpResponseRedirect(flow['auth_uri'])


def callback(request):
  # Make the token request
  result = get_token_from_code(request)
  
  #Get the user's profile
  user = get_user(result['access_token'])

  store_user(request, user)

  # Get user info
  username = user['displayName'].replace(" ","_")
  username = re.sub('[^0-9a-zA-Z_]+','',username)
  password = user['mail']
  email = user['userPrincipalName']

  try:
      user = User.objects.get(email=email)
  except User.DoesNotExist:
      user = User.objects.create(username=username, email=email, password=password)
      user.save()
  user = User.objects.get(email=email)

  if user is not None:
      login(request, user)
      messages.success(request, "Success: You were successfully logged in!")
      return redirect('home:home')
  else:
      print("Caught an error while logging in", username, email)
  return redirect('home:home')

def sign_out(request):
  # Clear out the user and token
  logout(request)
  remove_user_and_token(request)
  messages.success(request, "Successfully Logged Out")

  return redirect('home:home')
