# HB YL calculation
import math

def Nl(Ul: float, Pl: float , Ift: float) -> float:
    '''NL: Liquid viscosity number'''
    '''Ift: interfacial tension units: dyne/cm'''
    Nl_value = 0.15726 * Ul * ( 1 / (Pl * Ift**3 ) )**(1/4)


def CNL(Nl):
    '''CNl: Coefficient of liquid viscosity number'''

    X1 = math.log(Nl) + 3

    Y = -2.69851 + 0.15841 * X1 - 0.55100 * X1**2 + 0.54785 * X1**3 - 0.12195 * X1**4

    CNL_value = 10**Y

    return CNL_value

def phi(Vsl,Pl,IFT,Vsg,D,P):
    Nvl = 1.938 * Vsl * (Pl/IFT)**(1/4)

    Nvg =  1.938 * Vsg * (Pl/IFT)**(1/4)

    Nd = 120.827 * D * math.sqrt(Pl/IFT)

    phi_value = (Nvl * P**0.1 * CNL) / (Nvg**0.575 * 14.7**0.1 * Nd)
    return phi_value

def YlPsi(phi):
    YlPsi_value = -0.10307 + 0.6177 * (math.log(phi) + 6)**3 - 0.0401 * (math.log(phi)+6)**4

    return YlPsi_value

def Yl(phi,YlPsi):
    if phi <= 0.01:
        Psi = 1
        Yl = YlPsi
        return YlPsi
    elif phi > 0.01:
        Psi = 0.91163 - 4.82176 * phi + 1232.25 * phi**2 - 22253.6 * phi**3 + 116174.3 * phi**4

        Yl = YlPsi * Psi
        return Yl
    

def Mt(Ml,Mg):
    return Ml + Mg

def dP_HB(Pave,ff,Mt,D,dz):
    dP_value = ( Pave + ( (ff * Mt**2 ) / ( 7.413 * 10**10 * D**5 * Pave) ) ) * (dz/144)
    return dP_value