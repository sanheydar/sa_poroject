# پروژه انتخاب واحد
که با استفاده از fastapiوdatabase این برنامه را نوشتیم و در زیر چگونگی کار هرکدام را بررسی می‌کنیم 
اولین بخش که بررسی می‌کنیم:
# فایل database.py 
این فایل  تنظیمات پایه‌ای برای اتصال به پایگاه داده با استفاده از SQLAlchemy را فراهم می‌کند و امکانات لازم برای تعریف مدل‌ها و مدیریت سشن‌ها را ارائه می‌دهد. این فایل شامل چند بخش اصلی است که در زیر توضیح میدهیم
<img src="https://github.com/sanheydar/sa_poroject/blob/main/one.png?raw=true" />


بخش اول شامل ایمپورت‌های لازم از کتابخانه SQLAlchemy برای ایجاد موتور پایگاه داده، تعریف مدل‌ها و ایجاد سشن‌ها است.بعد URL پایگاه داده تعریف شده است.  از یک پایگاه داده SQLite با نام sql_app.db استفاده می‌شود که در دایرکتوری جاری قرار دارد.بعد موتور پایگاه داده با استفاده از URL تعریف شده ایجاد می‌شود. تنظیمات connect_args={"check_same_thread": False} برای سازگاری با SQLite در هنگام استفاده از چندین نخ (thread) استفاده می‌شود.
بعد یک کلاس سشن محلی (SessionLocal) ایجاد می‌شود که برای برقراری ارتباط با پایگاه داده استفاده خواهد شد. پارامترهای autocommit=False و autoflush=False به این معنا هستند که تغییرات به صورت خودکار کامیت  نشوند.بعد یک کلاس پایه به نام Base ایجاد می‌شود که از آن برای تعریف مدل‌های پایگاه داده استفاده خواهد شد.

# فایل models.py 
این فایل شامل تعریف مدل‌های داده‌ای با استفاده از SQLAlchemy است که نمایانگر جداول پایگاه داده هستند. هر مدل شامل ویژگی‌هایی است که به ستون‌های جدول متناظر در پایگاه داده نگاشت می‌شوند. این مدل‌ها به ما اجازه می‌دهند تا به راحتی با داده‌های پایگاه داده (database)کار کنیم، از جمله ایجاد، خواندن، به‌روزرسانی و حذف داده‌ها.در زیر عملکرد آن را توضیح میدهیم

بخش اول شامل ایمپورت‌های لازم از SQLAlchemy برای تعریف ستون‌ها و نوع‌های داده، تنظیم مسیر سیستم برای دسترسی به فایل‌های دیگر و ایمپورت Base از فایل database.py است که برای ایجاد کلاس‌های مدل استفاده می‌شود.کلاس (Student)یک مدل برای جدول Student در پایگاه داده تعریف می‌کند. هر خصوصیت کلاس یک ستون در جدول پایگاه داده را نشان می‌دهد. STID به عنوان کلید اصلی جدول تعریف شده.
کلاس(Professor) یک مدل برای جدول Professor در پایگاه داده تعریف می‌کند. LID به عنوان کلید اصلی جدول تعریف شده.
 کلاس (Course)یک مدل برای جدول Course در پایگاه داده تعریف می‌کند. CID به عنوان کلید اصلی جدول تعریف شده.

# فایل schemas.py 
این فایل شامل تعریف مدل‌های داده‌ای و توابع اعتبارسنجی است که اطمینان حاصل می‌کنند اطلاعات ورودی مطابق با الگوها و فرمت‌های مشخص شده باشند. در صورت عدم تطابق، پیام‌های خطای مناسبی به کاربر بازگردانده می‌شود.در زیر توضیحی درباره عملکرد آن می‌گوییم

بخش اول شامل ایمپورت‌های مورد نیاز برای تایپ‌ها، ریگولار اکسپرشن‌ها، مدیریت خطاها با FastAPI و استفاده از Pydantic برای تعریف مدل‌ها است.
کلاس  Studentمدل مشخصات یک دانشجو را شامل می‌شود.
کلاسProfessor مدل مشخصات یک استاد را شامل می‌شود.
کلاس Course مدل مشخصات یک درس را شامل می‌شود.


تابع اعتبار سنجی دانشجو(validate_student) است .
این تابع صحت اطلاعات ورودی دانشجو را با استفاده از الگوهای مختلف بررسی می‌کند و در صورت وجود خطاها، یک استثناء HTTPException با کد وضعیت 400 برمی‌گرداند.

تابع اعتبارسنجی استاد (validate_professor)است.
این تابع صحت اطلاعات ورودی استاد را بررسی می‌کند و در صورت وجود خطاها، یک استثناء HTTPException با کد وضعیت 400 برمی‌گرداند.

تابع اعتبارسنجی درس (validate_course)است
این تابع صحت اطلاعات ورودی درس را بررسی می‌کند و در صورت وجود خطاها، یک استثناء HTTPException با کد وضعیت 404 برمی‌گرداند.

# فایل crud.py
این اسکریپت شامل مجموعه‌ای از توابع CRUD (ایجاد، خواندن، به‌روزرسانی، حذف) برای مدیریت داده‌های مربوط به دانشجویان، اساتید و دروس در یک پایگاه داده است. از SQLAlchemy برای مدیریت ارتباط با پایگاه داده و انجام عملیات‌های مختلف استفاده شده است.در زیر بخش های آنرا توضیح میدهیم

این بخش ماژول‌های لازم را وارد می‌کند و مسیر سیستم را تنظیم می‌کند تا به ماژول‌های models و schemas دسترسی داشته باشد.

 تابع get_student دانشجویی را با استفاده از student_id از پایگاه داده می‌گیرد و همین نوع تابع برای گرفتن استاد و درس نیز استفاده می‌شود با پارامتر های مخصوص به خود 
 
 تابع create_student یک رکورد جدید از دانشجو را در پایگاه داده ایجاد می‌کند.و همین نوع تابع با پارامتر های مخصوص به خود استاد و درس را نیز به پایگاه داده اضافه می کند. 

 تابع update_student اطلاعات یک دانشجو را به‌روزرسانی می‌کند.و همین نوع تابع با پارامتر های مخصوص به خود استاد و درس را نیز اطلاعاتشان به روز رسانی می‌کند.

تابعremovestudent یک دانشجو را از پایگاه داده حذف می‌کند.همین نوع تابع با پارامترهای مخصوص به خود استاد و درس را نیز از پایگاه داده حذف میکند. 



