from django import forms


class FormStepOne(forms.Form):
    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone = forms. CharField(max_length=100, required=False)
    email = forms.EmailField()


class FormStepTwo(forms.Form):
    job = forms.CharField(max_length=100, required=False)
    salary = forms.CharField(max_length=100, required=False)
    job_description = forms.CharField(widget=forms.Textarea, required=False)


class FormStepThree(forms.Form):
    dob = forms.DateField(input_formats=('%d/%m/%Y',), required=False)

