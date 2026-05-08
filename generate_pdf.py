import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import FancyBboxPatch
import warnings
warnings.filterwarnings('ignore')

OUTPUT = "output/"
DATA   = "data/"

df         = pd.read_csv(DATA + "StudentsPerformance.csv")
cleaned_df = pd.read_csv(OUTPUT + "cleaned_students.csv")
messy_df   = pd.read_csv(OUTPUT + "messy_students.csv")
score_cols = ['math score', 'reading score', 'writing score']

pdf_path = "output/AbuHuraira_Sp24-BAI-002_DataAnalysis_Tasks.pdf"

def add_page_header(fig, title, color="#2E86AB"):
    fig.patch.set_facecolor('white')
    ax_header = fig.add_axes([0, 0.93, 1, 0.07])
    ax_header.set_facecolor(color)
    ax_header.text(0.5, 0.5, title, ha='center', va='center',
                   fontsize=16, fontweight='bold', color='white',
                   transform=ax_header.transAxes)
    ax_header.axis('off')

def text_page(pdf, title, lines, color="#2E86AB"):
    fig = plt.figure(figsize=(11, 8.5))
    add_page_header(fig, title, color)
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.86])
    ax.axis('off')
    ax.text(0.0, 1.0, "\n".join(lines), va='top', ha='left',
            fontsize=9, fontfamily='monospace',
            transform=ax.transAxes, wrap=True)
    pdf.savefig(fig, bbox_inches='tight')
    plt.close()

def image_page(pdf, title, img_path, color="#2E86AB"):
    fig = plt.figure(figsize=(11, 8.5))
    add_page_header(fig, title, color)
    ax = fig.add_axes([0.02, 0.02, 0.96, 0.89])
    img = mpimg.imread(img_path)
    ax.imshow(img)
    ax.axis('off')
    pdf.savefig(fig, bbox_inches='tight')
    plt.close()

