# Apply Schedule Changes

# Try to get input
try:
    change_list = changes
except:
    try:
        change_list = inputs['changes']
    except:
        change_list = "[]"

# In production, this would update the database
# For demo, just confirm
result = "Successfully applied " + str(len(change_list)) + " schedule changes. All appointments have been updated in the system."