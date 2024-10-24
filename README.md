

# Third Eye for the Blind

**Third Eye for the Blind** is a capstone project aimed at providing assistance to visually impaired individuals by using advanced deep learning, computer vision, and voice recognition technologies. The system captures the user's environment through a camera, processes the visual data using real-time object detection and face recognition, and provides audio feedback to the user via a voice assistant named Nancy. This solution empowers visually impaired individuals by enhancing their situational awareness and independence.

## Guided By
Under the Guidance of:

  **Prof. Bolem Sai Chandana**
 
Project Developed by:

- **Jinka Chandra Kiran** (20BCI7045)
- **Kokkula Lokesh** (20BCR7142)
- **Tatigunta Bhaviteja Reddy** (20BCI7053)
- **Arab Shahansha**(20BCI7039)
![image](https://github.com/user-attachments/assets/01ae09a5-a4ae-4d15-bab8-af5dc2989577)
![image](https://github.com/user-attachments/assets/938300eb-6173-42c0-ad4f-04516a16f541)
![image](https://github.com/user-attachments/assets/883877e8-39f0-44bf-b245-429fa115acfd)
![image](https://github.com/user-attachments/assets/f6578549-e4e6-4bc7-ac00-2e9c93090f74)

## Features

- **Real-time Object Detection:** Utilizes YOLO (You Only Look Once) for recognizing objects in the environment.
- **Face Recognition:** Employs OpenCV for recognizing and identifying faces, aiding social interactions.
- **Text Recognition:** Uses OCR (Optical Character Recognition) to read text from images and convey it audibly.
- **Speech Recognition:** Integrated with VOSK for converting speech to text for user interaction.
- **Voice Assistant (Nancy):** Provides auditory feedback, narrating surroundings, time, date, and object identification.
- **Multilingual Support:** Nancy supports both English and Hindi, making it more accessible for a diverse user base.

## Technologies Used

- **Hardware:** ESP-32 microcontroller with a 2-megapixel camera, microphone for audio input, and a speaker for audio output.
- **Software:**
  - **YOLO (You Only Look Once):** For real-time object detection.
  - **OpenCV:** For face recognition.
  - **VOSK:** For offline speech recognition.
  - **OCR:** For text recognition from images.
  - **PyAudio:** For generating audio feedback.
  - **Languages Supported:** English and Hindi.

## System Architecture

The project integrates hardware and software to create a robust and user-friendly interface for visually impaired individuals:
1. **ESP-32 and Camera:** Captures real-time images of the user's environment.
2. **YOLO & OpenCV:** Detects objects and recognizes faces within the captured images.
3. **VOSK & PyAudio:** Converts user commands into text and generates auditory feedback.
4. **Nancy (Voice Assistant):** Provides a seamless interaction between the user and the environment through voice communication.
![image](https://github.com/user-attachments/assets/3618fa60-86ae-4166-b725-e2dd2af4d8dd)


## Setup Instructions

### Prerequisites

1. **Hardware Requirements:**
   - ESP-32 microcontroller
   - 2-megapixel camera module
   - Microphone and speaker for audio input/output

2. **Software Requirements:**
   - Python 3.x
   - Required libraries: YOLO, OpenCV, VOSK, PyAudio, OCR

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/third-eye-for-the-blind.git
   cd third-eye-for-the-blind
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the ESP-32 with the camera and microphone as per the hardware instructions.

4. Run the program:
   ```bash
   python main.py
   ```

### Usage

- Power on the ESP-32 device to start capturing the environment.
- Nancy will provide real-time feedback by narrating the detected objects, faces, and text.
- Speak commands to interact with the system using the integrated speech recognition.

## Future Enhancements

- **Improved Object Detection Models:** Enhance object recognition with additional deep learning models.
- **Indoor & Outdoor Navigation:** Incorporate navigation support for diverse environments.
- **Additional Language Support:** Expand support for more languages to cater to a global audience.
- **Wearable Integration:** Integrate with wearable devices like smart glasses for more seamless interaction.

## Contributing

We welcome contributions to this project. Please follow the standard GitHub process:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Contact

For any inquiries or support, contact the project maintainers:
- **Jinka Chandra Kiran** (chandrakiran.20bci7045@vitap.ac.in)
- **Kokkula Lokesh** (lokesh.20bcr7142@vitap.ac.in)
- **Tatigunta Bhaviteja Reddy** (bhaviteja.20bci7053@vitap.ac.in)
## For More Details 
[Download the PDF here](https://drive.google.com/file/d/1akwVFR-1NcGCSgvYOOBSV8feVQkH2oFc/view?usp=sharing)

## Achievements:
<h3>FALL SEM 2022-2023 : Second Prize Among 500 Engineering Clinics </h3>

![image](https://github.com/user-attachments/assets/0bd7b6e4-aca1-40d8-90f6-ca632f1a6110)

<h3>WIN SEM 2022-2023 : The Most Socially Relevant Project in  Engineering Clinics </h3>


![image](https://github.com/user-attachments/assets/c391f543-2c31-4b7f-83e9-eed18059a685)





