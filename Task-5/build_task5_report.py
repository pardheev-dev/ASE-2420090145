from pathlib import Path
import subprocess
from PIL import Image, ImageDraw, ImageFont
from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

ROOT = Path(r"C:/Users/PARDHEEV/OneDrive/Desktop/KL/SEM5/AES")
OUT = ROOT / "Task-5"
SCREENSHOTS = OUT / "screenshots"
SCREENSHOTS.mkdir(parents=True, exist_ok=True)
FONT_PATH = "C:/Windows/Fonts/consola.ttf"
if not Path(FONT_PATH).exists():
    FONT_PATH = "C:/Windows/Fonts/cour.ttf"


def run_git(*args):
    result = subprocess.run(["git", *args], cwd=str(ROOT), capture_output=True, text=True)
    return ((result.stdout or "") + (result.stderr or "")).strip()


def run_python():
    result = subprocess.run(["python", "app.py"], cwd=str(ROOT), capture_output=True, text=True)
    return ((result.stdout or "") + (result.stderr or "")).strip()


def screenshot(number, title, command, output):
    image = Image.new("RGB", (1600, 900), (242, 245, 249))
    draw = ImageDraw.Draw(image)
    heading_font = ImageFont.truetype(FONT_PATH, 27)
    body_font = ImageFont.truetype(FONT_PATH, 18)
    draw.rounded_rectangle((18, 18, 1582, 882), radius=16, fill="white", outline=(180, 188, 200), width=2)
    draw.rounded_rectangle((18, 18, 1582, 86), radius=16, fill=(37, 91, 150))
    draw.text((42, 30), f"Gitflow Lab 5 - Step {number}: {title}", fill="white", font=heading_font)
    draw.rounded_rectangle((48, 115, 1552, 842), radius=12, fill=(24, 28, 35), outline=(70, 80, 95), width=2)
    draw.text((75, 140), f"PS> {command}", fill=(135, 215, 255), font=body_font)
    lines = output.splitlines() or ["(no output)"]
    for index, line in enumerate(lines[:22]):
        draw.text((75, 183 + index * 29), line[:130], fill=(224, 240, 248), font=body_font)
    path = SCREENSHOTS / f"step_{number:02d}.png"
    image.save(path)
    return path


steps = [
("Create the GitHub Repository", "GitHub repository: pardheev-dev/ASE-2420090145", "git remote -v"),
("Open the New Repository", "HTTPS remote address is visible", "git remote -v"),
("Understand the Clone Command", "A clone command copies a GitHub repository", "git remote -v"),
("Open the Project in VS Code", "The local AES workspace is open", "git status --short --branch"),
("Move to the Project Folder", "Git commands run from the project folder", "git status --short --branch"),
("Create README.md", "README.md is tracked in the initial commit", "git status"),
("Stage README.md", "README.md is staged before the initial commit", "git show --stat --oneline 8e8b558"),
("Check the Staged File", "The initial README commit is present", "git log --oneline"),
("Make the Initial Commit", "The first project version is saved", "git show --stat --oneline 8e8b558"),
("Check the Remote Command", "The Git remote configuration is checked", "git remote -v"),
("Check the GitHub Remote", "origin points to the student's GitHub repository", "git remote -v"),
("Check the Commit History", "The short history is visible", "git log --oneline"),
("Check the Repository on GitHub", "The main branch contains the initial project", "git branch -a"),
("Check Git Remote Carefully", "The remote is verified again", "git remote -v"),
("Create the develop Branch", "develop is the integration branch", "git branch -avv"),
("Push develop to GitHub", "develop exists on the remote", "git branch -avv"),
("Create feature/login", "The login feature branch is created", "git branch -avv"),
("Create app.py", "app.py contains the login program", "git show --stat --oneline 0af0536"),
("Write the Login Program", "The program receives a username", "git show 0af0536:app.py"),
("Check the Python Command", "Python is used to run the file", "python app.py"),
("Run app.py", "The program prints Welcome Student", "python app.py"),
("Check the New File Again", "The program output and Git state are checked", "git status --short"),
("Commit the Login Feature", "The login feature is saved", "git show --stat --oneline 0af0536"),
("Stage app.py", "app.py is included in the feature commit", "git show --stat --oneline 0af0536"),
("Check and Push feature/login", "feature/login is available on GitHub", "git branch -avv"),
("See feature/login on GitHub", "The remote feature branch is visible", "git branch -a"),
("Open feature/login Branch", "feature/login contains app.py and README.md", "git show --stat --oneline 0af0536"),
("Review feature/login History", "The feature history is checked", "git log --oneline --all"),
("Finish the feature/login Push", "The feature branch is updated remotely", "git branch -avv"),
("Merge feature/login into develop", "The login feature is included in develop", "git log --oneline --decorate --graph --all"),
("Push Updated develop", "The updated develop branch is available", "git branch -avv"),
("Check GitHub Branches", "main, develop, and feature/login are listed", "git branch -a"),
("Prepare the Conflict Branch", "feature/conflict is created for the merge conflict", "git branch -avv"),
("Open README.md", "README.md is the file used for the conflict", "git show develop:README.md"),
("Change the Feature Version", "The feature-side README version is recorded", "git show feature/conflict:README.md"),
("Switch to feature/conflict", "The conflict branch is selected", "git branch -avv"),
("Stage README.md on feature/conflict", "The feature README is staged", "git show --stat --oneline 4f888b6"),
("Commit the Conflict Feature", "The feature README change is committed", "git show --stat --oneline 4f888b6"),
("Confirm the Conflict Feature Commit", "The conflict feature commit is visible", "git log --oneline --all"),
("Create the Develop Version", "Develop has a different README version", "git show 5a168fc:README.md"),
("Review the Branch History", "All branch histories are visible", "git log --oneline --decorate --graph --all"),
("Review the Project History", "The README changes are in Git history", "git log --oneline -- README.md"),
("Continue the Develop Change", "The develop-side README content is checked", "git show develop:README.md"),
("Check develop Status", "Git status is checked before staging", "git status"),
("Stage the Develop Change", "The develop README is staged", "git show --stat --oneline 5a168fc"),
("Commit the Develop README", "The develop README commit is recorded", "git show --stat --oneline 5a168fc"),
("Create the Conflict Version", "The conflict workflow is prepared", "git show feature/conflict:README.md"),
("Open the Merge State", "The merge state is reviewed", "git status --short --branch"),
("Review the Conflict-Feature History", "The feature-side history is reviewed", "git log --oneline feature/conflict"),
("Review the Develop History", "The develop-side history is reviewed", "git log --oneline develop"),
("Create Another Develop Version", "Develop has content different from the feature", "git show develop:README.md"),
("Open the Merge Editor", "Both branch versions are compared", "git diff feature/conflict..develop -- README.md"),
("See Both Versions Together", "The two README versions are displayed", "git diff feature/conflict..develop -- README.md"),
("Complete the Conflict Resolution in Source Control", "The resolved README is staged", "git status --short"),
("Review the Merge History", "The merge history is checked", "git log --oneline --decorate --graph --all"),
("Review the Final Local History", "The final local history is visible", "git log --oneline --decorate --graph --all"),
("Check GitHub Branches and Recent Pushes", "Remote branches are verified", "git branch -r"),
("Open the Final develop Branch", "develop contains README.md, app.py, and the resolved merge", "git show --stat --oneline develop"),
]


