from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
# karşılama sayfası ve login olduktan sonra yönlendirmek istediğim view fonksiyonumu yazdım


def home(request):
    return render(request, 'users/home.html')


def user_login(request):
    # django auth formstan import ediyoruz
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user = form.get_user()  # formdan gelen bilgileri alıyoruz
        login(request, user)  # formda gelen bilgilerle istek atıyoruz
        # urls.py da tanımladığımız name patterninden gelen değer
        return redirect('home')
    return render(request, 'users/login.html', {'form': form})
# register için de kendiniz fonksiyon yazabilirsiniz. Dediğim gibi bu yazımda asıl odaklanacağımız kısım google ile giriş konusu o nedenle ben burada örnek bir yapı kuruyorum.
