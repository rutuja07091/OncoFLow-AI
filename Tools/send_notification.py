# Send Notification (Simulated)

# Try to get inputs
try:
    msg = message
except:
    msg = "No message provided"

try:
    pid = patient_id
except:
    pid = "Unknown"

# In production, this would integrate with email/SMS service
# For demo, just log and confirm
status = "✓ Notification sent successfully to patient " + pid + ". Message: " + msg[:100] + "..."