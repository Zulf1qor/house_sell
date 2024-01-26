from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

""" Start Get"""

@api_view(['GET'])
def GetBanner(request):
    banner = Banner.objects.all()
    ser = BannerSerializres(banner, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetRecomendation(request):
    recomendation = Recomendation.objects.all()
    ser = RecomendationSerializres(recomendation, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetSell(request):
    sell = Sell.objects.all()
    ser = SellSerializres(sell, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetDetail(request):
    detail = Detail.objects.all()
    ser = DetailSerializres(detail, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetPresintaiton(request):
    presintaition = Presintaiton.objects.all()
    ser = PresintaitonSerializres(presintaition, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetTestimonial(request):
    testimonial = Testimonial.objects.all()
    ser = TestimonialSerializres(hotel, many=True)
    return Response(ser.data)


@api_view(['GET'])
def GetAbout_us(request):
    about_us = About_us.objects.all()
    ser = About_usSerializres(about_us, many=True)
    return Response(ser.data)


""" End Get"""
