import streamlit as st
import pandas as pd
from datetime import date

from database import (
    create_table,
    add_patient,
    view_patients,
    update_patient,
    delete_patient
)

from model import predict_risk

# Create database table
create_table()

# App Title
st.title("Health Prediction Application")

# Sidebar Menu
menu = st.sidebar.selectbox(
    "Menu",
    [
        "Add Patient",
        "View Patients",
        "Update Patient",
        "Delete Patient"
    ]
)

# ==================================================
# ADD PATIENT
# ==================================================

if menu == "Add Patient":

    st.subheader("Add Patient")

    name = st.text_input("Full Name")

    dob = st.date_input("Date of Birth",
    min_value=date(1900, 1, 1),
    max_value=date.today()
)

    email = st.text_input("Email Address")

    glucose = st.number_input(
        "Glucose",
        min_value=0.0,
        format="%.2f"
    )

    haemoglobin = st.number_input(
        "Haemoglobin",
        min_value=0.0,
        format="%.2f"
    )

    cholesterol = st.number_input(
        "Cholesterol",
        min_value=0.0,
        format="%.2f"
    )

    # Generate Prediction

    if st.button("Generate Prediction"):

        if "@" not in email:

            st.error("Please enter a valid email address.")

        else:

            risk = predict_risk(
                glucose,
                haemoglobin,
                cholesterol
            )

            st.success(f"Predicted Risk Level: {risk}")

    # Save Patient
    if st.button("Save Patient"):

       if dob > date.today():

         st.error("Date of Birth cannot be in the future")

       elif "@" not in email:

         st.error("Please enter a valid email address")

       else:
            risk = predict_risk(
                glucose,
                haemoglobin,
                cholesterol
            )

            add_patient(
                name,
                str(dob),
                email,
                glucose,
                haemoglobin,
                cholesterol,
                risk
            )

            st.success("Patient Saved Successfully")


# ==================================================
# VIEW PATIENTS
# ==================================================

elif menu == "View Patients":

    st.subheader("Patient Records")

    data = view_patients()

    if data:

        df = pd.DataFrame(
            data,
            columns=[
                "ID",
                "Name",
                "DOB",
                "Email",
                "Glucose",
                "Haemoglobin",
                "Cholesterol",
                "Remarks"
            ]
        )

        st.dataframe(df)

    else:

        st.info("No patient records found.")


# ==================================================
# UPDATE PATIENT
# ==================================================

elif menu == "Update Patient":

    st.subheader("Update Patient")

    patient_id = st.number_input(
        "Patient ID",
        min_value=1,
        step=1
    )

    new_name = st.text_input("New Name")

    new_dob = st.date_input("New Date of Birth",
    min_value=date(1900, 1, 1),
    max_value=date.today()
    )

    new_email = st.text_input("New Email Address")

    new_glucose = st.number_input(
        "New Glucose",
        min_value=0.0,
        format="%.2f"
    )

    new_haemoglobin = st.number_input(
        "New Haemoglobin",
        min_value=0.0,
        format="%.2f"
    )

    new_cholesterol = st.number_input(
        "New Cholesterol",
        min_value=0.0,
        format="%.2f"
    )

    if st.button("Update Patient"):
        if new_dob > date.today():

          st.error("Date of Birth cannot be in the future")

        elif "@" not in new_email:

          st.error("Please enter a valid email address")

        else:

             risk = predict_risk(
             new_glucose,
             new_haemoglobin,
             new_cholesterol
             )

             update_patient(
             patient_id,
             new_name,
             str(new_dob),
             new_email,
             new_glucose,
             new_haemoglobin,
             new_cholesterol,
             risk
             )

             st.success("Patient Updated Successfully")


# ==================================================
# DELETE PATIENT
# ==================================================

elif menu == "Delete Patient":

    st.subheader("Delete Patient")

    patient_id = st.number_input(
        "Patient ID to Delete",
        min_value=1,
        step=1
    )

    if st.button("Delete Patient"):

        delete_patient(patient_id)

        st.success("Patient Deleted Successfully")