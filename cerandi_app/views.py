from django.shortcuts import render
from django.shortcuts import redirect
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


def index_page(request):
    '''Render the index page'''
    all_stocks = Stock.objects.all().order_by('-wkn')
    if mobileBrowser(request):
        t = loader.get_template('landing.html')
    else:
        t = loader.get_template('landing.html') # Kehne: IMMER MOBILE ZUM TESTEN!

    c = Context( { }) # normally your page data would go here

    #return HttpResponse(t.render(c))
    return render(request, 'swipe.html',{'all_stocks': all_stocks})

def advisor_page(request):
    '''Render the advisor page'''

    if mobileBrowser(request):
        t = loader.get_template('client_list.html')
    else:
        t = loader.get_template('client_list.html') # Kehne: IMMER MOBILE ZUM TESTEN!

    c = Context( { }) # normally your page data would go here

    return HttpResponse(t.render(c))



def login_form(request):
    return render(request, 'login_form.html')

def logout(request):
    return render(request, 'logout.html')

def register_user(request):
    first_name = request.POST['first_name']
    new_Client = Client()
    new_Client.first_name = first_name
    new_Client.save()
    print first_name
    request.session['new_client'] = new_Client.pk
    return render(request,'persona_score.html',{'new_Client' : new_Client})

def persona_score(request):
    new_Client = request.session.get('new_client', None)
    print new_Client
    new_Client = Client.objects.get(pk=new_Client)
    new_Client.risk_ratio = request.POST['persona_score']
    new_Client.save()
    return render(request, 'swipe.html',{'new_Client' : new_Client})

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