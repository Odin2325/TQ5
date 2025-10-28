zahlen = [1, 0, -4, 12, 3413, -28432, 7, "Stop"]
summiert=0
i=0
 
while zahlen[i] !="Stop":
    if zahlen[i] >=1:
        print(zahlen[i])
        summiert=summiert+zahlen[i]
    i+=1
print(summiert)