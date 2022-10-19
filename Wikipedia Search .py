import wikipedia

subjectno =0
while True :
    x= input ('What do you want?\n')
    print (wikipedia.summary(x,sentences =3))
    if x=='q' :
        exit(0)

    r= wikipedia.search(x)
    c=0
    for i in r:
        print (c,"..........",i)
        c+=1

    subjectno = int(input ('Enter subject number: '))
    page = wikipedia.page(r[subjectno])

    print (page.title)
    print ('*******************************************************************')
    print (page.content)
        