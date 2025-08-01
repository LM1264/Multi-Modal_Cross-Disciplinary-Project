# 🧠 Multi-Modal & Cross-Disciplinary Project

This repository contains two AI-driven mini projects developed as part of the **Multi-Modal and Cross-Disciplinary Project** for the **BCA Summer Internship 2025** under **Guru Gobind Singh Indraprastha University**.

---

## 📁 Project Structure

This repo includes two key projects:

### 1. 🤖 AI-Powered Recipe Generator from Fridge Photos
Uses YOLOv5 object detection to identify ingredients in fridge images and suggests recipe ideas accordingly.

### 2. 🖼️ Image Caption & Voice Generator
Generates image captions using BLIP (by Salesforce) and then converts those captions to speech using ElevenLabs API.

---

## 🚀 Live Demos / Outputs

| Project | Functionality | Output Preview1 | Output Preview2 | Output Preview3 | Output Preview4 |
|--------|---------------|----------------|----------------|----------------|----------------|
| **Recipe Generator** | Ingredient detection + recipe suggestion | ![Image1](Screenshots/AI_recipe_suggestions.png) | ![Image2](Screenshots/Fp1.jpg) | ![Image3](Screenshots/Fp2.jpg) | ![Image4](Screenshots/Fp3.jpg) |
| **Caption & Voice** | Auto-caption + voice-over | ![Image1](Screenshots/Img_Cap_&_Voice_Generated.png) |

---

## 🛠️ Technologies Used

- Python
- YOLOv5 (Ultralytics)
- OpenCV
- PyTorch
- Google Colab (for BLIP and ElevenLabs integration)
- BLIP Model (`Salesforce/blip-image-captioning-base`)
- ElevenLabs TTS API
- Git & GitHub
- VS Code

---

## ⚙️ How It Works

### 🔹 Recipe Generator:
1. Takes fridge images as input.
2. YOLOv5 detects common food items (e.g., apple, banana, carrot).
3. Maps detections to pre-defined recipe suggestions.
4. Shows images for preview.
5. Outputs results to a text file `recipes_output.txt`.

### 🔹 Caption & Voice Generator:
1. Uploads an image via Google Colab.
2. BLIP generates a caption using a pre-trained model.
3. Caption is passed to ElevenLabs API.
4. Generates and plays voice output of the caption in the notebook.

---

## 📂 Folder Structure

📦Multi-Modal_Cross-Disciplinary-Project/   

├── AI_Recipe_Generator/

│----├── recipe_generator.py

│----├── yolov5/

│----├── runs/detect/exp*/Fp*.jpg

│----└── recipes_output.txt

├── Image Caption & Voice Generator.ipynb

├── Fp1.jpg / Fp2.jpg / Fp3.jpg

├── README.md ✅

├── LICENSE ✅

├── requirements.txt ✅

└── Project Report.docx
                                                                                                                                                                       
---

## 🧪 Installation & Run Instructions

### 🧑‍🍳 Recipe Generator

**#Step into the project folder**
- cd AI_Recipe_Generator

**#Activate virtual environment (if not already)**
- .\venv\Scripts\activate

**#Run the script**
- python recipe_generator.py

### 🖼️ Caption & Voice Generator

- Open Image Caption & Voice Generator.ipynb in Google Colab.
- Upload an image when prompted.
- Enter your ElevenLabs API key.
- Run the cells to get the caption and audio.

---

## 🔑 License

This project is open source and available under the MIT License.
This project is developed for academic and educational purposes only under the 2025 Summer Internship program at Sansoftech Services Pvt. Ltd..
It may be reused for learning and demonstration with proper attribution.
Do not use the ElevenLabs API key publicly or commercially.
See the **[LICENSE](LICENSE.txt)** file for further details.

---

## 👨‍💻 Contributions

- Developed and integrated YOLOv5-based ingredient detection.
- Mapped object detection results to relevant recipes.
- Implemented real-time image preview using OpenCV.
- Created Google Colab notebook for BLIP-based image captioning.
- Integrated ElevenLabs API for realistic voice generation.
- Structured and documented both mini-projects under one repository.
- Prepared university-compliant final report and ensured smooth GitHub deployment.

---

## 📅 Submission Info

- University: Guru Gobind Singh Indraprastha University

- Department: Bachelor of Computer Applications (BCA)

- Internship: Summer Internship 2025

- Project Title: Multi-Modal and Cross-Disciplinary Project

- Company: Sansoftech Services Private Limited

- Mentor: Santanoo Pattnaik (CEO)

- Faculty Advisor: Mr. Devanshu Dube

- Submission Date: 27th July, 2025

---

## 📷 Screenshots

### 📂[Screenshots Folder](Screenshots/) included in the repo demonstrate:
- Detection results
- Recipe suggestions
- Image previews
- Captions and voice generation in Colab

---

## requirements

### Common dependencies
- torch
- opencv-python
- Pillow
- transformers
- requests
- ipython

### Install using:
pip install -r **[requirements.txt](requirements.txt)**                
