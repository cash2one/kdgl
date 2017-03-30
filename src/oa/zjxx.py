# coding: utf8
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
import os, json, datetime, xlsxwriter
from zjyw_utils import *
from const import *

log.init_log( 'kdgl' , True )

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def kd_info_view(request):
    try:
        content={}
        ls=[]
        content['xym'] = '0'
        if not request.session.get('username',''):
            return HttpResponseRedirect('/')
        username = request.session.get('username','').encode('utf8')
        password = request.session.get('password','').encode('utf8')
        log.info( "kdgl", '用户【%s】已进入kdgl_view函数', username)
        sql = "select * from express_info order by id desc"
        with myapi.connection() as con:
            cur = con.cursor()
            rs = myapi.sql_execute(cur, sql)
            while rs.next():
                rs_lst = rs.to_dict()
                ls.append(rs_lst)
        content['xym'] = '000000'
        content['cont'] = render_to_string( 'kdxx_idx.html', {'kd_info':ls} )
        return HttpResponse( json.dumps( content), content_type='application/json' )
    except Exception, e :
        content['xyxx'] = '后台函数[kd_info_view]执行错误:%s' % str( e )
        log.exception( 'kdgl', '后台函数[kd_info_view]执行错误:%s', str( e ) )
        return HttpResponse( json.dumps( content) , content_type='application/json' )


# 删除快递信息
def kdxx_del_view(request):
    try:
        content={}
        ls=[]
        content['xym'] = '0'
        if not request.session.get('username',''):
            return HttpResponseRedirect('/')
        id = request.POST.get('id','').encode('utf8')
        # 删除
        sql = "delete from express_info where id='%s' " % id 
        with myapi.connection() as con:
            cur = con.cursor()
            cur.execute(sql)
           
        log.info( "kdgl", "快递信息删除sql【%s】", sql )
        if cur.rowcount == 1:
            log.info( "kdgl", "主机删除成功！" )
            content['xym'] = '000000'
            content['xyxx'] = '主机删除成功！'
            return HttpResponse( json.dumps( content), content_type='application/json' )
        else:
            # 返回错误信息
            log.info( "kdgl", '快递信息删除失败')
            content['xyxx'] = '快递信息删除失败！'
            return HttpResponse( json.dumps( content) , content_type='application/json' )
    except Exception, e :
        content['xyxx'] = '后台函数[kdxx_del_view]执行错误:%s' % str( e )
        log.exception( 'kdgl', '后台函数[kdxx_del_view]执行错误:%s', str( e ) )
        return HttpResponse( json.dumps( content) , content_type='application/json' )

# 更新快递信息页面跳转     
def update_kdxx_view(request):
    try:
        content={}
        content['xym'] = '0'
        id = request.GET.get('id','').encode('utf8')
        express_classification = request.GET.get('express_classification','').encode('utf8')
        express_user_id = request.GET.get('express_user_id','').encode('utf8')
        sender_name = request.GET.get('sender_name','').encode('utf8')
        sender_address = request.GET.get('sender_address','').encode('utf8')
        sender_phone = request.GET.get('sender_phone','').encode('utf8')
        reciver_name = request.GET.get('reciver_name','').encode('utf8')
        reciver_address = request.GET.get('reciver_address','').encode('utf8')
        reciver_phone = request.GET.get('reciver_phone','').encode('utf8')
        express_money = request.GET.get('express_money','').encode('utf8')
        express_number = request.GET.get('express_number','').encode('utf8')
        express_status = request.GET.get('express_status','').encode('utf8')
        shelf_number = request.GET.get('shelf_number','').encode('utf8')
        type = request.GET.get('type','').encode('utf8')
        created_at = request.GET.get('created_at','').encode('utf8')
        if not request.session.get('username',''):
            return HttpResponseRedirect('/')
        content['xym'] = '000000'
        return render_to_response( 'kdxx_edit.html', {'express_classification': express_classification, 'express_user_id': express_user_id, 'sender_name': sender_name, 'express_money':express_money, 'express_number': express_number, 'express_status': express_status, 'sender_address': sender_address, 'reciver_name': reciver_name, 'id': id, 'sender_phone': sender_phone, 'reciver_address': reciver_address, 'shelf_number': shelf_number, 'reciver_phone': reciver_phone, 'type': type, 'created_at': created_at }, context_instance=RequestContext(request) )
    except Exception, e :
        log.exception( 'kdgl', '后台函数[update_kdxx_view]执行错误:%s', str( e ) )
        return render_to_response( 'kdxx_edit.html', {'xyxx':'后台函数[update_kdxx_view]执行错误:%s' % str( e )}, context_instance=RequestContext(request) )

