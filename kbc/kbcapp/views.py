from django.shortcuts import render, HttpResponse
import json
import requests

# Create your views here.


def home(request):
    return HttpResponse('Hello My Dear...')


def quiz(request):
    rewards = [{"reward":1000,"class":"highlight"},{"reward": 2000,"class":""},{"reward": 3000,"class":""},{"reward": 5000,"class":""},
               {"reward": 10000,"class":""},{"reward": 20000,"class":""},{"reward": 40000,"class":""},{"reward": 80000,"class":""},
                {"reward": 160000,"class":""},{"reward": 320000,"class":""},{"reward": 1250000,"class":""},{"reward": 2500000,"class":""},
                 {"reward": 5000000,"class":""},{"reward": 10000000,"class":""},{"reward": 70000000,"class":""}, ]

    qno = 0
    result = ''
    status = ''
    selected_option = ''
    if request.POST:
        qno = int(request.POST['qno'])
        selected_option = int(request.POST['selected_option'])
        ans = int(request.POST['ans'])
        print("Answers ", selected_option, ",", ans)
        if ans == selected_option:
            print("Correct")
        else:
            return render(request, "end.html")
            print("Wrong")
        n=len(rewards)
        print(n)
        
        for i in range(n):
            print(i)
            
    url = "https://gist.githubusercontent.com/AzadIdrisi88/5ee4683ecf3cbdc2cc63e2ea41448021/raw/26f28474e05a3dd2d1ef94a1fce5a7ba22462534/kbc_quiz"
    response = requests.get(url)
    code = response.status_code

    if code != 200:
        status = "error"
        print("error")
    else:
        status = "success"
        result = json.loads(response.text)
        result = result["questions"]
        result = result[qno]
        quest = result['qno']
        question = result["question"]
        # option=result['options']
        a = result['options'][0]
        b = result['options'][1]
        c = result['options'][2]
        d = result['options'][3]
        ans = result['correct_option']

        # user_answers.append({"question": question, "is_correct": is_correct})
        # print(option,a,b,c,d,sep=',')
        # print(result[qno])
        # print(question)
        # print(quest)
        # print(result.keys())
        # return render(request,"quiz.html",{"qno":qno+1,"result":result,"status":status})

    return render(request, "quiz.html", {"rewards": rewards[::-1], "qno": qno+1, "result": result, "status": status, 'quest': quest,
                                         "question": question, 'a': a, 'b': b, 'c': c, 'd': d, "ans": ans})
