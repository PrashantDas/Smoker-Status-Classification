from django import forms


class MyForm(forms.Form):
    age      = forms.IntegerField()
    height   = forms.FloatField(min_value=100, step_size=0.5, label='Height (cm)')
    weight   = forms.IntegerField(min_value=20, label='Weight (kg)')
    waist   = forms.IntegerField(min_value=60, step_size=1, label='Waist (cm)')
    triglyceride     = forms.IntegerField(min_value=10, max_value=500, label='Triglyceride, generally around 150 milligrams per deciliter (mg/dL)')
    hdl     = forms.IntegerField(min_value=25, max_value=150, label ='High density lipoprotein, generally around 35 to 80 milligrams per deciliter (mg/dL)')
    ldl     = forms.IntegerField(min_value=20, max_value=1700, label ='Low density lipoprotein, generally around 120 milligrams per deciliter (mg/dL)')
    haemoglobin     = forms.FloatField(min_value=6, max_value=20, step_size=0.1, label='Haemoglobin, generally around 13.8 to 17.2 grams per deciliter (g/dL)')
    alt     = forms.IntegerField(min_value=3, max_value=3000, label ='Alanine Trans-aminase, generally around 4 to 36 U/L')
    gtp     = forms.IntegerField(min_value=1, max_value=650, label ='Gamma-glutamyl, generally around 7 to 50 U/L')