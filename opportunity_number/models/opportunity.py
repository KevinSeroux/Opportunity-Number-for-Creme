# -*- coding: utf-8 -*-
# Inspired from http://www.cremecrm.com/forum/viewtopic.php?f=6&t=563&start=10#p629

from django.db.models import Model, PositiveIntegerField
from creme.opportunities.models.opportunity import Opportunity
from creme.creme_core.utils.contribute_to_model import contribute_to_model
from django.utils.translation import ugettext_lazy as _

class MakinaOpportunity(Model):
    opportunity_number = PositiveIntegerField(_("Opportunity number"), unique=True)

    class Meta:
        abstract = True

contribute_to_model(MakinaOpportunity, Opportunity)
