# coding: utf8

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
import os
admin.autodiscover()

urlpatterns = patterns('',
    # 静态文件
    url(r'^css/(.*)$' , 'django.views.static.serve', {'document_root': os.path.join( settings.STATIC_DIR , 'css' ) } ) ,
    url(r'^font/(.*)$' , 'django.views.static.serve', {'document_root': os.path.join( settings.STATIC_DIR , 'font' ) } ) ,
    url(r'^img/(.*)$' , 'django.views.static.serve', {'document_root': os.path.join( settings.STATIC_DIR , 'img' ) } ) ,
    url(r'^js/(.*)$' , 'django.views.static.serve', {'document_root': os.path.join( settings.STATIC_DIR , 'js' ) } ) ,    
    # 登录页面
    url(r'^$' , 'oa.views.index', name='index') ,
    
    #登陆部分
    url(r'^login_up/$', 'oa.views.login_view'), 
    url(r'^main/$', 'oa.views.main_view'), 
    url(r'^admin/', include(admin.site.urls)),
    
    #快递发货
    url(r'^kd_info/$', 'oa.zjxx.kd_info_view'), 
    url(r'^update_kdxx/$', 'oa.zjxx.update_kdxx_view'), 
    url(r'^kdxx_del/$', 'oa.zjxx.kdxx_del_view'), 
    url(r'^kd_edit/$', 'oa.zjxx.kd_edit_view'),
    url(r'^add_kdxx_tz/$', 'oa.zjxx.add_kdxx_tz_view'),
    url(r'^add_kdxx/$', 'oa.zjxx.add_kdxx_view'),

    # 用户信息管理
    url(r'^user_info/$', 'oa.zjxx.user_info_view'), 
    url(r'^update_user/$', 'oa.zjxx.update_user_view'), 
    url(r'^user_del/$', 'oa.zjxx.user_del_view'), 
    url(r'^user_edit/$', 'oa.zjxx.user_edit_view'),
    url(r'^add_user_tz/$', 'oa.zjxx.add_user_tz_view'),
    url(r'^add_user/$', 'oa.zjxx.add_user_view'),

    #导出文件
    url(r'^file_download_tz/$', 'oa.zjxx.file_download_tz_view'),
    url(r'^download/$', 'oa.zjxx.download_view'),
 
 

)