from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import redirect
from .commands import create_user, create_watchlist, optimize_watchlist
import random
# Author: Kehne, 17.11 - 12:42

# Some standard Django stuff
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, loader
from cerandi_app.models import *;

# list of mobile User Agents
mobile_uas = [
	'w3c ','acs-','alav','alca','amoi','audi','avan','benq','bird','blac',
	'blaz','brew','cell','cldc','cmd-','dang','doco','eric','hipt','inno',
	'ipaq','java','jigs','kddi','keji','leno','lg-c','lg-d','lg-g','lge-',
	'maui','maxo','midp','mits','mmef','mobi','mot-','moto','mwbp','nec-',
	'newt','noki','oper','palm','pana','pant','phil','play','port','prox',
	'qwap','sage','sams','sany','sch-','sec-','send','seri','sgh-','shar',
	'sie-','siem','smal','smar','sony','sph-','symb','t-mo','teli','tim-',
	'tosh','tsm-','upg1','upsi','vk-v','voda','wap-','wapa','wapi','wapp',
	'wapr','webc','winw','winw','xda','xda-'
	]

mobile_ua_hints = [ 'SymbianOS', 'Opera Mini', 'iPhone' ]


def mobileBrowser(request):
    ''' Super simple device detection, returns True for mobile devices '''

    mobile_browser = False
    ua = request.META['HTTP_USER_AGENT'].lower()[0:4]

    if (ua in mobile_uas):
        mobile_browser = True
    else:
        for hint in mobile_ua_hints:
            if request.META['HTTP_USER_AGENT'].find(hint) > 0:
                mobile_browser = True

    return mobile_browser

def tinder(request,client_pk):
    stocks_left = Stock.objects.filter(~Q(investment__client__pk=client_pk))
    all_stocks = stocks_left
    return render(request, 'swipe.html',{'all_stocks': all_stocks, "client": Client.objects.get(pk=client_pk)})

def watchlist(request, client_pk):
    stocks_invested = Stock.objects.filter(investment__client__pk=client_pk)
    return render(request, "watchlist.html", {"stocks_invested": stocks_invested, "client": Client.objects.get(pk=client_pk)})

def index_page(request):
    return render(request, 'landing.html')

def login_form(request):
    return render(request, 'login_form.html')

def chat(request,client_pk):
    last_name = Client.objects.get(pk=client_pk).last_name
    first_name = Client.objects.get(pk=client_pk).first_name
    chat_url = first_name+"_"+ last_name+"_"+client_pk
    return render(request, 'chat.html',{'chat_url' : chat_url})

def logout(request):
    return render(request, 'logout.html')

def register_user(request):
    items = ['63065', '60311', '64283']
    first_name = request.POST['first_name']
    last_name = request.POST["last_name"]
    new_Client = Client()
    new_Client.first_name = first_name
    new_Client.last_name = last_name
    new_Client.plz_location = random.choice(items)
    new_Client.save()
    request.session['new_client'] = new_Client.pk
    return render(request,'persona_score.html',{'new_Client' : new_Client})

def persona_score(request):
    new_Client = request.session.get('new_client', None)
    print new_Client
    new_Client = Client.objects.get(pk=new_Client)
    new_Client.risk_ratio = request.POST['persona_score']
    new_Client.save()
    #return render(request, 'swipe.html',{'new_Client' : new_Client})
    return redirect('tinder', client_pk=new_Client.pk)

def update_investment(request,client_pk,stock_pk):
    #stock_pk = request.POST['stock_pk']
    #client_pk = request.POST['client_pk']
    new_investment = Investment()
    new_investment.stock = Stock.objects.get(pk= stock_pk)
    new_investment.client = Client.objects.get(pk = client_pk)
    new_investment.save()
    return render(request, 'login_form.html')

#no plz filtering implemented
def client_list(request, advisor_pk):
    all_clients = Client.objects.all().order_by('-plz_location')
    return render(request, 'client_list.html',
                  {'all_clients': all_clients,
                   'advisor': Advisor.objects.get(pk=advisor_pk)})

def client_detail(request, advisor_pk, client_pk):
    investments = Investment.objects.filter(client__pk = client_pk)
    client = Client.objects.get(pk=client_pk)
    chat_url = client.first_name+"_"+ client.last_name+"_"+client_pk
    return render(request, 'client_detail.html',
                  {'client': Client.objects.get(pk=client_pk),
                   'advisor': Advisor.objects.get(pk=advisor_pk),
                   'investments': investments,
                   'chat_url': chat_url})


def analyze(request, advisor_pk, client_pk):
    client = Client.objects.get(pk=client_pk)
    user_id = create_user(str(random.randint(0,1000)))
    investments = Investment.objects.filter(client__pk = client_pk)
    stock_ids = [x.stock.sap_id for x in investments]
    watchlist_id = create_watchlist(user_id, stock_ids)
    allocation_and_return = optimize_watchlist(watchlist_id)
    chat_url = client.first_name+"_"+ client.last_name+"_"+client_pk
    return render(request, 'analyze.html',
                  {"allocation_optimized": allocation_and_return[0],
                   "estimated_return": allocation_and_return[1],
                   "client": client,
                   "advisor": Advisor.objects.get(pk=advisor_pk),
                   'chat_url': chat_url})

# def persona_score(request):#,new_Client_pk):
#     #print new_Client_pk
#     #persona_score = request.POST['persona_score']
#     #new_Client.moral_ratio = 4
#     #num_results = Client.objects.filter(first_name = first_name).count()
#
#     #if num_results != 0:
#     #    num_results = num_results+1
#
#     #new_Client = Client()
#     #new_Statement.url = url.replace('#','')
#     #new_Statement.count_statement = num_results
#     #new_Statement.statement = request.POST['statement_input']
#     #new_Statement.gender = request.POST['m_or_w']
#     #new_Client.save()
#     print "NEW persona score has to be saved"
#     return redirect('index_page')#, url=new_Client.pk,count_statement=new_Client.pk)
#       #p = update_or_create(Statement, pk=question_id)
#       #statement_detail(request,Statement.url)
#       #return HttpResponseRedirect(reverse('Statement:generate_Statement', args=(p.id,)))