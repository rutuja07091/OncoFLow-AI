doctor_id = context.inputs["doctor_id"]
start_time = context.inputs["start_time"]
end_time = context.inputs["end_time"]
patient_id = context.inputs["patient_id"]

result = {
    "status": "success",
    "message": f"Calendar slot blocked for doctor {doctor_id} from {start_time} to {end_time} for patient {patient_id}.",
    "doctor_id": doctor_id,
    "start_time": start_time,
    "end_time": end_time,
    "patient_id": patient_id
}

context.outputs = result
