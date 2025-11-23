# Get Appointments for Window - UPDATED VERSION

# Try to get inputs
try:
    doc_id = doctor_id
except:
    try:
        doc_id = inputs['doctor_id']
    except:
        doc_id = "D001"

try:
    start = start_time
except:
    try:
        start = inputs['start_time']
    except:
        start = "2025-11-25T13:00"

try:
    end = end_time
except:
    try:
        end = inputs['end_time']
    except:
        end = "2025-11-25T17:00"

# SAME MOCK DATA
appointments = [
    {"appointment_id": "A001", "doctor_id": "D001", "patient_id": "P001", "patient_name": "John Carter", "start_time": "2025-11-25T10:00", "end_time": "2025-11-25T11:00", "status": "BOOKED"},
    {"appointment_id": "A002", "doctor_id": "D002", "patient_id": "P002", "patient_name": "Sarah Miller", "start_time": "2025-11-25T14:00", "end_time": "2025-11-25T15:00", "status": "BOOKED"},
    {"appointment_id": "A006", "doctor_id": "D001", "patient_id": "P002", "patient_name": "Sarah Miller", "start_time": "2025-11-25T14:00", "end_time": "2025-11-25T15:00", "status": "BOOKED"},
    {"appointment_id": "A007", "doctor_id": "D001", "patient_id": "P003", "patient_name": "Mrs. Rodriguez", "start_time": "2025-11-25T15:30", "end_time": "2025-11-25T16:30", "status": "BOOKED"}
]

# Get doctor name
doctor_names = {"D001": "Dr. John", "D002": "Dr. Emily"}
doctor_name = doctor_names.get(doc_id, "Unknown Doctor")

# Find affected appointments (simple string comparison)
affected = []
for apt in appointments:
    if apt["doctor_id"] == doc_id and apt["status"] == "BOOKED":
        # Check if appointment time overlaps with window
        if apt["start_time"] >= start and apt["start_time"] <= end:
            affected.append(apt)

# Format output
lines = ["=== AFFECTED APPOINTMENTS FOR " + doctor_name + " ==="]
lines.append("Time window: " + start + " to " + end)
lines.append("")

if not affected:
    lines.append("No appointments affected during this time window.")
else:
    lines.append(str(len(affected)) + " appointment(s) affected:")
    lines.append("")
    for apt in affected:
        lines.append("• Patient: " + apt["patient_name"] + " (" + apt["patient_id"] + ")")
        lines.append("  Appointment: " + apt["appointment_id"])
        lines.append("  Time: " + apt["start_time"] + " to " + apt["end_time"])
        lines.append("")

affected_appointments = "\n".join(lines)
