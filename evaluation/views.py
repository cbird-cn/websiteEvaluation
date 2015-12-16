# Create your views here.
from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse
from evaluation.models import case
from django.template.loader import get_template

def caseShow(request):
	caseShow=case.objects.get(caseName="youku")#(id=1)
	caseName=caseShow.caseName
	attribute=caseShow.attribute
	return render_to_response('D:\Django\practice\websiteEvaluation\\templates\index.html',{'caseName':caseName,'attribute':attribute})