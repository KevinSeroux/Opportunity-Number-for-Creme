# -*- coding: utf-8 -*-

from creme.opportunities.forms.opportunity import OpportunityCreateForm, \
                                                  OpportunityEditForm
from creme.opportunity_number.forms.opportunity import place_opportunity_number_field

OpportunityCreateForm.add_post_init_callback(place_opportunity_number_field)
OpportunityEditForm.add_post_init_callback(place_opportunity_number_field)
