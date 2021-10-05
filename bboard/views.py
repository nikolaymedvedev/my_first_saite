from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Bb
from .models import Rubrik
from .forms import BbForm

def index(request) :
	bbs = Bb.objects.all()
	rubriks = Rubrik.objects.all()
	context = {'bbs': bbs, "rubriks":rubriks}
	return render(request, 'bboard/index.html', context)

def by_rubrik(request, rubrik_id):
	bbs = Bb.objects.filter(rubrik=rubrik_id)
	rubriks = Rubrik.objects.all()
	current_rubrik = Rubrik.objects.get(pk=rubrik_id)
	context = {"bbs":bbs, "rubriks":rubriks, "current_rubrik":current_rubrik}
	return render(request, "bboard/by_rubrik.html", context)

class BbCreateView(CreateView):
	template_name = 'bboard/create.html'
	form_class = BbForm
	success_url = reverse_lazy("add")

	def get_context_data(self, **kargs):
		context = super().get_context_data(**kargs)
		context["rubriks"] = Rubrik.objects.all()
		return context
