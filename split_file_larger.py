csvfile = open('SQL/aluguel_movimento_202201151609.csv', 'r').readlines()
filename = 1
for i in range(len(csvfile)):
    if i % 10000 == 0:
        open(str(filename) + '.csv', 'w+').writelines(csvfile[i:i+10000])
        filename += 1

