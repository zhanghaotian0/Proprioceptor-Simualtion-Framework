
import scipy.interpolate as interplot
from proprioceptor_model import spindle,gto,primary_afferent

def control_excitation_get(t,dett,alpha_now,alpha_next):
    path="C:/OpenSim 4.0/Resources/Models/Gait2392_Simbody/ResultsForwardfeedback"+str(dett)+"/"
    fiber_length_file="subject01_walk1_states.sto"
    force_file="subject01_walk1_Actuation_force.sto"
    with open(path+force_file) as fp:
        data=fp.readlines()
    data_split=[]
    for i in range(len(data)):
        data_split.append(list(filter(None,data[i].split("\t"))))
    data.clear()
    #print(data_split)
    time=[]
    for i in range(len(data_split)-23):
        time.append(float(data_split[i+23][0]))
    #print(time)
    all_force=[]
    for i in range(12):
        force=[]
        for j in range(len(data_split)-23):

            force.append(float(data_split[j+23][32+i]))
        all_force.append(force)
    data_split.clear()
    force_t=[]
    '''
    for i in range(12):
        fx=interplot.interp1d(time,all_force[i],kind="cubic")
        force_t.append(fx(t-dett))
    '''
    for i in range(12):
        fx=interplot.splrep(time,all_force[i],s=0)
        force_t.append(interplot.splev(t-dett,fx,der=0))

    with open(path+fiber_length_file) as fp:
        data=fp.readlines()
    #print(data)
    data_split=[]
    for i in range(len(data)):
       data_split.append(list(filter(None,data[i].split("\t"))))
    data.clear()
    time=[]
    for i in range(len(data_split)-7):
        time.append(float(data_split[i+7][0]))
    all_fiber_length=[]
    for i in range(12):
        fiber_length=[]
        for j in range(len(data_split)-7):
            fiber_length.append(float(data_split[j+7][110+i*2]))
        all_fiber_length.append(fiber_length)
    data_split.clear()
    #print(time)
    length_t=[]
    velocity_t=[]
    acceleration_t=[]=[]
    for i in range(12):
        fx=interplot.splrep(time,all_fiber_length[i],s=0)
        length_t.append(float(interplot.splev(t-dett,fx,der=0)))
        velocity_t.append(float(interplot.splev(t-dett,fx,der=1)))
        acceleration_t.append(float(interplot.splev(t-dett,fx,der=2)))
    optimal_fiber_length = [0.06, 0.064, 0.05, 0.031, 0.034, 0.043, 0.098, 0.05, 0.049, 0.079, 0.102, 0.111]
    max_isometric_force = [1558, 683, 3549, 1558, 310, 322, 905, 435, 943, 180, 512, 162]
    excitations=[]
    for i in range(12):
        #print(length_t[i],velocity_t[i],acceleration_t[i],optimal_fiber_length[i],alpha_now[0][i])
        spindle_generate=spindle(length_t[i],velocity_t[i],acceleration_t[i],optimal_fiber_length[i],alpha_now[i])
        BAG1=spindle_generate.BAG1()
        BAG2=spindle_generate.BAG2()
        CHAIN=spindle_generate.CHAIN()
        #print(BAG1)
        spindle_excitation=primary_afferent(BAG1, BAG2, CHAIN)
        normalized_force=force_t[i] / max_isometric_force[i]
        if normalized_force>0.7:
            gto_excitation=gto(normalized_force)
        if normalized_force<0.7:
            gto_excitation=0
        excitation=spindle_excitation-gto_excitation+alpha_next[i]
        if excitation<0:
            excitation=0
        if excitation>1:
            excitation=1
        excitations.append(excitation)
    print(excitations)
    return excitations