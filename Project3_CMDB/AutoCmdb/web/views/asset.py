#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from web.service import asset
from django.utils.decorators import method_decorator
from utils.my_decorator import login_decorator


class AssetListView(View):
    @method_decorator(login_decorator)
    def get(self, request, *args, **kwargs):
        return render(request, 'asset_list.html')


class AssetJsonView(View):

    def __init__(self, **kwargs):
        self.obj = asset.Asset()
        super(AssetJsonView, self).__init__(**kwargs)

    @method_decorator(login_decorator)
    def get(self, request):
        response = self.obj.fetch_queryset(request)
        return JsonResponse(response.__dict__)

    @method_decorator(login_decorator)
    def delete(self, request):
        response = self.obj.delete_queryset(request)
        return JsonResponse(response.__dict__)

    @method_decorator(login_decorator)
    def put(self, request):
        response = self.obj.put_queryset(request)
        return JsonResponse(response.__dict__)

    @method_decorator(login_decorator)
    def post(self, request):
        response = self.obj.post_queryset(request)
        return JsonResponse(response.__dict__)


class AssetDetailView(View):
    @method_decorator(login_decorator)
    def get(self, request, device_type_id, asset_nid):
        response = asset.Asset.assets_detail(device_type_id, asset_nid)
        return render(request, 'asset_detail.html', {'response': response, 'device_type_id': device_type_id})


class AddAssetView(View):
    @method_decorator(login_decorator)
    def get(self, request, *args, **kwargs):
        service_obj = asset.Asset()
        model_form_class = service_obj.create_model_form()
        model_form_obj = model_form_class()
        return render(request, 'add_asset.html', {
            "model_form_obj": model_form_obj,
            "service_obj": service_obj
        })


class AddServerView(View):
    @method_decorator(login_decorator)
    def get(self, request, *args, **kwargs):
        service_obj = asset.Asset()
        model_form_class = service_obj.create_model_form()
        model_form_obj = model_form_class()
        return render(request, 'add_asset.html', {
            "model_form_obj": model_form_obj,
            "service_obj": service_obj
        })
