# -*- coding: utf-8 -*-

"""We should not place fields in code. But this feature (for the form creation)
   is not available yet in the UI module blocks settings"""
def place_opportunity_number_field(form_instance):
    nameFieldIndex = form_instance.fields.keyOrder.index("name")
    opportunityNumberFieldIndex = \
        form_instance.fields.keyOrder.index("opportunity_number")

    form_instance.fields.keyOrder.insert(nameFieldIndex + 1,
                                         form_instance.fields.keyOrder.pop \
                                             (opportunityNumberFieldIndex))
