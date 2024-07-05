from typing import Union
import re
from fastapi import HTTPException
from pydantic import BaseModel


#student

class Student(BaseModel):
    STID: str
    FName: str
    LName: str
    Father: str
    Birth: str
    IDS : str
    BornCity:str
    Address: str
    PostalCode: str
    CPhone: str
    HPhone: str
    Department: str
    Major : str
    Married: str
    ID : str
    SCourseids : str
    LIDs : str


def validate_student(student):
    pattern_farsi=r"[آ-ی]+"
    pattern_stid= r"^(400|401|402)114150((0[1-9])|([1-9][0-9]))$"
    #به خاطر قابل استفاده بودن کد تا 30 سال دیگر تاریخ تولد تا 1403 گذاشتم
    pattern_birth = r"^(13[0-9]{2}|140[0-3])/((0[1-9])|(1[0-2]))/((0[1-9])|([1-2][0-9])|(3[0-1]))$"
    pattern_ids = r"^([1-9][0-9]{5})/([آ-ی])/([1-9][0-9])$"
    pattern_borncity= r"^(تهران)|(تبریز)|(آبادان)|(ارومیه)|(ازنا)|(اردبیل)|(اسلام شهر)|(آمل)|(اصفهان)|(کرج)|(ایلام)|(بوشهر)|(شهرکرد)|(بیرجند)|(مشهد)|(بجنورد)|(اهواز)|(زنجان)|(سمنان)|(زاهدان)|(شیراز)|(قزوین)|(قم)|(سنندج)|(کرمان)|(کرمانشاه)|(یاسوج)|(گرگان)|(رشت)|(خرم‌آباد)|(ساری)|(اراک)|(بندرعباس)|(همدان)|(یزد)$"
    pattern_cphone = r"^((09)|(\+989))\d{9}$"
    pattern_hphone = r"^(0[1-9][0-9])([1-9](\d){7})$"
    pattern_department= r"^(فنی و مهندسی)|(منابع طبیعی)|(دامپزشکی)|(اقتصاد)|(علوم پایه)|(علوم انسانی)|(کشاورزی)$"
    pattern_major = r"^(مهندسی آب)|(مهندسی عمران)|(مهندسی مکانیک)|(مهندسی معدن)|(مهندسی برق)|(مهندسی شهرسازی)|(مهندسی کامپیوتر)|(مهندسی پلیمر)|(مهندسی مواد)|(مهندسی شیمی)$"
    pattern_married = r"^(مجرد)|(متاهل)$"
    SCourseids = student.SCourseids.split(",")
    LIDs = student.LIDs.split(",")
    pattern_id = r"^\d{10}$"
    def check_id(id):
        l = 10
        sum = 0
        for i in range(0 , l - 1):
                code = ord(id[i])
                code -= 48
                sum = sum + code *(l - i)
        r = sum % 11
        code = ord(id[l - 1])
        code -= 48
        if r > 2:
            r = 11 - r
        if r == code:
            return True
    error= {}
    if re.fullmatch(pattern=pattern_stid,string=student.STID)== None :
        error["STID"]= "شماره دانشجویی وارد شده درست نمی باشد"
    if re.fullmatch(pattern=pattern_farsi,string=student.FName)== None or len(student.FName)>10:
        error["FName"] = "نام باید  با حروف فارسی,بدون علائم,حداکثر 10 کاراکتر  باشد"
    if re.fullmatch(pattern=pattern_farsi,string=student.LName)== None or len(student.LName)>10:
        error["LName"] = "نام خانوادگی  باید  با حروف فارسی,بدون علائم,حداکثر 10 کاراکتر باشد"
    if re.fullmatch(pattern=pattern_farsi,string=student.Father)== None or len(student.Father)>10:
        error["Father"] = "نام پدر  باید با حروف فارسی,,بدون علائم,حداکثر ده کاراکتر باشد"
    if re.fullmatch(pattern=pattern_birth,string=student.Birth)== None:
        error["Birth"] = "تاریخ تولد نا معتبر است"
    if re.fullmatch(pattern=pattern_ids,string=student.IDS)== None:
        error["IDS"] = "سریال شناستانه نا معتبر است"
    if re.fullmatch(pattern=pattern_borncity,string=student.BornCity)== None:
        error["BornCity"] = "شهر محل تولد نا معتبر است "     
    if len(student.Address) > 100 :
        error["Address"] = "آدرس حداکثر باید 100 کراکتر است"
    if len(student.PostalCode) != 10 or student.PostalCode.isdigit()==False :
        error["PostalCode"] = "کد پستی 10 رقم است"
    if re.fullmatch(pattern=pattern_cphone,string=student.CPhone)== None:
        error["CPhone"] = "شماره تلفن نا معتبر است"        
    if re.fullmatch(pattern=pattern_hphone,string=student.HPhone)== None:
        error["HPhone"] = "شماره تلفن ثابت نا معتبر است"              
    if re.fullmatch(pattern=pattern_department,string=student.Department)== None:
        error["Department"] = "دانشکده ورودی نامعتبر است"
    if re.fullmatch(pattern=pattern_major,string=student.Major)== None:
        error["Major"] = "رشته تحصیلی نا معتبر است" 
    if re.fullmatch(pattern=pattern_married,string=student.Married)== None:
        error["Married"] ="وضعیت تاهل را مشخص کنید"
    if re.fullmatch(pattern=pattern_id,string=student.ID) == None or check_id(student.ID) != True :
        error["ID"] = "کد ملی نا معتبر است"
    for code in SCourseids:
        if len(code) != 5 or code.isdigit()==False :
            error["SCourseid"] = " کد درس ورودی باید 5 رقم  و با, از هم جدا شده اند"
    for code in LIDs:
        if len(code) != 6 or code.isdigit()==False :
            error["LIDs"] = " کد استاد ورودی باید 6 رقم  و با,از هم جدا شده اند"
    if error:
        raise HTTPException(detail=error , status_code=400)
    
    


