from django.conf.urls import include, url
from django.contrib import admin
from basehandler.views import HomePage, CompanyStatistics, CompanyRating


urlpatterns = [
    # Examples:
    # url(r'^$', 'compstats.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomePage.as_view(), name='home'),
    url(r'^company-rating/$', CompanyRating.as_view(), name='compratings'),
    url(r'^company-statistics/$', CompanyStatistics.as_view(), name='companystatistics'),
]
