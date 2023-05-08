from django.shortcuts import render
from django.urls import reverse_lazy
from formtools.wizard.views import SessionWizardView
from .forms import StoreNameForm, BalanceForm, PriceForm, NetworkForm, AddressForm, EmailForm
from .models import Survey

class QuestionWizard(SessionWizardView):
    template_name = 'survey.html'
    form_list = [StoreNameForm,BalanceForm,PriceForm,NetworkForm,AddressForm,EmailForm]
    success_url = reverse_lazy('done')

    
    def process_step(self, form):
        print('Current Step:', self.steps.current)
        if self.steps.current == '0':
            # Save survey object on first step
            self.survey = form.save(commit=False)
            self.storage.extra_data['survey'] = self.survey.pk
        else:
            # Get survey object from previous step and associate question object with it
            survey_pk = self.storage.extra_data.get('survey')
            if survey_pk:
                self.survey = Survey.objects.get(pk=survey_pk)
                question = form.save(commit=False)
                question.survey = self.survey
                question.save()
        return super().process_step(form)

    def get_form(self, step=None, data=None, files=None):
        if step is None:
            step = self.steps.current
        if data is None:
            data = self.storage.get_step_data(step)
        if files is None:
            files = self.storage.get_step_files(step)
        return self.form_list[step](data, files, initial=self.get_form_initial(step))

    def form_valid(self, form):
        self.storage.set_step_data(self.steps.current, self.request.POST.dict())
        self.storage.set_step_files(self.steps.current, self.request.FILES.dict())
        return self.render_next_step(form)
    
    def done(self, form_list, **kwargs):
        print(self.steps.current)
        current_step = int(self.steps.current)
        self.process_step(form_list[current_step])
        form_data = [form.cleaned_data for form in form_list]
        print("formdata", form_data)
        survey = Survey(**form_data[0], **form_data[1], **form_data[2], **form_data[3], **form_data[4], **form_data[5])
        survey.save()
        return render(self.request, 'done.html', {'form_data': form_data})
    
    def results(request):
        surveys = Survey.objects.all()
        context = {
            'surveys': surveys
        }
        return render(request, 'results.html', context)