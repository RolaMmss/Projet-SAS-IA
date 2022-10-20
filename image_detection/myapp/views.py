from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import User

from myapp.forms import UserForm
from django.shortcuts import redirect  

# Create your views here.
def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « User » et la sauvegarder dans la db
            user = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('user-detail', user.id)

    else:
        form = UserForm()

    return render(request,
            'myapp/user_create.html',
            {'form': form})

def user_list(request):  # renommer la fonction de vue
   users = User.objects.all()
   return render(request,
           'myapp/user_list.html',  # pointe vers le nouveau nom de modèle
           {'users': users})

def user_detail(request, id):
  user = User.objects.get(id=id)  # nous insérons cette ligne pour obtenir le Band avec cet id
  return render(request,
          'myapp/User_detail.html',
          {'user': user}) # nous mettons à jour cette ligne pour passer le groupe au gabarit
