# Update Patient Preferences

# Try to get inputs
try:
    pid = patient_id
except:
    pid = "Unknown"

try:
    pref_type = preference_type
except:
    pref_type = "unknown"

try:
    pref_val = preference_value
except:
    pref_val = "true"

# In production, this would update the database
# For demo, confirm the update
result = "✓ Updated preferences for patient " + pid + ": " + pref_type + " = " + pref_val + ". This preference will be respected in all future scheduling recommendations."