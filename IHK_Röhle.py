
aa)
40 0 42 1 47 2 52 3 50 4 60 5 64 6 66 7 71 8

ab)
for(let i=0; i<18; i++){
    if(i%2==0){
        ram2[i] =i/2 + 1
    }else{
        ram2[i] = ram1[i-1/2]
    }
}


ab)

[1, 40, 2, 42]

Fehler 1: Füllwerte müssen eins höher sein.
Zeile5: RAM2[i*2] = i+1
Fehler 2: Felder müssen getauscht sein.
Zeile6: RAM2[i*2+1] = RAM1[i]


Vierter Schleifendurchlauf
i = 3 
RAM2[7] = 3 
RAM2[6] = 52

RAM2 = [40, 0, 42, 1, 47, 2, 52, 3]



Dritter Schleifendurchlauf
i = 2
RAM2[5] = 2
RAM2[4] = 47

RAM2 = [40, 0, 42, 1, 47, 2]

Zweiter Schleifendurchlauf
i = 1
RAM2[3] = 1
RAM2[2] = 42

RAM2 = [40, 0, 42, 1]


Erster Schleifendurchlauf

i = 0
RAM2[0 * 2 + 1] -> RAM2[1]

RAM2[1] = 0

RAM2[0] = RAM1[i]
RAM2[0] = 40

RAM2 = [40, 0] # Nach erstem Schleifendurchlauf