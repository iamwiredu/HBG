import math
def P_ave(Yl,Pl,Pg):
    P_ave_value = Yl * Pl + (1 - Yl) * Pg

## chenning correlation 
def ff(e,Re):
    ffValue = -4 * math.log( e/3.7065 - (5.0452/Re) * math.log( ( (e**1.1098)/2.8257 ) + (7.148/Re)**0.8981 )  ) 
