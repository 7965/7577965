import datetime

def old_register(): # enter old register
    h = int(input('горячяя вода за прошлый месяц: '))
    c = int(input('холоная вода за прошлый месяц: '))
    e = int(input('електроэнергия за прошлый месяц: '))
    hce = '{0}   {1}   {2}'.format(h, c, e)
    title = 'hot   cold   elec    date'
    l.write(title)
    l.write('\n')
    l.write(hce)
    l.write('\n')

def Price():  # func enter price
    ph = float(input('тариф за гор.воду: '))
    pc = float(input('тариф за хол. воду: '))
    pe = float(input('тариф за электроэнергию: '))
    ps = float(input('тариф за стоки: '))
    pri = '{0}{1}{2}{3}{4}{5}{6}'.format(ph,'\t', pc,'\t', pe,'\t', ps)
    title = 'hot  cold  elec  stocks'
    price.write(pri)

def newregister():  # func new register
    hot = int(input('hot water: '))
    cold = int(input('cold water: '))
    elec = int(input('electic: '))
    for regi in open('register.txt'):
        reg = regi.split()
    oldhot, oldcold, oldelec = int(reg[0]), int(reg[1]), int(reg[2])
    H = hot - oldhot
    C = cold - oldcold
    E = elec - oldelec
    stock = H + C
    for pr in open('/home/vladick/7577965/project/price.txt'):
        pr = pr.split()
        pH = H * float(pr[0])
        pC = C * float(pr[1])
        pE = E * float(pr[2])
        pS = stock * float(pr[3])
    now = datetime.datetime.now()
    t = now.date()
    z = '{0}   {1}   {2}{3}{4}'.format(hot, cold, elec,'\t',t)
    l.write(z)
    l.write('\n')
    print('холодная вода: ',C,' на сумму: ',pC,'\n','горячяя вода: ',H,' на сумму: ',pH,'\n','свет: ',E,' на сумму: ',pE,'\n','стоки: ',stock,' на сумму: ',pS,'\n','итого: ',pC + pH + pS + pE)

def openTxt():
    global l
    global price
    global ll
    global pr
    l = open('/home/vladick/7577965/project/register.txt','r+')
    price = open('/home/vladick/7577965/project/price.txt', 'r+')
    ll = list(l)
    pr = list(price)

def closeTxt():
    l.close()
    price.close()

def main():
    openTxt()
    if len(ll) == 0:
        old_register()
    if len(pr) == 0:
        Price()
    closeTxt()
    openTxt()
    if len(ll) != 0 and len(pr) != 0:
        newregister()
    l.close()
    price.close()
main()
