from django.conf.urls.defaults import url,include

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
import homepage.views as homepage
import contact.views as contacts
from django.conf.urls.static import static
from django.conf import settings
#import testDan.views as views3

urlpatterns = [url(r'^$',homepage.index,name='home'),
               url(r'^contact/$',contacts.index,name='contacts'),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Examples:
    # url(r'^$', 'DownHomeTAP.views.home', name='home'),
    # url(r'^DownHomeTAP/', include('DownHomeTAP.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
