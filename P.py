import cv2
import http.server
import socketserver
import threading

# فتح الكاميرا
camera = cv2.VideoCapture(0)

# الصفحة الرئيسية التي تعرض الفيديو
html = """
<html>
<head>
<title>مراقبة</title>
</head>
<body>
<h1>بث مباشر من كاميرا المراقبة</h1>
<img src="stream.mjpg" width="640" height="480"/>
</body>
</html>
"""

# خدمة HTTP لعرض الصفحة
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Content-type', 'multipart/x-mixed-replace; boundary=frame')
            self.end_headers()
            while True:
                success, frame = camera.read()
                if not success:
                    break
                else:
                    ret, buffer = cv2.imencode('.jpg', frame)
                    self.wfile.write(b'--frame\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', str(len(buffer)))
                    self.end_headers()
                    self.wfile.write(buffer.tobytes())

# تشغيل الخادم في سلسلة منفصلة
def start_server():
    PORT = 8000
    handler = MyHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"الخادم يعمل على المنفذ {PORT}")
        httpd.serve_forever()

# تشغيل الخادم في سلسلة منفصلة
server_thread = threading.Thread(target=start_server)
server_thread.start()

# اغلاق الكاميرا عند ايقاف الخادم
try:
    while True:
        pass
except KeyboardInterrupt:
    camera.release()
    print("تم إيقاف الخادم")
