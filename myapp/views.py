from django.shortcuts import render, get_object_or_404
from .models import Scheme, SchemeCasteMapping
import datetime

def home(request):
    schemes = Scheme.objects.filter(end_date__gte=datetime.date.today()).order_by('end_date')  
    casteMapping = SchemeCasteMapping.objects.all()

    if request.method == 'POST':
        scheme_name = request.POST.get('scheme-name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        education = request.POST.get('education')

        if scheme_name:
            schemes = schemes.filter(name__icontains=scheme_name)
        if gender:
            schemes = schemes.filter(gender=gender)
        if age:
            casteMapping = casteMapping.filter(min_age__lte=age, max_age__gte=age)
            casteMapping_scheme_ids = casteMapping.values_list('scheme_id', flat=True)
            schemes = schemes.filter(id__in=casteMapping_scheme_ids)
        if education:
            schemes = schemes.filter(edu_eligibility__choice=education)

    context = {
        'schemes': schemes,
        'casteMapping': casteMapping
    }

    return render(request, 'myapp/home.html', context)


def scheme_details(request, scheme_id):
    scheme = get_object_or_404(Scheme, id=scheme_id)
    casteMapping = SchemeCasteMapping.objects.filter(scheme=scheme)
    scheme.views += 1  
    scheme.save()  
    
    return render(request, 'myapp/scheme_details.html', {'scheme': scheme, 'casteMapping': casteMapping})


def archived_schemes(request):
  
  schemes = Scheme.objects.filter(end_date__lt=datetime.date.today()).order_by('-end_date')
  casteMapping = SchemeCasteMapping.objects.all()
  if request.method == 'POST':
        scheme_name = request.POST.get('scheme-name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        education = request.POST.get('education')

        if scheme_name:
            schemes = schemes.filter(name__icontains=scheme_name)
        if gender:
            schemes = schemes.filter(gender=gender)
        if age:
            casteMapping = casteMapping.filter(min_age__lte=age, max_age__gte=age)
            casteMapping_scheme_ids = casteMapping.values_list('scheme_id', flat=True)
            schemes = schemes.filter(id__in=casteMapping_scheme_ids)
        if education:
            schemes = schemes.filter(edu_eligibility__choice=education)
      
  context = {'schemes': schemes, 'casteMapping': casteMapping}
  return render(request, 'myapp/archived_schemes.html', context)
