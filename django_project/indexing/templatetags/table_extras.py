from django import template
from django.db.models import Sum

from indexing.models import Grade


register = template.Library()

@register.filter
def total(student, request):
    g = Grade.objects.filter(teacher__username=request.user, key_to_student=student).aggregate(Sum('grades'))['grades__sum']
    return g
