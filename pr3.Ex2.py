def check_placement_eligibility(graduation_score, active_backlogs):
    if graduation_score >= 70 and active_backlogs == 0:
        return "Eligible for placement."

    return "Not eligible for placement."


# Get candidate details
score = float(input("Enter graduation score (%): "))
backlogs = int(input("Enter number of active academic backlogs: "))

# Validate eligibility
result = check_placement_eligibility(score, backlogs)

print(result)