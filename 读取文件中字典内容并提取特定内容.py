d1=open('2048list.txt','r',encoding='utf-8')
d3=eval(d1.read())
d3keys=d3.keys()
#print(d3keys)
#print(type(d3keys))
yie=0

for i in d3keys:
    if '写真' in i :
        print(i)
        print(d3[i])
        yie+=1
        with open('findok.txt','a',encoding='utf-8') as fp:
            fp.write(i+'\n')
            fp.write(d3[i]+'\n')

print('共{}条'.format(yie))

