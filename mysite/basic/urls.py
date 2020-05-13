from basic import views
from django.conf.urls import url

urlpatterns = [
        url(r'^home/$', views.Home.as_view(), name='home'),
        url(r'^about/$', views.About.as_view(), name='about'),
        url(r'^forecast/$', views.forecast, name='forecast'),
        url(r'^test$', views.test, name='test'),
        url(r'^update/$', views.Update.as_view(), name='update'),
        url(r'^browse/$', views.Browse.as_view(), name='browse'),
        url(r'^browse_megawatts/$', views.browse_megawatts, name='browse_megawatts'),
        url(r'^browse_festival/$', views.browse_festival, name='browse_festival'),
        url(r'^update_megawatts/$', views.upload_megawatts, name='update_megawatts'),
        url(r'^update_festival/$', views.upload_festival, name='update_festival'),
        url(r'^results/$', views.Results.as_view(), name='results'),
        url(r'^user_login/$', views.log_in, name='loginpage'),
        url(r'^user_logout/$', views.log_out, name='logoutpage'),
]
