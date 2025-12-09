
from xml.etree.ElementTree import ElementTree,Element


def controls_feedbackfile_create():
    path = "C:/OpenSim 4.0/Resources/Models/Gait2392_Simbody/ResultsCMC/"
    file = "subject01_walk1_controls.xml"
    tree=ElementTree()
    tree.parse(path+file)
    ControlLinears = tree.findall("ControlSet/objects/ControlLinear")
    for i in range(12):
        x_nodes=ControlLinears[i+31].find("x_nodes")
        x_nodes.clear()
    new_path=path+file[:-4]+"feedback"+".xml"
    tree.write(new_path,encoding="utf-8",xml_declaration=True)
    return new_path

def controls_file_change(time,excitations):
    path="C:/OpenSim 4.0/Resources/Models/Gait2392_Simbody/ResultsCMC/"
    file="subject01_walk1_controlsfeedback.xml"
    tree=ElementTree()
    tree.parse(path+file)
    ControlLinears = tree.findall("ControlSet/objects/ControlLinear")
    for i in range(12):
        x_nodes = ControlLinears[i + 31].find("x_nodes")
        ControlLinearNode=Element("ControlLinearNode")
        x_nodes.append(ControlLinearNode)
        t=Element("t")
        ControlLinearNode.append(t)
        t.text=str(time)
        value=Element("value")
        ControlLinearNode.append(value)
        value.text=str(excitations[i])
        tree.write(path + file, encoding="utf-8", xml_declaration=True)

def setup_file_time_change(final_time,dett):
    path="C:/OpenSim 4.0/Resources/Models/Gait2392_Simbody/"
    file="subject01_Setup_Forwardfeedback.xml"
    tree=ElementTree()
    tree.parse(path+file)
    initial_time_e=tree.find("ForwardTool/initial_time")
    final_time_e=tree.find("ForwardTool/final_time")
    initial_time_e.text=str(0.53)
    final_time_e.text=str(final_time)
    results_directory=tree.find("ForwardTool/results_directory")
    results_directory.text="ResultsForwardfeedback"+str(dett)
    tree.write(path+file,encoding="utf-8",xml_declaration=True)

#unit test
if __name__=="__main__":
    setup_file_time_change()
    controls_feedbackfile_create()
    #controls_file_change(0.53,np.zeros(12,1))