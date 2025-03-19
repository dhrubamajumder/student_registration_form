from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Book
from .forms import BookForms

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'auth/login.html')
    else:
        initial_data = {'username':'', 'password1':'', 'password2':''}
        form = UserCreationForm(initial = initial_data)
    return render(request, 'auth/register.html', {'form':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage')
    else:
        initial_data = {'username':'', 'password':''}
        form = UserCreationForm(initial = initial_data)
    return render(request, 'auth/login.html', {'form':form})


def dashboard(request):
    return render(request, 'book_list.html')

def logout_view(request):
    logout(request)
    return redirect('login')



# Create your views here.

def homepage(request):
    books = Book.objects.all()
    # books = Book.objects.filter(user=request.user)

    # user_id = request.user.id -------- 'user_id' : user_id
    
    return render(request, 'book_list.html', {'books':books})

# --------     Add to Book  --------------
def add_book(request):
    if request.method == 'POST':
        form = BookForms(request.POST)
        if form.is_valid():
            book = form.save(commit=False)  # Create object but don't save yet
            book.user = request.user  # Assign logged-in user
            book.save()  # Save to the database
            return redirect('homepage')
    else:
        print("Get the form")  # This line is optional, can be removed
    
    form = BookForms()
    return render(request, 'add_book.html', {'form': form})


# -----------  Update Book View  --------------
def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForms(request.POST, instance=book) 
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = BookForms(instance=book)
    return render(request, 'add_book.html', {'form':form})



# ----------    Delete Book View  -------------------
def delete_book(request,book_id):
    book = Book.objects.get(id=book_id)
    if book: 
        
        book.delete()
        
    return redirect('homepage')