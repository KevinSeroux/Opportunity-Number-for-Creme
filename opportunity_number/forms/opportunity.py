# -*- coding: utf-8 -*-
from creme.opportunities.models.opportunity import Opportunity

def add_opportunity_init(form_instance):

    # We don't need to display the reference field, we already have the opportunity_number
    del form_instance.fields["reference"]

    # To retrieve the last opportunity number in the db
    try:
        lastOpportunityItem = Opportunity.objects.latest("opportunity_number")
        newOpportunityNumber = lastOpportunityItem.opportunity_number + 1

    except Opportunity.DoesNotExist: # If table is empty
        newOpportunityNumber = 0

    form_instance.fields["opportunity_number"].initial = newOpportunityNumber


def edit_opportunity_init(form_instance):

    # We don't need to display the reference field, we already have the opportunity_number
    del form_instance.fields["reference"]
