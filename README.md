# 🚀 Django Task Management App
**Họ và tên:** Trần Khắc Liêm
**Mssv:** 22685251
**Lớp**: KHDL18A

# 🚀 Django Task Management App

## 💡 Giới thiệu
Ứng dụng quản lý công việc bằng Django, hỗ trợ **tạo, chỉnh sửa, xóa** và **cập nhật trạng thái công việc**.  
Người dùng có thể **quản lý tài khoản** và xem số **công việc trễ hạn**.  

---

## 🛠️ Cài đặt

### 1️⃣ Clone repository
```sh
git clone https://github.com/username/django-task-app.git
cd ptud-gk-de-2
```

### 2️⃣ Tạo virtual environment và cài đặt dependencies
```sh
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Chạy migration để tạo database
```sh
python manage.py makemigrations
python manage.py migrate
```

### 4️⃣ Tạo superuser để truy cập admin
```sh
python manage.py createsuperuser
```

---

## 🌐 Chạy ứng dụng
Sau khi cài đặt xong, chạy server bằng lệnh:  
```sh
python manage.py runserver
```
Truy cập ứng dụng tại: **http://localhost:8000/**  

---

## ✨ Tính năng
✅ Đăng ký, đăng nhập, quản lý tài khoản.  
✅ Tạo, sửa, xóa công việc.  
✅ Cập nhật trạng thái công việc.  
✅ Thông báo công việc trễ hạn.  

---

📌 **Liên hệ & đóng góp**: Nếu có lỗi hoặc muốn đóng góp, vui lòng tạo issue hoặc gửi pull request! 🚀

