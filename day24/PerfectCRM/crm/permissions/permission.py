#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Breakering"
# Date: 2017/12/21
import re
import logging
from django.urls import resolve
from django.shortcuts import redirect, HttpResponse, render
from crm.permissions import permission_dict
from crm.permissions.permission_dict import PermissionDict

logger = logging.getLogger("__name__")  # 生成一个以当前模块名为名字的logger实例


def check_user_permission(request, *args, **kwargs):
    """验证用户是否有权限"""
    ret = {"status": False, "errors": [], "data": {}}  # 要返回的内容
    for permission_name, permission_detail in PermissionDict.items():
        url_matched = False  # url是否匹配上
        if permission_detail["url_type"] == 0:  # 相对路径
            resolve_obj = resolve(request.path)  # 生成url resolve对象
            url_name = resolve_obj.url_name  # 获取请求的相对路径，及URL别名
            if permission_detail["url"] == url_name:
                url_matched = True
        elif permission_detail["url_type"] == 1:  # 绝对路径
            if permission_detail["url"] == request.path:
                url_matched = True
        elif permission_detail["url_type"] == 2:  # 模糊路径
            if re.match(permission_detail["url"], request.path):
                url_matched = True

        if url_matched:  # url匹配上了继续往下走
            if permission_detail["method"] == request.method:  # 请求方式匹配上了
                args_matched = True  # 参数是否匹配上
                for arg in permission_detail["args"]:
                    # 如果定义的参数在用户请求的参数中获取不到,则表明用户不符合该条权限定义
                    if not getattr(request, permission_detail["method"]).get(arg):
                        args_matched = False
                        break  # 跳出参数循环，因为已经有一个参数不满足条件了，则不需要再验证其他参数

                if args_matched:  # 参数匹配上了才继续往下走
                    hooks_aproved = True  # 钩子是否通过验证
                    if permission_detail["hooks"]:  # 用户有添加钩子才会进行钩子验证，否则直接通过
                        judgment_str = ""
                        for hook_name in permission_detail["hooks"]:
                            if hook_name in ["or", "and"]:
                                judgment_str += "%s " % hook_name
                            else:
                                if hasattr(permission_dict, hook_name):  # 执行用户自定义钩子
                                    hook_fun = getattr(permission_dict, hook_name)
                                    hook_fun_ret = hook_fun(request, *args, **kwargs)
                                    if hook_fun_ret.get("errors"):  # 钩子执行有错误返回时需要添加至错误列表
                                        ret["errors"].extend(hook_fun_ret["errors"])
                                    if hook_fun_ret.get("data"):  # 钩子执行返回的数据需要添加至数据字典中
                                        ret["data"].update(hook_fun_ret.get("data"))
                                    judgment_str += "%s " % hook_fun_ret.get("status")
                        judgment_str = "all([%s])" % judgment_str
                        hooks_aproved = eval(judgment_str)

                    if hooks_aproved:  # 通过了用户自定义的钩子验证
                        if request.user.has_perm(permission_name):  # 用户如果有该条权限，则通过权限认证系统
                            ret["status"] = True
                            break  # 权限匹配上了直接跳出循环
    if not ret["status"]:  # 用户没通过权限验证
        ret["errors"].insert(0, "对不起，您没权限执行此功能，请联系管理员开通！")

    return ret


def check_permission_decorate(func):
    """检查用户是否有权限的装饰器"""

    def inner(request, *args, **kwargs):
        if request.user.is_authenticated():  # 首先判断用户是否登录
            ret = check_user_permission(request, *args, **kwargs)
            if ret["status"]:  # 权限认证通过
                response = func(request, *args, **kwargs)
            else:  # 权限认证不通过
                logger.warning("用户:%s正在尝试访问无权限接口%s" % (request.user.email, request.path))
                response = render(request, "pages-403.html", {"errors": ret["errors"]})
                if ret["data"]:  # 对返回的数据进行处理
                    should_redirect = ret["data"].get("should_redirect")  # 如果有跳转需要则进行跳转操作
                    if should_redirect:
                        response = redirect(should_redirect)
        else:  # 没登录跳转至登录页
            response = redirect("/accounts/login/")
        return response

    return inner
