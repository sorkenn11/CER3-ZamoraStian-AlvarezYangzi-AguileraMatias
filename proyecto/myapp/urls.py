from django.urls import path,include
from rest_framework import routers
from myapp  import views

router=routers.DefaultRouter()
router.register(r'producciondiaria',views.ProduccionDiariaSet)

urlpatterns=[
    path('',include(router.urls))
]