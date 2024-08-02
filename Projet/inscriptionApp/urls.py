from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home_view, name="home-view"),
    path('save/',views.save_etudiant, name="save-etudiant"),
    path('update/<str:pk>',views.update_etudiant, name="update-etudiant"),
    path('delete/<str:id>',views.delete_etudiant, name='delete-etudiant'),
    path('list/',views.list_etudiant, name="list-etudiant"),
    path('inscrire/',views.save_inscription, name='save-inscription'),
    path('liste-inscrit/',views.list_inscrit, name="list-inscrit"),
    path('login/',views.login_view, name="login"),
    path('logout/',views.logout_view, name="logout")
]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
