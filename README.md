# IntellAI_Cam
#### AI-Powered Surveillance Software

IntellAI_Cam is a CCTV-style camera system which uses [OpenCV](https://pypi.org/project/opencv-python/) and [Deepface](https://github.com/serengil/deepface) to detect and analyse human faces in real time. Analysis results are saved to an SQLite database and are easily searchable through the provided GUI, which also allows running the individual models and displays live analysis info as it is processed.

This system was created to assist in comparing the efficiency and accuracy differences between two possible face recognition and analysis implementations, and as such is not meant to be fully-featured nor used for any real workload. 

### Installation
> This branch only supports analysis using the CPU. For GPU support using **WSL2 and Tensorflow with CUDA support**, use the [wsl](https://github.com/MGBrebu/intellai_cam/tree/wsl) branch. Make sure to follow the relevant (and extensive) installation instructions for the WSL branch.

> You **must** have ***Python 3.12*** installed and set as the current interpreter (for this project or globally). Python 3.13 has issues with the TensorFlow packages required.

1. Clone the repository
```
git clone https://github.com/MGBrebu/intellai_cam.git
cd intellai_cam
```

2. *(OPTIONAL, but highly recommended)*, create a virtual environment
```
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```
pip install -r requirements.txt
```

### Usage
>The system can be used either through the provided GUI utility, or an individual model can be run manually.

**Recommended** | Run the GUI
```
python intellai_gui.py
```
Run an individual model
```
python intellai_single.py
OR
python intellai_hybrid.py
```


-----
Authored By **Mario G. Brebu**

`Created and submitted as a final year project and thesis to Technological University Dublin in partial fulfilment of the requirements for the degree of Bachelor of Science in Computing in Digital Forensics & Cyber Security`
