from django.shortcuts import render,HttpResponse
import requests,json
# Create your views here.
def index(request):
    
    url = "https://livescore6.p.rapidapi.com/matches/v2/list-live"
    querystring = {"Category":"soccer"}
    headers = {
        'x-rapidapi-key': "0ec2caeb83msh6e33b962033e669p1d1f91jsn809f4fccd578",
        'x-rapidapi-host': "livescore6.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)

    variables={
        'response':response,
        'country':response.objects.all()
    }
    return render(request,'index.html',variables)
    # return HttpResponse(response)   
    