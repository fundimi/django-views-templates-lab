from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Course, Lesson, Enrollment
from django.urls import reverse
from django.views import generic, View
from django.http import Http404
from django.contrib.auth import logout, authenticate, login
import logging

from django.contrib.auth.models import User
logger = logging.getLogger(__name__)

# Create your views here.

def registration_request(request):
    context = {}

    if request.method == 'GET':
        return render(request, 'onlinecourse/user_registration.html', context)

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']

        user_exist = False

        try:
            User.objects.get(username=username)
            user_exist = True
        except User.DoesNotExist:
            logger.debug("{} is new user".format(username))

        if not user_exist:
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password
            )

            login(request, user)
            return redirect("onlinecourse:popular_course_list")

        return render(request, 'onlinecourse/user_registration.html', context)

def login_request(request):
    context = {}

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('onlinecourse:popular_course_list')
        else:
            return render(request, 'onlinecourse/user_login.html', context)

    return render(request, 'onlinecourse/user_login.html', context)

def logout_request(request):
    print("Log out the user `{}`".format(request.user.username))
    logout(request)
    return redirect('onlinecourse:popular_course_list')

#def popular_course_list(request):

#    context = {}
#    # Se a requisição for GET, significa que o usuário quer visualizar a página
#    if request.method == 'GET':
#        # Busca os 10 cursos com mais matrículas, em ordem decrescente
#        course_list = Course.objects.order_by('-total_enrollment')[:10]
#        # Envia a lista de cursos para o template
#        context['course_list'] = course_list
#        # Renderiza o template HTML usando os dados do contexto
#        return render(request, 'onlinecourse/course_list.html', context)

# class CourseListView(View):
#     def get(self, request):
#         context = {}
#         course_list = Course.objects.order_by('-total_enrollment')[:10]
#         context['course_list'] = course_list
#         return render(request, 'onlinecourse/course_list.html', context)

class CourseListView(generic.ListView):
    template_name = 'onlinecourse/course_list.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        courses = Course.objects.order_by('-total_enrollment')[:10]
        return courses

class CourseDetailsView(generic.DetailView):
    model = Course
    template_name = 'onlinecourse/course_detail.html'

# def enroll(request, course_id):
#    # Se o usuário enviou o formulário pelo método POST
#    if request.method == 'POST':
#        # Busca o curso pelo id.
#        # Se não encontrar, retorna erro 404 automaticamente.
#        course = get_object_or_404(Course, pk=course_id)
#        # Aumenta o número de matrículas em 1
#        course.total_enrollment += 1
#        # Salva a alteração no banco de dados
#        course.save()
#        # Redireciona o usuário de volta aos detalhes 
#        return HttpResponseRedirect(
#            reverse(viewname='onlinecourse:course_details', args=(course.id,))
#        )

class EnrollView(View):
    def post(self, request, *args, **kwargs):
        course_id = kwargs.get('pk')
        course = get_object_or_404(Course, pk=course_id)

        course.total_enrollment += 1
        course.save()

        return HttpResponseRedirect(
            reverse(viewname='onlinecourse:course_details', args=(course.id,))
        )



# def course_details(request, course_id):
#     context = {}
#     # Se a requisição for GET, o usuário quer visualizar a página
#     if request.method == 'GET':
#         try:
#             # Busca o curso pelo id recebido na URL
#             course = Course.objects.get(pk=course_id)
#             # Envia o curso para o template
#             context['course'] = course
#             # Renderiza a página de detalhes
#             return render(request, 'onlinecourse/course_detail.html', context)
#         except Course.DoesNotExist:
#             # Se o curso não existir, mostra erro 404
#             raise Http404("No course matches the given id.")
        
# class CourseDetailsView(View):
#     def get(self, request, *args, **kwargs):
#         context = {}
#         course_id = kwargs.get('pk')
#
#         try:
#             course = Course.objects.get(pk=course_id)
#             context['course'] = course
#             return render(request, 'onlinecourse/course_detail.html', context)
#         except Course.DoesNotExist:
#             raise Http404("No course matches the given id.")

