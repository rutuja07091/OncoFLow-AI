# Propose Schedule Changes

# Mock data
patients = [
    {"patient_id": "P001", "name": "John Carter", "risk_score": 4, "risk_level": "HIGH"},
    {"patient_id": "P002", "name": "Sarah Miller", "risk_score": 2, "risk_level": "MEDIUM"},
    {"patient_id": "P003", "name": "Mrs. Rodriguez", "risk_score": 4, "risk_level": "HIGH"}
]

available_slots = [
    {"slot_id": "A003", "doctor_id": "D001", "start_time": "2025-11-26T14:00"},
    {"slot_id": "A004", "doctor_id": "D002", "start_time": "2025-11-26T10:00"},
    {"slot_id": "A005", "doctor_id": "D001", "start_time": "2025-11-27T09:00"}
]

# Sort patients by risk score (highest first)
sorted_patients = sorted(patients, key=lambda x: x["risk_score"], reverse=True)

# Assign slots to highest-risk patients first
changes = []
for i, patient in enumerate(sorted_patients):
    if i < len(available_slots):
        slot = available_slots[i]
        changes.append({
            "patient_id": patient["patient_id"],
            "patient_name": patient["name"],
            "risk_level": patient["risk_level"],
            "assigned_slot": slot["slot_id"],
            "doctor_id": slot["doctor_id"],
            "time": slot["start_time"]
        })

proposed_changes = str(changes)
summary = str(len(changes)) + " high-priority patients scheduled, " + str(len(sorted_patients) - len(changes)) + " still need slots"