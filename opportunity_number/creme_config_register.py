# -*- coding: utf-8 -*-

from creme.opportunities.forms.opportunity import OpportunityCreateForm, OpportunityEditForm
from creme.makina.forms.opportunity import add_opportunity_init, edit_opportunity_init

OpportunityCreateForm.add_post_init_callback(add_opportunity_init)
OpportunityEditForm.add_post_init_callback(edit_opportunity_init)
