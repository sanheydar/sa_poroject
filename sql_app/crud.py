from sqlalchemy.orm import Session
import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

from sql_app import models , schemas


#student 
#گرفتن دانشجو
def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.STID == student_id).first()

#برای اضافه کردن دانشجو
def create_student(db: Session, student: schemas.Student):
    db_student = models.Student(STID=student.STID ,FName=student.FName,LName=student.LName,Father=student.Father,Birth=student.Birth,IDS=student.IDS,BornCity=student.BornCity,Address=student.Address,PostalCode=student.PostalCode,CPhone=student.CPhone,HPhone=student.HPhone,Department=student.Department,Major=student.Major,Married=student.Married,ID=student.ID,SCourseids=student.SCourseids,LIDs=student.LIDs)            
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

#تغیر یا بروزرسانی اطلاعات 
def update_student(db: Session, student_id: str, student: models.Student):
    db_student = db.query(models.Student).filter(models.Student.STID == student_id).first()
    if db_student is None:
        return "not found"
    else:
        for key, value in student.dict().items():
            setattr(db_student, key, value)
        db.commit()
        db.refresh(db_student)
        return db_student

#برای حذف اطلاعات
def removestudent(db: Session , Student_id: int):
    db_student = db.query(models.Student).filter(models.Student.STID == Student_id).first()
    db.delete(db_student)
    db.commit()

#Professor 
#گرفتن استاد
def get_professor(db: Session, Professor_id: int):
    return db.query(models.Professor).filter(models.Professor.LID == Professor_id).first()

#برای اضافه کردن استاد
def create_professoe(db: Session, professor: schemas.Professor):
    db_professor = models.Professor(LID=professor.LID ,FName=professor.FName,LName=professor.LName,ID=professor.ID,Department=professor.Department,Major=professor.Major,Birth=professor.Birth,BornCity=professor.BornCity,Address=professor.Address,Postalcode=professor.Postalcode,CPhone=professor.CPhone,HPhone=professor.HPhone,LCourseIDs=professor.LCourseIDs)            
    db.add(db_professor)
    db.commit()
    db.refresh(db_professor)
    return db_professor

#تغیر یا بروزرسانی اطلاعات 
def update_prefessor(db: Session, prefessor_id: str, prefessor: models.Professor):
    db_prefessor = db.query(models.Professor).filter(models.Professor.LID == prefessor_id).first()
    if db_prefessor is None:
        return "not found"
    else:
        for key, value in prefessor.dict().items():
            setattr(db_prefessor, key, value)
        db.commit()
        db.refresh(db_prefessor)
        return db_prefessor

#برای حذف اطلاعات
def removeprefessor(db: Session , Professor_id: int):
    db_professor = db.query(models.Professor).filter(models.Professor.LID == Professor_id).first()
    db.delete(db_professor)
    db.commit()


#course 
#گرفتن درس
def get_course(db: Session, Course_id: int):
    return db.query(models.Course).filter(models.Course.CID == Course_id).first()

#برای اضافه کردن درس
def create_cource(db: Session, course: schemas.Course):
    db_course = models.Course(CID=course.CID,CName=course.CName,Department=course.Department,Credit=course.Credit)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


#تغیر یا بروزرسانی اطلاعات 
def update_course(db: Session, course_id: str, course: models.Course):
    db_course = db.query(models.Course).filter(models.Course.CID == course_id).first()
    if  db_course is None:
        return "not found"
    else:
        for key, value in course.dict().items():
            setattr(db_course, key, value)
        db.commit()
        db.refresh(db_course)
        return db_course


#برای حذف اطلاعات
def removecourse(db: Session , Course_id: int):
    db_course = db.query(models.Course).filter(models.Course.CID == Course_id).first()
    db.delete(db_course)
    db.commit()