from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import itertools

# Tạo mảng chữ cái Alphabet [A, B,..., Z]
alphabets = [alphabet for alphabet in ascii_uppercase] 

# Hàm chuyển chuỗi thành mảng ký tự
def split(word):
    return [char for char in word]

def removeSpaceString(strsArr):
    result = []

    for i in range(0, len(strsArr)):
        if (strsArr[i] != ' '):
            result.append(strsArr[i])
    
    return result

def convertToNumbers(char):
    return alphabets.index(char)

# Hàm chia mảng thành các mảng con m phần tử
def divideTheArray(arr, m):
    result = []

    for i in range(0, len(arr) - 1, m):
        elementArr = [arr[i], arr[i + 1]]
        result.append(elementArr)

    return result

def matrixMultiplication(arr, key):
    result = []

    for i in range(0, len(arr)):
        # Công thức nhân ma trận bản rõ số với khóa số
        numEncryptionFirst = (key[0] * arr[i][0]) + (key[1] * arr[i][1])
        numEncryptionSecond = (key[2] * arr[i][0]) + (key[3] * arr[i][1])

        # Tạo phần tử mảng con trong mảng cha (ma trận 2 chiều)
        numEncryptions = [numEncryptionFirst, numEncryptionSecond]
        result.append(numEncryptions)
    
    return result

def mod(numsArr):
    return numsArr % 26

def convertToString(alphabetString, plaintextNum):
    result = []
    
    for i in range(0, len(plaintextNum)):
        result.append(alphabetString[plaintextNum[i]])
    
    return result

def mainEncryption():
    # Lấy ra giá trị ở 2 ô input bản rõ và khóa K
    inputPlaintext = inpPlaintext.get()
    key = inputKey.get()

    # Chuyển bản rõ và khóa K thành một mảng các ký tự
    inpPlaintextArr = removeSpaceString(split(inputPlaintext.upper()))
    keyArr = removeSpaceString(split(key.upper()))
    
    lenKey = len(keyArr)
    m = int(lenKey / 2)

    #Ta chuyển đổi 2 mảng ký tự ở trên thành mảng các số tương ứng từ 0 đến 25 ( dựa vào vị trí của các ký tự trong mảng alphabets )
    inputPlaintextArrNum = list(map(convertToNumbers, inpPlaintextArr))
    keyArrNum = list(map(convertToNumbers, keyArr))

    # Do độ dài khóa K = 4 => m = K / 2 = 2 nên ta chia bản rõ và khóa K thành các đoạn con có độ dài bằng 2
    plaintextArrNumAfter = divideTheArray(inputPlaintextArrNum, m) #[[13, 6], [20, 24], [4, 13], [21, 0], [13, 10], [7, 0], [13, 7]]

    # Kết quả sau khi tính toán nhân cộng từ bản rõ với khóa K và chia lấy dư cho 26 ta được kết quả sau
    plaintextArrNumEncryption = matrixMultiplication(plaintextArrNumAfter, keyArrNum) #[[6, 44], [24, 112], [13, 47], [0, 42], [10, 56], [0, 14], [7, 47]]
    
    # Kết quả sau khi tính được ta sẽ làm phẳng mảng 2 chiều ở trên về mảng 1 chiều
    flatPlaintextNum = list(itertools.chain.from_iterable(plaintextArrNumEncryption)) #[6, 44, 24, 112, 13, 47, 0, 42, 10, 56, 0, 14, 7, 47]
    
    # Chia lấy dư cho 26
    plaintextNumMod = list(map(mod, flatPlaintextNum)) #[6, 18, 24, 8, 13, 21, 0, 16, 10, 4, 0, 14, 7, 21]

    alphabetJoin = ''.join(alphabets) #ABCDEFGHIJKLMNOPQRSTUVWXYZ
    
    # Chuyển từ mảng số sang mảng ký tự dựa vào vị trí của chuỗi alphabet
    stringEncryptionArr = convertToString(alphabetJoin, plaintextNumMod) #['G', 'S', 'Y', 'I', 'N', 'V', 'A', 'Q', 'K', 'E', 'A', 'O', 'H', 'V']
    
    #Kết quả đã được mã hóa từ bản rõ NGUYENVANKHANH với key là ABCD
    resultEncryption = ''.join(stringEncryptionArr) 
    
    tb_x1.insert(0,resultEncryption)

def mainDecryption():
    inputPlaintext = inpPlaintext.get()
    tb_x2.insert(0, inputPlaintext)

def mainReset():
    inpPlaintext.delete(0, END)
    inputKey.delete(0, END)
    tb_x1.delete(0, END)
    tb_x2.delete(0, END)

# Khởi tạo form cho chương trình
gpt = Tk()

gpt.title("Hill encryption")

titleImportPlaintext = Label(gpt, text="Nhập bản rõ", font=("Arial" "bold"))
titleImportPlaintext.pack()

inpPlaintext = Entry(gpt, width=30, font=("Consolas", 12))
inpPlaintext.pack()

titleImportKey = Label(gpt, text="Nhập khóa K", font=("Arial" "bold"))
titleImportKey.pack()

inputKey = Entry(gpt, width=30, font=("Consolas", 12))
inputKey.pack()

titleResult = Label(gpt, text="Kết quả mã hóa", font=("Arial" "bold"), fg="red")
titleResult.pack()

tb_x1 = Entry(gpt, width=30, font=("Consolas", 12))
tb_x1.pack()

btnEncryption = Button(gpt, text="Mã hóa",font=("Consolas", 15), fg="white", bg="blue", width=10, height=1, command=mainEncryption)
btnEncryption.pack()

btnDecryption = Button(gpt, text="Giải mã",font=("Consolas", 15), fg="white", bg="blue", width=10, height=1, command=mainDecryption)
btnDecryption.pack()

titleDe = Label(gpt, text="Kết quả giải mã", font=("Arial" "bold"), fg="red")
titleDe.pack()

tb_x2 = Entry(gpt, width=30, font=("Consolas", 12))
tb_x2.pack()

btnReset = Button(gpt, text="Reset",font=("Consolas", 15), fg="white", bg="blue", width=10, height=1, command=mainReset)
btnReset.pack()

gpt.mainloop()
