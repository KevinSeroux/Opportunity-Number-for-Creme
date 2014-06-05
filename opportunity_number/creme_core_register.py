# -*- coding: utf-8 -*-

from django.db.models.signals import pre_save
from creme.opportunities.forms.opportunity import OpportunityCreateForm, \
                                                  OpportunityEditForm
from creme.opportunities.models.opportunity import Opportunity
from creme.opportunity_number.forms.opportunity import place_opportunity_number_field
from creme.opportunity_number.models.opportunity import slot_pre_save

pre_save.connect(slot_pre_save, sender=Opportunity)

OpportunityCreateForm.add_post_init_callback(place_opportunity_number_field)
OpportunityEditForm.add_post_init_callback(place_opportunity_number_field)
