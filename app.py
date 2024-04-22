from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib  # for loading the model
app = Flask(__name__)
model = joblib.load('model.pkl')
import spacy
l=['Acne', 'Arthritis', 'Bronchial Asthma', 'Cervical spondylosis',
       'Chicken pox', 'Common Cold', 'Dengue', 'Dimorphic Hemorrhoids',
       'Fungal infection', 'Hypertension', 'Impetigo', 'Jaundice',
       'Malaria', 'Migraine', 'Pneumonia', 'Psoriasis', 'Typhoid',
       'Varicose Veins', 'allergy', 'diabetes', 'drug reaction',
       'gastroesophageal reflux disease', 'peptic ulcer disease',
       'urinary tract infection']
dermatology = ['acne', 'psoriasis', 'fungal infection', 'impetigo']
orthopedics = ['arthritis', 'cervical spondylosis', 'varicose veins']
internal_medicine = ['hypertension', 'diabetes', 'jaundice', 'migraine', 'typhoid', 'drug reaction']
infectious_diseases = ['chicken pox', 'dengue', 'malaria', 'pneumonia', 'urinary tract infection']
respiratory_medicine = ['bronchial asthma', 'common cold', 'gastroesophageal reflux disease', 'peptic ulcer disease', 'allergy']
nlp = spacy.load("en_core_web_lg")
tfidf=joblib.load('a.pkl')
# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling form submission
@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']
    
        

        
    # Assuming here you have some function or code to process user input
    # and get the result
    disease =l[ model.predict(process_input(user_input))[0]].lower()
    if disease in dermatology:
            result= "Dermatology"
    elif disease in orthopedics:
        result= "Orthopedics"
    elif disease in internal_medicine:
        result="Internal Medicine"
    elif disease in infectious_diseases:
        result= "Infectious Diseases"
    elif disease in respiratory_medicine:
        result= "Respiratory Medicine"
    else:
        result= "General medicine"
    
    return render_template(f'{result.lower().replace(" ", "_")}.html')

# Dummy function to simulate processing of user input
def process_input(user_input):
    list =[]
    for token in nlp(user_input):
        if token.is_space or token.is_punct:
            continue
        list.append(token.lemma_)
    text=' '.join(list)
    # tfidf_vectorizer = TfidfVectorizer()
    text_transformed = tfidf.transform([text])
    return text_transformed

if __name__ == '__main__':
    app.run(debug=True)

