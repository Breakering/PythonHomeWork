#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Breakering"
# Date: 2017/5/20
"""用户类模块"""
import os
from core.base import BaseClass
from lib.public import create_id
from conf import settings


class User(BaseClass):
    """用户类"""
    def __init__(self):
        self.id = create_id()
        self.username = None
        self.password = None

    def __str__(self):
        return self.username

    def create_directory(self):
        """创建用户目录"""
        home_dir = settings.USER_DIRECTORY_DIR
        user_directory_path = os.path.join(home_dir, self.username)
        if os.path.isdir(user_directory_path):
            return
        os.mkdir(user_directory_path)
        return "done"
