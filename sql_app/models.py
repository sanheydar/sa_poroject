from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)


from sql_app.database import Base

#student

class Student(Base):
    __tablename__ = "Student"
    STID = Column(String , primary_key=True)
    FName = Column(String)
    LName = Column(String)
    Father = Column(String)
    Birth = Column(String)
    IDS  = Column(String)
    BornCity = Column(String)
    Address = Column(String)
    PostalCode = Column(String)
    CPhone = Column(String)
    HPhone = Column(String)
    Department = Column(String)
    Major  = Column(String)
    Married = Column(String)
    ID  = Column(String)
    SCourseids  = Column(String)
    LIDs  = Column(String)

#Professor

class Professor(Base):
    __tablename__ = "Professor"
    LID = Column(String , primary_key=True)
    FName = Column(String)
    LName = Column(String)
    ID  = Column(String)
    Department = Column(String)
    Major  = Column(String)
    Birth = Column(String)
    BornCity = Column(String)
    Address = Column(String)
    Postalcode = Column(String)
    CPhone = Column(String)
    HPhone = Column(String)
    LCourseIDs  = Column(String)


#course

class Course(Base):
    __tablename__ = "Courses"
    CID = Column(String, primary_key=True)
    CName = Column(String)
    Department = Column(String)
    Credit = Column(Integer)
