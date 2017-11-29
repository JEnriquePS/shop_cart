# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView

from app.courses.models import Course

class HomeView(ListView):
    login_url = 'login/'
    template_name = 'home/index.html'
    model = Course
    context_object_name = 'courses'


def add_courses(request, id):
    if request.method == 'GET':
        print request
        print  request.session.get('ere', False)
        if 'courses_id' in request.session:
            if not id in request.session['courses_id']:
                request.session['courses_id'].append(id)
            else:
                messages.warning(request, 'Curso ya esta Agregado')
                return redirect('/')
        else:
            request.session['courses_id'] = [id]
        if 'cost' in  request.session:
            request.session['cost'] += float(Course.objects.get(id=id).cost)
        else:
            request.session['cost'] = float(Course.objects.get(id=id).cost)
        return redirect('/')


class ListCourses(TemplateView):
    template_name = 'courses/list_courses.html'

    def get_context_data(self, **kwargs):
        context = super(ListCourses, self).get_context_data(**kwargs)
        courses = Course.objects.filter(id__in = self.request.session['courses_id'])
        context['courses'] = courses
        return context