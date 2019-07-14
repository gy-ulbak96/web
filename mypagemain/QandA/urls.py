from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('', views.qa_list, name="qa_list"),
    path('qa_new/', views.qa_new, name = "qa_new" ),
    path('qa_detail/<int:qa_id>', views.qa_detail, name = "qa_detail" ),
    path('qa_detail/<int:qa_id>/update', views.qa_update, name = "qa_update" ),
    path('qa_detail/<int:qa_id>/delete', views.qa_detail, name = "qa_delete" ),
]