from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# from django.core.files import File

# Create your views here.
# def getCertificate(request):
#     return render(request,"home.html")

def getCertificate(request,roll_no=None):
    if request.method=="GET":
        cntxt = {}
        # cntxt = {roll_no : -1}
        if roll_no==None:
            return render(request,"home.html",context=cntxt)
        try:
            cntxt["files"] = Student.objects.get(pk=roll_no)
            
        except Student.DoesNotExist:
            cntxt["error"] = "!!! Roll No : {0} is not found. !!! Please enter a valid Roll No.".format(roll_no)
        return render(request,"home.html",context=cntxt)
    # if request.method=="POST":
    #     cntxt = {
    #         "roll_no": request.roll_no
    #     }
    #     # return render(request,"home.html",context=cntxt)
    #     print("Post")
    #     return HttpResponse("<h1>Hello World</h1>")