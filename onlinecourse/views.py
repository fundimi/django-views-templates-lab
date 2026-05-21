from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, Lesson, Enrollment
from django.urls import reverse
from django.views import generic
from django.http import Http404

# Create your views here.

def popular_course_list(request):
    context = {}

    # Se a requisição for GET, significa que o usuário quer visualizar a página
    if request.method == 'GET':
        # Busca os 10 cursos com mais matrículas, em ordem decrescente
        course_list = Course.objects.order_by('-total_enrollment')[:10]

        # Envia a lista de cursos para o template
        context['course_list'] = course_list

        # Renderiza o template HTML usando os dados do contexto
        return render(request, 'onlinecourse/course_list.html', context)

def enroll(request, course_id):
    # Se o usuário enviou o formulário pelo método POST
    if request.method == 'POST':

        # Busca o curso pelo id.
        # Se não encontrar, retorna erro 404 automaticamente.
        course = get_object_or_404(Course, pk=course_id)

        # Aumenta o número de matrículas em 1
        course.total_enrollment += 1

        # Salva a alteração no banco de dados
        course.save()

        # Redireciona o usuário de volta aos detalhes 
        return HttpResponseRedirect(
            reverse(viewname='onlinecourse:course_details', args=(course.id,))
        )


def course_details(request, course_id):
    context = {}

    # Se a requisição for GET, o usuário quer visualizar a página
    if request.method == 'GET':
        try:
            # Busca o curso pelo id recebido na URL
            course = Course.objects.get(pk=course_id)

            # Envia o curso para o template
            context['course'] = course

            # Renderiza a página de detalhes
            return render(request, 'onlinecourse/course_detail.html', context)

        except Course.DoesNotExist:
            # Se o curso não existir, mostra erro 404
            raise Http404("No course matches the given id.")