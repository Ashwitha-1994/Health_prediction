import sqlite3
def create_table():

    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        dob TEXT,
        email TEXT,
        glucose REAL,
        haemoglobin REAL,
        cholesterol REAL,
        remarks TEXT
    )
    """)

    conn.commit()
    conn.close()

# Add patient
def add_patient(name,dob,email,glucose,haemoglobin,cholesterol,remarks):

    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO patients
    (full_name,dob,email,glucose,haemoglobin,cholesterol,remarks)
    VALUES(?,?,?,?,?,?,?)
    """,(name,dob,email,glucose,haemoglobin,cholesterol,remarks))

    conn.commit()
    conn.close()
# View all patients
def view_patients():

    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients")

    data = cursor.fetchall()

    conn.close()

    return data
# Delete patient
def delete_patient(patient_id):

    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM patients WHERE id=?",(patient_id,))

    conn.commit()
    conn.close()
# Update patient
def update_patient(patient_id,name,dob,email,glucose,haemoglobin,cholesterol    
,remarks):

    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE patients SET
    full_name=?,
    dob=?,
    email=?,
    glucose=?,
    haemoglobin=?,
    cholesterol=?,
    remarks=?
    WHERE id=?
    """,(name,dob,email,glucose,haemoglobin,cholesterol,remarks,patient_id))

    conn.commit()
    conn.close()    