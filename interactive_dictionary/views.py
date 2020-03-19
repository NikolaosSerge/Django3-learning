from django.shortcuts import render
import difflib
import json
data=json.load(open("interactive_dictionary/data.json"))

def home(request):
    return render(request,'interactive_dictionary/index.html')


def interDic(request):

    keyword=request.GET.get('usr_input').strip()
    if keyword in data.keys():
        key=data[keyword]
        return render(request,'interactive_dictionary/index.html',{'result':key})
    else:
        key=difflib.get_close_matches(keyword,data.keys(),n=10)
        return render(request,'interactive_dictionary/index.html',{'matches':key})
