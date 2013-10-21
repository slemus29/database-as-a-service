# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django_services import admin
from ..service.bind import BindService


class BindAdmin(admin.DjangoServicesAdmin):
    service_class = BindService
    list_display = ("created_at", "service_name", "service_hostname", "instance")
    list_filter = ("service_name",)
    save_on_top = True