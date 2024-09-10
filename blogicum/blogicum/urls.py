from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import path, include, reverse_lazy, reverse
from django.shortcuts import redirect

# Функция для перенаправления на страницу профиля
def redirect_to_profile(request):
    return redirect(reverse('blog:profile', args=[request.user.username]))

urlpatterns = [
    path('admin/', admin.site.urls),
    path("pages/", include('pages.urls')),
    path('', include('blog.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('pages:homepage'),
        ),
        name='registration',
    ),
    # Добавляем перенаправление после авторизации
    path('accounts/profile/', redirect_to_profile),
]

handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'

