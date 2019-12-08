
# file = open('txt.txt')
# text = file.read()
# print(text)
# file.close()

# with open ('./folder/inherit1.py') as f:
#     print(f.read())


# with open('txt.txt','w') as W: # w 是写入覆盖之前的
#     W.write('this is new write text')

with open('txt.txt','a') as w:
    w.write('appdener ist My new text \n this is new line \n')


with open('txt.txt') as r:
    print(r.read())

# read = W.read()
    #print(read)