# 编辑快递信息
def kd_edit_view(request):
    try:
        content={}
        ls=[]
        content['xym'] = '0'
        if not request.session.get('username',''):
            return HttpResponseRedirect('/')
        id = request.POST.get('id','').encode('utf8')
        express_classification = request.POST.get('express_classification','').encode('utf8')
        express_user_id = request.POST.get('express_user_id','').encode('utf8')
        sender_name = request.POST.get('sender_name','').encode('utf8')
        sender_address = request.POST.get('sender_address','').encode('utf8')
        sender_phone = request.POST.get('sender_phone','').encode('utf8')
        reciver_name = request.POST.get('reciver_name','').encode('utf8')
        reciver_address = request.POST.get('reciver_address','').encode('utf8')
        reciver_phone = request.POST.get('reciver_phone','').encode('utf8')
        express_money = request.POST.get('express_money','').encode('utf8')
        express_number = request.POST.get('express_number','').encode('utf8')
        express_status = request.POST.get('express_status','').encode('utf8')
        shelf_number = request.POST.get('shelf_number','').encode('utf8')
        type = request.POST.get('type','').encode('utf8')
        created_at = request.POST.get('created_at','').encode('utf8')
        #校验快递员编号是否重复
        sql = "select number from auth_user where number='%s'"%express_user_id
        with myapi.connection() as con:
            cur = con.cursor()
            rs = myapi.sql_execute(cur, sql)
            if not rs.next():
                log.info( "kdgl", '快递员编号不存在')
                content['xyxx'] = '快递员编号不存在'
                return HttpResponse( json.dumps( content) , content_type='application/json' )
        sql2 = "select type from express_info where id='%s'"%id
        with myapi.connection() as con:
            cur = con.cursor()
            rs = myapi.sql_execute(cur, sql2)
            if rs.next():
                rs_dic = rs.to_dict()
                type_old = rs_dic['type']
        # 修改快递信息
        sql = "update express_info set express_classification='%s', express_user_id='%s', sender_name='%s', express_money='%s', express_number='%s', express_status='%s', sender_address='%s', reciver_name='%s', sender_phone='%s', reciver_address='%s', shelf_number='%s', reciver_phone='%s', type='%s', created_at='%s', type='%s' where id='%s'" % (express_classification,  express_user_id,  sender_name, express_money,  express_number,  express_status, sender_address, reciver_name, sender_phone, reciver_address, shelf_number,  reciver_phone,  type, created_at, type, id )
        with myapi.connection() as con:
            cur = con.cursor()
            cur.execute(sql)
        log.info( "kdgl", "修改快递信息sql【%s】", sql )
        if cur.rowcount == 1:
            log.info( "kdgl", "修改快递信息成功！" )
            # 计算用户绩效
            sql2 = "select performance from auth_user where number='%s'"%express_user_id
            with myapi.connection() as con:
                cur = con.cursor()
                rs = myapi.sql_execute(cur, sql2)
                if rs.next():
                    rs_dic = rs.to_dict()
                    performance = rs_dic['performance']
            if type=='2' and type_old=='1':
                performance = str(float(performance)-float(express_money)*0.1)
            elif type=='1' and type_old=='2':
                performance = str(float(performance)+float(express_money)*0.1)
            else:
                performance = performance
            # 更新用户绩效
            sql3 = "update auth_user set performance='%s' where number='%s'" % ( performance, express_user_id )
            with myapi.connection() as con:
                cur = con.cursor()
                cur.execute(sql3)
            content['xym'] = '000000'
            content['xyxx'] = '修改快递信息成功！'
            return HttpResponse( json.dumps( content), content_type='application/json' )
        else:
            # 返回错误信息
            log.info( "kdgl", '修改快递信息失败')
            content['xyxx'] = '修改快递信息失败！'
            return HttpResponse( json.dumps( content) , content_type='application/json' )
    except Exception, e :
        content['xyxx'] = '后台函数[kd_edit_view]执行错误:%s' % str( e )
        log.exception( 'kdgl', '后台函数[kd_edit_view]执行错误:%s', str( e ) )
        return HttpResponse( json.dumps( content) , content_type='application/json' )


