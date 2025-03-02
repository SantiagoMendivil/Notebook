from django.views import View
from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm
from django.views import generic

"""Simple class base view"""
class CourseView(View):
    
    def get(self, request):
        course = Course.objects.get(pk=course.pk)
        template = "courses.html"
        
        return render(request, template)
    
    def post(self, request):
        course = Course.objects.get(pk=course.pk)
        form = CourseForm(request.POST, instance=course)
        
        if form.is_valid():
            form.save()
            return redirect('course_detail', pk=course.pk)
        
        return render(request, 'courses.html', {'form': form})
        

"""Generic DetailView: Represents the details of an object"""
class CourseViewDetail(generic.DetailView):
    model = Course 
    template_name = 'courses.html'
    context_object_name = 'course'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = Course.objects.get(pk=course.pk)
        context['course'] = course
        return context
    
"""Generic ListView: Represents a list of objects

    - You have to specify the model
    - You have to specify the context_object_name hat will display the model
    - You can order the objects by a field in ascending or descending order (-)
    - You can paginate the objects with paginate_by
"""
class CourseListView(generic.ListView):
    model = Course
    template_name = 'courses.html'
    context_object_name = 'courses'
    ordering = ['-created_at']
    paginate_by = 5
    
"""Form View: Represents a form for submitting data

    - You have to create the form in forms.py
    - You have to validate the form with form_valid
    - You have to redirect the user when the form is successfully submitted
    - You have to pass the class some context with get_context_data()
"""
class CourseFormView(generic.FormView):
    template_name = 'courses.html'
    form_class = CourseForm
    
    def form_valid(self, form):
        form.save()
        return redirect('course_list')
    
    def get_success_url(self):
        return reverse('course_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = Course.objects.get(pk=course.pk)
        context['course'] = course
        return context
    
    