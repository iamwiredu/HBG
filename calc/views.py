from django.shortcuts import render, redirect
from django.http import HttpResponse
from .base import *
from .regime import *
from .grifth import *
from .HB import *
# Create your views here.

def calc(request):
    if 'ABdatasetSubmission' in request.POST:
        Qw = float(request.POST.get('Qw'))
        Qo = float(request.POST.get('Qo'))
        Qg =  float(request.POST.get('Qg'))
        D =  float(request.POST.get('D'))
        
        Vsg_value = Vsg(Qg,D)
        Vsl_value = Vsl(Qo,Qw,D) 

        Vm_value = Vsl_value +  Vsg_value
        regime_value = regime(Vm_value,Vsl_value,D)

        request.session['ABdataset'] = {
            'Qw':Qw,
            'Qo':Qo,
            'Qg':Qg,
            'D':D,
            'Vsg_value':Vsg_value,
            'Vsl_value':Vsl_value,
            'Vm_value':Vm_value,
            'regime_value':regime_value,
        }
        if regime_value == 'bubble':
            return redirect(bubble)
        elif regime_value == 'slug':
            return redirect(slug)

    return render(request,'calc.html')

def bubble(request):
    try:
        ABdataset = request.session['ABdataset']

        if 'bubbleflowcalc' in request.POST:
            Pw = float(request.POST.get('Pw'))
            
            Ul = float(request.POST.get('Ul'))
            Pl = float(request.POST.get('Pl'))
            Pg = float(request.POST.get('Pg'))
            Ml = ABdataset['Qo']*(Pl-Pw) + ABdataset['Qw']*Pw
            e = float(request.POST.get('e'))
            dl = float(request.POST.get('dl'))

            Yl_value = Yl(ABdataset['Vm_value'],ABdataset['Vsg_value'])
            Re_value = Re(Ml,ABdataset['D'],Ul)
            P_ave_value = P_ave(Yl_value,Pl,Pg)
            ff_value = ff(e,Re_value)


            dP_value = dP_grifth(P_ave_value,ff_value,Ml,ABdataset['D'],Pl,Yl_value,dl)
            request.session['dP_value'] = dP_value
            return redirect(results)
        
        if 'recalculate' in request.POST:
            del request.session['ABdataset'] 
            return redirect(calc)
        
        return render(request,'bubble.html')
    except KeyError:
        return redirect(calc)

def results(request):
    try:
        ABdataset = request.session['ABdataset']


        try:
            dP_value =  request.session['dP_value']
        except KeyError:
            dP_value = 'None'

        if 'recalculate' in request.POST:
            del request.session['ABdataset'] 
            del request.session['dP_value']
            return redirect(calc)

        context={
            'ABdataset' :request.session['ABdataset'],
            'dP_value': dP_value
            
        }
        return render(request,'results.html',context)
    except KeyError:
        return redirect(calc)

  


  



    

def slug(request):
    try:
        ABdataset = request.session['ABdataset']

        print(ABdataset)
        if 'slugflowcalc' in request.POST:
            Pl = float(request.POST.get('Pl'))
            Pg = float(request.POST.get('Pg'))
            Ul = float(request.POST.get('Ul'))
            Ug = float(request.POST.get('Ug'))
            IFT_value = float(request.POST.get('IFT_value'))
            P_value = float(request.POST.get('P'))
            e = float(request.POST.get('e'))
            dl = float(request.POST.get('dl'))
            
            Nl_value = Nl(Ul,Pl,IFT_value)
            CNL_value = CNL(Nl_value)
            phi_value = phi(ABdataset['Vsl_value'],Pl,IFT_value,ABdataset['Vsg_value'],ABdataset['D'],P_value,CNL_value)
            comPhi_value = comPhi(Ul,Pl,IFT_value,ABdataset['Vsg_value'],ABdataset['D'])
            YlPsi_value = YlPsi(phi_value)
            Yl_HB_value =Yl_HB(comPhi_value,YlPsi_value)
            P_ave_value = P_ave(Yl_HB_value,Pl,Pg)
            Mt_value = Mt(ABdataset['Qo']+ABdataset['Qw'],Pl,ABdataset['Qg'],Pg)
            Re_value = Re_HB(Mt_value,Ul,Ug,ABdataset['D'],Yl_HB_value)
            ff_value = ff(e,Re_value)
            dP_HB_value = dP_HB(P_ave_value,ff_value,Mt_value,ABdataset['D'],dl)
            request.session['dP_value'] = dP_HB_value
            print(comPhi_value)
            return redirect(results)
        context={
            'ABdataset':ABdataset,
        }
        if 'recalculate' in request.POST:
            del request.session['ABdataset']
            return redirect(calc)
        return render(request,'slug.html',context)

    except KeyError:
        return redirect(calc)