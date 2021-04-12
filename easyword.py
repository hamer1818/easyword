import time

#colors
red='\033[91m'
b='\033[21m'
gren='\033[92m'
yellow='\033[93m'
cyan='\033[96m'
blue='\033[94m'


print (gren+b+"            <===[[ coded by hamer1818 ]]===>"+b+gren)
print (" ")

length=int(raw_input(cyan+b+"Hane sayisini girin: "+b+cyan))
print (" ")
name=raw_input(cyan+b+"Wordlistinizin ismini yazin sonuna (.txt) koyun: "+b+cyan)
tic = time.clock()
print (" ")
print (blue+b+"<><><><><><><><><><><><><><><><><><><><><>"+b+blue)
print (" ")
print (yellow+b+"Wordlist olusturuluyor lutfen bekleyin!"+b+yellow)
print (" ")
print (blue+b+"<><><><><><><><><><><><><><><><><><><><><>"+b+blue)
print (" ")
lista=[0 for x in xrange(length)]
x=length-1
string="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ1234567890!@#$%^&*"
list_of_results=[]
file1=file(name,"w")
while(x>-1):
    result=""
    if lista[x]==len(string)-1:
        for z in xrange (length):
            result+=string[lista[z]]
        lista[x]=0
        x-=1
    elif x==length-1:
        for z in xrange(length):
            result+=string[lista[z]]
        lista[x]+=1
    else:
        for z in xrange(length):
            result+=string[lista[z]]
        lista[x]+=1
        if x>0:
            x+=1
        else:
            x=length-1
    file1.write(result+"\n")
toc = time.clock()
ttn = toc - tic
print (red+b+"<<<========================================>>>"+b+red)
print (" ")
print (gren+b+"Tamamlandi "+str(ttn)+" saniye surdu."+b+gren)
print (" ")
print (gren+b+"Lutfen kontrol et "+str(name)+" programin klasorune bak"+b+gren)
print (" ")
print (red+b+"<<<========================================>>>"+b+red)
print (" ")