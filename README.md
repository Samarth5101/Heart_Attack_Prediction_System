
# Heart Attack Prediction System

![Banner](https://github.com/Samarth5101/Heart_Attack_Prediction_System/blob/fc3bfabc688988f2370942ad5e338b11ac1d53da/banner.jpg)

<h2>Table of Contents</h2>

Introduction  
Project Structure  
Installation  
Usage    
Model Explanation  
Results  
Future Improvements  
Contributors  

## Introduction
The Heart Attack Prediction System is a machine learning project designed to predict the likelihood of a heart attack based on several health parameters like cholesterol level, blood pressure (Systolic & Diastolic), heart rate, gender, blood sugar, CK-MB, troponin, and age. The model was developed using Python, and it utilizes logistic regression and random forest classifiers. 

## Project Structure

<pre>
Heart_Attack_Prediction_System/
├── <strong>data/</strong>
│   ├── heart.csv
├── <strong>notebooks/</strong>
│   ├── EDA.ipynb
│   ├── model_training.ipynb
├── <strong>src/</strong>
│   ├── model.py
│   ├── preprocess.py
│   └── utils.py
├── <strong>app/</strong>
│   ├── app.py
│   └── templates/
├── <strong>requirements.txt</strong>
└── <strong>README.md</strong>
</pre>

## Instalation

Pre-requisite: Git Bash, download latest version of git bash from; https://git-scm.com/downloads

Follow these steps to set up the project on your local machine, try these commands to put on GitBash:

1. Clone the repository:
   git clone https://github.com/Samarth5101/Heart_Attack_Prediction_System.git

2. Navigate to the project directory:
   cd Heart_Attack_Prediction_System

3. Install the required Python packages:
   pip install -r requirements.txt

4. To run the Flask app locally:
   python app/app.py

## Usage

After, Installing this repository and poking gitbash you should run some commands on your terminal of your local IDE, but before this please add this whole project on your local IDE.

Try these commands on your loacal IDE : 

1. **For Backend**  
   1.1 Open up a fresh terminal and type:  
       1.1.1 `cd backend`  
       1.1.2 `nodemon index.js`

2. **For Frontend**  
   2.1 Open up a fresh terminal again and type:  
       2.1.1 `cd frontend`  
       2.1.2 `npm run dev`

3. **For Flask server**  
   3.1 Open up a fresh terminal again and:  
       3.1.1 Run the code of `flaskserver.py`

4. **For live site**  
   4.1 Navigate back to "node frontend"  
   4.2 Focusing on the same terminal frontend's output, find your Local Development Server URL         or localhost.  
   4.3 Click on the Local Development Server URL while pressing `ctrl`. Displayed as:  
       `http://localhost:XXXX/`  
   4.4 This allows you to test and view your application in a browser before deploying it to a         live server.

Conclusion: This whole process will land you at the home page of this project. Navigate to Predict page, enter your details and boom 💥 here is your answer or a prediction that you might have or not have heart attack on the same health conditions.

## Model Explanation

<h3> Logistic Regression </h3>
The compilation of data is an essential stage in the logistic regression prediction of heart 
attacks. For the model to work well, preprocessing characteristics like age, blood 
pressure, and cholesterol levels is necessary. To properly assess the performance of the 
model, the prepared data is divided into training and testing sets. Subsequently, the model 
is trained using logistic regression to determine the correlation between these attributes 
and the risk of a heart attack. Metrics such as accuracy are computed to measure the 
predictive power of the model after it has been trained on the test set. To enhance 
performance and develop a trustworthy heart attack prediction system, model 
modifications or feature engineering can be required. 

The logistic function is of the form: p(x)={1/1+e^{-(x )} 

The Flask web framework is used in the creation of the web application. Either the 
physician or the patient can log in to the system, enter the patient's health information, 
and press the "predict" button. For prediction, the provided input is compared with the
curent model. The user is shown the outcome once the forecast has been completed. 

## Result 




