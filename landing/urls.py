from django.urls import path

from landing import views

urlpatterns = [
    # path("detail/", views.detail),
    path("create/", views.landing_post_create),
    path("home/",views.landing_home),
    path("post-read/<int:post_id>/", views.landing_post_read),
    path("post-update/<int:post_id>/", views.landing_post_update),
    path("post-delete/<int:post_id>/", views.landing_post_delete),
    path("detail/", views.landing_post_collect),
]