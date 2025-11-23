# Find Available Slots

# Try to get input
try:
    doc_id = doctor_id
except:
    try:
        doc_id = inputs['doctor_id']
    except:
        doc_id = "D001"

# Mock appointments
appointments = [
    {"appointment_id": "A001", "doctor_id": "D001", "patient_id": "P001", "start_time": "2025-11-25T10:00", "end_time": "2025-11-25T11:00", "status": "BOOKED"},
    {"appointment_id": "A002", "doctor_id": "D002", "patient_id": "P002", "start_time": "2025-11-25T14:00", "end_time": "2025-11-25T15:00", "status": "BOOKED"},
    {"appointment_id": "A003", "doctor_id": "D001", "patient_id": None, "start_time": "2025-11-26T14:00", "end_time": "2025-11-26T15:00", "status": "AVAILABLE"},
    {"appointment_id": "A004", "doctor_id": "D002", "patient_id": None, "start_time": "2025-11-26T10:00", "end_time": "2025-11-26T11:00", "status": "AVAILABLE"},
    {"appointment_id": "A005", "doctor_id": "D001", "patient_id": None, "start_time": "2025-11-27T09:00", "end_time": "2025-11-27T10:00", "status": "AVAILABLE"}
]

# Find available slots for this doctor
slots = []
for apt in appointments:
    if apt["doctor_id"] == doc_id and apt["status"] == "AVAILABLE":
        slots.append({
            "slot_id": apt["appointment_id"],
            "start_time": apt["start_time"],
            "end_time": apt["end_time"]
        })

available_slots = str(slots)