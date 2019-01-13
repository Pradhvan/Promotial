from django import forms
from .models import Rule


class RuleForm(forms.ModelForm):
    class Meta:
        model = Rule
        fields = ['rule_name', 'campaigns', 'schedule',
                  'condition', 'STATUS', 'ACTION']
