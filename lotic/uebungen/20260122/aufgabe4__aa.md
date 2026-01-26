i= 0

ram2[1] = 0
ram2[0] = 40

i= 1

ram2[3] = 1
ram2[2] = 42

i = 2

ram2[5] = 2
ram2[4] = 47


i = 3

ram2[7] = 3
ram2[6] = 52


i = 8
ram2[17] = 8
ram2[16] = 71


aa)
40 0 42 1 47 2 52 3 50 4 60 5 64 6 66 7 71 8

ab)
for(let i=0; i<18; i++){
    if(i%2==0){
        ram2[i]=i/2 + 1
    }else{
        ram2[i]= ram1[i-1/2]
    }
}



