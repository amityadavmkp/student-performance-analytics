# Student Performance Analytics System

A comprehensive, beginner-friendly Python data analysis system designed to evaluate, analyze, and report individual and class-level academic performance from student records.

Developed in accordance with the **EWB Courses Python with AI** project curriculum.

---

## 1. Project Title
**Student Performance Analytics System**

---

## 2. Project Description
The **Student Performance Analytics System** is a modular Python application that loads student academic data from a CSV file, performs statistical and performance calculations using **NumPy** and **Pandas**, and prints a structured, executive-level academic report alongside a final summarized student performance table.

The project strictly adheres to pure Python data analysis fundamentals without relying on unnecessary web frameworks or complex machine learning models, making it educational, robust, and easy to explain during a viva examination.

---

## 3. Objective
The primary objective of this project is to build an automated, reliable data analytics pipeline that:
- Reads student examination marks and attendance from a flat CSV dataset.
- Computes essential metrics: total marks, average percentage, letter grades, and pass/fail eligibility.
- Leverages **NumPy** for high-performance numerical operations (mean, min, max, summation).
- Leverages **Pandas** for structured tabular operations, data preview, filtering, and sorting.
- Detects academic highlights including top rankers, lowest performers, subject-level trends, and low-attendance alerts.

---

## 4. Key Features
- **Data Ingestion with Validation**: Safe loading of CSV records with built-in checks for missing files, empty files, and missing headers.
- **Total & Average Calculation**: Row-wise summation and averaging across academic subjects using NumPy array vectorization.
- **Automated Grade Assignment**: Clear six-tier grading ladder from `A+` down to `F`.
- **Dual-Criterion Pass/Fail Verification**: Enforces minimum academic average (>= 40%) **AND** strict minimum attendance threshold (>= 75%).
- **Subject-Wise Statistical Analysis**: Identifies averages, maximum scores, and minimum scores for each subject (Maths, Python, DBMS).
- **Top 5 Rankers Identification**: Automatic sorting and extraction of top academic achievers.
- **Attendance Monitoring**: Flags students failing to meet mandatory 75% attendance criteria.
- **Clean Terminal Reporting**: Formatted ASCII reporting designed for clarity and viva presentation.

---

## 5. Technologies Used
- **Programming Language**: Python 3.x
- **Numerical Processing**: NumPy (`numpy`)
- **Data Analysis & Manipulation**: Pandas (`pandas`)
- **File Format**: Comma-Separated Values (`.csv`)

> **Note**: No heavy web frameworks (Django/Flask), databases (MySQL/MongoDB), or unnecessary machine learning models are used.

---

## 6. Project Structure

```text
Student-Performance-Analytics/
│
├── main.py                    # Main executable driver script
├── functions.py               # Reusable analytics and processing functions
├── students.csv               # Dataset containing 25 student records
├── README.md                  # Project overview and run instructions
└── Project_Documentation.md   # In-depth viva documentation and analysis report
```

---

## 7. Dataset Description
The dataset is stored in `students.csv` and contains **25 realistic student records** across multiple engineering and technology departments.

### Schema:
| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `Student_ID` | Integer | Unique identifier for each student (e.g., 101, 102) |
| `Name` | String | Full name of the student |
| `Department` | String | Department (e.g., Computer Science, IT, AI, Data Science) |
| `Maths` | Float / Int | Marks scored in Mathematics (0–100) |
| `Python` | Float / Int | Marks scored in Python Programming (0–100) |
| `DBMS` | Float / Int | Marks scored in Database Management Systems (0–100) |
| `Attendance` | Float / Int | Class attendance percentage (0–100%) |

---

## 8. Grading Rule

Grades are assigned based on the student's **Average Marks** across all subjects:

| Average Marks Range | Grade | Description |
| :---: | :---: | :--- |
| **90 - 100** | **A+** | Outstanding Performance |
| **80 - 89** | **A** | Excellent Performance |
| **70 - 79** | **B** | Very Good Performance |
| **60 - 69** | **C** | Good / Satisfactory Performance |
| **50 - 59** | **D** | Average / Pass Performance |
| **Below 50** | **F** | Fail / Unsatisfactory Performance |

---

## 9. Pass / Fail Rule

A student is officially marked as **`Pass`** only if they fulfill **both** of the following conditions:
1. **Average Marks $\ge$ 40%** (Minimum passing academic benchmark)
2. **Attendance $\ge$ 75%** (Mandatory attendance criterion)

$$\text{Status} = \begin{cases} \text{Pass}, & \text{if } \text{Average Marks} \ge 40 \text{ and } \text{Attendance} \ge 75 \\ \text{Fail}, & \text{otherwise} \end{cases}$$

> **Important Edge Case**: A student scoring high marks (e.g., 82%) will still receive a **`Fail`** status if their attendance is below 75%. This showcases real-world academic compliance rules.

---

## 10. How to Install Requirements

Ensure you have Python 3 installed. Install the required libraries via `pip`:

```bash
pip install pandas numpy
```

---

## 11. How to Run the Project

1. Open your terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd Student-Performance-Analytics
   ```
3. Execute `main.py`:
   ```bash
   python main.py
   ```

---

## 12. Sample Output

```text
================================================
      STUDENT PERFORMANCE ANALYTICS SYSTEM      
================================================

[1] LOADING DATASET...
 -> Successfully loaded dataset from 'students.csv'
 -> Total Records Found : 25
 -> Total Columns       : 7
 -> Columns Available   : Student_ID, Name, Department, Maths, Python, DBMS, Attendance

[Preview of Raw Student Records (First 5 Rows)]:
 Student_ID      Name            Department        Maths  Python  DBMS  Attendance
    101        Amit Yadav        Computer Science   92      95     88       94    
    102       Priya Singh  Information Technology   89      91     90       92    
    103       Rohit Kumar Artificial Intelligence   84      88     85       88    
    104     Anjali Sharma        Computer Science   82      85     87       90    
    105      Shivam Verma            Data Science   80      84     82       86    

[2] PROCESSING ACADEMIC PERFORMANCE METRICS...
 -> Total Marks calculated using NumPy row-wise summation.
 -> Average Marks calculated using NumPy mean and rounded to 2 decimals.
 -> Letter Grades assigned based on defined grading scale.
 -> Pass/Fail status evaluated (Pass: Avg >= 40 AND Attendance >= 75%).

================================================
        COMPREHENSIVE PERFORMANCE REPORT        
================================================

Total Students: 25
Overall Class Average: 70.24
Passed Students: 21 (84.0%)
Failed Students: 4

Highest Performing Student:
 -> Amit Yadav (Computer Science) - 91.67% (Grade: A+)

Lowest Performing Student:
 -> Rahul Kumar (Computer Science) - 32.33% (Grade: F)

Subject-wise Average:
 -> Maths    : 68.44 (Highest: 92.0, Lowest: 30.0)
 -> Python   : 72.40 (Highest: 95.0, Lowest: 35.0)
 -> DBMS     : 69.88 (Highest: 90.0, Lowest: 32.0)
 * Highest Scoring Subject: Python (Avg: 72.40)
 * Lowest Scoring Subject : Maths (Avg: 68.44)

Top 5 Students by Performance:
 1. Amit Yadav         | Dept: Computer Science         | Avg: 91.67% | Grade: A+
 2. Priya Singh        | Dept: Information Technology   | Avg: 90.00% | Grade: A+
 3. Tanvi Bansal       | Dept: Information Technology   | Avg: 87.67% | Grade: A
 4. Rohit Kumar        | Dept: Artificial Intelligence  | Avg: 85.67% | Grade: A
 5. Anjali Sharma      | Dept: Computer Science         | Avg: 84.67% | Grade: A

