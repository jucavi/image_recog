import cv2
import pytesseract
import csv
import matplotlib.pyplot as plt

img = cv2.imread('images/image1.png')
img = cv2.resize(img, (1250, 1810))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(thresh, img) = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)
img = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
img = 255 - img

height , width = img.shape[:2]
print(height, width)
# start_row, start_col = int(width * 0), 0
# end_row, end_col = int(width * 0.2), int(height)

cv2.imshow('threshold_img', img)
cv2.waitKey(0)
# # cropped = img[start_row:end_row, start_col:end_col]
# start_row, start_col = end_row, 0
# end_row, end_col = int(end_row + width * 0.1), int(height)
# cropped = img[start_row:end_row, start_col:end_col]

start_row, start_col = 0, 0
end_row, end_col = 30, 0
while end_row < height:

    start_row, start_col = end_row, 0
    end_row, end_col = int(end_row + width * 0.05), int(height)
    cropped = img[start_row:end_row, start_col:end_col]
    print(end_row, end_col)
    cv2.imshow('threshold_img', cropped)
    cv2.waitKey(0)
cv2.destroyAllWindows()

# custom_config = r'--oem 3 --psm 6'
# details = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT, config=custom_config, lang='eng')

# print(details.keys())
# total_boxes = len(details['text'])

# for sequence_number in range(total_boxes):
#     if float(details['conf'][sequence_number]) > 35:
#         (x, y, w, h) = (details['left'][sequence_number], details['top'][sequence_number], details['width'][sequence_number],  details['height'][sequence_number])
#         threshold_img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# parse_text = []

# word_list = []
# last_word = ''
# for word in details['text']:
#     if word!='':
#         word_list.append(word)
#         last_word = word
#     if (last_word!='' and word == '') or (word==details['text'][-1]):
#         parse_text.append(word_list)
#         word_list = []

# with open('result_text.txt',  'w', newline="") as file:
#    csv.writer(file, delimiter=" ").writerows(parse_text)

# cv2.imshow('captured text', threshold_img)
# cv2.imshow('threshold_img', cropped)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
