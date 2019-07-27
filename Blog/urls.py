
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('showblog/', views.showblog, name = 'showblog'),
    path('detail/<int:blog_id>/', views.detail, name = 'detail'),
    path('comment/', views.comment, name = 'comment'),
    path('delete/<int:cmnt_id>/', views.delete, name = 'delete'),
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('logged_in/', views.logged_in, name = 'logged_in'),
    path('create/', views.create, name = 'create'),
    path('postarticle/', views.postarticle, name = 'postarticle'),
    path('deletearticle/<int:article_id>/', views.deletearticle, name = 'deletearticle'),
    path('updatearticle/<int:article_id>/', views.updatearticle, name = 'updatearticle'),
    path('updated/<int:article_id>/', views.updated, name = 'updated'),
     path('upvote/<int:blog_id>/', views.upvote, name = 'upvote'),
]
