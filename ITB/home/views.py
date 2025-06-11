from django.shortcuts import render
from home.modals import Course, MissionVision, TeamMember

def home(request):
    context = {
        'courses': Course.objects.filter(is_featured=True),
        'mission_vision': MissionVision.objects.first(),
        'ceo': TeamMember.objects.filter(is_ceo=True).first()
    }
    return render(request, 'home.html', context)