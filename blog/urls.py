from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('article/<slug:slug>/', views.PostDetail.as_view(),  name='post_detail'),
    path('add_blog/', views.Addblog.as_view() , name='add_blog'),
    path('article/update/<int:pk>', views.Updateblog.as_view(), name='update_blog'),
    path('article/<int:pk>/delete', views.Deleteblog.as_view(), name='delete_blog'),
    path('about/', views.about, name='about'),
]

