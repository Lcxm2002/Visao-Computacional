import cv2
import pytesseract
import test

def confusionMatrix(database):
    tp = 0
    fn = 0
    fp = 0
    tn = 0

    for i in database:
        if i[0] == 'i_l' or i[0] == 'I_u':
            if i[2] == 0:
                tp+=1
            else:
                fn+=1
        else:
            if i[2] == 0:
                tn+=1
            else:
                fp+=1

    accuracy = (tp+tn)/(tp+tn+fp+fn)
    precision = (tp)/(tp+fp)
    recall = (tp)/(tp+fn)
    f1Score = (2*precision*recall)/(precision+recall)

    print("----------Matrix de confusão----------")
    print(f"True Positive: {tp} | False Positive: {fp}\nFalse Negative: {fn} | True Negative: {tn}\n")

    print("--------------Pontuation--------------")
    print(f"Acurácia: {round(accuracy*100, 2)}%\nPrecisão: {round(precision*100, 2)}%\nRevocação: {round(recall*100, 2)}%\nF1-Score: {round(f1Score*100, 2)}%")

def recognizeImg(pathImg):
    # Lendo a imagem
    img = cv2.imread(pathImg)

    # Caminho onde foi instalado o PYTESSERACT(sem isso seu código dará um erro)
    pytesseract.pytesseract.tesseract_cmd = r"D:\Program Files\tesseract\tesseract.exe"

    # Reconhecendo a imagem e retornando em string o reconhecimento da imagem
    return pytesseract.image_to_string(img, lang="eng", config=r"--oem 0 --psm 10 -c tessedit_char_blacklist=0123456789").strip().lower()

def recognizeAll():
    database = []
    count = 0

    directory = 1
    while directory <= 10:
        if directory == 1:
            for i in range(1000):
                if i < 10:
                    path = f"./dataset/a_l/train_61/train_61_0000{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
                elif i < 100:
                    path = f"./dataset/a_l/train_61/train_61_000{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
                else:
                    path = f"./dataset/a_l/train_61/train_61_00{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
        elif directory == 2:
            for i in range(1000):
                if i < 10:
                    path = f"./dataset/A_u/train_41/train_41_0000{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
                elif i < 100:
                    path = f"./dataset/A_u/train_41/train_41_000{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
                else:
                    path = f"./dataset/A_u/train_41/train_41_00{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
        elif directory == 3:
            for i in range(1000):
                if i < 10:
                    path = f"./dataset/e_l/train_65/train_65_0000{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
                elif i < 100:
                    path = f"./dataset/e_l/train_65/train_65_000{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
                else:
                    path = f"./dataset/e_l/train_65/train_65_00{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
        elif directory == 4:
            for i in range(1000):
                if i < 10:
                    path = f"./dataset/E_u/train_45/train_45_0000{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
                elif i < 100:
                    path = f"./dataset/E_u/train_45/train_45_000{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
                else:
                    path = f"./dataset/E_u/train_45/train_45_00{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
        elif directory == 5:
            for i in range(1000):
                if i < 10:
                    path = f"./dataset/i_l/train_69/train_69_0000{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
                elif i < 100:
                    path = f"./dataset/i_l/train_69/train_69_000{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
                else:
                    path = f"./dataset/i_l/train_69/train_69_00{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
        elif directory == 6:
            for i in range(1000):
                if i < 10:
                    path = f"./dataset/I_u/train_49/train_49_0000{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
                elif i < 100:
                    path = f"./dataset/I_u/train_49/train_49_000{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
                else:
                    path = f"./dataset/I_u/train_49/train_49_00{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
        elif directory == 7:
            for i in range(1000):
                if i < 10:
                    path = f"./dataset/o_l/train_6f/train_6f_0000{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
                elif i < 100:
                    path = f"./dataset/o_l/train_6f/train_6f_000{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
                else:
                    path = f"./dataset/o_l/train_6f/train_6f_00{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
        elif directory == 8:
            for i in range(1000):
                if i < 10:
                    path = f"./dataset/O_u/train_4f/train_4f_0000{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
                elif i < 100:
                    path = f"./dataset/O_u/train_4f/train_4f_000{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
                else:
                    path = f"./dataset/O_u/train_4f/train_4f_00{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
        elif directory == 9:
            for i in range(1000):
                if i < 10:
                    path = f"./dataset/u_l/train_75/train_75_0000{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
                elif i < 100:
                    path = f"./dataset/u_l/train_75/train_75_000{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
                else:
                    path = f"./dataset/u_l/train_75/train_75_00{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
        elif directory == 10:
            for i in range(1000):
                if i < 10:
                    path = f"./dataset/U_u/train_55/train_55_0000{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
                elif i < 100:
                    path = f"./dataset/U_u/train_55/train_55_000{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])
                else:
                    path = f"./dataset/U_u/train_55/train_55_00{i}.png"
                    letter = recognizeImg(path)
                    print(f"{path} → {letter}")
                    if letter == 'i' or letter == 'í':
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 0])
                        count += 1
                    else:
                        database.append([path.split('/')[2], path.split('/')[4].split('_')[2].replace('.png', ''), 1])

        directory +=1

    print(f"Reconheci a letra i {count} vezes")

    confusionMatrix(database)

if __name__ == '__main__':

   recognizeAll()