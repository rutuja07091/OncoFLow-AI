# Extract inputs safely from context
name = context.inputs.get("patient_name", "Patient")
reason = context.inputs.get("reason", "schedule_change")
old_time = context.inputs.get("old_time", "")
new_time = context.inputs.get("new_time", "")
doctor_name = context.inputs.get("doctor_name", "your doctor")
risk_level = context.inputs.get("risk_level", "").upper()

# Generate message text
if "sick" in reason.lower():
    message = (
        f"Dear {name}, "
        f"Due to {doctor_name}'s unexpected unavailability, we need to reschedule "
        f"your appointment originally scheduled for {old_time}. We sincerely apologize "
        f"for the inconvenience. Your treatment timeline remains a top priority, and "
        f"we’ve identified {new_time} as a safe alternative within your treatment window. "
        f"Please confirm if this time works for you. "
        f"- OncoFlow Scheduling Team"
    )

elif "emergency" in reason.lower():
    message = (
        f"Dear {name}, "
        f"Due to an unexpected emergency, we must reschedule your appointment "
        f"from {old_time} to {new_time}. We understand the importance of maintaining "
        f"your treatment plan and have prioritized finding the earliest safe slot. "
        f"Please reach out if you have concerns or need assistance. "
        f"- OncoFlow Scheduling Team"
    )

else:
    message = (
        f"Dear {name}, "
        f"We’re writing to inform you of a necessary change to your appointment. "
        f"Your appointment has been moved from {old_time} to {new_time}. "
        f"This adjustment helps ensure smooth scheduling while keeping your treatment "
        f"timeline protected. Please let us know if this time works for you. "
        f"- OncoFlow Scheduling Team"
    )

# Add risk-specific reassurance
if risk_level == "HIGH":
    message += " Please note that this adjustment has been prioritized to avoid any impact on your treatment plan."
elif risk_level == "LOW":
    message += " This change does not affect your overall treatment schedule."

# Return the final message
context.outputs = {
    "patient_message": message
}
