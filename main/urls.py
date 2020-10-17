from django.urls import path,re_path


from . import views

urlpatterns = [
    path('all', views.index, name='main'),
    path('<str:listing_id>', views.listing, name ='listing'),
    path('', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('update/<int:rec_id>',views.editrec,name = 'update'),
    path('add/<int:rec_id>',views.addrec,name = 'add')
]