import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, maxLineGap=100)

    if lines is not None and len(lines) >= 2:
        line1 = lines[0][0]
        line2 = lines[1][0]
        x1,y1,x2,y2 = line1
        x3,y3,x4,y4 = line2

        # Calculate angle between the lines
        angle = np.arctan2(y4-y3, x4-x3) - np.arctan2(y2-y1, x2-x1)
        angle = np.degrees(angle)

        # Draw lines and display angle
        cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.line(frame, (x3, y3), (x4, y4), (0, 255, 0), 2)
        cv2.putText(frame, "Angle: {:.2f} degrees".format(angle), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
