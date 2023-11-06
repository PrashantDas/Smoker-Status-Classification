from django.shortcuts import render
from .forms import MyForm
import numpy as np
import pickle
pickled_model = pickle.load(open('Model_LR_Smoker2023.pkl', 'rb'))

def face(request):
    if request.method == 'POST':
        form_instance = MyForm(request.POST)
        if form_instance.is_valid():
            age          = form_instance.cleaned_data.get('age')
            height       = form_instance.cleaned_data.get('height')
            weight       = form_instance.cleaned_data.get('weight')
            waist        = form_instance.cleaned_data.get('waist')
            triglyceride = form_instance.cleaned_data.get('triglyceride')
            hdl          = form_instance.cleaned_data.get('hdl')
            ldl          = form_instance.cleaned_data.get('ldl')
            haemoglobin  = form_instance.cleaned_data.get('haemoglobin')
            alt          = form_instance.cleaned_data.get('alt')
            gtp          = form_instance.cleaned_data.get('gtp')
            data ={'age': age, 'height': height, 'weight': weight, 'waist': waist, 'triglyceride':triglyceride,
                   'hdl':hdl, 'ldl':ldl, 'haemoglobin':haemoglobin, 'alt':alt, 'gtp':gtp}
            data_list = list(data.values())
            input_array = np.array(data_list).reshape(1, -1)
            prediction = pickled_model.predict(input_array)
            prediction = 'smoker' if prediction[0] else 'non-smoker'
            prediction = 'The algorithm has assessed that the individual has the measurement units of a ' + prediction
            return render(request, 'frontapp/main.html', {'that_form': MyForm(), 'prediction': prediction})
        else:
            return render(request, 'frontapp/main.html', {'that_form': MyForm()})
        
    else:
        return render(request, 'frontapp/main.html', {'that_form': MyForm()})

    
def contact(request):
    return render(request, 'frontapp/contact.html', {})


def methodology(request):
    return render(request, 'frontapp/methodology.html', {})