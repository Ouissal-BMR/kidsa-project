from django.shortcuts import render

def home(request):
    return render(request, 'iindex.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def event(request):
    return render(request, 'event.html')
def event_details(request):
    return render(request,'event-details.html')
def event_carousel(request):
    return render(request, 'event-carousel.html')
def faq(request):
    return render(request, 'faq.html')
def index(request):
    return render(request,'index.html')
def index2(request):
    return render(request, 'index-2.html')
def index3(request):
    return render(request,'index-3.html')
def index4(request):
    return render(request, 'index-4.html')
def indexFour(request):
    return render(request, 'index-four-page.html')
def indexOne(request):
    return render(request, 'index-one-page.html')
def indexThree(request):
    return render(request, 'index-three-page.html')
def indexTwo(request):
    return render(request, 'index-two-page.html')
def news(request):
    return render(request, 'news.html')
def news_carousel(request):
    return render(request, 'news-carousel.html')
def news_details(request):
    return render(request, 'news-details.html')
def news_grid(request):
    return render(request,'news-grid.html')
def pricing(request):
    return render(request, 'pricing.html')
def program(request):
    return render(request, 'program.html')
def program_carousel(request):
    return render(request, 'program-carousel.html')
def program_details(request):
    return render(request, 'program-details.html')
def team(request):
    return render(request,'team.html')
def team_carousel(request):
    return render(request, 'team-carousel.html')
def team_details(request):
    return render(request, 'team-details.html')
def NotfoundPage(request):
    return render(request, '404.html')

def ContactPHP(request):
    return render(request, 'contact.php')