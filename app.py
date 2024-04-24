from flask import Flask, render_template, request, url_for
import mysql.connector
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
def get_database_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='PASSWORD',
        database='doc'
    )
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
    
    dermatology_doctors = get_doctors_by_specialisation(result)
    print(dermatology_doctors)
    return render_template(f'{result.lower().replace(" ", "_")}.html', dermatology_doctors=dermatology_doctors)
@app.route('/register-doctor', methods=['GET', 'POST'])
def register_doctor():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        location = request.form['location']
        contact = request.form['contact']
        timings = request.form['timings']
        rating = request.form['rating']
        specialisation = request.form['specialisation']
        
        # Insert form data into the database
        connection = get_database_connection()
        cursor = connection.cursor()
        query = "INSERT INTO doctors (name, location, contact, timings, rating, specialisation) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (name, location, contact, timings, rating, specialisation))
        connection.commit()
        connection.close()
        
        # Redirect to homepage after registration
        return render_template('index.html')
    else:
        return render_template('register-doctor.html')
def get_doctors_by_specialisation(specialisation):
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='PASSWORD',
        database='doc'
    )

    # Execute the query to fetch doctors
    cursor = connection.cursor()
    query = "SELECT name, location, contact, timings, rating FROM doctors WHERE specialisation = %s"
    cursor.execute(query, (specialisation,))
    doctors = cursor.fetchall()

    # Close the database connection
    cursor.close()
    connection.close()

    return doctors

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

