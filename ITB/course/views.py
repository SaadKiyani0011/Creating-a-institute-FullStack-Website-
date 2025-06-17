from django.shortcuts import render, get_object_or_404
from .models import Course, CourseCategory

def course_list(request, category_slug=None):
    categories = CourseCategory.objects.all()
    courses = Course.objects.all()

    selected_category = None
    if category_slug:
        selected_category = get_object_or_404(CourseCategory, slug=category_slug)
        courses = courses.filter(category=selected_category)

    context = {
        'categories': categories,
        'courses': courses,
        'selected_category': category_slug,
    }
    return render(request, 'courses.html', context)


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'courses.html', {'course': course})
