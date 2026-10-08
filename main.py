"""
Student Performance Analytics System
Entry Point: main.py

Description:
Main executable script that coordinates loading, processing, and analyzing
student academic performance data. Demonstrates core Python concepts,
NumPy array mathematics, and Pandas DataFrame operations.
"""

import sys
import os

# Prevent creation of __pycache__ bytecode files to keep repository clean
sys.dont_write_bytecode = True

import pandas as pd
import numpy as np

# Import custom reusable analytics functions
from functions import (
    load_student_data,
    process_student_data,
    get_highest_performing_student,
    get_lowest_performing_student,
    get_overall_class_average,
    get_top_students,
    subject_analysis,
    attendance_analysis,
    pass_fail_summary
)


def display_header(title):
    """Prints a styled header box for clean report presentation."""
    border = "=" * 48
    print("\n" + border)
    print(f" {title.center(46)} ")
    print(border + "\n")


def main():
    """Main execution function for the Student Performance Analytics System."""
    # Configure Pandas display settings for readable table output
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    pd.set_option('display.colheader_justify', 'center')

    # Resolve dataset path dynamically based on script location
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(base_dir, 'students.csv')

    display_header("STUDENT PERFORMANCE ANALYTICS SYSTEM")

    # Step 1: Load and Inspect Dataset
    print("[1] LOADING DATASET...")
    try:
        raw_df = load_student_data(csv_file)
        print(f" -> Successfully loaded dataset from '{os.path.basename(csv_file)}'")
        print(f" -> Total Records Found : {raw_df.shape[0]}")
        print(f" -> Total Columns       : {raw_df.shape[1]}")
        print(f" -> Columns Available   : {', '.join(raw_df.columns)}")
    except Exception as error:
        print(f"\n[Fatal Error] Unable to initialize system: {error}")
        return

    # Display First Few Records (Pandas Demonstration)
    print("\n[Preview of Raw Student Records (First 5 Rows)]:")
    print(raw_df.head().to_string(index=False))

    # Step 2: Process Student Data (Calculations, Grades, Pass/Fail)
    print("\n[2] PROCESSING ACADEMIC PERFORMANCE METRICS...")
    processed_df = process_student_data(raw_df)
    print(" -> Total Marks calculated using NumPy row-wise summation.")
    print(" -> Average Marks calculated using NumPy mean and rounded to 2 decimals.")
    print(" -> Letter Grades assigned based on defined grading scale.")
    print(" -> Pass/Fail status evaluated (Pass: Avg >= 40 AND Attendance >= 75%).")

    # Step 3: Run Analytics
    class_avg = get_overall_class_average(processed_df)
    pf_stats = pass_fail_summary(processed_df)
    best_student = get_highest_performing_student(processed_df)
    lowest_student = get_lowest_performing_student(processed_df)
    sub_analysis = subject_analysis(processed_df, subjects=['Maths', 'Python', 'DBMS'])
    top_5_students = get_top_students(processed_df, top_n=5)
    att_stats = attendance_analysis(processed_df, threshold=75.0)

    # Step 4: Display Formatted Executive Report
    display_header("COMPREHENSIVE PERFORMANCE REPORT")

    print(f"Total Students: {pf_stats['total']}")
    print(f"Overall Class Average: {class_avg:.2f}")
    print(f"Passed Students: {pf_stats['passed']} ({pf_stats['pass_percentage']}%)")
    print(f"Failed Students: {pf_stats['failed']}")

    print("\nHighest Performing Student:")
    print(f" -> {best_student['Name']} ({best_student['Department']}) - {best_student['Average_Marks']:.2f}% (Grade: {best_student['Grade']})")

    print("\nLowest Performing Student:")
    print(f" -> {lowest_student['Name']} ({lowest_student['Department']}) - {lowest_student['Average_Marks']:.2f}% (Grade: {lowest_student['Grade']})")

    print("\nSubject-wise Average:")
    for subject, stats in sub_analysis['statistics'].items():
        print(f" -> {subject:<8} : {stats['Average']:.2f} (Highest: {stats['Highest']}, Lowest: {stats['Lowest']})")
    print(f" * Highest Scoring Subject: {sub_analysis['highest_subject']} (Avg: {sub_analysis['highest_subject_avg']:.2f})")
    print(f" * Lowest Scoring Subject : {sub_analysis['lowest_subject']} (Avg: {sub_analysis['lowest_subject_avg']:.2f})")

    print("\nTop 5 Students by Performance:")
    for rank, (_, row) in enumerate(top_5_students.iterrows(), start=1):
        print(f" {rank}. {row['Name']:<18} | Dept: {row['Department']:<24} | Avg: {row['Average_Marks']:.2f}% | Grade: {row['Grade']}")

    print(f"\nAverage Class Attendance: {att_stats['average_attendance']:.2f}%")
    print(f"Students with Attendance Below {att_stats['threshold']}% (Total: {att_stats['low_attendance_count']}):")
    if att_stats['low_attendance_count'] > 0:
        low_att_df = att_stats['low_attendance_students']
        for _, row in low_att_df.iterrows():
            print(f" -> ID: {row['Student_ID']} | {row['Name']:<18} | Dept: {row['Department']:<24} | Attendance: {row['Attendance']}% | Status: {row['Status']}")
    else:
        print(" -> All students meet the required 75% attendance threshold.")

    # Step 5: Final Processed DataFrame Output
    display_header("FINAL STUDENT PERFORMANCE TABLE")
    final_columns = [
        'Student_ID',
        'Name',
        'Department',
        'Total_Marks',
        'Average_Marks',
        'Grade',
        'Status',
        'Attendance'
    ]
    final_table = processed_df[final_columns]
    print(final_table.to_string(index=False))

    print("\n" + "=" * 48)
    print(" ANALYSIS COMPLETED SUCCESSFULLY ".center(48, "="))
    print("=" * 48 + "\n")


if __name__ == "__main__":
    main()
