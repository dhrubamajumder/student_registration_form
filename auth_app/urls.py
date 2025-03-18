from django.urls import path
from . import views
from.views import homepage, add_book, delete_book, update_book,dashboard,logout_view, login_view, register_view


urlpatterns = [
    path('', register_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('dashboard/', dashboard, name="dashboard"),

    path('homepage/', homepage, name="homepage"),
    path('add_book/', add_book, name="add_book"),
    path('delete/<int:book_id>/',delete_book, name='delete_book'),   
    path('update/<int:book_id>/',update_book, name='update_book'),
]

