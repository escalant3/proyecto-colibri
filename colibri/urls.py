from django.conf.urls import patterns, include, url
from tastypie.api import Api
from parliamentarygroup.api import GroupResource, PartyResource
from member.api import MemberResource, MemberPartyResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(GroupResource())
v1_api.register(PartyResource())
v1_api.register(MemberPartyResource())
v1_api.register(MemberResource())

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls))

)