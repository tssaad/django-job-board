from django.shortcuts import render
from job.forms import ApplicationForm
from .models import Job, Category
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.

def job_list(request):
    job_list = Job.objects.all()
    job_list = pagination_func(request, job_list)
    context = {'jobs': job_list} 
    return render(request, 'job/job_list.html', context)

def job_detail(request, slug):
    job_detail = Job.objects.get(JOBSlug=slug)
    if request.method == "POST":
        form=ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            #form.save()
            myform = form.save(commit=False)
            myform.APPJob = job_detail
            myform.save()
            message="Thanks for applying"
            messages.add_message(request, messages.INFO, message)
    else:
        form=ApplicationForm

    context = {'job': job_detail, 'form' :form}
    return render(request, 'job/job_detail.html', context)

def pagination_func(request, list):
    paginator = Paginator(list, 25) # Show 25 contacts per page.
    
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)

