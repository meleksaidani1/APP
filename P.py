import cv2
import threading
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk

# فتح الكاميرا
camera = cv2.VideoCapture(0)

# وظيفة لعرض الفيديو في إطار Tkinter
def update_frame(label):
    ret, frame = camera.read()
    if ret:
        # تحويل إطار الفيديو إلى صورة باستخدام PIL
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.configure(image=imgtk)
    label.after(10, update_frame, label)

# إنشاء واجهة المستخدم GUI باستخدام Tkinter
def create_gui():
    root = tk.Tk()
    root.title("نظام المراقبة")

    # إعداد نافذة العرض
    label = Label(root)
    label.pack()

    # زر لإيقاف الفيديو
    def stop_camera():
        camera.release()
        root.quit()

    stop_button = tk.Button(root, text="إيقاف", command=stop_camera)
    stop_button.pack()

    # بدء عرض الفيديو
    update_frame(label)
    root.mainloop()

# تشغيل الواجهة في سلسلة منفصلة
gui_thread = threading.Thread(target=create_gui)
gui_thread.start()
