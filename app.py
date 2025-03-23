import streamlit as st
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import base64

# Title of the Streamlit app
st.title("Acute Lymphoblastic Leukemia Detection System")

# Upload the image
uploaded_file = st.file_uploader("Choose an image...", type="jpg")
st.write(uploaded_file)
# Load the model (replace with the actual path to your model)
# model = load_model('path_to_your_model.h5')

if uploaded_file is not None:
    # Display the uploaded image
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image.', use_container_width=True)
    
    # Convert the image to array
    img = img.resize((224, 224))  # Resize the image if necessary
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    
    # Simulate prediction (replace this with actual model prediction)
    val = np.array([[0.85]])  # Replace with: val = model.predict(images)
    prediction_percentage = round(float(val[0][0]) * 100, 2)

    # Prepare report text based on prediction
    report_text = ""
    if prediction_percentage < 50:
        status = " Not Affected"
        report_text += f"""
        Acute Lymphoblastic Leukemia Detection Report

        Prediction Result: {status}
        Detection Probability: {100 - prediction_percentage:.2f}%
        Condition Summary: No significant signs of Acute Lymphoblastic Leukemia (ALL) detected.

        Recommendations:
        - Maintain healthy lifestyle
        - Regular screenings
        - Balanced diet

        Treatment Plan: None required
        Medicines: None
        """
    elif 50 <= prediction_percentage < 70:
        status = " Mild Risk"
        report_text += f"""
        Acute Lymphoblastic Leukemia Detection Report

        Prediction Result: {status}
        Detection Probability: {prediction_percentage:.2f}%
        Condition Summary: Early indicators of leukemic presence. Clinical follow-up advised.

        Recommendations:
        - Consult a hematologist
        - CBC, Bone Marrow Biopsy
        - Stress-free lifestyle

        Treatment Plan:
        - Observation
        - Preventive supportive care

        Medicines:
        - Multivitamins
        - Corticosteroids (if advised)
        """
    elif 70 <= prediction_percentage < 90:
        status = " Moderate to High Risk"
        report_text += f"""
        Acute Lymphoblastic Leukemia Detection Report

        Prediction Result: {status}
        Detection Probability: {prediction_percentage:.2f}%
        Condition Summary: Strong likelihood of ALL. Immediate consultation needed.

        Recommendations:
        - Urgent tests: CBC, Flow Cytometry
        - Start induction therapy

        Treatment Plan:
        - Induction Chemotherapy
        - Monitoring
        - Consolidation phase

        Medicines:
        - Vincristine
        - Methotrexate
        - Doxorubicin
        - Asparaginase
        """
    else:
        status = " Critical Risk"
        report_text += f"""
        Acute Lymphoblastic Leukemia Detection Report

        Prediction Result: {status}
        Detection Probability: {prediction_percentage:.2f}%
        Condition Summary: Severe indicators of ALL detected. Emergency care recommended.

        Recommendations:
        - Immediate hospitalization
        - Confirmatory tests

        Treatment Plan:
        - Induction Chemotherapy
        - Maintenance therapy
        - Stem Cell Transplantation

        Medicines:
        - Vincristine
        - Dexamethasone
        - Asparaginase
        - Cyclophosphamide
        - Cytarabine
        """

    # Display report
    st.markdown("---")
    st.subheader(" Diagnostic Report")
    st.text_area("Full Report:", report_text, height=400)

    # PRINT BUTTON (opens browser print dialog)
    st.markdown("""
        <button onclick="window.print()" style="padding:10px 20px; background-color:#4CAF50; color:white; border:none; border-radius:8px; font-size:16px;">
            🖨️ Print Report
        </button>
    """, unsafe_allow_html=True)

    # DOWNLOAD BUTTON (as .txt file)
    def generate_download_link(text, filename):
        b64 = base64.b64encode(text.encode()).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="{filename}"> Download Report (.txt)</a>'
        return href

    st.markdown(generate_download_link(report_text, "Leukemia_Report.txt"), unsafe_allow_html=True)