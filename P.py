from flask import Flask, Response
import cv2

app = Flask(__name__)

# فتح الكاميرا (0 تعني الكاميرا الخلفية، 1 للكاميرا الأمامية)
camera = cv2.VideoCapture(0)

def generate_frames():
    while True:
        # قراءة الإطار من الكاميرا
        success, frame = camera.read()
        if not success:
            break
        else:
            # ترميز الإطار بتنسيق JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            
            # بث الإطار كجزء من الفيديو المستمر
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    # عرض بث الفيديو على هذه الصفحة
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
