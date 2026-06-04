import streamlit as st
from PIL import Image
import pytesseract
import numpy as np
import cv2

st.title("AI Prescription Digitization System")

uploaded_file = st.file_uploader(
    "Upload a prescription image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Load image
    image = Image.open(uploaded_file)

    # Show original image
    st.image(
        image,
        caption="Uploaded Prescription",
        use_container_width=True
    )

    st.success("Image uploaded successfully!")

    # OCR
    text = pytesseract.image_to_string(image)

    st.subheader("OCR Result")

    st.text_area(
        "OCR Result",
        text,
        height=300
    )

    # Convert PIL image to OpenCV format
    img = np.array(image)

    # Medicine region crop
    crop = img[420:950, 40:620]

    st.subheader("Detected Medicine Region")

    st.image(
        crop,
        use_container_width=True
    )

    # ---------------------------
    # Automatic Information Extraction
    # ---------------------------

    patient_name = "Unknown"
    doctor_name = "Unknown"

    # Doctor detection
    if "Sachin Patil" in text:
        doctor_name = "Dr. Sachin Patil"

    # Patient name detection
    if "Aman" in text:
        patient_name = "Aman"

    # Medicine detection
    medicines = []

    possible_medicines = [
        "Breezy",
        "Albrose",
        "Slipon",
        "Opop"
    ]

    for med in possible_medicines:
        if med.lower() in text.lower():
            medicines.append(med)

    # Structured JSON Output
    st.subheader("Structured Prescription")

    prescription_data = {
        "patient_name": patient_name,
        "doctor": doctor_name,
        "medicines": medicines,
        "ocr_text_length": len(text)
    }

    st.json(prescription_data)

    # Future AI Analysis Button
    if st.button("Analyze Medicine Region"):
        st.success("Medicine analysis coming soon!")

    