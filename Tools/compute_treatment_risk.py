# Compute Treatment Risk

# Try to get input
try:
    pid = patient_id
except:
    try:
        pid = inputs['patient_id']
    except:
        pid = "P001"

# Mock today's date
today = "2025-11-23"

# Mock patients
patients = [
    {"patient_id": "P001", "name": "John Carter", "treatment_type": "CHEMO", "window_start": "2025-11-24", "window_end": "2025-11-28"},
    {"patient_id": "P002", "name": "Sarah Miller", "treatment_type": "RADIATION", "window_start": "2025-11-25", "window_end": "2025-11-29"},
    {"patient_id": "P003", "name": "Mrs. Rodriguez", "treatment_type": "CHEMO", "window_start": "2025-11-25", "window_end": "2025-11-30"}
]

# Find patient
patient = None
for p in patients:
    if p["patient_id"] == pid:
        patient = p
        break

if not patient:
    risk_level = "UNKNOWN"
    risk_score = "0"
    reason = "Patient not found"
else:
    score = 0
    reasons = []
    
    # Overdue check
    if today > patient["window_end"]:
        score += 3
        reasons.append("OVERDUE")
    # Within 2 days of end
    elif patient["window_end"] <= "2025-11-25":
        score += 3
        reasons.append("CRITICAL - near window end")
    # Within window
    elif today >= patient["window_start"]:
        score += 2
        reasons.append("Active window")
    else:
        score += 1
        reasons.append("Early window")
    
    # CHEMO priority
    if patient["treatment_type"] == "CHEMO":
        score += 1
        reasons.append("CHEMO priority")
    
    # Classify
    if score >= 4:
        risk_level = "HIGH"
    elif score >= 2:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"
    
    risk_score = str(score)
    reason = " | ".join(reasons)