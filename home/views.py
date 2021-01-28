from django.shortcuts import render
# import the class name is contactdata
from home.models import contactdata
# from datetime import datetime    
# def index (request):
#     return HttpResponse("Hey Farheen! This is your 1st page")
# def about (request):
#     return HttpResponse("Hey Farheen! This is your 2nd page..")

# variable examples
# def index(request):
#     context = {
#         "variable1" : "Farheen, you are next PM",
#         "variable2" : "Be confident"
#     }
#     return render(request,'hello.html',context)
    # return render(request,'hello.html',{'name':'Mini'})
# Create your views here.
# def index(request):
#     return render(request,'bars.html')

def index(request):
    return render(request,'index.html') 
def home(request):
    return render(request,'index.html')  
def skills(request):
    return render(request,'skills.html')  
def workexp(request):
    return render(request,'workexp.html')
def educatiion(request):
    return render(request,'education.html')
def contact(request):
    if request.method == 'POST':
        # trying to connect with sql
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        comment = request.POST['comment']
        # Contactdata = contactdata.objects.create_contactdata(name=name, email=email, phone=phone,comment=comment,date=datetime.today())
        # Contactdata.save();
        x = contactdata(name=name, email=email, phone=phone,comment=comment)
        x.save();
    return render(request,'contact.html')
def footer(request):
    return render(request,'footer.html')
def about(request):
    return render(request,'about.html')

    # need some clarity for contact page
# def client(request):
#     return HttpResponse("This is a client page")
# def add(request):
#     val1 = int(request.POST["num1"])
#     val2 = int(request.POST["num2"])
#     res = val1 + val2

#     return render(request,'Result.html', {'result' : res})


