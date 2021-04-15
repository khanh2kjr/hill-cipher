from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import itertools

alphabets = [alphabet for alphabet in ascii_uppercase] #['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def split(word):
    return [char for char in word]

def convertToNumbers(char):
    return alphabets.index(char)

def divideTheArray(arr):
    result = []

    for i in range(0, len(arr) - 1, 2):
        elementArr = [arr[i], arr[i + 1]]
        result.append(elementArr)

    return result

def numEncryption(arr, key):
    result = []

    for i in range(0, len(arr)):
        numEncryptionFirst = (key[0][0] * arr[i][0]) + (key[0][1] * arr[i][1])
        numEncryptionSecond = (key[1][0] * arr[i][0]) + (key[1][1] * arr[i][1])
        numEncryption = [numEncryptionFirst % 26, numEncryptionSecond % 26]
        result.append(numEncryption)
    
    return result

def convertToString(alphabetString, plaintextNum):
    result = []
    
    for i in range(0, len(plaintextNum)):
        result.append(alphabetString[plaintextNum[i]])
    
    return result

def mainEncryption():
    inputPlaintext = inpPlaintext.get()
    key = inputKey.get()
    inpPlaintextArr = split(inputPlaintext) #['N', 'G', 'U', 'Y', 'E', 'N', 'V', 'A', 'N', 'K', 'H', 'A', 'N', 'H']
    keyArr = split(key) #['A', 'B', 'C', 'D']
    
    inputPlaintextArrNum = list(map(convertToNumbers, inpPlaintextArr)) #[13, 6, 20, 24, 4, 13, 21, 0, 13, 10, 7, 0, 13, 7]
    keyArrNum = list(map(convertToNumbers, keyArr)) #[0, 1, 2, 3]

    keyArrMatrix = [[keyArrNum[0], keyArrNum[1]], [keyArrNum[2], keyArrNum[3]]] #[[0, 1], [2, 3]]
    plaintextArrNumAfter = divideTheArray(inputPlaintextArrNum) #[[13, 6], [20, 24], [4, 13], [21, 0], [13, 10], [7, 0], [13, 7]]
    
    plaintextArrNumEncryption = numEncryption(plaintextArrNumAfter, keyArrMatrix) #[[6, 18], [24, 8], [13, 21], [0, 16], [10, 4], [0, 14], [7, 21]]
    
    flatPlaintextNum = list(itertools.chain.from_iterable(plaintextArrNumEncryption)) #[6, 18, 24, 8, 13, 21, 0, 16, 10, 4, 0, 14, 7, 21]
    
    alphabetJoin = ''.join(alphabets) #ABCDEFGHIJKLMNOPQRSTUVWXYZ
    
    stringEncryptionArr = convertToString(alphabetJoin, flatPlaintextNum) #['G', 'S', 'Y', 'I', 'N', 'V', 'A', 'Q', 'K', 'E', 'A', 'O', 'H', 'V']
    
    resultEncryption = ''.join(stringEncryptionArr) #GSYINVAQKEAOHV - Kết quả đã được mã hóa từ bản rõ NGUYENVANKHANH với key là ABCD
    
    tb_x1.insert(0,resultEncryption)

def mainDecryption():
    inputPlaintext = inpPlaintext.get()
    tb_x2.insert(0, inputPlaintext)

def mainReset():
    inpPlaintext.delete(0, END)
    inputKey.delete(0, END)
    tb_x1.delete(0, END)
    tb_x2.delete(0, END)

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

btnEncryption = Button(gpt, text="Mã hóa",font=("Consolas", 15), fg="black", bg="orange", width=10, height=1, command=mainEncryption)
btnEncryption.pack()

btnDecryption = Button(gpt, text="Giải mã",font=("Consolas", 15), fg="black", bg="orange", width=10, height=1, command=mainDecryption)
btnDecryption.pack()

titleDe = Label(gpt, text="Kết quả giải mã", font=("Arial" "bold"), fg="red")
titleDe.pack()

tb_x2 = Entry(gpt, width=30, font=("Consolas", 12))
tb_x2.pack()

btnReset = Button(gpt, text="Reset",font=("Consolas", 15), fg="black", bg="orange", width=10, height=1, command=mainReset)
btnReset.pack()

gpt.mainloop()
