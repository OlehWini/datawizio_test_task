from django.shortcuts import render
from dwapi import datawiz
import json, datetime, time, pandas, numpy as np
# from django.core.exceptions import

# Create your views here.


def index(request):
    return render(request, 'main/index.html', {})


def login(request):
    user_log = ''
    user_pass = ''

    if request.method == 'POST':
        user_log = request.POST.get('login')
        user_pass = request.POST.get('password')

    dw = datawiz.DW(user_log, user_pass)
    # try:
    #     dw = datawiz.DW(user_log, user_pass)
    # except request.SomeError:
    #     return render(request, 'main/index.html',{})
    #
    user_info = dw.get_client_info()
    user_name = user_info['name']
    date_from = user_info['date_from']
    date_to = user_info['date_to']
    count_of_shops = len(list(user_info['shops']))
    shops = user_info['shops']
    arr_shops_name = []
    all_shops = dw.get_shops()

    for id in shops:
        arr_shops_name.append(shops[id])
    # for id in shops:

    context = {
        'dw': dw,
        'user_name': user_name,
        'date_from': date_from,
        'date_to': date_to,
        'count_of_shops': count_of_shops,
        'all_shops': all_shops,
    }


    return render(request, 'main/main.html', context)
