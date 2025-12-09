# Proprioceptor-Simualtion-Framework
# **Proprioceptor Simualtion Framework**

A framework of a lower limb musculoskeletal model with implemented natural proprioceptive feedback

## **Overview**

 The feedback control framework was established by combining Python codes, control setting files, and a biomechanical musculoskeletal model. The biomechanical musculoskeletal model was based on OpenSim software from a 3D lower limb musculoskeletal model.The feedback control loop consists of ascending neural control signals from the CNS and descending feedback signals from the muscle-tendon components. We implemented this framework in the forward dynamic tool. The neural excitation travels and exchanges in this loop. At each timestep, the muscle controlling signal is iteratively calculated by combining descending and ascending controlling signals after a defined neural delay. The current ascending signal input is the excitation signals from the computed muscle control (CMC) procedure in OpenSim package.

<img width="928" height="748" alt="image" src="https://github.com/zhanghaotian0/Proprioceptor-Simualtion-Framework/tree/main/image/zhang2020" />

### **Key Features**

* **Multi-Array Ultrasound Probes**: The system uses a combination of **linear**, **convex**, and **phased array probes** to offer versatile imaging, enabling effective diagnosis across multiple organ systems.
* **AI-Powered Diagnostics**: The system employs **VUSB-Net** for image-based diagnosis and **YRLDW-Net** for video-based analysis, capable of diagnosing **effusions** and **pneumothorax** in real-time.
* **Portable and Lightweight**: Designed for easy handling and transport, it is perfectly suited for **emergency environments** and **fieldwork**.
* **Offline Operation**: Both AI models work **offline**, enabling real-time diagnostics without the need for cloud computing or internet access.

---

## **Diagnostic Models**

### **1. Medical Image Diagnosis - VUSB-Net**

**VUSB-Net** is a **UNet-based AI model** specifically designed for the **segmentation and classification of ultrasound images**. The model accurately identifies regions of **pericardial and abdominal effusion**, providing a reliable diagnosis in real-time. It is ideal for quick decision-making in emergency situations.

![VUSB-Net Architecture](https://github.com/user-attachments/assets/20d9cb06-4d2f-4fe6-baee-fffc31fa9a49)

*The **VUSB-Net** model efficiently segments effusion regions from ultrasound images, assisting in the diagnosis of conditions like pericardial and abdominal effusion.*

### **2. Medical Video Diagnosis - YRLDW-Net**

**YRLDW-Net** integrates **YOLOv8** for object detection and **LSTM** (Long Short-Term Memory) for video sequence analysis. This model is designed for **diagnosing pneumothorax** and other dynamic conditions in ultrasound video sequences. It tracks abnormalities over time, offering continuous monitoring for accurate diagnosis in clinical environments.

<img width="964" height="571" alt="image" src="https://github.com/user-attachments/assets/60d75afa-4494-41f0-9888-15fef73dee10" />


*The **YRLDW-Net** model uses YOLOv8 for object detection and LSTM for temporal video analysis to diagnose pneumothorax from continuous ultrasound video feeds.*

---

## **On-Device AI Inference**

The **USDiaSystem** leverages **edge AI models** optimized to run directly on devices such as smartphones or embedded systems. This allows for **real-time diagnostics** without the need for cloud-based computation, ensuring that the system remains operational even in remote or disaster scenarios.

* **Edge Computing**: Both the **VUSB-Net** and **YRLDW-Net** models are optimized to run on **smartphones** and **embedded devices**. The inference time for each image/frame is **<0.65s**, ensuring fast and responsive diagnostics.
* **Offline Operation**: Both AI models operate entirely offline once trained, making the system fully functional in environments without internet access.

![On-Device AI Inference](https://github.com/user-attachments/assets/edb0bc30-3641-4049-87df-118b3c19a068)

To run the models locally on your device:

1. **Prepare the ultrasound image or video.**
2. **Run the inference model** to get results in real time.

---

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

The models will output **segmentation masks** or **diagnostic labels** (such as **effusion** or **pneumothorax**), along with the regions of interest in the input image or video.

---

## **Code Structure**

The repository is organized into several folders, each corresponding to specific parts of the system. Here's a breakdown of the folder structure and the functionality of each file:

### **1. MedicalImageDiagnosis/**

Contains code related to image diagnosis using the **VUSB-Net** model.

* `classifier_model.py`: Classifies images using features extracted by a U-Net model.
* `get_miou.py`: Calculates mIoU for segmentation models in VOC format.
* `predict.py`: Predicts segmentation masks and supports video detection and FPS testing.
* `summary.py`: Displays U-Net model structure and calculates parameters and FLOPs.
* `train.py`: Trains U-Net model for semantic segmentation with various configurations.
* `voc_annotation.py`: Generates dataset lists and checks format for VOC datasets.

#### **nets/**

* `__init__.py`: Initializes the model definitions.
* `resnet.py`: ResNet backbone for feature extraction.
* `unet.py`: Defines the UNet architecture for image segmentation.
* `unet_training.py`: Script for training the UNet model.
* `vgg.py`: VGG model for image feature extraction.

#### **tools/**

* `MoveFile.py`: Utility to move files between directories.
* `Torch2ONNX.py`: Converts PyTorch models to ONNX format for edge deployment.
* `add-prefix.py`: Add prefix to the document.
* `json_to_dataset.py`: Converts dataset annotations into JSON format.
* `txtwrite.py`: Utility for writing text files (e.g., for logs or results).
* `unetout01.py`: Final output script for image inference.

#### **units/**

* `__init__.py`: Initializes Python package, enabling modular code organization.
* `callbacks.py`: Implements callbacks for loss tracking and model evaluation during training.
* `dataloader.py`: Loads and preprocesses image data with augmentation for training.
* `dataloader_medical.py`: Specialized data loader for medical images and labels.
* `utils.py`: Provides utility functions for image processing and training utilities.
* `utils_fit.py`: Manages model training, including loss computation and checkpoint saving.
* `utils_metrics.py`: Computes and visualizes evaluation metrics like mIoU and precision.

---

### **2. MedicalVideoDiagnosis/**

Contains code related to video diagnosis using the **YRLDW-Net** model.

* `config.py`: Contains configuration settings for dataset paths, model training, and evaluation.
* `cuda.py`: CUDA setup for GPU acceleration.
* `data_preprocessing.py`: Preprocesses video data for model inference.
* `evaluate.py`: Evaluates the model on video sequences.
* `logging_setup.py`: Sets up logging for tracking experiment results.
* `main.py`: Main script for training, evaluating, and visualizing model performance.
* `model.py`: Defines CNN and RNN-based models for sequence classification tasks.
* `resnet18_pretrained.pth`: Pretrained ResNet18 weight file.
* `train.py`: Trains the model, tracks performance metrics, and saves training history.
* `train_pro.py`: Improved training script with additional features and optimizations.
* `utils.py`: Provides utility functions for data processing, transformations, and dataset creation.
* `visualize.py`: Visualizes training metrics and model performance using plots.

#### **tool/**

* `pth2onnx.py`: Converts PyTorch models to ONNX format for edge deployment.

---

## **License**

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## **Acknowledgements**

We would like to acknowledge all the researchers, contributors, and institutions whose work has laid the foundation for this system. Special thanks to the developers in the fields of **medical imaging** and **machine learning** for their continuous efforts in advancing AI-assisted diagnostics.
