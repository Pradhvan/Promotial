from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import RuleForm
from .models import Rule
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    rules = Rule.objects.all()
    return render(request, 'home.html', {'rules': rules})


@login_required
def rule_form_view(request):
    form = RuleForm(request.POST or None)
    if form.is_valid():
        rule = form.save()
        return redirect('home', pk=rule.pk)

    context = {
        'form': form
    }

    return render(request, 'rule_form.html', context)


@login_required
def rule_form_edit(request, pk):
    rule = get_object_or_404(Rule, pk=pk)
    form = RuleForm(request.POST or None, instance=rule)
    if request.method == 'POST':
        form = RuleForm(request.POST, instance=rule)
        if form.is_valid():
            rule.save()
            return redirect('home')
    context = {
        'form': form
    }

    return render(request, 'rule_form.html', context)
