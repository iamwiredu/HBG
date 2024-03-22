import math
def P_ave(Yl,Pl,Pg):
    P_ave_value = Yl * Pl + (1 - Yl) * Pg
    return P_ave_value

## chenning correlation 
def ff(e,Re):
    ffValue = ( 1 / (-4 * math.log( e/3.7065 - (5.0452/Re) * math.log( ( (e**1.1098)/2.8257 ) + (7.149/Re)**0.8981 )  ) ) )**2
    return ffValue
def Vsl(Qo,Qw,D):
    Vsl_value = (Qo+Qw) / (math.pi/4 * D**2)
    return Vsl_value

def Vsg(Qg,D):
    Vsg_value = (Qg) / (math.pi/4 * D**2)
    return Vsg_value

