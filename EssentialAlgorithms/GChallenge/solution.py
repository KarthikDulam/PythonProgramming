def solution(s):
    brailledict = {'a':'100000',
                'b':'110000',
                'c':'100100',
                'd':'100110',
                'e':'100010',
                'f':'110100',
                'g':'110110',
                'h':'110010',
                'i':'010100',
                'j':'010110',
                'k':'101000',
                'l':'111000',
                'm':'101100',
                'n':'101110',
                'o':'101010',
                'p':'111100',
                'q':'111110',
                'r':'111010',
                's':'011100',
                't':'011110',
                'u':'101001',
                'v':'111001',
                'w':'010111',
                'x':'101101',
                'y':'101111',
                'z':'101011'}
    #brailledots = [1,12,14,145,15,124,1245,125,24,245,13,123,134,1345,135,1234,12345,1235,234,2345,136,1236,2456,1346,13456,1356]
    braillecode = ''

    for char in s:
        if char == ' ':
            braillecode += '000000'
        elif char.isupper():
            braillecode += '000001'
            braillecode+= brailledict[char.lower()]
        else:
            if brailledict.get(char,0) == 0:
                return 'Invalid Characters Present - Cannot convert'
            else:
                braillecode+= brailledict[char]
    return print(braillecode)

solution("code")