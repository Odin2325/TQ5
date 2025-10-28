# Alternative mit 

teststring = 'madam'


def umgekehrt(str):
    r = ''
    for s in str:
        r = s + r

    return r

if teststring == umgekehrt(teststring):
    print('Palindrom')
else:
    print('Kein Palindrom')