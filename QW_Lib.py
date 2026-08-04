import numpy as np
import matplotlib.pyplot as plt

import Constants as const

q = const.q
me = const.me
h = const.h
hb = const.hb

def Pot(U, thickness, slope, Res):
    # U is potential (eV)
    # Thickness (in nm, 0.1nm resolution)
    # Slope (V/nm)
    pix = round(thickness * Res)
    if (slope == 0):
    	result = np.full(pix, U)
    else:
        result = []
        for i in range(pix):
            result.append(U - slope*i/Res)
    return result

def Single_Well(Bias, param, Res, full):
    left_bar = param["lBar_Thickness"] * 1e9
    right_bar = param["rBar_Thickness"] * 1e9
    qw_l = param["QW_Length"] * 1e9
    EA_lBar = param["EA_lBarrier"]/q
    EA_rBar = param["EA_rBarrier"]/q
    BG_lBar = param["BG_lBarrier"]/q
    EA_QW = param["EA_QW"]/q
    EA_Cond = param["EA_Cond"]/q
    
    vac = EA_lBar + BG_lBar
    cond_height = (vac - EA_Cond) + Bias
    qw_height = vac - EA_QW
    lbar_height = (vac - EA_lBar)
    rbar_height = (vac - EA_rBar)
    distance = left_bar + right_bar + qw_l
    angle = Bias/distance
    qw_pos = (right_bar + qw_l/2)/distance
    
    l_bar_height = lbar_height + Bias
    r_bar_height = rbar_height + right_bar*Bias/distance
    real_qw_height = qw_height + 0.5*qw_l*Bias/distance + qw_pos*Bias
        
    C1 = Pot(cond_height, 10, 0, Res)
    B1 = Pot(l_bar_height, left_bar, angle, Res)
    C2 = Pot(real_qw_height, qw_l, angle, Res)
    B2 = Pot(r_bar_height, right_bar, angle, Res)
    C3 = Pot(0, 10, 0, Res)
    if (full):
        result = np.concatenate((C1, B1, C2, B2, C3))
    else:
        result = np.concatenate((B1, C2, B2))
    return result

def Show_Potential(Well, Bias, Res):
    distance = np.linspace(0, len(Well)/Res, len(Well))
    text = "New QW under bias (" + str(Bias) + "V)"
    plt.plot(distance, Well)
    plt.title(text)
    plt.xlabel("length (nm)")
    plt.ylabel("Barrier potential (eV)")
    plt.show()