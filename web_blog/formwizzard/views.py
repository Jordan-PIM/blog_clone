from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models
from .forms import FormStepOne, FormStepTwo, FormStepThree
from formtools.wizard.views import SessionWizardView

# Create your views here.
class FormWizardView(SessionWizardView):
    template_name = "formwizzard/mpform.html"
    form_list = [FormStepOne, FormStepTwo, FormStepThree]

    def done(self, form_list, **kwargs):
        return render(self.request, 'formwizzard/formfilled.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })

    def get(self, request, *args, **kwargs):
        try:
            return self.render(self.get_form())
        except KeyError:
            return super().get(request, *args, **kwargs)
