# coding: utf8
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
import os, json, datetime
from zjyw_utils import *

log.init_log( 'kd_info' , True )

def kd_info_view(request):
    try:
        content={}
        ls=[]
        content['xym'] = '0'
        if not request.session.get('username',''):
            return HttpResponseRedirect('/')
        username = request.session.get('username','').encode('utf8')
        password = request.session.get('password','').encode('utf8')
        log.info( "kd_info", '用户【%s】已进入kd_info_view函数', username)
        sql = "select * from express_info order by id desc"
        with myapi.connection() as con:
            cur = con.cursor()
            rs = myapi.sql_execute(cur, sql)
            while rs.next():
                rs_lst = rs.to_dict()
                ls.append(rs_lst)
        if ls:
            log.info( "kd_info",  repr(ls))
            content['xym'] = '000000'
            content['cont'] = render_to_string( 'kdxx_idx.html', {'kd_info':ls} )
            return HttpResponse( json.dumps( content), content_type='application/json' )
        else:
            # 返回错误信息
            log.info( "kd_info", '快递信息不存在')
            content['xyxx'] = '主机信息不存在！'
            return HttpResponse( json.dumps( content) , content_type='application/json' )
    except Exception, e :
        content['xyxx'] = '后台函数[kd_info_view]执行错误:%s' % str( e )
        log.exception( 'kd_info', '后台函数[kd_info_view]执行错误:%s', str( e ) )
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
           
        log.info( "kd_info", "快递信息删除sql【%s】", sql )
        if cur.rowcount == 1:
            log.info( "kd_info", "主机删除成功！" )
            content['xym'] = '000000'
            content['xyxx'] = '主机删除成功！'
            return HttpResponse( json.dumps( content), content_type='application/json' )
        else:
            # 返回错误信息
            log.info( "kd_info", '快递信息删除失败')
            content['xyxx'] = '快递信息删除失败！'
            return HttpResponse( json.dumps( content) , content_type='application/json' )
    except Exception, e :
        content['xyxx'] = '后台函数[kdxx_del_view]执行错误:%s' % str( e )
        log.exception( 'kd_info', '后台函数[kdxx_del_view]执行错误:%s', str( e ) )
        return HttpResponse( json.dumps( content) , content_type='application/json' )

# 更新快递信息页面跳转     
def update_kdxx_view(request):
    try:
        content={}
        content['xym'] = '0'
        id = request.POST.get('id','')
        if not request.session.get('username',''):
            return HttpResponseRedirect('/')
        sql = "select * from express_info where id='%s' " % id
        log.info( "update_kdxx",  sql)
        with myapi.connection() as con:
            cur = con.cursor()
            rs = myapi.sql_execute(cur, sql)
            while rs.next():
                rs_lst = rs.to_dict()
                log.info( "kd_info",  repr(rs_lst))
        if rs_lst:
            
            content['xym'] = '000000'
            content['cont'] = render_to_string( 'kdxx_edit.html', {'express_classification': rs_lst['express_classification'], 'express_user_id': rs_lst['express_user_id'], 'sender_name': rs_lst['sender_name'], 'express_money':rs_lst['express_money'], 'express_number': rs_lst['express_number'], 'express_status': rs_lst['express_status'], 'sender_address': rs_lst['sender_address'], 'reciver_name': rs_lst['reciver_name'], 'id': rs_lst['id'], 'sender_phone': rs_lst['sender_phone'], 'reciver_address': rs_lst['reciver_address'], 'shelf_number': rs_lst['shelf_number'], 'reciver_phone': rs_lst['reciver_phone'], 'type': rs_lst['type'], 'created_at': rs_lst['created_at'] } )
            return HttpResponse( json.dumps( content), content_type='application/json' )
        else:
            # 返回错误信息
            log.info( "kd_info", '快递信息不存在')
            content['xyxx'] = '快递信息不存在！'
            return HttpResponse( json.dumps( content) , content_type='application/json' )
    except Exception, e :
        log.exception( 'update_kdxx', '后台函数[update_kdxx_view]执行错误:%s', str( e ) )
        return render_to_response( 'kdxx_edit.html', {'xyxx':'后台函数[update_kdxx_view]执行错误:%s' % str( e )}, context_instance=RequestContext(request) )

# 编辑快递信息
def kd_edit_view(request):
    try:
        content={}
        ls=[]
        content['xym'] = '0'
        if not request.session.get('username',''):
            return HttpResponseRedirect('/')
        # {express_classification,  express_user_id,  sender_name, express_money,  express_number,  express_status, sender_address, reciver_name,  id,  sender_phone, reciver_address, shelf_number,  reciver_phone,  type, created_at }
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
        shelf_number = request.session.get('shelf_number','').encode('utf8')
        type = request.session.get('type','').encode('utf8')
        created_at = request.session.get('created_at','').encode('utf8')
        # 修改快递信息
        sql = "update express_info set express_classification='%s', express_user_id='%s', sender_name='%s', express_money='%s', express_number='%s', express_status='%s', sender_address='%s', reciver_name='%s', sender_phone='%s', reciver_address='%s', shelf_number='%s', reciver_phone='%s', type='%s', created_at='%s' where id='%s' " % (express_classification,  express_user_id,  sender_name, express_money,  express_number,  express_status, sender_address, reciver_name, sender_phone, reciver_address, shelf_number,  reciver_phone,  type, created_at, id )
        with myapi.connection() as con:
            cur = con.cursor()
            cur.execute(sql)
           
        log.info( "update_kdxx", "修改快递信息sql【%s】", sql )
        if cur.rowcount == 1:
            log.info( "update_kdxx", "修改快递信息成功！" )
            content['xym'] = '000000'
            content['xyxx'] = '修改快递信息成功！'
            return HttpResponse( json.dumps( content), content_type='application/json' )
        else:
            # 返回错误信息
            log.info( "update_kdxx", '修改快递信息失败')
            content['xyxx'] = '修改快递信息失败！'
            return HttpResponse( json.dumps( content) , content_type='application/json' )
    except Exception, e :
        content['xyxx'] = '后台函数[kd_edit_view]执行错误:%s' % str( e )
        log.exception( 'update_kdxx', '后台函数[kd_edit_view]执行错误:%s', str( e ) )
        return HttpResponse( json.dumps( content) , content_type='application/json' )

