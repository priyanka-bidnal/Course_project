import sys
def calculate_engagement_score(students, hours):
    return students * hours
def get_learning_status(score):
    if score >= 120:
        return "Highly Engaged Course"
    elif 70 <= score < 120:
        return "Moderately Engaged Course"
    else:
        return "Low Engagement Course"
if __name__ == "__main__":
    script_name = sys.argv[0]
# If user provides input through command line
    if len(sys.argv) > 4:
        course_name = sys.argv[1]
        platform = sys.argv[2]
        students = int(sys.argv[3])
        hours = int(sys.argv[4])
        print("User provided online learning details:")
    else:
        # Default values (Jenkins-safe)
        course_name = "Introduction to Python"
        platform = "Coursera"
        students = 20
        hours = 4
        print("No input given - using default values:")
    engagement_score = calculate_engagement_score(students, hours)
    status = get_learning_status(engagement_score)
    print("\n========== Smart Online Learning Engagement Report ==========")
    print("Script Name         :", script_name)
    print("Course Name         :", course_name)
    print("Learning Platform   :", platform)
    print("Active Students     :", students)
    print("Study Hours / Week  :", hours)
    print("Engagement Score    :", engagement_score)
    print("Engagement Status   :", status)