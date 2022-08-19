from django.contrib import messages
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth

from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'accounts/register.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        try:
            validate_email(email)
        except ValidationError:
            messages.info(request, 'Invalid EMAIL')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Invalid USERNAME')
            return redirect('register')

        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Invalid EMAIL')
            return redirect('register')

        else:
            user = User.objects.create_user(username=username, email=email,
                                            password=password)
            user.save()
            return redirect('login')

    images = ['anonymity.png', 'bitcoin.png', 'blackcoin.png',
              'block_chain.png', 'centralized.png', 'conversion.png',
              'currency_cap.png', 'decentralized.png', 'decryption.png',
              'digital_key.png', 'disclosed_identity.png', 'distributed.png',
              'dogecoin.png', 'emercoin.png', 'encryption.png', 'ethereum.png',
              'feathercoin.png', 'free.png', 'ledger.png', 'litecoin.png',
              'lost_key.png', 'mastercoin.png', 'miner.png', 'miner2.png',
              'mining.png', 'mining2.png', 'mining_center.png',
              'mining_pool.png',
              'mining_pool2.png', 'monero.png', 'myriad.png', 'namecoin.png',
              'no_double_spending.png', 'nxt.png', 'p2p.png', 'peercoin.png',
              'ponzi_scheme.png', 'primecoin.png', 'pseudonimity.png',
              'pyramid_scheme.png', 'receive.png', 'ripple.png', 'send.png',
              'siacoin.png', 'stellar_lumen.png', 'transaction.png',
              'tumbler.png',
              'wallet.png', 'zcash.png', 'zcoin.png']
    context = {'deck': range(2), 'row': range(5), 'col': range(5),
               'len': range(25), 'images': images}
    return render(request, 'accounts/register.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'Invalid Request')
            return redirect('login')

    return render(request, 'accounts/login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('/')


def about(request):
    return render(request, 'accounts/about.html')


def team(request):
    return render(request, 'accounts/team.html')
