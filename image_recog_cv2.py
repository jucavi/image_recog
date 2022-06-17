import cv2
import pytesseract
import csv

image = cv2.imread('images/image1.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# cv2.imshow('threshold_image', threshold_image)
image = 255 - image
custom_config = r'--oem 3 --psm 6'
details = pytesseract.image_to_data(threshold_image, output_type=pytesseract.Output.DICT, config=custom_config, lang='eng')

print(details.keys())
total_boxes = len(details['text'])

for sequence_number in range(total_boxes):
    if float(details['conf'][sequence_number]) > 35:
        (x, y, w, h) = (details['left'][sequence_number], details['top'][sequence_number], details['width'][sequence_number],  details['height'][sequence_number])
        threshold_img = cv2.rectangle(threshold_image, (x, y), (x + w, y + h), (255, 255, 255), 2)

parse_text = []

word_list = []
last_word = ''
for word in details['text']:
    if word!='':
        word_list.append(word)
        last_word = word
    if (last_word!='' and word == '') or (word==details['text'][-1]):
        parse_text.append(word_list)
        word_list = []

with open('result_text.txt',  'w', newline="") as file:
   csv.writer(file, delimiter=" ").writerows(parse_text)

cv2.imshow('captured text', threshold_image)
cv2.waitKey(0)
cv2.destroyAllWindows()