# В текстовый файл построчно записаны фамилия и имя учащихся класса и его
# оценка за контрольную. Вывести на экран всех учащихся, чья оценка меньше 3
# баллов и посчитать средний балл по классу

with open('2.txt', 'r', encoding='utf-8') as f:
    # f.write('Cидоров У - 2' + '\n')
    # f.write('Cидоров П - 5' + '\n')
    # f.write('Cидоров В- 4' + '\n')
    # f.write('Cидоров К - 1' + '\n')
    # f.write('Cидоров Ш- 3' + '\n')
    # f.write('Cидоров М- 4' + '\n')
    # f.write('Cидоров Т - 1' + '\n')
    # f.write('Cидоров Ь- 2' + '\n')


    strok = f.readlines()
    vsego = int(len(strok))
    # print(vsego)
    sm = 0
    for st in strok:
        # print(st)
        for i in st:
            if i.isdigit():
                # print(i)
                sm += int(i)
                if int(i) <= 3:
                    print(" оценка меньше 3-х балов у", st)
# print(sm)
print("Средний бал по классу:", sm//vsego)
