"""
URL mapping for the recipe app.
"""
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)


app_name = "recipe"
# urls created automatic by router
urlpatterns = [
    path('', include(router.urls)),
]