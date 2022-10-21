from django.urls import path

from . import views
from .views import APPUpdateView

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('hello/',views.Hello.as_view(),name='hello'),
    path('update/<int:id>/', APPUpdateView.as_view(),name='update'),
    path('delete/<int:id>', views.delete, name='delete'),

]