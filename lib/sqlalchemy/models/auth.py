# -*- coding: utf-8 -*-
from __future__ import absolute_import

import rest.models
from .base import from_django_model


WsAuthGroup = from_django_model(rest.models.WsAuthGroup)