# 新增快递息页面跳转
def add_kdxx_tz_view(request):
    try:
        if not request.session.get('username',''):
            return HttpResponseRedirect('/')
        return render_to_response( 'kdxx_add.html', {}, context_instance=RequestContext(request) )
    except Exception, e :
        log.exception( 'kdgl', '后台函数[add_kdxx_tz_view]执行错误:%s', str( e ) )
        return render_to_response( 'kdxx_add.html', {'xyxx':'后台函数[add_kdxx_tz_view]执行错误:%s' % str( e )}, context_instance=RequestContext(request) )
        
# 新增快递信息
def add_kdxx_view(request):
    try:
        content={}
        ls=[]
        content['xym'] = '0'
        performance = 0.00
        if not request.session.get('username',''):
            return HttpResponseRedirect('/')
        express_classification = request.POST.get('express_classification','').encode('utf8')
        express_user_id = request.POST.get('express_user_id','').encode('utf8')
        sender_name = request.POST.get('sender_name','').encode('utf8')
        sender_address = request.POST.get('sender_address','').encode('utf8')
        sender_phone = request.POST.get('sender_phone','').encode('utf8')
        reciver_name = request.POST.get('reciver_name','').encode('utf8')
        reciver_address = request.POST.get('reciver_address','').encode('utf8')
        reciver_phone = request.POST.get('reciver_phone','').encode('utf8')
        express_money = request.POST.get('express_money','').encode('utf8')
        express_number = request.POST.get('express_number','').encode('utf8')
        express_status = request.POST.get('express_status','').encode('utf8')
        shelf_number = request.POST.get('shelf_number','').encode('utf8')
        type = request.POST.get('type','').encode('utf8')
        created_at = request.POST.get('created_at','').encode('utf8')

        #校验订单号是否重复
        sql = "select type from express_info where express_number='%s'"%express_number
        with myapi.connection() as con:
            cur = con.cursor()
            rs = myapi.sql_execute(cur, sql)
            while rs.next():
                log.info( "kdgl", '订单编号已存在')
                content['xyxx'] = '订单编号已存在'
                return HttpResponse( json.dumps( content) , content_type='application/json' )
        #校验快递员编号是否重复
        sql = "select number from auth_user where number='%s'"%express_user_id
        with myapi.connection() as con:
            cur = con.cursor()
            rs = myapi.sql_execute(cur, sql)
            if not rs.next():
                log.info( "kdgl", '快递员编号不存在')
                content['xyxx'] = '快递员编号不存在'
                return HttpResponse( json.dumps( content) , content_type='application/json' )
        # 新增快递信息
        sql1 = "insert into  express_info(type, shelf_number, express_status, express_number, express_money, reciver_phone, reciver_address, reciver_name, sender_phone, sender_address, sender_name,express_user_id, express_classification,created_at)values( '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % ( type, shelf_number, express_status, express_number, express_money, reciver_phone, reciver_address, reciver_name, sender_phone, sender_address, sender_name,express_user_id, express_classification,created_at )
        with myapi.connection() as con:
            cur = con.cursor()
            cur.execute(sql1)
        log.info( "kdgl", "添加快递信息sql【%s】", sql1 )
        if cur.rowcount == 1:
            log.info( "add_kdxx", "添加快递信息成功！" )
            # 计算用户绩效
            sql2 = "select performance from auth_user where number='%s'"%express_user_id
            with myapi.connection() as con:
                cur = con.cursor()
                rs = myapi.sql_execute(cur, sql2)
                if rs.next():
                    rs_dic = rs.to_dict()
                    performance = rs_dic['performance']
            performance = str(float(performance)+float(express_money)*0.1) if type=='1' else performance
            # 更新用户绩效
            sql3 = "update auth_user set performance='%s' where number='%s'" % ( performance, express_user_id )
            with myapi.connection() as con:
                cur = con.cursor()
                cur.execute(sql3)
            content['xym'] = '000000'
            content['xyxx'] = '添加快递信息成功！'
            return HttpResponse( json.dumps( content), content_type='application/json' )
        else:
            # 返回错误信息
            log.info( "kdgl", '添加快递信息失败')
            content['xyxx'] = '添加快递信息失败！'
            return HttpResponse( json.dumps( content) , content_type='application/json' )
    except Exception, e :
        content['xyxx'] = '后台函数[add_kdxx_view]执行错误:%s' % str( e )
        log.exception( 'kdgl', '后台函数[add_kdxx_view]执行错误:%s', str( e ) )
        return HttpResponse( json.dumps( content) , content_type='application/json' )



