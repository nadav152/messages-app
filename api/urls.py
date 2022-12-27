from api import views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'message', views.MessageViewSet,basename='message')
router.register(r'message-to-user', views.MessageToUserViewSet,basename='message-to-user')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # url for the main API view page
    path('', include(router.urls)),

    # url that allow us using log in and log out (username and password)
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
