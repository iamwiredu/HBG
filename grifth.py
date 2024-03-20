import math
def Yl(Vm,Vsg):
    ''' Vm : Liiquid Mixture Velocity ''' 
    Vs = 0.8 # units ft/s
    Yl_value = 1 - [ 1 + (Vm/Vs) - math.sqrt( (1 + Vm/Vs )**2 - 4 * ( Vsg/Vs ) ) ]
    return Yl_value

def Re(Ml,D,Ul):
    '''Ml : Mass flow rate of liquid'''
    ''' D : Inner Diameter of the tube '''
    ''' ul : Visosity of the liquid '''

    Re_value = (2.2 * 10**(-2) * Ml ) / ( D * Ul ) 
    return Re_value


def dP_grifth(P_ave,ff,Ml,D,Pl,Yl,dl):
    dp_value = (P_ave + (ff * Ml**2 ) / (7.413 * 10**10 * D**5 * Pl * Yl**2) ) * dl/144

    return dp_value