from django.views.generic import TemplateView


from newsfeed.models import Issue

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['latest_issue'] = Issue.objects.all().prefetch_related(
            'posts', 'posts__category'
        ).latest('issue_number')

        return context
