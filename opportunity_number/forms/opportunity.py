# -*- coding: utf-8 -*-
from creme.opportunities.models.opportunity import Opportunity

"""This function allows the opportunity number field to take the place of the reference field
when you create or edit an opportunity"""
def place_opportunity_number_field(fields):

    referenceFieldIndex = fields.keyOrder.index("reference")
    opportunityNumberFieldIndex = fields.keyOrder.index("opportunity_number")

    fields.keyOrder.insert(referenceFieldIndex, fields.keyOrder.pop(opportunityNumberFieldIndex))
    # We don't need to display the reference field, we already have the opportunity_number
    del fields["reference"]
    

def add_opportunity_init(form_instance):
    place_opportunity_number_field(form_instance.fields)

    # To retrieve the last opportunity number in the db
    try:
        lastOpportunityItem = Opportunity.objects.latest("opportunity_number")
        newOpportunityNumber = lastOpportunityItem.opportunity_number + 1

    except Opportunity.DoesNotExist: # If table is empty
        newOpportunityNumber = 0

    form_instance.fields["opportunity_number"].initial = newOpportunityNumber


def edit_opportunity_init(form_instance):
    place_opportunity_number_field(form_instance.fields)
