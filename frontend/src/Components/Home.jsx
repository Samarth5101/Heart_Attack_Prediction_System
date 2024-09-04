/* eslint-disable no-unused-vars */
import React, { useEffect } from 'react';
import axios from 'axios';

export default function Home() {

  useEffect(() => {

  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h1 style={{ textAlign: 'center', marginBottom: '40px' }}>Welcome to Heart Attack Predictor</h1>
      <p style={{ fontSize: '18px', lineHeight: '1.6' }}>
      A heart attack occurs when there is a loss of blood supply to part of the heart muscle, 
       often due to a blockage in a nearby artery. Symptoms include pain in the chest that may spread. 
       It is a medical emergency that needs hospital treatment.A person who is experiencing a heart attack
       — or myocardial infarction — will feel pain in their chest and other parts of their body,
        as well as other symptoms, including nausea, sweating, and shortness of breath.
       Spotting the early signs of a heart attack and getting prompt treatment is crucial and can save a person’s life.
       Recognizing the importance of early detection and prevention, we present to you the Heart Attack Predictor – 
       a revolutionary tool aimed at assessing your risk of experiencing a heart attack.
    
        
      
      </p>
      <p style={{ fontSize: '18px', lineHeight: '1.6' }}>
       Understanding your risk of a heart attack empowers you to take proactive steps towards better cardiovascular health.
       Whether it's through lifestyle modifications, medical interventions, or regular monitoring, early 
       awareness can significantly improve outcomes and enhance quality of life.
       Join us on this journey towards a healthier future. 
       Let the Heart Attack Predictor be your partner in safeguarding your heart health.
        
        
        
      
        
        
        
      
      </p>
    </div>
  )
}