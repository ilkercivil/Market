from django.urls import path
from.views import IndexView,AboutsView,ServicesView,BlogsView,ContactsView



urlpatterns=[
    path ('',IndexView.as_view(), name='index'),
    path ('abouts',AboutsView.as_view(), name='abouts'),
    path ('services',ServicesView.as_view(), name='services'),
    path ('blogs',BlogsView.as_view(), name='blogs'),
    path ('contacts',ContactsView.as_view(), name='contacts')

]