from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import State
from .serializers import StateSerializer
# Create your views here.

class StateList(APIView):

	def get(self, request):
		states=State.objects.all();
		serializer=StateSerializer(states,many=True)
		return Response(serializer.data)

	def post(self):
		pass