Average Class Attendance: 81.28%
Students with Attendance Below 75.0% (Total: 3):
 -> ID: 119 | Aman Mehta         | Dept: Information Technology   | Attendance: 68% | Status: Fail
 -> ID: 120 | Divya Chawla       | Dept: Artificial Intelligence  | Attendance: 70% | Status: Fail
 -> ID: 122 | Rahul Kumar        | Dept: Computer Science         | Attendance: 62% | Status: Fail

================================================
        FINAL STUDENT PERFORMANCE TABLE         
================================================

 Student_ID      Name             Department        Total_Marks  Average_Marks Grade Status  Attendance
    101         Amit Yadav        Computer Science     275          91.67        A+   Pass       94    
    102        Priya Singh  Information Technology     270          90.00        A+   Pass       92    
    103        Rohit Kumar Artificial Intelligence     257          85.67         A   Pass       88    
    104      Anjali Sharma        Computer Science     254          84.67         A   Pass       90    
    105       Shivam Verma            Data Science     246          82.00         A   Pass       86    
    106        Sneha Patel  Information Technology     239          79.67         B   Pass       85    
    107        Vikas Gupta        Computer Science     229          76.33         B   Pass       80    
    108       Pooja Mishra Artificial Intelligence     226          75.33         B   Pass       84    
    109          Kunal Roy            Data Science     216          72.00         B   Pass       82    
    110        Neha Tiwari        Computer Science     210          70.00         B   Pass       78    
    111       Manish Joshi  Information Technology     203          67.67         C   Pass       76    
    112           Ritu Raj Artificial Intelligence     195          65.00         C   Pass       81    
    113     Deepak Chauhan            Data Science     191          63.67         C   Pass       79    
    114        Simran Kaur        Computer Science     181          60.33         C   Pass       83    
    115      Aditya Saxena  Information Technology     171          57.00         D   Pass       77    
    116       Kavita Rawat Artificial Intelligence     162          54.00         D   Pass       75    
    117        Suresh Nair            Data Science     156          52.00         D   Pass       76    
    118          Mohit Sen        Computer Science     151          50.33         D   Pass       78    
    119         Aman Mehta  Information Technology     228          76.00         B   Fail       68    
    120       Divya Chawla Artificial Intelligence     248          82.67         A   Fail       70    
    121       Gaurav Bhatt            Data Science     115          38.33         F   Fail       80    
    122        Rahul Kumar        Computer Science      97          32.33         F   Fail       62    
    123       Tanvi Bansal  Information Technology     263          87.67         A   Pass       91    
    124      Harsh Vardhan Artificial Intelligence     232          77.33         B   Pass       88    
    125       Isha Nambiar            Data Science     253          84.33         A   Pass       89    

================================================
======= ANALYSIS COMPLETED SUCCESSFULLY ========
================================================
```

---

## 13. Learning Outcomes
By exploring and running this project, students learn:
1. How to read and validate structured CSV files using **Pandas**.
2. How to leverage **NumPy** arrays for vectorized mathematical operations (`np.sum`, `np.mean`, `np.argmax`, `np.argmin`).
3. How to write modular, reusable Python functions with clean docstrings.
4. How to combine multiple conditions (`if`, `and`, `or`) for decision logic (grades, pass/fail rules).
5. How to manipulate, sort, and slice DataFrames for data presentations.
6. How to prepare clean, production-standard documentation suitable for technical interviews and viva examinations.

---

## 14. GitHub Repository Section

### Steps to push this project to GitHub:
```bash
# 1. Initialize git inside project folder
git init

# 2. Add all project files
git add main.py functions.py students.csv README.md Project_Documentation.md

# 3. Commit the changes
git commit -m "Initial commit: Student Performance Analytics System"

# 4. Set the main branch
git branch -M main

# 5. Link your GitHub remote repository
git remote add origin https://github.com/amityadavmkp/student-performance-analytics

# 6. Push to GitHub
git push -u origin main
```
