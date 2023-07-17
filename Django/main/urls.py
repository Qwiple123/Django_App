
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path("", views.index,name="homepage"),
    path("<int:id>/", views.test_view),
    path('create',views.test_create,name='test_create'),
    path('create_question/<int:id>',views.test_question_create,name="create_question"),
    path('create_answer/<int:test_id>/<int:question_id>',views.test_answer_create,name="create_answer"),
    path('update_test/<int:test_id>',views.update_test,name='update_test'),
    path('delete_test/<int:test_id>',views.delete_test,name='delete_test'),
    path("reg", views.register_request,name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
