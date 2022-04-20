from django.conf.urls import url, include
from rest_framework import routers
from quickstart import views

# 注册视图
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# 添加路由
urlpatterns = [
    url(r"^", include(router.urls)),
    url(r"^api-auth/", include('rest_framework.urls', namespace='rest_framework'))
]
