# Get Doctor Constraints - UPDATED VERSION

# Try to get input
try:
    doc_id = doctor_id
except:
    try:
        doc_id = inputs['doctor_id']
    except:
        doc_id = "D001"

# SAME MOCK DATA AS MAIN TOOL
doctors = [
    {"doctor_id": "D001", "doctor_name": "Dr. John", "unavailable_days": ["Monday", "Friday"], "hard_constraints": {"no_nights": True, "no_weekends": True}},
    {"doctor_id": "D002", "doctor_name": "Dr. Emily", "unavailable_days": ["Wednesday"], "hard_constraints": {"no_nights": False, "no_weekends": True}}
]

# Find the doctor
doctor = None
for d in doctors:
    if d["doctor_id"] == doc_id:
        doctor = d
        break

if doctor:
    # Format constraints nicely
    lines = ["=== SCHEDULING CONSTRAINTS FOR " + doctor["doctor_name"] + " (" + doctor["doctor_id"] + ") ==="]
    lines.append("")
    
    # Unavailable days
    if doctor["unavailable_days"]:
        lines.append("UNAVAILABLE DAYS:")
        for day in doctor["unavailable_days"]:
            lines.append("  • " + day)
        lines.append("")
    
    # Hard constraints
    lines.append("HARD CONSTRAINTS:")
    if doctor["hard_constraints"]["no_nights"]:
        lines.append("  • No night shifts allowed")
    else:
        lines.append("  • Night shifts OK")
    
    if doctor["hard_constraints"]["no_weekends"]:
        lines.append("  • No weekend appointments")
    else:
        lines.append("  • Weekend appointments OK")
    
    constraints = "\n".join(lines)
else:
    constraints = "Doctor " + doc_id + " not found in system."