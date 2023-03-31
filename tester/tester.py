from screen_cutter import get_nicknames_images
import pytesseract
import cv2 as cv

def load_dictionary(path):
    dct = {}
    with open(path, 'r') as dictionary:
        number_of_lines = 66
        for i in range(number_of_lines):
            character = dictionary.readline().split()
            dct[character[1]] = character[0]
    return dct
def decode(number, dct):
    if len(number)<4:
        return ""
    nickname = ""
    for i in range(0, len(number), 2):
        if number[i:i+2] in dct:
            nickname += dct[number[i:i+2]]
        else:
            nickname += '#'
    return nickname

def result_proccessing(result, side):
    if result == '':
        return result
    if ' ' in result:
        return result.split()[side]
    else:
        return result
def remove_clantag(nickname):
    if not ('[' in nickname):
        return nickname
    if nickname.index('[') == 0:
        return nickname[nickname.index(']')+1:]
    else: return nickname[0:nickname.index('[')]
f_out = open("for_check.txt.txt", 'w')
dct = load_dictionary("../source/encoding_dictionary.txt")
ot = 1
do = 53
for i in range(ot, do+1):
    nicknames = get_nicknames_images("screens/"+'-'+str(i)+'.png', "../configs/1920.1080.125.txt")
    #f_out.write("скрин: "+str(i)+'\n')
    for i in range(0, 2):
        block_selector = -1
        if i == 0:
            block_selector = 0
        if i == 0: f_out.write("союзники"+'\n')
        else: f_out.write("противники"+'\n')
        for j in range(0, 7):
            img = nicknames[i][j]
            img = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_LINEAR)
            img = cv.threshold(img, 240, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)[1]
            #cv.imshow("1", img)
            #print(j+1, pytesseract.image_to_string(img, config="-c tessedit_char_whitelist=0,1,2,3,4,5,6,7,8,9")[0:-1])
            raw_result = pytesseract.image_to_string(img, config="-c tessedit_char_whitelist=0,1,2,3,4,5,6,7,8,9")[0:-1]
            proccessed_result = result_proccessing(raw_result, block_selector)
            decoded_result = decode(proccessed_result, dct)
            result_without_tag = remove_clantag(decoded_result)
            #print(result_without_tag)
            #f_out.write(str(j+1)+" "+result_without_tag+'\n')
            f_out.write(result_without_tag + '\n')
            #cv.waitKey(0)