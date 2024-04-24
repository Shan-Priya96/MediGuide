# MediGuide

MediGuide is a web-based application designed to assist users in finding the right medical specialist based on their symptoms. Leveraging machine learning algorithms and a comprehensive dataset, the app accurately predicts potential diseases and recommends corresponding specialists.

## Features

1. **Simple Interface**: Patients can input their symptoms into the simple web interface.
2. **Personalised Recommendations**: Patients receive recommendations of medical specialists based on the input symptoms.
3. **Doctor Details**: Patients can view detailed information about recommended doctors, including their names, location, contact information, timings, and ratings and can thus find the most relavent healthcare providers.
4. **Quick Decision-making**: Patients can make informed decisions about their healthcare provider quickly and efficiently.
5. **Accurate Disease Prediction**: The AI model boasts high accuracy, with predictions achieving around 98.33% accuracy. This ensures that patients receive precise recommendations from medical specialists based on their symptoms, leading to more effective healthcare outcomes.

## Installation
1. Clone the repository:
 git clone https://github.com/Shan-Priya96/MediGuide.git 
 2. Install dependencies:
pip install -r requirements.txt
3. Run the application:
 python app.py
4. Access the application in your web browser at `http://localhost:5000`.

## Usage

### For Patients

1. Navigate to the web interface.
2. Enter your symptoms into the provided form.
3. Submit the form to receive recommendations for medical specialists.
4. Review the recommendations and contact the appropriate specialist for further consultation or treatment.

### For Doctors

1. Register as a doctor on the website by providing necessary details such as name, contact information, and specialization.

## Dataset
The dataset is collected from an already existing public database available on Kaggle. Available at: https://www.kaggle.com/datasets/niyarrbarman/symptom2disease

## Future Enhancements
- Incorporate real patient data from hospitals to improve model accuracy.
- Expand the dataset to include a wider range of diseases and symptoms.
- Implement additional features such as user authentication, dashboard, speech to text assistant etc.

