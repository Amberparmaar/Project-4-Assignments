import qrcode
import cv2

# --- Encoder ---
data = 'https://q2-nextjs-blog-oq7h.vercel.app/'
qr_img = qrcode.make(data)
filename = 'AP_Coffee_Blog_QR.png'
qr_img.save(filename)
print('✅ QR Code Generated!')

# --- Decoder using OpenCV ---
img = cv2.imread(filename)
qr_detector = cv2.QRCodeDetector()
decoded_data, points, _ = qr_detector.detectAndDecode(img)

if decoded_data:
    print("✅ Decoded QR Code Data:", decoded_data)
else:
    print("❌ QR Code could not be decoded.")