# 主机分组
def zjfz_view(request):
    try:
        content={}
        ls = []
        ls_agent = []
        content['xym'] = '0'
        if not request.session.get('username',''):
            return HttpResponseRedirect('/')
            
        # 查询所有主机组信息
        sql = "select * from AgentGroupInfo "
        # 查询所有主机ID
        agent_sql = "select agent_id, agent_name from AgentInfo "
        with myapi.connection() as con:
            cur = con.cursor()
            rs = myapi.sql_execute(cur, sql)
            while rs.next():
                rs_lst = rs.to_dict()
                ls.append(rs_lst)
            
            agent_rs = myapi.sql_execute(cur, agent_sql)
            while agent_rs.next():
                agent_lst = agent_rs.to_dict()
                ls_agent.append(agent_lst)
        if ls or ls_agent:
            log.info( "zjxx", "获取到的主机组信息：【%s】", repr(ls) or '' )
            log.info( "zjxx", "获取到的主机ID：【%s】", repr(ls_agent) or '' )
            dic_group = {}
            ls_group = []   #[{主机组ID1:[主机ID1,主机ID2,....]},{主机组ID2:[主机ID3,主机ID4,....]}]
            #ls_group_id = [] #[]
            for group in ls:
                group["group_agent"] = group["group_agent"]
                ls_group.append(group)
                #ls_group_id.append(group["group_id"])
            content['xym'] = '000000'
            content['cont'] = render_to_string( 'zjfz.html', {'ls_group':ls_group, 'ls_agent':ls_agent} )
            return HttpResponse( json.dumps( content), content_type='application/json' )
        else:
            # 返回错误信息
            log.info( "zjxx", '主机信息不存在')
            content['xyxx'] = '主机信息不存在！'
            return HttpResponse( json.dumps( content) , content_type='application/json' )
    except Exception, e :
        content['xyxx'] = '后台函数[zjfz_view]执行错误:%s' % str( e )
        log.exception( 'zjxx', '后台函数[zjfz_view]执行错误:%s', str( e ) )
        return HttpResponse( json.dumps( content) , content_type='application/json' )


        
# 主机id生成
def zjid_view(request):
    try:
        content={}
        content['xym'] = '0'
        if not request.session.get('username',''):
            return HttpResponseRedirect('/')
        log.info( "zjxx", "自动生成的主机ID的页面跳转")
        content['xym'] = '000000'
        content['cont'] = render_to_string( 'zjid.html', {} )
        return HttpResponse( json.dumps( content), content_type='application/json' )
    except Exception, e :
        content['xyxx'] = '后台函数[zjid_view]执行错误:%s' % str( e )
        log.exception( 'zjxx', '后台函数[zjid_view]执行错误:%s', str( e ) )
        return HttpResponse( json.dumps( content) , content_type='application/json' )
        
# 主机id生成
def zjid_made_view(request):
    try:
        content={}
        content['xym'] = '0'
        if not request.session.get('username',''):
            return HttpResponseRedirect('/')
        # 主机组是固定的20个组，页面上可以操作的仅仅是主机
        # 查询所有主机序列，获取自动生成的主机ID
        sql = "select nextval('agent_id') as agent_id "
        sql_mm = "select nextval('agent_mm') as agent_mm "
        with myapi.connection() as con:
            cur = con.cursor()
            rs = myapi.sql_execute(cur, sql)
            while rs.next():
                rs_dic = rs.to_dict()
            rs_mm = myapi.sql_execute(cur, sql_mm)
            while rs_mm.next():
                rs_mm_dic = rs_mm.to_dict()
        if rs_dic and rs_mm_dic:
            log.info( "zjxx", "自动生成的主机ID：【%s】", repr(rs_dic) or '' )
            content['agent_id'] = rs_dic['agent_id']
            content['agent_mm'] = rs_mm_dic['agent_mm']
            with myapi.connection() as con:
                cur = con.cursor()
                # 获取主机信息更新：agent_name, agent_system, agent_ip, agent_mac
                # 主机分组更新：agent_group, 
                # 任务定制更新：agent_task, 
                # 主机基本信息插入：agent_id, agent_code, agent_state, agent_user, agent_date_joined, agent_joiner
                sql = "insert into AgentInfo( agent_id, agent_code, agent_state, agent_user, agent_date_joined, agent_joiner ) values( '%s', '%s', '00', '%s', '%s', '%s' )"%( content['agent_id'], content['agent_mm'], request.session.get('username'), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), request.session.get('username') )
                log.info( "zjxx", "插入主机基本信息的sql：【%s】", sql )
                cur.execute(sql)
            content['xym'] = '000000'
            return HttpResponse( json.dumps( content), content_type='application/json' )
        else:
            # 返回错误信息
            log.info( "zjxx", '主机信息不存在')
            content['xyxx'] = '主机信息不存在！'
            return HttpResponse( json.dumps( content) , content_type='application/json' )
    except Exception, e :
        content['xyxx'] = '后台函数[zjid_view]执行错误:%s' % str( e )
        log.exception( 'zjxx', '后台函数[zjid_view]执行错误:%s', str( e ) )
        return HttpResponse( json.dumps( content) , content_type='application/json' )
