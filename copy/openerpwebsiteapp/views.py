from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from openerpwebsiteapp.forms import ContactusForm
from openerpwebsiteapp.models import ContactUs,news


def home(request):
	newss=news.objects.all().order_by('-date')[:10]
        return render_to_response('index.html',{'new':newss},)



#def base(request):
#	ci=RequestContext(request)
 #       newss=news.objects.all()[0:10]
  #      return render_to_response('base.html',{'new':newss},ci)
def content(request,title):
	return render_to_response(title+'.html')

@csrf_exempt
def contactus(request):
	ci=RequestContext(request)
	if request.is_ajax():
        	if request.method=="POST":
                	contactusform=ContactusForm(request.POST or none)
                   	if contactusform.is_valid():
                        	name=contactusform.cleaned_data['name']
                       		mobile=contactusform.cleaned_data['mobile']
                        	email=contactusform.cleaned_data['email']
                                message=contactusform.cleaned_data['message']
                                ContactUs.objects.create(name=name,email=email,mobile=mobile,message=message)
				msg="your form has been submitted"
				contactusform=ContactusForm()
                                return render_to_response('contactus.html',{'form':contactusform,'msg':msg},ci)
			else:
                               return render_to_response('contactus.html',{'form':contactusform},ci)
		else:
	                contactusform=ContactusForm()
        	        return render_to_response('contactus.html',{'form':contactusform},ci)
	else:
		contactusform=ContactusForm()
                return render_to_response('contactus.html',{'form':contactusform},ci)

			

