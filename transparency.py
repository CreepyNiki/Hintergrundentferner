"""
Eine kleine Anwendung, die den Hintergrund eines Bildes entfernt anhand dessen HSV-Farbbereichs.
"""


# Import von opencv und numpy
import cv2
import numpy as np

# Einlesen des Bildes
img = cv2.imread("testbild.jpg")

# Definieren des Farbbereichs, der als Hintergrund behandelt werden soll -> in diesem Fall ist der HSV-Farbbereich der Farbe grün ausgewählt
lower_hue = 40  # Untere Grenze für den Farbton
upper_hue = 80  # Obere Grenze für den Farbton
lower_saturation = 40  # Untere Grenze für die Sättigung
upper_saturation = 255  # Obere Grenze für die Sättigung

# Konvertieren des Bildes in den HSV-Farbbereich
hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Zuweisen des Bereichs an die beiden Variablen "lower_bound" und "upper_bound"
lower_bound = np.array([lower_hue, lower_saturation, 40], dtype=np.uint8)
upper_bound = np.array([upper_hue, upper_saturation, 255], dtype=np.uint8)

# Erzeugen einer Maske für den Hintergrund
mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

# Invertieren der Maske, um den Hintergrund auszuwählen
mask = cv2.bitwise_not(mask)

# Extrahieren Sie den Vordergrund (ohne Hintergrund)
result = cv2.bitwise_and(img, img, mask=mask)

# Abspeichern des Ergebnisses
cv2.imwrite("testbild_finished.png", result)