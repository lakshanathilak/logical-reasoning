
facts = [
    "good_marks",
    "good_attendance",
    "completed_projects",
    "programming_skill"
]

rules = {
    "EligibleForPlacement": [
        "good_marks",
        "good_attendance",
        "completed_projects"
    ],

    "GoodAcademicPerformance": [
        "good_marks",
        "good_attendance"
    ],

    "NeedsExtraPractice": [
        "programming_skill"
    ]
}



def backward_chaining(goal):

    print("Checking:", goal)

    # If goal is already a fact
    if goal in facts:
        print("Fact found:", goal)
        return True


    if goal in rules:

        for condition in rules[goal]:

            print("Need:", condition)

            if not backward_chaining(condition):
                return False

        return True

    return False



goal = "EligibleForPlacement"

print("Goal:", goal)
print()

result = backward_chaining(goal)

print()

if result:
    print("Final Conclusion:")
    print(goal, "is TRUE")
else:
    print("Final Conclusion:")
    print(goal, "is FALSE")


#     Backward Chaining starts with the goal and works backwards to find the facts needed to prove it.

# For example:

# Goal: EligibleForPlacement
#         ↓
# Need good_marks
#         ↓
# Fact found ✓

# Need good_attendance
#         ↓
# Fact found ✓

# Need completed_projects
#         ↓
# Fact found ✓

# Therefore:
# EligibleForPlacement = TRUE