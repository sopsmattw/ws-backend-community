# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .base import from_django_model
import rest.models


DefaultFlag = from_django_model(rest.models.DefaultFlag)
OrganizationFlag = from_django_model(rest.models.OrganizationFlag)
