from django.conf.urls import url

urlpatterns = [
    url('r^$/',view.),
    url('catalog/', include('catalog.urls')),
]