from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

students = {
    "S001": {"name": "Ravu", "marks": 84, "grade": "A"},
    "S002": {"name": "Ravi", "marks": 74, "grade": "B"},
    "S003": {"name": "Raju", "marks": 64, "grade": "C"}
}

# Input Schema for Student
class MarksSubmission(BaseModel):
    student_id:str
    marks:int
    subject:str



@app.get("/students/{student_id}")
def get_student(student_id:str):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
        
    return students[student_id]


@app.post("/students/submit_marks")
def submit_marks(marks_submission:MarksSubmission):

    if marks_submission.student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    if marks_submission.marks < 0 or marks_submission.marks > 100:
        raise HTTPException(status_code=400, detail="Marks should be between 0 and 100")

    if marks_submission.subject.strip() == "":
        raise HTTPException(status_code=400, detail="Subject cannot be empty")

    try:
        students[marks_submission.student_id]["marks"] = marks_submission.marks

        return {
        "message": f"Marks for student {students[marks_submission.student_id]["name"]} in subject {marks_submission.subject} submitted successfully.",
        "student": students[marks_submission.student_id]["name"],
        "marks":marks_submission.marks,
    }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while submitting marks: {str(e)}")


  