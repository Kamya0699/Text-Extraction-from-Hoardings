# Text-Extraction-from-Hoardings
The proposed approach leads to the extraction of the text
from the complex background of an image of hoarding. We have used the Canny algorithm for
gray scale conversion and MSER (Maximally Stable Extremal Region) for text region
recognition to provide the required output.

 Objectives
● Edge Detection from a hoarding. (using Canny algorithm)
● Shortlisting the objects (Hoardings) with text. (using MSER algorithm)
● Text extraction using Tesseract - OCR

The proposed method includes 5 steps to follow:-
1. Input an RGB image
2. Conversion to grayscale image 
3. Edge detection (using Canny edge detection algorithm)
4. text region detection (using MSER algorithm)
5. character segmentation
