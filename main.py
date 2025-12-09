
import opensim as osim
import shutil
from file_operation import controls_feedbackfile_create,controls_file_change,setup_file_time_change
from origin_excitaion_get import alpha_get
from feedback_excitation_get import control_excitation_get


def forward_sim(path,file):
    forward_tool=osim.ForwardTool(path+file)
    forward_tool.run()

#setup_file_time_change(0.53,0.1)
def control_frame(initial_time,dett):
    
    path="C:/OpenSim 4.0/Resources/Models/Gait2392_Simbody/"
    file="subject01_Setup_Forwardfeedback.xml"
    controls_feedbackfile_create()
    alpha_initial=alpha_get(initial_time)
    alpha_final=alpha_get(initial_time+dett)
    controls_file_change(initial_time,alpha_initial)
    final_time = initial_time + dett
    controls_file_change(final_time, alpha_final)
    setup_file_time_change(final_time,dett)
    forward_sim(path,file)

  
    iter_cnt=2
    while(final_time<=1.989):
        final_time=initial_time+dett*iter_cnt
        alpha_final_time=alpha_get(final_time)
        alpha_last_time=alpha_get(final_time-dett)
        excitations=control_excitation_get(final_time,dett,alpha_last_time,alpha_final_time)
        controls_file_change(final_time,excitations)
        setup_file_time_change(final_time,dett
        forward_sim(path, file
        iter_cnt+=1
       
        shutil.copyfile("C:/OpenSim 4.0/Resources/Models/Gait2392_Simbody/ResultsCMC/subject01_walk1_controlsfeedback.xml","C:/OpenSim 4.0/Resources/Models/Gait2392_Simbody/ResultsForwardfeedback"+str(dett)+"/subject01_walk1_controls.xml")

control_frame(0.53,0.005*(3))