with PdfPages(pdf_path) as pdf:

    # ── COVER PAGE ──────────────────────────────────────────────────────────
    fig = plt.figure(figsize=(11, 8.5))
    fig.patch.set_facecolor('#1a1a2e')
    ax = fig.add_subplot(111)
    ax.set_facecolor('#1a1a2e')
    ax.axis('off')

    ax.text(0.5, 0.88, "COMSATS University Islamabad",         ha='center', fontsize=18, color='white',      fontweight='bold')
    ax.text(0.5, 0.80, "Lahore Campus – Department of Computer Science", ha='center', fontsize=13, color='#aaaaaa')
    ax.axhline(y=0.75, xmin=0.1, xmax=0.9, color='#2E86AB', linewidth=2)
    ax.text(0.5, 0.67, "Lab Assignment 03 – Spring 2026",      ha='center', fontsize=20, color='#2E86AB',   fontweight='bold')
    ax.text(0.5, 0.59, "Student Performance Analysis",         ha='center', fontsize=16, color='white')
    ax.axhline(y=0.54, xmin=0.1, xmax=0.9, color='#2E86AB', linewidth=2)

    info = [
        ("Student Name",  "Abu Huraira"),
        ("Roll Number",   "Sp24-BAI-002"),
        ("Course",        "AIC270 - Programming for Artificial Intelligence"),
        ("Instructor",    "Mr. Shahrukh Naeem"),
        ("Semester",      "5th"),
        ("Date",          "08-05-2026"),
        ("Total Marks",   "100"),
    ]
    y = 0.47
    for label, value in info:
        ax.text(0.25, y, f"{label}:",  ha='right',  fontsize=12, color='#aaaaaa')
        ax.text(0.27, y, value,        ha='left',   fontsize=12, color='white', fontweight='bold')
        y -= 0.065

    pdf.savefig(fig, bbox_inches='tight')
    plt.close()

    # ── TASK 1: GIT ──────────────────────────────────────────────────────────
    text_page(pdf, "Task 1 – Git & Version Control",
    [
        "OBJECTIVE: Learn professional Git workflow and reproducibility.",
        "",
        "Steps Completed:",
        "  1. Created project folder: Student_Performance_Analysis (Lab_Assignment3)",
        "  2. Initialized Git repository using: git init",
        "  3. Created .gitignore file (ignores: archive.zip, __pycache__, .ipynb_checkpoints)",
        "  4. Created README.md with student details and project description",
        "  5. Created Jupyter notebook, loaded dataset, showed basic information",
        "  6. Made 4+ meaningful commits:",
        "       e1c0340  Initial commit: project setup with dataset and README",
        "       781743a  Add completed analysis notebook with all task outputs",
        "       564716b  branch-a: update course version to 1.0",
        "       bf3d799  branch-b: update course version to 2.0",
        "       f969fbc  Resolve merge conflict between branch-a and branch-b",
        "  7. Created branch feature/statistics, added describe() statistics, merged into main",
        "  8. Simulated merge conflict using branch-a and branch-b on README.md",
        "     - branch-a changed course line to: Version 1.0",
        "     - branch-b changed same line to:   Version 2.0",
        "     - Conflict markers appeared in README.md (<<<<<<< HEAD ... >>>>>>>)",
        "     - Resolved by keeping Version 2.0 and committing the fix",
        "  9. Pushed all branches to public GitHub repository:",
        "     https://github.com/abuhurairashabbir1/Student_Performance_Analysis",
    ], "#2E86AB")

    image_page(pdf, "Task 1 – Notebook: Header & Dataset Load", OUTPUT + "Screenshot 2026-05-08 164347.png", "#2E86AB")
    image_page(pdf, "Task 1 – GitHub Repository", OUTPUT + "Screenshot 2026-05-08 155440.png", "#2E86AB")
    image_page(pdf, "Task 1 – Git Commit Output", OUTPUT + "Screenshot 2026-05-08 161239.png", "#2E86AB")
    image_page(pdf, "Task 1 – Git Log Graph (git log --oneline --graph --all)", OUTPUT + "Screenshot 2026-05-08 162537.png", "#2E86AB")

    # ── TASK 2: DESCRIPTIVE STATISTICS ──────────────────────────────────────
    stats = pd.DataFrame({
        'Mean'  : df[score_cols].mean(),
        'Median': df[score_cols].median(),
        'Mode'  : df[score_cols].mode().iloc[0],
        'Std'   : df[score_cols].std(),
        'Min'   : df[score_cols].min(),
        'Max'   : df[score_cols].max()
    }).round(2)

    fig, axes = plt.subplots(1, 1, figsize=(11, 8.5))
    add_page_header(fig, "Task 2 – Descriptive Statistics", "#E94F37")
    axes.axis('off')

    tbl1 = axes.table(
        cellText  = stats.values,
        rowLabels = [s.title() for s in stats.index],
        colLabels = stats.columns,
        loc='upper center', cellLoc='center'
    )
    tbl1.auto_set_font_size(False)
    tbl1.set_fontsize(11)
    tbl1.scale(1.3, 2.2)
    for (r, c), cell in tbl1.get_celld().items():
        if r == 0 or c == -1:
            cell.set_facecolor('#E94F37')
            cell.set_text_props(color='white', fontweight='bold')
        else:
            cell.set_facecolor('#f9f9f9' if r % 2 == 0 else 'white')

    axes.set_title("Mean | Median | Mode | Std | Min | Max", fontsize=12, pad=10, color='#333')
    pdf.savefig(fig, bbox_inches='tight')
    plt.close()

    # Mean vs Median
    lines = ["MEAN vs MEDIAN COMPARISON:", ""]
    for col in score_cols:
        mean = df[col].mean(); median = df[col].median(); diff = mean - median
        direction = "slightly right-skewed (mean > median)" if diff > 0 else "slightly left-skewed (mean < median)"
        lines += [
            f"  {col.upper()}:",
            f"    Mean   = {mean:.2f}",
            f"    Median = {median:.2f}",
            f"    Diff   = {diff:.2f}  →  {direction}",
            ""
        ]
    lines += [
        "CONCLUSION:",
        "  The mean and median values are very close for all three subjects,",
        "  which means the score distributions are approximately symmetric.",
        "  There is no heavy skew, indicating a balanced dataset.",
        "  Math scores show the largest gap between mean and median,",
        "  suggesting slightly more variation in math performance."
    ]
    text_page(pdf, "Task 2 – Mean vs Median Comparison", lines, "#E94F37")

    # GroupBy gender
    gender_grp = df.groupby('gender')[score_cols].mean().round(2)
    fig, ax = plt.subplots(figsize=(11, 8.5))
    add_page_header(fig, "Task 2 – Average Scores by Gender", "#E94F37")
    ax.axis('off')
    tbl = ax.table(cellText=gender_grp.values, rowLabels=gender_grp.index,
                   colLabels=score_cols, loc='upper center', cellLoc='center')
    tbl.auto_set_font_size(False); tbl.set_fontsize(13); tbl.scale(1.5, 3)
    for (r, c), cell in tbl.get_celld().items():
        if r == 0 or c == -1:
            cell.set_facecolor('#E94F37'); cell.set_text_props(color='white', fontweight='bold')
        else:
            cell.set_facecolor('#fff5f5' if r % 2 == 0 else 'white')
    pdf.savefig(fig, bbox_inches='tight'); plt.close()

    # GroupBy parental education
    edu_grp = df.groupby('parental level of education')[score_cols].mean().round(2)
    fig, ax = plt.subplots(figsize=(11, 8.5))
    add_page_header(fig, "Task 2 – Average Scores by Parental Level of Education", "#E94F37")
    ax.axis('off')
    tbl = ax.table(cellText=edu_grp.values, rowLabels=edu_grp.index,
                   colLabels=score_cols, loc='upper center', cellLoc='center')
    tbl.auto_set_font_size(False); tbl.set_fontsize(11); tbl.scale(1.4, 2.5)
    for (r, c), cell in tbl.get_celld().items():
        if r == 0 or c == -1:
            cell.set_facecolor('#E94F37'); cell.set_text_props(color='white', fontweight='bold')
        else:
            cell.set_facecolor('#fff5f5' if r % 2 == 0 else 'white')
    pdf.savefig(fig, bbox_inches='tight'); plt.close()

    text_page(pdf, "Task 2 – 5 Important Observations", [
        "OBSERVATION 1 – GENDER DIFFERENCES IN SUBJECTS:",
        "  Female students score higher in reading (avg ~72) and writing (avg ~72),",
        "  while male students score higher in math (avg ~69).",
        "  This shows a clear subject-based performance difference between genders.",
        "",
        "OBSERVATION 2 – PARENTAL EDUCATION MATTERS:",
        "  Students whose parents hold a master's degree score the highest on average",
        "  across all subjects, while students with parents who only completed",
        "  some high school score the lowest. Education level at home influences",
        "  student academic performance significantly.",
        "",
        "OBSERVATION 3 – BALANCED SCORE DISTRIBUTION:",
        "  The mean and median are very close for all three subjects, meaning",
        "  the score distributions are symmetric with no extreme outliers.",
        "  This tells us the dataset is fairly representative and balanced.",
        "",
        "OBSERVATION 4 – READING AND WRITING ARE CLOSELY LINKED:",
        "  Students who perform well in reading almost always perform well in writing.",
        "  This strong relationship makes sense as both skills are language-based.",
        "",
        "OBSERVATION 5 – MATH HAS THE MOST VARIATION:",
        "  Math scores have the highest standard deviation among the three subjects,",
        "  meaning student performance in math is more spread out (some very high,",
        "  some very low), compared to reading and writing which are more consistent.",
    ], "#E94F37")

    # ── TASK 3: DATA CLEANING ────────────────────────────────────────────────
    text_page(pdf, "Task 3 – Data Cleaning", [
        "OBJECTIVE: Learn to clean messy real-world data.",
        "",
        "STEP 1 – MESSY DATASET CREATED (messy_students.csv):",
        "  Problems intentionally added to the original dataset:",
        f"  • Missing values added randomly to score columns (5% of rows)",
        f"  • 20 duplicate rows added",
        f"  • 3 outliers added: math=200, reading=-10, writing=999",
        f"  • Messy dataset shape: {messy_df.shape[0]} rows x {messy_df.shape[1]} columns",
        "",
        "STEP 2 – PROBLEMS FOUND:",
        f"  • Missing values:  math={messy_df['math score'].isnull().sum()}  |  reading={messy_df['reading score'].isnull().sum()}  |  writing={messy_df['writing score'].isnull().sum()}",
        f"  • Duplicate rows:  {messy_df.duplicated().sum()}",
        f"  • Outliers (score < 0 or > 100):",
        f"      math score:    {len(messy_df[(messy_df['math score'] < 0) | (messy_df['math score'] > 100)])} outlier(s)",
        f"      reading score: {len(messy_df[(messy_df['reading score'] < 0) | (messy_df['reading score'] > 100)])} outlier(s)",
        f"      writing score: {len(messy_df[(messy_df['writing score'] < 0) | (messy_df['writing score'] > 100)])} outlier(s)",
        "",
        "STEP 3 – CLEANING PROCESS:",
        "  1. Outliers fixed → replaced values outside 0-100 with NaN",
        "  2. Missing values filled → replaced NaN with median of each column",
        "  3. Duplicates removed → used drop_duplicates()",
        "  4. Index reset after cleaning",
        "",
        "STEP 4 – BEFORE vs AFTER SUMMARY:",
        f"  Rows:       Before = {len(messy_df)}   |   After = {len(cleaned_df)}",
        f"  Missing:    Before = {messy_df.isnull().sum().sum()}    |   After = {cleaned_df.isnull().sum().sum()}",
        f"  Duplicates: Before = {messy_df.duplicated().sum()}    |   After = {cleaned_df.duplicated().sum()}",
        f"  Outliers:   Before = 3       |   After = 0",
        "",
        "  Cleaned dataset saved to: data/cleaned_students.csv",
    ], "#393E41")

    # ── TASK 3 SCREENSHOTS ───────────────────────────────────────────────────
    image_page(pdf, "Task 3 – Messy Dataset Info (info() output)", OUTPUT + "Screenshot 2026-05-08 164334.png", "#393E41")
    image_page(pdf, "Task 3 – Missing Values, Duplicates & Outliers Found", OUTPUT + "Screenshot 2026-05-08 164325.png", "#393E41")
    image_page(pdf, "Task 3 – Cleaning Steps: Fix Outliers, Fill NaN, Remove Duplicates", OUTPUT + "Screenshot 2026-05-08 164133.png", "#393E41")

    # ── TASK 4: EDA ──────────────────────────────────────────────────────────
    race_grp = cleaned_df.groupby('race/ethnicity')[score_cols].mean().round(2)
    fig, ax = plt.subplots(figsize=(11, 8.5))
    add_page_header(fig, "Task 4 – GroupBy: Race/Ethnicity", "#6A0572")
    ax.axis('off')
    tbl = ax.table(cellText=race_grp.values, rowLabels=race_grp.index,
                   colLabels=score_cols, loc='upper center', cellLoc='center')
    tbl.auto_set_font_size(False); tbl.set_fontsize(12); tbl.scale(1.5, 2.8)
    for (r, c), cell in tbl.get_celld().items():
        if r == 0 or c == -1:
            cell.set_facecolor('#6A0572'); cell.set_text_props(color='white', fontweight='bold')
        else:
            cell.set_facecolor('#f9f0ff' if r % 2 == 0 else 'white')
    pdf.savefig(fig, bbox_inches='tight'); plt.close()

    prep_grp = cleaned_df.groupby('test preparation course')[score_cols].mean().round(2)
    fig, ax = plt.subplots(figsize=(11, 8.5))
    add_page_header(fig, "Task 4 – GroupBy: Test Preparation Course", "#6A0572")
    ax.axis('off')
    tbl = ax.table(cellText=prep_grp.values, rowLabels=prep_grp.index,
                   colLabels=score_cols, loc='upper center', cellLoc='center')
    tbl.auto_set_font_size(False); tbl.set_fontsize(13); tbl.scale(1.5, 3)
    for (r, c), cell in tbl.get_celld().items():
        if r == 0 or c == -1:
            cell.set_facecolor('#6A0572'); cell.set_text_props(color='white', fontweight='bold')
        else:
            cell.set_facecolor('#f9f0ff' if r % 2 == 0 else 'white')
    pdf.savefig(fig, bbox_inches='tight'); plt.close()

    corr = cleaned_df[score_cols].corr().round(2)
    fig, ax = plt.subplots(figsize=(11, 8.5))
    add_page_header(fig, "Task 4 – Correlation Matrix", "#6A0572")
    ax.axis('off')
    tbl = ax.table(cellText=corr.values, rowLabels=corr.index,
                   colLabels=corr.columns, loc='upper center', cellLoc='center')
    tbl.auto_set_font_size(False); tbl.set_fontsize(13); tbl.scale(1.8, 3)
    for (r, c), cell in tbl.get_celld().items():
        if r == 0 or c == -1:
            cell.set_facecolor('#6A0572'); cell.set_text_props(color='white', fontweight='bold')
        else:
            cell.set_facecolor('#f9f0ff' if r % 2 == 0 else 'white')
    pdf.savefig(fig, bbox_inches='tight'); plt.close()

    image_page(pdf, "Task 4 – GroupBy Test Prep & Correlation Matrix (Notebook Output)", OUTPUT + "Screenshot 2026-05-08 164113.png", "#6A0572")
    image_page(pdf, "Task 4 – Correlation Heatmap", OUTPUT + "correlation_heatmap.png", "#6A0572")

    text_page(pdf, "Task 4 – Detailed Insights (EDA)", [
        "1. GENDER DIFFERENCES:",
        "   Female students consistently outperform male students in reading and writing scores.",
        "   However, male students tend to score slightly higher in math. This pattern suggests",
        "   a gender-based difference in subject preference or teaching approach. Schools could",
        "   benefit from gender-targeted strategies to bridge these gaps.",
        "",
        "2. PARENTAL EDUCATION IMPACT:",
        "   Students whose parents hold a master's or bachelor's degree score noticeably higher",
        "   in all three subjects compared to students whose parents only completed high school.",
        "   This highlights the strong influence of family educational background on student",
        "   performance and suggests a cycle of educational advantage.",
        "",
        "3. TEST PREPARATION COURSE:",
        "   Students who completed the test preparation course scored significantly higher",
        "   across all subjects compared to those who did not complete it. This confirms that",
        "   structured preparation directly and measurably improves academic performance.",
        "   Encouraging more students to complete prep courses could raise overall scores.",
        "",
        "4. RACE/ETHNICITY:",
        "   Group E students have the highest average scores across all subjects, while",
        "   Group A students tend to score the lowest. This could reflect differences in",
        "   access to educational resources, support systems, or socioeconomic factors.",
        "",
        "5. CORRELATION BETWEEN SCORES:",
        "   Reading and writing scores are very strongly correlated (0.95+), meaning students",
        "   who are good at reading are almost always good at writing too. Math shows a",
        "   moderate correlation (~0.82) with both, suggesting these skills share some",
        "   foundation but are more independent than reading and writing.",
        "",
        "6. LUNCH TYPE (SOCIOECONOMIC INDICATOR):",
        "   Students with standard lunch score higher on average than students with free/reduced",
        "   lunch. This socioeconomic indicator suggests that financial background plays a",
        "   role in academic outcomes, possibly through access to tutoring and resources.",
    ], "#6A0572")

    # ── TASK 5: VISUALIZATIONS ───────────────────────────────────────────────
    image_page(pdf, "Task 5 – Plot 1: Histogram of Math Scores with KDE", OUTPUT + "plot1_histogram.png", "#F18F01")
    image_page(pdf, "Task 5 – Plot 2: Boxplot of Math Score by Gender",   OUTPUT + "plot2_boxplot.png",  "#F18F01")
    image_page(pdf, "Task 5 – Plot 3: Reading vs Writing Score by Gender", OUTPUT + "plot3_scatter.png", "#F18F01")
    image_page(pdf, "Task 5 – Plot 4: Average Math Score by Parental Education", OUTPUT + "plot4_barchart.png", "#F18F01")
    image_page(pdf, "Task 5 – Combined 2x2 Visualization (best_visualization.png)", OUTPUT + "best_visualization.png", "#F18F01")

print(f"PDF created successfully: {pdf_path}")
