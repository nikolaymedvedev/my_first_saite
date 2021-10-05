from django.urls import path
from .views import index
from .views import by_rubrik
from .views import BbCreateView

urlpatterns = [
		path('', index, name='index'),
		path('<int:rubrik_id>/', by_rubrik, name='by_rubrik'),
		path('add/', BbCreateView.as_view(), name='add'),
			]