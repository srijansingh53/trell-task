from django.shortcuts import render,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponse

from .forms import UserForm
from .models import Movies, Tickets

from django.contrib import messages
# Create your views here.


def index(request):
    # authenticate
    
    if request.method=='GET':
        if not request.user.is_authenticated:
            return render(request, 'movies/login.html')
        else:
            return render(request, 'movies/index.html')
    

def signup(request):
    
    form = UserForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        # print(username,password,'dshashbdj')
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'movies/index.html')
    context = {
        "form": form,
    }
    return render(request, 'movies/signup.html', context)



def login_user(request):
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'movies/index.html')
            return render(request, 'movies/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'movies/login.html', {'error_message': 'Invalid login'})

    return render(request, 'movies/login.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'movies/login.html', context)

# def search_movies(request):
#     if request.method=='GET':
#         if not request.user.is_authenticated:
#             return render(request, 'movies/login.html')
#         else:
#             return render(request, 'movies/searched.html')

def search_autocomplete(request):
    if not request.user.is_authenticated:
            return render(request, 'movies/login.html')
    
    if 'term' in request.GET:
        movie_searched = Movies.objects.filter(name__istartswith=request.GET.get('term'))[:10]
        names = list()

        for movie in movie_searched:
            names.append(movie.name)

        return JsonResponse(names, safe=False)
        
    elif 'q' in request.GET:
        q = request.GET.get('q')
        print(q)
        movies = Movies.objects.filter(name__istartswith=str(q))
        return render(request, 'movies/movies.html',{ 'movies':movies })

def add_movies(request):
    if not request.user.is_authenticated:
        return render(request, 'movies/login.html')
    else:
        if request.method == "POST":

            name = request.POST['movie_name']
            desc = request.POST['desc']
            director = request.POST['director']
            duration = int(request.POST['duration'])

            if Movies.objects.filter(name=name).exists():
                messages.success(request, 'The movie already exists')
                return render(request, 'movies/add_movies.html')

            Movies(name=name, dec=desc, director=director, duration=duration).save()
            return render(request, 'movies/movies.html')
        return render(request, 'movies/add_movies.html')

def show_movies(request):
    # print('done')
    if not request.user.is_authenticated:
        return render(request, 'movies/login.html')
    else:
        if request.method == "GET":
            movies = Movies.objects.all()
            # print(movies,'jhdgjasgkjs')
            return render(request, 'movies/movies.html', {'movies': movies})

def add_timing(request, movie_id):
    print('f')
    if not request.user.is_authenticated:
        return render(request, 'movies/login.html')
    else:
        if request.method=='GET':
            movie = get_object_or_404(Movies, pk=movie_id)
            print(movie.name)
            movie={'name':movie.name}
            return render(request, 'movies/timing.html', {'movie': movie})

def timing(request):
    if request.method=='POST':
        name = request.POST['movie_name']
        movie = Movies.objects.get(name=name)
        timing = request.POST['time']
        price = request.POST['price']
        total_tickets = int(request.POST['tickets'])

        Tickets(name=movie, timing=timing, price=price, total_tickets=total_tickets).save()

        return render(request, 'movies/index.html')

def purchase(request, movie_id):
    if not request.user.is_authenticated:
        return render(request, 'movies/login.html')
    else:
        if request.method=='GET':
            movie = get_object_or_404(Movies, pk=movie_id)
            tickets = Tickets.objects.filter(name=movie)

            return render(request, 'movies/purchase.html', {'tickets':tickets})
            

