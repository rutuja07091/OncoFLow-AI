# OncoFlow Mock Data - EXPLICIT NAME FORMAT

# Try to get data_type
input_type = None
try:
    input_type = data_type
except NameError:
    try:
        input_type = inputs['data_type']
    except:
        input_type = "unknown"

# Mock data
mock_data = {
    "doctors": [
        {"doctor_id": "D001", "doctor_name": "Dr. John", "unavailable_days": ["Monday", "Friday"], "hard_constraints": {"no_nights": True, "no_weekends": True}},
        {"doctor_id": "D002", "doctor_name": "Dr. Emily", "unavailable_days": ["Wednesday"], "hard_constraints": {"no_nights": False, "no_weekends": True}}
    ],
    
    "patients": [
        {"patient_id": "P001", "name": "John Carter", "treatment_type": "CHEMO", "ideal_next_date": "2025-11-25", "window_start": "2025-11-24", "window_end": "2025-11-28", "preferences": {"no_mornings": False, "no_fridays": False}},
        {"patient_id": "P002", "name": "Sarah Miller", "treatment_type": "RADIATION", "ideal_next_date": "2025-11-26", "window_start": "2025-11-25", "window_end": "2025-11-29", "preferences": {"no_mornings": True, "no_fridays": True}},
        {"patient_id": "P003", "name": "Mrs. Rodriguez", "treatment_type": "CHEMO", "ideal_next_date": "2025-11-27", "window_start": "2025-11-25", "window_end": "2025-11-30", "preferences": {"no_mornings": False, "no_fridays": False}}
    ],
    
    "appointments": [
        {"appointment_id": "A001", "doctor_id": "D001", "patient_id": "P001", "start_time": "2025-11-25T10:00", "end_time": "2025-11-25T11:00", "status": "BOOKED"},
        {"appointment_id": "A002", "doctor_id": "D002", "patient_id": "P002", "start_time": "2025-11-25T14:00", "end_time": "2025-11-25T15:00", "status": "BOOKED"},
        {"appointment_id": "A003", "doctor_id": "D001", "patient_id": None, "start_time": "2025-11-26T14:00", "end_time": "2025-11-26T15:00", "status": "AVAILABLE"},
        {"appointment_id": "A004", "doctor_id": "D002", "patient_id": None, "start_time": "2025-11-26T10:00", "end_time": "2025-11-26T11:00", "status": "AVAILABLE"}
    ],
    
    "preferences": [
        {"patient_id": "P001", "learned_preferences": {}}
    ]
}

# Get input type
input_type_clean = str(input_type).lower().strip() if input_type else "none"

# Match data type
if "doctor" in input_type_clean:
    result = mock_data["doctors"]
    # SUPER EXPLICIT FORMAT - IMPOSSIBLE TO MISINTERPRET
    lines = ["=== DOCTOR DATABASE RECORDS ==="]
    for d in result:
        lines.append("")
        lines.append("DOCTOR RECORD:")
        lines.append("  DOCTOR_ID: " + d["doctor_id"])
        lines.append("  FULL_NAME: " + d["doctor_name"] + " (THIS IS THE EXACT NAME - DO NOT CHANGE)")
        lines.append("  UNAVAILABLE_DAYS: " + ", ".join(d.get("unavailable_days", [])))
        lines.append("  NO_NIGHTS: " + str(d["hard_constraints"]["no_nights"]))
        lines.append("  NO_WEEKENDS: " + str(d["hard_constraints"]["no_weekends"]))
    lines.append("")
    lines.append("IMPORTANT: Use the FULL_NAME exactly as written above. Do NOT invent different names.")
    data = "\n".join(lines)
    
elif "patient" in input_type_clean:
    result = mock_data["patients"]
    lines = ["=== PATIENT DATABASE RECORDS ==="]
    for p in result:
        lines.append("")
        lines.append("PATIENT RECORD:")
        lines.append("  PATIENT_ID: " + p["patient_id"])
        lines.append("  FULL_NAME: " + p["name"] + " (THIS IS THE EXACT NAME - DO NOT CHANGE)")
        lines.append("  TREATMENT_TYPE: " + p["treatment_type"])
        lines.append("  TREATMENT_WINDOW: " + p["window_start"] + " to " + p["window_end"])
    lines.append("")
    lines.append("IMPORTANT: Use patient names exactly as written above.")
    data = "\n".join(lines)
    
elif "appointment" in input_type_clean:
    result = mock_data["appointments"]
    lines = ["=== APPOINTMENT RECORDS ==="]
    for a in result:
        patient = "UNASSIGNED" if a["patient_id"] is None else a["patient_id"]
        lines.append("SLOT_ID: " + a["appointment_id"] + " | DOCTOR: " + a["doctor_id"] + " | PATIENT: " + patient + " | TIME: " + a["start_time"] + " to " + a["end_time"] + " | STATUS: " + a["status"])
    data = "\n".join(lines)
    
elif "preference" in input_type_clean:
    result = mock_data["preferences"]
    data = "PREFERENCES: " + str(result)
    
else:
    data = "ERROR: Invalid data type requested. Available types: doctors, patients, appointments, preferences"