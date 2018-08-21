# Third Party Stuff
from rest_framework.routers import DefaultRouter

# IVR Management Stuff
from ivr_management.base.api.routers import SingletonRouter
from ivr_management.users.api import CurrentUserViewSet
from ivr_management.users.auth.api import AuthViewSet

default_router = DefaultRouter(trailing_slash=False)
singleton_router = SingletonRouter(trailing_slash=False)

# Register all the django rest framework viewsets below.
default_router.register('auth', AuthViewSet, base_name='auth')
singleton_router.register('me', CurrentUserViewSet, base_name='me')

# Combine urls from both default and singleton routers and expose as
# 'urlpatterns' which django can pick up from this module.
urlpatterns = default_router.urls + singleton_router.urls
