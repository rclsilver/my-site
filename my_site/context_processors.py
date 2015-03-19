# -*- coding: utf-8 -*-
from django.conf import settings


def google_analytics(context):
    return {'GOOGLE_ANALYTICS': getattr(settings, "GOOGLE_ANALYTICS", False)}

def google_analytics_account(context):
    return {'GOOGLE_ANALYTICS_ACCOUNT': getattr(settings, "GOOGLE_ANALYTICS_ACCOUNT", None)}
