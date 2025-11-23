# Get Doctor Schedule - UPDATED VERSION

# Try to get input
try:
    doc_id = doctor_id
except:
    try:
        doc_id = inputs['doctor_id']
    except:
        doc_id = "D001"

# SAME MOCK DATA AS MAIN TOOL
appointments = [
    {"appointment_id": "A001", "doctor_id": "D001", "patient_id": "P001", "patient_name": "John Carter", "start_time": "2025-11-25T10:00", "end_time": "2025-11-25T11:00", "status": "BOOKED"},
    {"appointment_id": "A002", "doctor_id": "D002", "patient_id": "P002", "patient_name": "Sarah Miller", "start_time": "2025-11-25T14:00", "end_time": "2025-11-25T15:00", "status": "BOOKED"},
    {"appointment_id": "A003", "doctor_id": "D001", "patient_id": None, "patient_name": None, "start_time": "2025-11-26T14:00", "end_time": "2025-11-26T15:00", "status": "AVAILABLE"},
    {"appointment_id": "A004", "doctor_id": "D002", "patient_id": None, "patient_name": None, "start_time": "2025-11-26T10:00", "end_time": "2025-11-26T11:00", "status": "AVAILABLE"},
    {"appointment_id": "A005", "doctor_id": "D001", "patient_id": None, "patient_name": None, "start_time": "2025-11-27T09:00", "end_time": "2025-11-27T10:00", "status": "AVAILABLE"}
]

# Get doctor name
doctor_names = {
    "D001": "Dr. John",
    "D002": "Dr. Emily"
}
doctor_name = doctor_names.get(doc_id, "Unknown Doctor")

# Filter appointments for this doctor
doctor_schedule = []
for apt in appointments:
    if apt["doctor_id"] == doc_id:
        doctor_schedule.append(apt)

# Format output nicely
lines = ["=== SCHEDULE FOR " + doctor_name + " (" + doc_id + ") ==="]
lines.append("")

if not doctor_schedule:
    lines.append("No appointments found.")
else:
    for apt in doctor_schedule:
        if apt["status"] == "BOOKED":
            patient_info = apt["patient_name"] + " (" + apt["patient_id"] + ")"
        else:
            patient_info = "AVAILABLE SLOT"
        
        lines.append("• Slot " + apt["appointment_id"] + ": " + apt["start_time"] + " to " + apt["end_time"])
        lines.append("  Status: " + apt["status"] + " | Patient: " + patient_info)
        lines.append("")

schedule = "\n".join(lines)
schedule