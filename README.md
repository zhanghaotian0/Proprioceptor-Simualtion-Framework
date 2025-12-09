# Proprioceptor-Simualtion-Framework
# **Proprioceptor Simualtion Framework**

A framework of a lower limb musculoskeletal model with implemented natural proprioceptive feedback

## **Overview**

 The feedback control framework was established by combining Python codes, control setting files, and a biomechanical musculoskeletal model. The biomechanical musculoskeletal model was based on OpenSim software from a 3D lower limb musculoskeletal model.The feedback control loop consists of ascending neural control signals from the CNS and descending feedback signals from the muscle-tendon components. We implemented this framework in the forward dynamic tool. The neural excitation travels and exchanges in this loop. At each timestep, the muscle controlling signal is iteratively calculated by combining descending and ascending controlling signals after a defined neural delay. The current ascending signal input is the excitation signals from the computed muscle control (CMC) procedure in OpenSim package.

<img width="500" height="700" alt="image" src="https://github.com/zhanghaotian0/Proprioceptor-Simualtion-Framework/blob/main/image/zhang2020.png" /><img width="500" height="400" alt="image" src="https://github.com/zhanghaotian0/Proprioceptor-Simualtion-Framework/blob/main/image/zhang20202.jpg" />

## **System Usage**

### **1. Clone the Repository**

```bash
git clone https://github.com/Moonwolf129/USDiaSystem.git
```

### **2. Install Dependencies**

Make sure that **Python 3.x** and the required libraries are installed:

```bash
pip install -r requirements.txt
```

### **3. Results**

Build your own model of proprioceptor and run the scripts.

## **License**

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## **Acknowledgements**

We would like to acknowledge all the researchers, contributors, and institutions whose work has laid the foundation for this system. Special thanks to the developers in the fields of **medical imaging** and **machine learning** for their continuous efforts in advancing AI-assisted diagnostics.
