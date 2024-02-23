from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.views.generic import FormView,CreateView,TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.urls import reverse_lazy



class LoginView(FormView):
    template_name="login.html"
    form_class=LogForm
    def post(self,request,*args,**kwargs):
        log_form=LogForm(data=request.POST)
        if log_form.is_valid():  
            us=log_form.cleaned_data.get('username')
            ps=log_form.cleaned_data.get('password')
            user=authenticate(request,username=us,password=ps)
            if user: 
                login(request,user)
                return redirect('h')
            else:
                return render(request,'login.html',{"form":log_form})
        else:
            return render(request,'login.html',{"form":log_form}) 
        

class RegView(CreateView):
     form_class=Reg
     template_name="reg.html"
     model=User
     success_url=reverse_lazy("log")    



from django.shortcuts import render
from better_profanity import profanity
import re

def Home(request):
    if request.method == 'POST':
        user_input = request.POST.get('text', '').lower()
        x = profanity.censor(user_input)
        x_list = x.split()
        pattern = r"[****]"
        def has_special_characters(text):
            return bool(re.search(pattern, text))
        c=0
        for item in x_list:
            if has_special_characters(item):
                
                c=c+1
        if c!=0:
            result = "offensive" 
        else :
            result = "not offensive"
        
        mild = ['bitch', 'bloody', 'bugger', 'chav', 'cow', 'crap', 'damn', 'douchebag', 'effing', 'feck', 'ginger', 'git', 'minger', 'pissed', 'pissed off', 'sod off',
                'uppity', 'arse', 'balls', 'bawbag', 'choad', 'bang', 'bonk', 'frigging', 'ho', 'tart']

        moderate = ['bastard', 'bellend', 'bloodclaat', 'bumberclat', 'dickhead', 'shit', 'shite', 'son of a bitch', 'twat', 'arsehole', 'beaver', 'bollocks', 'idiot',
                    'lunge', 'cock', 'dick', 'fanny', 'knob', 'minge', 'prick', 'pussy', 'snatch', 'tits', 'jizz', 'milf', 'shag', 'skank', 'slag', 'slapper', 'spunk', 'tosser', 'wanker', 'whore']

        strong = ['fuck', 'motherfucker', 'cunt', 'gash', 'japs eye', 'punani', 'pussy hole', 'cocksucker', 'cum', 'nonce', 'prickteaser', 'raped', 'slut']

        profanity_words = mild + moderate + strong

        pattern = fr'\b({"|".join(map(re.escape, profanity_words))})\b'

        censored_words = re.findall(pattern, user_input, flags=re.IGNORECASE)

        categorized_words = {}
        for word in censored_words:
            if word in strong:
                categorized_words[word] = "High Offensive"
            elif word in moderate:
                categorized_words[word] = "Moderate"
            elif word in mild:
                categorized_words[word] = "Mild"
            else :
                categorized_words = "No Offensive"

        context = {
            'user_input': user_input,
            'result':result,
            'censored':censored_words,
            'categorized_words': categorized_words,
        }
        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html')

