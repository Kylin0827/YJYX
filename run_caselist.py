import os
with open('tclist.txt') as rF,open('args.txt','w') as wF:
    caselist1=rF.read().replace('\n','').split(' | ')
    caselist=list(filter(None, caselist1))
    writelist=[]
    for one in caselist:
        one='--test *'+one
        writelist.append(one)
    Wlist='\n'.join(writelist)
    Wlist=Wlist+'\n'+'--pythonpath .'+'\n'+'tc'
    print(Wlist)
    wF.write(Wlist)

os.system('robot --loglevel debug -A args.txt')