#Professor

class Professor(BaseModel):
    LID: str
    FName: str
    LName:str
    ID: str
    Department: str
    Major:str
    Birth:str
    BornCity:str
    Address:str
    Postalcode:str
    CPhone:str
    HPhone:str
    LCourseIDs:str

def validate_professor(professor):
    pattern_farsi=r"[آ-ی]+"
    pattern_department= r"^(فنی و مهندسی)|(اقتصاد)|(منابع طبیعی)|(کشاورزی)|(دامپزشکی)|(علوم پایه)|(علوم انسانی)$"
    pattern_major = r"^(مهندسی آب)|(مهندسی عمران)|(مهندسی مکانیک)|(مهندسی معدن)|(مهندسی برق)|(مهندسی شهرسازی)|(مهندسی کامپیوتر)|(مهندسی پلیمر)|(مهندسی مواد)|(مهندسی شیمی)$"
    pattern_birth = r"^(13[0-9]{2})/((0[1-9])|(1[0-2]))/((0[1-9])|([1-2][0-9])|(3[0-1]))$"
    pattern_borncity= r"^(تهران)|(تبریز)|(آبادان)|(ارومیه)|(ازنا)|(اردبیل)|(اسلام شهر)|(آمل)|(اصفهان)|(کرج)|(ایلام)|(بوشهر)|(شهرکرد)|(بیرجند)|(مشهد)|(بجنورد)|(اهواز)|(زنجان)|(سمنان)|(زاهدان)|(شیراز)|(قزوین)|(قم)|(سنندج)|(کرمان)|(کرمانشاه)|(یاسوج)|(گرگان)|(رشت)|(خرم‌آباد)|(ساری)|(اراک)|(بندرعباس)|(همدان)|(یزد)$"
    pattern_cphone = r"^((09)|(\+989))\d{9}$"
    pattern_hphone = r"^(0[1-9][0-9])([1-9](\d){7})$"
    LCourseIDs = professor.LCourseIDs.split(",")
    pattern_id = r"^\d{10}$"
    def check_id(id):
        l = 10
        sum = 0
        for i in range(0 , l - 1):
                code = ord(id[i])
                code -= 48
                sum = sum + code *(l - i)
        r = sum % 11
        code = ord(id[l - 1])
        code -= 48
        if r > 2:
            r = 11 - r
        if r == code:
            return True
    error= {}
    if len(professor.LID) != 6 or professor.LID.isdigit()==False :
        error["LID"]= "کد استاد نا معتبر است"
    if re.fullmatch(pattern=pattern_farsi,string=professor.FName)== None or len(professor.FName)>10:
        error["FName"] = "نام  باید  با حروف فارسی,بدون علائم,حداکثر 10 کاراکتر  باشد"
    if re.fullmatch(pattern=pattern_farsi,string=professor.LName)== None or len(professor.LName)>10:
        error["LName"] = "نام خانوادگی  باید  با حروف فارسی,بدون علائم,حداکثر 10 کاراکتر باشد"
    if re.fullmatch(pattern=pattern_id,string=professor.ID) == None or check_id(professor.ID) != True :
        error["ID"] = "کد ملی به اشتباه وارد شده است"
    if re.fullmatch(pattern=pattern_department,string=professor.Department)== None:
        error["Department"] = "دانشکده ورودی نامعتبر است"
    if re.fullmatch(pattern=pattern_major,string=professor.Major)== None:
        error["Major"] =  "رشته تحصیلی نا معتبر است"
    if re.fullmatch(pattern=pattern_birth,string=professor.Birth)== None:
        error["Birth"] = "تاریخ تولد نا معتبر است"
    if re.fullmatch(pattern=pattern_borncity,string=professor.BornCity)== None:
        error["BornCity"] ="شهر محل تولد نا معتبر است"   
    if len(professor.Address) > 100 :
        error["Address"] =  "آدرس حداکثر باید 100 کراکتر است"
    if len(professor.Postalcode) != 10 or professor.Postalcode.isdigit()==False :
        error["Postalcode"] = "کد پستی 10 رقم است"
    if re.fullmatch(pattern=pattern_cphone,string=professor.CPhone)== None:
        error["CPhone"] = "شماره تلفن نا معتبر است"        
    if re.fullmatch(pattern=pattern_hphone,string=professor.HPhone)== None:
        error["HPhone"] = "شماره تلفن ثابت نا معتبر است"        
    for code in LCourseIDs:
        if len(code) != 5 or code.isdigit()==False :
            error["LCourseIDs"] = " کد درس ورودی باید 5 رقم  و با , از هم جدا شده اند"
    if error:
        raise HTTPException(detail= error, status_code=400)
#course

class Course(BaseModel):
    CID: str 
    CName: str 
    Department: str 
    Credit: int
    
def validate_course(course):
    pattern_farsi=r"[آ-ی]+"
    pattern_department= r"^(فنی و مهندسی)|(منابع طبیعی)|(دامپزشکی)|(اقتصاد)|(علوم پایه)|(علوم انسانی)|(کشاورزی)$"
    pattern_credit = r"[1-4]"
    error = {}
    if len(course.CID) != 5 or course.CID.isdigit()==False :
        error["CID"]="کد درس نامعتبر است"
    if re.fullmatch(pattern=pattern_farsi,string=course.CName)== None or len(course.CName)>25:
        error["CName"] = "نام درس باید  با حروف فارسی,بدون علائم,حداکثر 25 کاراکتر  باشد"
    if re.fullmatch(pattern=pattern_department,string=course.Department)== None:
        error["Department"] ="دانشکده ورودی نامعتبر است"
    if re.fullmatch(pattern=pattern_credit,string=str(course.Credit))== None :
        error["Credit"] = "تعداد واحد عددی بین1 تا 4 است"
    if error:
        raise HTTPException(detail=error , status_code=404)