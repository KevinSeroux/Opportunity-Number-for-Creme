# -*- coding: utf-8 -*-
# Inspired from http://www.cremecrm.com/forum/viewtopic.php?f=6&t=563&start=10#p629

from django.db.models import Model, PositiveIntegerField
from django.utils.translation import ugettext_lazy as _
from creme.creme_core.utils.contribute_to_model import contribute_to_model
from creme.opportunities.models.opportunity import Opportunity

class CustomOpportunity(Model):
    #If you want to process to a datas migration set unique=True while you're setting opportunity numbers
    opportunity_number = PositiveIntegerField(_("Opportunity number"), unique=True)

    class Meta:
        abstract = True

contribute_to_model(CustomOpportunity, Opportunity)
