#!/bin/bash

# تحديث الحزم
echo "تحديث الحزم..."
pkg update -y && pkg upgrade -y

# تثبيت Python
echo "تثبيت Python..."
pkg install python -y

# تثبيت pip (مدير الحزم لـ Python)
echo "تثبيت pip..."
pkg install python-pip -y

# تثبيت OpenCV
echo "تثبيت OpenCV..."
pip install opencv-python

# تثبيت Tkinter (إذا كان متاحاً في Termux)
echo "تثبيت Tkinter..."
pkg install python-tkinter -y

# تثبيت Flask (اختياري إذا كنت تريد استخدامه)
echo "تثبيت Flask..."
pip install flask

# تثبيت مكتبات PIL (لمعالجة الصور)
echo "تثبيت PIL..."
pip install Pillow

# تثبيت termux-api (للوصول إلى ميزات الجهاز مثل الكاميرا)
echo "تثبيت termux-api..."
pkg install termux-api -y

# تأكيد انتهاء التثبيت
echo "تم تثبيت جميع المكتبات والمتطلبات بنجاح!"
