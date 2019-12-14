from django.urls import path
from . import views


urlpatterns = [
    path('example/', views.hello, name="example-hello"),
    path('',  views.CrudView.as_view(), name='crud_ajax'),
    path('create/',  views.CreateCrudUser.as_view(), name='crud_ajax_create'),
    path('update/',  views.UpdateCrudUser.as_view(), name='crud_ajax_update'),
    path('delete/',  views.DeleteCrudUser.as_view(), name='crud_ajax_delete'),
]