
import scipy.interpolate as interplot
from xml.etree.ElementTree import ElementTree



def alpha_get(t):
    path="C:/OpenSim 4.0/Resources/Models/Gait2392_Simbody/ResultsCMC/"
    file="subject01_walk1_controls.xml"
    tree=ElementTree()
    tree.parse(path+file)
    ControlLinears=tree.findall("ControlSet/objects/ControlLinear")
    
    all_excitation=[]
    for i in range(12):
        time=[]
        ts=ControlLinears[i+31].findall("x_nodes/ControlLinearNode/t")
        for j in range(len(ts)):
            time.append(float(ts[j].text))
        excitation=[]
        values=ControlLinears[i+31].findall("x_nodes/ControlLinearNode/value")
        for k in range(len(values)):
            excitation.append(float(values[k].text))
        all_excitation.append(excitation)
    
    alpha=[]
    for i in range(12):
        fx=interplot.splrep(time,all_excitation[i],s=0)
        alpha.append(interplot.splev(t,fx,der=0))
    print(alpha)
    return alpha

#if __name__=="__main__":
    #alpha_get(0.53)
