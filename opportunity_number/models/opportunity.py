# -*- coding: utf-8 -*-

# Inspired from
# http://www.cremecrm.com/forum/viewtopic.php?f=6&t=563&start=10#p629

from django.db.models.signals import pre_save
from django.db.models import Model, PositiveIntegerField
from django.utils.translation import ugettext_lazy as _
from creme.creme_core.utils.contribute_to_model import contribute_to_model, \
                                                       delete_model_fields
from creme.opportunities.models.opportunity import Opportunity


class NumberedOpportunity(Model):
    # If you want to process to a datas migration set unique=True while you're
    # setting opportunity numbers
    # Although this field is required we allow blank values, in this case the
    # opportunity number will be computed while saving
    opportunity_number = PositiveIntegerField(_("Opportunity number"),
                                              unique=True, blank=True)

    class Meta:
        abstract = True

contribute_to_model(NumberedOpportunity, Opportunity)

#Opportunity number replace the existing reference field
delete_model_fields(Opportunity, "reference")


"""To retrieve the last opportunity number in the db"""
def slot_pre_save(sender, instance, **kwargs):
    if not instance.opportunity_number:
        try:
            lastOpportunityItem = Opportunity.objects.latest \
                                      ("opportunity_number")
            newOpportunityNumber = lastOpportunityItem.opportunity_number + 1

        except Opportunity.DoesNotExist: # If table is empty
            newOpportunityNumber = 0
   
        instance.opportunity_number = newOpportunityNumber

pre_save.connect(slot_pre_save, sender=Opportunity)
