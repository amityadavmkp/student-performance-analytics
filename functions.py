"""
Student Performance Analytics System
Module: functions.py

Description:
Contains reusable functions for loading student data, calculating
academic performance (total marks, averages, grades, pass/fail status),
performing subject-wise and attendance analysis, and generating reports.
Built using Python 3, Pandas, and NumPy.
"""

import os
import pandas as pd
import numpy as np


def load_student_data(file_path):
    """
    Loads student records from a CSV file into a Pandas DataFrame.
    Includes basic error handling for file existence, empty files,
    and missing essential columns.

    Parameters:
        file_path (str): Relative or absolute path to the CSV file.

    Returns:
        pd.DataFrame: Cleaned DataFrame containing student records.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error: Dataset file '{file_path}' was not found.")

    try:
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        raise ValueError("Error: The CSV file is empty.")
    except Exception as e:
        raise RuntimeError(f"Error reading CSV file: {e}")

    # Verify required columns exist
    required_columns = ['Student_ID', 'Name', 'Department', 'Maths', 'Python', 'DBMS', 'Attendance']
    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        raise ValueError(f"Error: Missing required column(s) in CSV: {missing_columns}")

    # Ensure marks and attendance are numeric, converting invalid entries to NaN
    numeric_columns = ['Maths', 'Python', 'DBMS', 'Attendance']
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Drop or report any rows with missing or invalid numerical values
    if df[numeric_columns].isnull().any().any():
        print("[Warning] Missing or invalid numerical values detected. Rows with NaN will be dropped.")
        df = df.dropna(subset=numeric_columns)

    return df


def calculate_total_marks(df, subject_columns=['Maths', 'Python', 'DBMS']):
    """
    Calculates the total marks across all specified subjects for each student.
    Uses NumPy's sum function along axis 1 (row-wise sum).

    Parameters:
        df (pd.DataFrame): DataFrame containing student marks.
        subject_columns (list): List of subject column names.

    Returns:
        np.ndarray: 1D array of total marks for each student.
    """
    # Extract numerical marks as a NumPy 2D array
    marks_array = df[subject_columns].to_numpy()

    # NumPy calculation: row-wise summation
    total_marks = np.sum(marks_array, axis=1)

    return total_marks


def calculate_average_marks(df, subject_columns=['Maths', 'Python', 'DBMS']):
    """
    Calculates the average marks across all specified subjects for each student.
    Uses NumPy's mean function along axis 1, rounded to 2 decimal places.

    Parameters:
        df (pd.DataFrame): DataFrame containing student marks.
        subject_columns (list): List of subject column names.

    Returns:
        np.ndarray: 1D array of average marks rounded to 2 decimal places.
    """
    marks_array = df[subject_columns].to_numpy()

    # NumPy calculation: row-wise mean and rounding
    average_marks = np.round(np.mean(marks_array, axis=1), 2)

    return average_marks


def assign_grade(average_mark):
    """
    Assigns an academic letter grade based on a student's average marks.

    Grading Scale:
        90 - 100 : A+
        80 - 89  : A
        70 - 79  : B
        60 - 69  : C
        50 - 59  : D
        Below 50 : F

    Parameters:
        average_mark (float): Average mark of the student.

    Returns:
        str: Assigned letter grade.
    """
    if average_mark >= 90:
        return 'A+'
    elif average_mark >= 80:
        return 'A'
    elif average_mark >= 70:
        return 'B'
    elif average_mark >= 60:
        return 'C'
    elif average_mark >= 50:
        return 'D'
    else:
        return 'F'


def check_pass_fail(average_mark, attendance):
    """
    Determines whether a student has passed or failed based on two criteria:
    1. Average marks must be greater than or equal to 40.
    2. Attendance percentage must be greater than or equal to 75%.

    If both conditions are met, the student passes; otherwise, they fail.

    Parameters:
        average_mark (float): Student's average marks.
        attendance (float): Student's attendance percentage.

    Returns:
        str: 'Pass' or 'Fail'.
    """
    if average_mark >= 40 and attendance >= 75:
        return 'Pass'
    else:
        return 'Fail'


def process_student_data(df):
    """
    Processes the raw student DataFrame by computing Total Marks,
    Average Marks, Grades, and Pass/Fail Status using helper functions.

    Parameters:
        df (pd.DataFrame): Raw student DataFrame.

    Returns:
        pd.DataFrame: Augmented DataFrame with performance metrics.
    """
    processed_df = df.copy()

    # Calculate Total and Average Marks using NumPy functions
    processed_df['Total_Marks'] = calculate_total_marks(processed_df)
    processed_df['Average_Marks'] = calculate_average_marks(processed_df)

    # Assign Grades using Python loop / list comprehension with assign_grade()
    grades = [assign_grade(avg) for avg in processed_df['Average_Marks']]
    processed_df['Grade'] = grades

    # Determine Pass/Fail Status using check_pass_fail()
    statuses = [
        check_pass_fail(avg, att)
        for avg, att in zip(processed_df['Average_Marks'], processed_df['Attendance'])
    ]
    processed_df['Status'] = statuses

    return processed_df


def get_highest_performing_student(df):
    """
    Identifies the student with the highest average marks in the class.
    Uses NumPy argmax on average marks array.

    Parameters:
        df (pd.DataFrame): Processed DataFrame.

    Returns:
        dict: Details of the highest performing student (Name, Marks, Grade).
    """
    avg_marks = df['Average_Marks'].to_numpy()
    highest_idx = int(np.argmax(avg_marks))

    best_student = df.iloc[highest_idx]
    return {
        'Student_ID': best_student['Student_ID'],
        'Name': best_student['Name'],
        'Department': best_student['Department'],
        'Average_Marks': best_student['Average_Marks'],
        'Grade': best_student['Grade']
    }


def get_lowest_performing_student(df):
    """
    Identifies the student with the lowest average marks in the class.
    Uses NumPy argmin on average marks array.

    Parameters:
        df (pd.DataFrame): Processed DataFrame.

    Returns:
        dict: Details of the lowest performing student (Name, Marks, Grade).
    """
    avg_marks = df['Average_Marks'].to_numpy()
    lowest_idx = int(np.argmin(avg_marks))

    lowest_student = df.iloc[lowest_idx]
    return {
        'Student_ID': lowest_student['Student_ID'],
        'Name': lowest_student['Name'],
        'Department': lowest_student['Department'],
        'Average_Marks': lowest_student['Average_Marks'],
        'Grade': lowest_student['Grade']
    }


def get_overall_class_average(df):
    """
    Calculates the overall class average across all students.
    Uses NumPy mean.

    Parameters:
        df (pd.DataFrame): Processed DataFrame.

    Returns:
        float: Overall class average rounded to 2 decimal places.
    """
    avg_array = df['Average_Marks'].to_numpy()
    return float(np.round(np.mean(avg_array), 2))


def get_top_students(df, top_n=5):
    """
    Returns the top N students ranked by Average Marks in descending order.
    Uses Pandas sorting.

    Parameters:
        df (pd.DataFrame): Processed DataFrame.
        top_n (int): Number of top students to return (default 5).

    Returns:
        pd.DataFrame: Top N students.
    """
    sorted_df = df.sort_values(by='Average_Marks', ascending=False)
    return sorted_df.head(top_n).reset_index(drop=True)


def subject_analysis(df, subjects=['Maths', 'Python', 'DBMS']):
    """
    Performs statistical analysis for each subject including mean, max, and min.
    Uses NumPy functions for calculations.

    Parameters:
        df (pd.DataFrame): Student DataFrame.
        subjects (list): List of subject names.

    Returns:
        dict: Analysis dictionary containing subject statistics,
              subject with highest average, and subject with lowest average.
    """
    subject_stats = {}

    for subject in subjects:
        marks = df[subject].to_numpy()
        subject_stats[subject] = {
            'Average': float(np.round(np.mean(marks), 2)),
            'Highest': float(np.max(marks)),
            'Lowest': float(np.min(marks))
        }

    # Identify subject with highest and lowest average
    highest_sub = max(subject_stats.items(), key=lambda item: item[1]['Average'])
    lowest_sub = min(subject_stats.items(), key=lambda item: item[1]['Average'])

    return {
        'statistics': subject_stats,
        'highest_subject': highest_sub[0],
        'highest_subject_avg': highest_sub[1]['Average'],
        'lowest_subject': lowest_sub[0],
        'lowest_subject_avg': lowest_sub[1]['Average']
    }


def attendance_analysis(df, threshold=75.0):
    """
    Analyzes student attendance, computing the class average attendance
    and identifying students who fall below the required threshold.

    Parameters:
        df (pd.DataFrame): Student DataFrame.
        threshold (float): Minimum required attendance percentage (default 75%).

    Returns:
        dict: Dictionary containing class average attendance and DataFrame of low attendance students.
    """
    attendance_array = df['Attendance'].to_numpy()
    avg_attendance = float(np.round(np.mean(attendance_array), 2))

    # Pandas filtering for attendance below threshold
    low_attendance_students = df[df['Attendance'] < threshold][
        ['Student_ID', 'Name', 'Department', 'Attendance', 'Status']
    ].reset_index(drop=True)

    return {
        'average_attendance': avg_attendance,
        'threshold': threshold,
        'low_attendance_students': low_attendance_students,
        'low_attendance_count': len(low_attendance_students)
    }


def pass_fail_summary(df):
    """
    Summarizes the count of passed and failed students.

    Parameters:
        df (pd.DataFrame): Processed DataFrame with 'Status' column.

    Returns:
        dict: Counts of passed and failed students and pass percentage.
    """
    total = len(df)
    passed = int((df['Status'] == 'Pass').sum())
    failed = int((df['Status'] == 'Fail').sum())
    pass_percentage = float(np.round((passed / total) * 100, 2)) if total > 0 else 0.0

    return {
        'total': total,
        'passed': passed,
        'failed': failed,
        'pass_percentage': pass_percentage
    }
