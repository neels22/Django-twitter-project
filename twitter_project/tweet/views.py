from django.shortcuts import render,redirect
from .models import Tweet
from .forms import TweetForm


# Create your views here.


def index(req):
    return render(req,'index.html')


def tweet_list(request):
    tweet = Tweet.objects.all()
    return render(request, 'tweet_list.html',{
        "tweets":tweet 
    })

def tweet_create(request):

    if request.method =="POST":
        form = TweetForm(request.POST,)

        # ......
    else:
        form = TweetForm()
    return render(request, "tweet_form.html",{
        "form":form
    })
 

def tweet_edit(request,tweet_id):
    pass 

def tweet_delete(request,tweet_id):
    pass 