def user_info_view(request):
    try:
        content={}
        ls=[]
        content['xym'] = '0'
        if not request.session.get('username',''):
            return HttpResponseRedirect('/')
        username = request.session.get('username','').encode('utf8')
        password = request.session.get('password','').encode('utf8')
        log.info( "kdgl", '用户【%s】已进入user_info_view函数', username)
        sql = "select * from auth_user order by id desc"
        with myapi.connection() as con:
            cur = con.cursor()
            rs = myapi.sql_execute(cur, sql)
            while rs.next():
                rs_lst = rs.to_dict()
                ls.append(rs_lst)
        if ls:
            content['xym'] = '000000'
            content['cont'] = render_to_string( 'user_idx.html', {'user_info':ls} )
            return HttpResponse( json.dumps( content), content_type='application/json' )
        else:
            # 返回错误信息
            log.info( "kdgl", '用户信息不存在')
            content['xyxx'] = '用户不存在！'
            return HttpResponse( json.dumps( content) , content_type='application/json' )
    except Exception, e :
        content['xyxx'] = '后台函数[user_info_view]执行错误:%s' % str( e )
        log.exception( 'kdgl', '后台函数[user_info_view]执行错误:%s', str( e ) )
        return HttpResponse( json.dumps( content) , content_type='application/json' )


# 删除用户信息
def user_del_view(request):
    try:
        content={}
        ls=[]
        content['xym'] = '0'
        if not request.session.get('username',''):
            return HttpResponseRedirect('/')
        id = request.POST.get('id','').encode('utf8')
        # 删除
        sql = "delete from auth_user where id='%s' " % id 
        with myapi.connection() as con:
            cur = con.cursor()
            cur.execute(sql)
           
        log.info( "kdgl", "用户信息删除sql【%s】", sql )
        if cur.rowcount == 1:
            log.info( "kdgl", "用户删除成功！" )
            content['xym'] = '000000'
            content['xyxx'] = '用户删除成功！'
            return HttpResponse( json.dumps( content), content_type='application/json' )
        else:
            # 返回错误信息
            log.info( "kdgl", '用户信息删除失败')
            content['xyxx'] = '用户信息删除失败！'
            return HttpResponse( json.dumps( content) , content_type='application/json' )
    except Exception, e :
        content['xyxx'] = '后台函数[user_del_view]执行错误:%s' % str( e )
        log.exception( 'kdgl', '后台函数[user_del_view]执行错误:%s', str( e ) )
        return HttpResponse( json.dumps( content) , content_type='application/json' )

