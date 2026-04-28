from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render,get_object_or_404
from .models import Student,TransferRequest
from django.contrib.auth.models import User
from .forms import AddNewRequest

# Create your views here.

def home(request):
    return render(request,'home.html')

@login_required
def add_request(request):
    if request.method == 'POST':
        form = AddNewRequest(request.POST)
        if form.is_valid():
            student = Student.objects.create(
                user=request.user,
                full_name = form.cleaned_data['full_name'],
                University_id = form.cleaned_data['University_id'],
                academic_year = form.cleaned_data['academic_year'],
                phone = form.cleaned_data['phone'],
                telegram_user = form.cleaned_data['telegram_user'],
            )
            
            TransferRequest.objects.create(
                student_id = student,
                current_section = form.cleaned_data['current_section'],
                target_section = form.cleaned_data['target_section']
            )
            student.save()
            
            return redirect('browse_requests')
    else :
            form = AddNewRequest()

    return render(request,'add_request.html',{'form':form})

def browse_requests(request):
    all_requests = TransferRequest.objects.all()
    return render(request,'browse_requests.html',{'all_requests':all_requests})

def request_detail(request,transferRequest_id):
    transfer_request = get_object_or_404(TransferRequest,pk = transferRequest_id)
    return render(request,'request_detail.html',{'transfer_request':transfer_request})