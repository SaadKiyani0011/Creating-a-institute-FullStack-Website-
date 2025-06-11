from django.shortcuts import render
from course.models import Course, CourseCategory
from django.shortcuts import render, get_object_or_404

def courses(request):
    categories = CourseCategory.objects.all()
    selected_category = request.GET.get('category')
    
    courses = Course.objects.all()
    if selected_category:
        courses = courses.filter(category__slug=selected_category)
    
    context = {
        'courses': courses,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'courses.html', context)


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    related_courses = Course.objects.filter(category=course.category).exclude(id=course.id)[:3]
    
    context = {
        'course': course,
        'related_courses': related_courses
    }
    return render(request, 'courses/course_detail.html', context)