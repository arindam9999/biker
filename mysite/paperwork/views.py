from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.
def home(request):
	query=request.GET.get("q")
	if query:
		posts=Post.objects.filter(registration_no=query)
		text='Documents'
		if posts:
			return render(request,'paperwork/view.html',{ 'post':posts, 'text':text})
		else:
			text='No Documents Found!'
			return render(request,'paperwork/view.html',{ 'post':posts , 'text':text})


	return render(request,'paperwork/search.html')


	