# 更新用户信息页面跳转     
def update_user_view(request):
    try:
        content={}
        content['xym'] = '0'
        id = request.GET.get('id','').encode('utf8')
        username = request.GET.get('username','').encode('utf8')
        phone = request.GET.get('phone','').encode('utf8')
        number = request.GET.get('number','').encode('utf8')
        performance = request.GET.get('performance','').encode('utf8')
        if not request.session.get('username',''):
            return HttpResponseRedirect('/')
        content['xym'] = '000000'
        return render_to_response( 'user_edit.html', {'username': username, 'phone': phone, 'number': number, 'performance':performance, 'id': id }, context_instance=RequestContext(request) )
    except Exception, e :
        log.exception( 'kdgl', '后台函数[update_user_view]执行错误:%s', str( e ) )
        return render_to_response( 'user_edit.html', {'xyxx':'后台函数[update_user_view]执行错误:%s' % str( e )}, context_instance=RequestContext(request) )

# 编辑用户信息
def user_edit_view(request):
    try:
        content={}
        ls=[]
        content['xym'] = '0'
        if not request.session.get('username',''):
            return HttpResponseRedirect('/')
        # {express_classification,  express_user_id,  sender_name, express_money,  express_number,  express_status, sender_address, reciver_name,  id,  sender_phone, reciver_address, shelf_number,  reciver_phone,  type, created_at }
        id = request.POST.get('id','').encode('utf8')
        username = request.POST.get('username','').encode('utf8')
        phone = request.POST.get('phone','').encode('utf8')
        number = request.POST.get('number','').encode('utf8')
        performance = request.POST.get('performance','').encode('utf8')
        
        # 修改用户信息
        sql = "update auth_user set username='%s', phone='%s', number='%s', performance='%s' where id='%s'" % (username,  phone,  number, performance, id )
        with myapi.connection() as con:
            cur = con.cursor()
            cur.execute(sql)
           
        log.info( "kdgl", "修改用户信息sql【%s】", sql )
        if cur.rowcount == 1:
            log.info( "kdgl", "修改用户信息成功！" )
            content['xym'] = '000000'
            content['xyxx'] = '修改用户信息成功！'
            return HttpResponse( json.dumps( content), content_type='application/json' )
        else:
            # 返回错误信息
            log.info( "kdgl", '修改用户信息失败')
            content['xyxx'] = '修改用户信息失败！'
            return HttpResponse( json.dumps( content) , content_type='application/json' )
    except Exception, e :
        content['xyxx'] = '后台函数[user_edit_view]执行错误:%s' % str( e )
        log.exception( 'kdgl', '后台函数[user_edit_view]执行错误:%s', str( e ) )
        return HttpResponse( json.dumps( content) , content_type='application/json' )


# 新增用户信息页面跳转
def add_user_tz_view(request):
    try:
        if not request.session.get('username',''):
            return HttpResponseRedirect('/')
        return render_to_response( 'user_add.html', {}, context_instance=RequestContext(request) )
    except Exception, e :
        log.exception( 'kdgl', '后台函数[add_user_tz_view]执行错误:%s', str( e ) )
        return render_to_response( 'user_add.html', {'xyxx':'后台函数[add_user_tz_view]执行错误:%s' % str( e )}, context_instance=RequestContext(request) )
        
# 新增用户信息
def add_user_view(request):
    try:
        content={}
        ls=[]
        content['xym'] = '0'
        if not request.session.get('username',''):
            return HttpResponseRedirect('/')
        username = request.POST.get('username','').encode('utf8')
        phone = request.POST.get('phone','').encode('utf8')
        number = request.POST.get('number','').encode('utf8')
        performance = request.POST.get('performance','').encode('utf8')
        password = request.POST.get('password','').encode('utf8')
        #校验用户信息
        sql = "select * from auth_user where number='%s'"%number
        with myapi.connection() as con:
            cur = con.cursor()
            rs = myapi.sql_execute(cur, sql)
            while rs.next():
                log.info( "kdgl", '快递员编号已存在')
                content['xyxx'] = '快递员编号已存在'
                return HttpResponse( json.dumps( content) , content_type='application/json' )
            
        # 新增用户信息
        sql = "insert into  auth_user(username, password, number, phone, performance)values( '%s', '%s','%s', '%s', '%s')" % ( username, password, number, phone, performance)
        with myapi.connection() as con:
            cur = con.cursor()
            cur.execute(sql)
        from django.contrib.auth.models import User
        u = User.objects.get(username='%s'%username)
        u.set_password(password)
        u.save()
        log.info( "kdgl", "添加用户信息sql【%s】", sql )
        if cur.rowcount == 1:
            log.info( "kdgl", "添加用户信息成功！" )
            content['xym'] = '000000'
            content['xyxx'] = '添加用户信息成功！'
            return HttpResponse( json.dumps( content), content_type='application/json' )
        else:
            # 返回错误信息
            log.info( "kdgl", '添加用户信息失败')
            
            content['xyxx'] = '添加用户信息失败！'
            return HttpResponse( json.dumps( content) , content_type='application/json' )
    except Exception, e :
        content['xyxx'] = '后台函数[add_user_view]执行错误:%s' % str( e )
        log.exception( 'kdgl', '后台函数[add_user_view]执行错误:%s', str( e ) )
        return HttpResponse( json.dumps( content) , content_type='application/json' )

