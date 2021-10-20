from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-project', views.add_project, name='add-project'),
    path('edit-project/<int:id>', views.edit_project, name='edit-project'),
    path('update-project', views.update_project, name='update-project'),
    path('run-git', views.run_git, name='run-git')
]
