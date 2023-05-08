# from django.urls import path
# from . import views

# urlpatterns = [
#     path('survey/', views.survey, name='survey'),
#     path('results/', views.results, name='results')
# ]


from .forms import StoreNameForm
from django.urls import path
from .views import QuestionWizard

urlpatterns = [
    path('survey/', QuestionWizard.as_view()),
    path('results/', QuestionWizard.results, name='results'),
]