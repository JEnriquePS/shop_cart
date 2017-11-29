# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Cart

@login_required
def compra(request):
    cart = Cart()
    cart.user = request.user
    cart.item = request.session.get('courses_id', [])
    cart.cost = request.session.get('cost', 0)
    cart.save()
    del request.session['courses_id']
    del request.session['cost']
    messages.info(request, 'Compra realizada')
    return redirect('/')