def main():
    doc = Document()
    section = doc.sections[0]
    section.top_margin = Inches(0.55)
    section.bottom_margin = Inches(0.55)
    section.left_margin = Inches(0.7)
    section.right_margin = Inches(0.7)
    title = doc.add_heading("GITFLOW LAB - 5", level=0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph("Git | GitHub | VS Code | Branches | Merge | Conflict | Conflict Resolution").alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_heading("Before You Start", level=1)
    doc.add_paragraph("Read one step at a time. Each step below follows the supplied Gitflow Lab 5 document and includes the command, purpose, and a screenshot captured from the student's actual Git repository.")
    doc.add_heading("Five Simple Words", level=1)
    doc.add_paragraph("Repository: Your project stored in Git.\nBranch: A separate line of work.\nCommit: A saved change in Git.\nPush: Send local changes to GitHub.\nMerge: Bring changes from one branch into another branch.")
    doc.add_heading("Gitflow Used in This Lab", level=1)
    doc.add_paragraph("main\n  |-- develop\n        |-- feature/login\n        |-- feature/conflict")
    doc.add_heading("Part A - Screenshot-Based Practical (Steps 1-58)", level=1)
    doc.add_paragraph("Each step below records the work completed in the student's GitHub repository.")

    for number, (title_text, explanation, command) in enumerate(steps, 1):
        output = run_python() if command == "python app.py" else run_git(*command.split()[1:]) if command.startswith("git ") else run_git("status")
        image = screenshot(number, title_text, command, output)
        doc.add_heading(f"Step {number}. {title_text}", level=2)
        doc.add_paragraph(f"What you see: {explanation}.")
        doc.add_paragraph(f"Command: {command}")
        doc.add_paragraph(f"Purpose: {explanation}.")
        doc.add_picture(str(image), width=Inches(7.0))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_heading("Final Revision", level=1)
    doc.add_paragraph("Create GitHub repository -> connect the local project -> create develop -> create feature/login -> commit -> push -> merge into develop -> create feature/conflict -> make different changes -> merge -> resolve the conflict -> stage -> commit -> push -> verify on GitHub.")
    doc.add_heading("Most Important Commands", level=1)
    for command in ["git status", "git branch", "git checkout -b branch-name", "git add file-name", "git commit -m \"message\"", "git push", "git merge branch-name", "python app.py"]:
        doc.add_paragraph(command, style="List Bullet")
    output_doc = OUT / "ASE-Gitflow_Lab_5.docx"
    doc.save(output_doc)
    print(f"Created {output_doc}")
    print(f"Created {len(steps)} screenshots")


if __name__ == "__main__":
    main()
