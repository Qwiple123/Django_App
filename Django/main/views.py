from django.shortcuts import  render, redirect,HttpResponse
from .forms import NewUserForm,NewTestForm,NewQuestionForm,NewAnswerForm
from django.contrib.auth import login
from .models import Test,Question,Answer


def index(request):
    if request.user.is_authenticated:
        tests = Test.objects.all()
        return render(request,'main/index.html',{
              'tests':tests
        })
    else:
        return redirect("/accounts/login/")

def test_view(request,id):
    answers = {}
    test = Test.objects.filter(id=id)[0]
    questions = Question.objects.filter(test=test)
    create_question = NewQuestionForm()
    create_answer = NewAnswerForm()
    for i in questions:
        try:
            answers[i.text]=Answer.objects.filter(question=i.id)
        except:
             pass    
        
    return render(request,'main/test_view.html',{
          'test':test,
          'create_question':create_question,
          'create_answer':create_answer,
          'questions':questions,
          'answers':answers
          
    })

def test_create(request):
    
    if request.method == "POST":
        form = NewTestForm(request.POST)
        test = form.save(commit=False)
        test.author = request.user.username
        test.save()
        test = Test.objects.filter(id=test.id)[0]
        return redirect(f"/{test.id}/")
    else:
        form = NewTestForm()

    return render(request,'main/test_create.html',{
         'form':form
    })


def test_question_create(request,id):
      if request.method == "POST":
        form = NewQuestionForm(request.POST)
        test = form.save(commit=False)
        test.test_id = id
        test.save()
        test = Test.objects.filter(id=id)[0]
        return redirect(f"/{test.id}/")
      

def test_answer_create(request,test_id,question_id):
      if request.method == "POST":
        form = NewAnswerForm(request.POST)
        answer = form.save(commit=False)
        answer.question_id = question_id
        answer.save()
        test = Test.objects.filter(id=test_id)[0]
        return redirect(f"/{test.id}/")




def update_test(request,test_id):
    if request.method == 'POST':
        answer_text = ""
        answer_is_correct = ""
        data = request.POST
        Test.objects.filter(id=test_id).update(title=request.POST['title'])
        for i in data:
            i_split = i.split('[')
            if i_split[0] == "questions_data":
                questiont_text=data[i]
                question_id=i_split[1][:-1]
                question = Question.objects.filter(id=question_id).update(text=questiont_text)
            elif i_split[0] == "answers_data":
                answer_split = i.split(' ')
                if answer_split[0] == 'answers_data[id':
                    answer_id = answer_split[1][:-1]
                elif answer_split[0] == 'answers_data[text':
                    answer_text = (data[i])

                    
                        
                elif answer_split[0] == 'answers_data[is_correct':
                        answer_is_correct = (data[i])
                        if answer_is_correct == 'true':
                             answer_is_correct = True
                        elif answer_is_correct == 'false':
                             answer_is_correct = False     
                if  len(answer_text)>=1 and type(answer_is_correct)== bool:
                    answer = Answer.objects.filter(id=answer_id).update(text=answer_text,is_correct=answer_is_correct)
                       
                        
                            
               
                
                     
        return HttpResponse(200)
    


def delete_test(request,test_id):
    Test.objects.filter(id=test_id).update(is_deleted=True)
    return redirect(f"/")


     
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			return redirect("main:homepage")


	form = NewUserForm()
	return render (request=request, template_name="main/reg.html", context={"form":form})