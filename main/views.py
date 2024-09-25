from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Categories



class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'N_K - Главная'
        context['content'] = "Магазин товаров для волейбола 'N_K'   "
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'N_K - О нас'
        context['content'] = "О нас"
        context['text_on_page'] = "Мы интернет магазин по продаче мячей Mikasa и не только."
        return context
    

# def index(request):

#     context = {
#         'title': 'Home - Главная',
#         'content': "Магазин волейбола",
#     }

#     return render(request, 'main/index.html', context)


# def about(request):
#     context = {
#         'title': 'Home - О нас',
#         'content': "О нас",
#         'text_on_page': "Текст о том почему этот магазин такой классный, и какой хороший товар."
#     }

#     return render(request, 'main/about.html', context)