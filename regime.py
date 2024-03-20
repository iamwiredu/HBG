def regime(Vm: float, Vsg: float, D: float):
    ''' Units are in Field Units '''
    ''' Vm : Liiquid Mixture Velocity ''' 
    ''' Vsg Gas Superficial Velocity '''
    ''' D : Inner Diameter of the tube '''
    try:
        A = 1.071 - 0.2218 * ( (Vm**2)/D )
        if A < 0.13: 
            A = 0.13

    except ZeroDivisionError:
        print(" The Inner Diameter of the tube cannot be zero")


    try:
        B = Vsg/Vm
    except ZeroDivisionError:
        print("The input of the Liquid Mixture Velocity can not be zero")

    # Finding correlation to use base on regime

    if (A > B):
        '''The regime is the bubble regime and we use the grifth method'''
        return 'bubble'
    elif ( B > A ) or ( (B-A) == 0 ):
        '''The regime is the slug regime and we use the Hagedorn Brown method'''
        return 'slug'        
    
    