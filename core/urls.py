from django.urls import path
from . import views
from django.views.generic import RedirectView
urlpatterns=[
  #  path('',views.index,name='index'),
    path('pet/list/',views.list_all_pet,name='listagem pets'),
    path('pet/user/',views.list_user_pet,name='MEUS PETS'),
    path('login/',views.login_user,name='LOGIN'),
    path('login/submit',views.submit_login),
    path('logout/',views.logout_user),
    path('',RedirectView.as_view(url='pet/list/')),
]
