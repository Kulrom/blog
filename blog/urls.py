from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    url(r'^post/(.+)/$', 'post.views.render_post'),
    url(r'^list/$', 'post.views.list_posts'),
    url(r'^list/(\d+)/$', 'post.views.list_posts'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'post.views.list_posts'),
)
