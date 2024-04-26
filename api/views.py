from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
import requests

# Create your views here.

# app_name/views.py


# @csrf_exempt
# @api_view()
# def email(request):
#     print(request.POST)  # Print the received data
#     subject = request.POST.get('subject', 'hello')
#     body = request.POST.get('body', 'very bad')
#     senderEmail = request.POST.get('senderEmail', 'my_email@gmail.com')

#     # You can add your custom logic here (e.g., sending an email)
#     # For now, let's just print the data to the console
#     print(f"Subject: {subject}, Body: {body}, Sender Email: {senderEmail}")

#     return Response("Email Send.")


# @api_view()
# def hello_world(request):
#     return Response({"message": "Hello, world from @api_view!"})

# class HelloWorldView(APIView):
#     def get(self, request):
#         return Response({"message": "Hello, World!"}, status=status.HTTP_200_OK)


# def home(request):
#     return HttpResponse('Hello World!')


@api_view(['GET', 'POST'])
def  cordinates(request):

    def send_messege(link):
        messege= f"Your current location {link}"

        # your API secret from (Tools -> API Keys) page
        apiSecret = "e4ae2edfec9523b65152d02b12d72276a8350c8b"

        message = {
            "secret": apiSecret,
            "mode": "devices",
            "device": "00000000-0000-0000-e401-e3a066dbc946",
            "sim": 1,
            "priority": 1,
            "phone": "+263781234991",
            "message": messege
        }

        r = requests.post(url = "https://www.cloud.smschef.com/api/send/sms", params = message)
        
        # do something with response object
        result = r.json()

        print(result)
        return messege

    def create_google_maps_url(latitude, longitude):
        
        base_url = f"http://maps.google.com/maps?z=12&t=m&q=loc:{latitude}+{longitude}"
        full_url = base_url 
        return full_url
    
    cordinates_data = "0000"
    if request.method == 'GET':
        return Response({"message": "Hello, World {cordinates_data}!"}, status=status.HTTP_200_OK)
     
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)

        # create_google_maps_url(tutorial_data["latitude"], tutorial_data["longitude"])
        # print( create_google_maps_url(tutorial_data["latitude"], tutorial_data["longitude"]))

        #send_messege_to_registred_mobile_device
        send_messege(create_google_maps_url(tutorial_data["latitude"], tutorial_data["longitude"]))
        
        return Response({"message": "Hello, World!"}, status=status.HTTP_200_OK)

    