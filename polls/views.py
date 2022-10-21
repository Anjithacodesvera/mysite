
from django.shortcuts import render,redirect
from django.template import loader
from django.urls import reverse
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views import generic, View
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Question,Choice
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.db import models
from .models import ques


# class LoginView(LoginView):
#     template_name = 'LoginView.html
# Create your views here.
@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    # key = ques.objects.all().order_by('-updated')
    # context = {'key': key}
    #
    # return render(request,'polls/index.html',context)


    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        # key = ques.objects.all()
        # return Question.objects.filter(
        #     pub_date__lte=timezone.now()
        #  ).order_by('-pub_date')[:5]
        return ques.objects.all()

    # def get(self,request):
    #     key = ques.objects.all().order_by('-updated')
    #     context = {'key': key}
    #
    #     return render(request, 'polls/index.html', context)






class DetailView(generic.DetailView):
    ...
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class Hello(View):

    def get(self,request):

        return render(request,'polls/hello.html')

    def post(self,request):


        quest=request.POST.get('quest')
        ques(quest=quest).save()
        print("********")
        # return HttpResponseRedirect("/")
        # return render(request,'polls/hello.html')

        return redirect('/polls/')

    # def edit(request, id):
    #     context = ques.objects.get(id=id)
    #
    #     return render(request, 'edit.html', {'context': context})

class APPUpdateView(View):
    # model =ques
    # fields = [
    #    "quest"
    # ]
    def get(self,request,id):
        a = ques.objects.get(id=id)
        return render(request,'polls/edit.html',{'a':a})
    def post(self,request,id):
        a = ques.objects.get(id=id)
        a.quest = request.POST.get('quest')
        a.save()
        return redirect('/polls/')

def delete(request,id):
   b= ques.objects.get(id=id)
   b.delete()
   return redirect('/polls/')








