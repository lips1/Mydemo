
from django.shortcuts import render, redirect
from princesswing.models import signin
from django.contrib import auth

def myarea(request):
    apiurl = 'https://desk.zoho.com/api/v1/tickets'
    headers={'Accept':'application/json',
		    'Content-Type':application/json,
		    "Authorization:zoho-oauthtokene759838d72241930d9448dbbd7b80417"}
             c = request.POST.get('cat')
             d = request.POST.get('message')
             e = request.POST.get('subject')
             f = request.POST.get('name')
             g = request.POST.get('url')
             h = request.POST.get('email')
             i = request.POST.get('phn')
             j= request.POST.get('image')
             k = request.POST.get('dep')
    request_data={"Category" : c,
                  "Discription" : d,
                  "subject" : e,
                  "contactname" : f,
                  "PWS lab project URL" :g,
                  "Email" : h,
                  "phone" : i,
                  "File Upload" : j,
                  "Department" : k,
                   }'
    data=json.dumps(request_data)
    try
	    response_body=request(method='POST',url=api_url,data=data,headers=headers)
    except Exception as e:
	    raise ValidationErroor(e)
    return response_body

    if response_data.status_code in [200,201]:
	    response_data=response_data.josn()
    return render(request,"princesswing/myarea.html")



def myarea(request):
	return render(request,"princesswing/myarea.html")


def homepage1(request):

		c = request.POST.get('uname')
		d = request.POST.get('psw')

		obj = signin(username=c, password=d)
		obj.save()
		return render(request, "princesswing/homepage1.html")


def signincall(request):
     return render(request,"princesswing/homepage1")


def myareacall(request):
    return render(request, "princesswing/myarea")



