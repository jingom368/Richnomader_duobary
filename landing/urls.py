from django.urls import path

from landing import views

app_name = "landing"
urlpatterns = [
    path("base/", views.base),
    path("duobary/", views.duobary),
    # path("detail/", views.detail),
    path("create/", views.landing_post_create, name="create"),
    path("home/",views.landing_home, name="home"),
    path("post-read/<int:post_id>/", views.landing_post_read),
    path("post-update/<int:post_id>/", views.landing_post_update),
    path("post-delete/<int:post_id>/", views.landing_post_delete),
    path("detail/", views.landing_post_collect),
    path("test/", views.landing_test),
    path("landing_index/", views.landing_index),
]