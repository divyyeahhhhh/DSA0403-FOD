import numpy as np

# Sample student_scores matrix (replace this with your actual data)
num_students = 4
num_subjects = 4
subjects = ['Math', 'Science', 'English', 'History']

# Get student scores from the user
student_scores = np.array([[int(input(f"Enter {subjects[j]} score for student {i+1}: ")) for j in range(num_subjects)] for i in range(num_students)])

# Print the input as a 4x4 matrix
print("Student Scores Matrix:")
print(student_scores)

# Calculate the average score for each subject (column-wise)
average_scores = np.mean(student_scores, axis=0)

# Determine the subject with the highest average score
highest_average_subject_index = np.argmax(average_scores)
highest_average_subject = subjects[highest_average_subject_index]

# Print the results
print("Average scores for each subject:", average_scores)
print("Subject with the highest average score:", highest_average_subject)
