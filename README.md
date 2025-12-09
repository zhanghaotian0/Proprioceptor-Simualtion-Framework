# Proprioceptor-Simualtion-Framework
# **Proprioceptor Simualtion Framework**

A framework of a lower limb musculoskeletal model with implemented natural proprioceptive feedback

## **Overview**

 The feedback control framework was established by combining Python codes, control setting files, and a biomechanical musculoskeletal model. The biomechanical musculoskeletal model was based on OpenSim software from a 3D lower limb musculoskeletal model.The feedback control loop consists of ascending neural control signals from the CNS and descending feedback signals from the muscle-tendon components. We implemented this framework in the forward dynamic tool. The neural excitation travels and exchanges in this loop. At each timestep, the muscle controlling signal is iteratively calculated by combining descending and ascending controlling signals after a defined neural delay. The current ascending signal input is the excitation signals from the computed muscle control (CMC) procedure in OpenSim package.

![Scheme of the simulation framework of the proprioceptive musculoskeletal model.](https://github.com/zhanghaotian0/Proprioceptor-Simualtion-Framework/blob/main/image/zhang2020.png)
<img width="500" height="400" alt="image" src="https://github.com/zhanghaotian0/Proprioceptor-Simualtion-Framework/blob/main/image/zhang20202.jpg" />

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
