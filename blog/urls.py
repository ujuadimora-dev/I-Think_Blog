from . import views
from django.urls import path

from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    #spath('logout/', views.logout_view, name='accounts_logout'),
]
