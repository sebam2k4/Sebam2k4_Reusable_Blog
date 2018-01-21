from django.conf.urls import url
import views

# Use the name = ' ' syntax in urls to enable the {% url ' ' %} links for html buttons.
urlpatterns = [
    url(r'^$', views.post_list, name="post_list"),
    url(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^top', views.top_posts),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^(?P<id>\d+)/edit/$', views.edit_post, name='edit'),
]