def file_download_tz_view(request):
    try:
        content={}
        ls=[]
        content['xym'] = '0'
        if not request.session.get('username',''):
            return HttpResponseRedirect('/')
        
        content['xym'] = '000000'
        content['cont'] = render_to_string( 'file_download.html', {} )
        return HttpResponse( json.dumps( content), content_type='application/json' )
    except Exception, e :
        content['xyxx'] = '后台函数[file_download_tz_view]执行错误:%s' % str( e )
        log.exception( 'kdgl', '后台函数[file_download_tz_view]执行错误:%s', str( e ) )
        return HttpResponse( json.dumps( content) , content_type='application/json' )

def file_iterator(file_name):
        with open(file_name, 'rb') as f:
            while True:
                c = f.read()
                if c:
                    yield c
                else:
                    break
def download_view(request):
    try:
        content={}
        ls=[]
        content['xym'] = '0'
        if not request.session.get('username',''):
            return HttpResponseRedirect('/')
        title = [u'快递单号', u'快递类型', u'快递分类', u'快递费(元)' , u'快递员编号', u'发货人姓名',
         u'发货人联系方式', u'发货人地址', u'收货人姓名', u'收货人联系方式', u'收货人地址', u'货架编号',
         u'快递状态', u'创建时间']
        sql = "select * from express_info order by id desc"
        with myapi.connection() as con:
            cur = con.cursor()
            rs = myapi.sql_execute(cur, sql)
            while rs.next():
                rs_dic = rs.to_dict()
                ls.append(rs_dic)
        
        filename = "express_{}.xlsx".format(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
        PROJECT_HOME = os.path.dirname(os.path.abspath(__file__))
        DOWNLOAD_DIR = os.path.join(PROJECT_HOME, '..','static', 'download')
        file_path = "{}/{}".format(DOWNLOAD_DIR,filename)
        workbook = xlsxwriter.Workbook(file_path)
        table = workbook.add_worksheet()
        table.write_row('A1', title)
        tmp_line = 2
        for l in ls:
            print '-------%s'%repr(l)
            tmp = [
                l['express_number'],
                u'发送' if l['type']=='1' else u'接收' ,
                classification_dic.get(l['express_classification'],'--'),
                l['express_money'],
                l['express_user_id'],
                l['sender_name'],
                l['sender_phone'],
                l['sender_address'],
                l['reciver_name'],
                l['reciver_phone'],
                l['reciver_address'],
                l['shelf_number'],
                status_dic.get(l['express_status'],'--'),
                l['created_at']
            ]
            table.write_row("A{}".format(tmp_line), tmp)
            tmp_line += 1
        workbook.close()
        # response = HttpResponse()
        # response['Content-Disposition'] = "attachment;filename='{0}'".format(filename)
        # content = open(file_path, 'rb').read()
        # response.write(content)
        # return response

        from django.http import StreamingHttpResponse
        response = StreamingHttpResponse(file_iterator(file_path))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename='{0}'".format(filename)
        return response
    except Exception, e :
        content['xyxx'] = '后台函数[download_view]执行错误:%s' % str( e )
        log.exception( 'kdgl', '后台函数[download_view]执行错误:%s', str( e ) )
        return HttpResponse( json.dumps( content) , content_type='application/json' )