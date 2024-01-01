from django.urls import path
from Recommend.views import popular_view , recommend_view, recommend_ui

urlpatterns = [
        path('popular/', popular_view, name="popular"),
        path('recommend', recommend_view, name= "recommend"),
        path('recommendation/', recommend_ui, name= "recommendation")

]