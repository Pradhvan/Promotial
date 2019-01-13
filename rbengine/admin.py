from django.contrib import admin
from .models import Campaign, Rule, VariableMetric

admin.site.register(Campaign)
admin.site.register(Rule)
admin.site.register(VariableMetric)
