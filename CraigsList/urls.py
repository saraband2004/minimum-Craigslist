"""CraigsList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from CraigsList import views
from listing import views as listing_views
from CraigsList import views

#from listing.views import post as post2


#from CraigsList import views
#from CraigsList.apps import Application

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', views.first),
    #url('recent/', recentlisting, name='recent'),
    url('all/', views.PostListView.as_view(), name='all'),
    url('recent/', views.recentlisting, name='recent'),
    path('listing/<int:pk>/', views.PostDetailView.as_view(), name='listing-detail'),
    url('post/', views.PostCreateView.as_view(), name='post'),
    url('thankyou/', views.thankyou, name='thank_you'),
    url('tosearch/', views.tosearch),
    #path('search2', views.PostSearchListView.as_view(), name = 'search-result'),
    path('search', views.search2, name = 'searchresult'),
    path('search_cap', views.search2caption, name = 'searchresult_caption'),
    path('paperbag/', include('CraigsList.url2')),
    path('paperbag', include('CraigsList.url2')),
]
