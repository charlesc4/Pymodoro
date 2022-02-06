import time
import platform
import subprocess
from playsound import playsound



def plataforma():
    
    if platform.system() == 'Windows':
        playsound('sound.mp3')
    else:
        return_code = subprocess.call(["afplay", "sound.mp3"])

min_sec_format= 0
end= 0

def startCountdown(temp1):
    while temp1:
        m, s = divmod(temp1, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format, end="\n")
        time.sleep(1)
        temp1 -= 1
    plataforma()

    

def litleRest(temp2):
    while temp2:
        m, s = divmod(temp2, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format, end="\n")
        time.sleep(1)
        temp2 -= 1
    plataforma()
 
def bigRest(temp3):
  temp3 = int (input("Digite de 15 a 30 minutos para descansar    "))*60
  while temp3:
        m, s = divmod(temp3, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format, end="\n")
        time.sleep(1)
        temp3 -= 1
  plataforma()

def restartMens():
  print ("Por favor reniciar a aplicação")
  retur = 0
        
    
temp1 = 1500
temp2 = 300
temp3 = 0


start = int (input("Digite 1 para iniciar ou 2 para sair   "))



if start == 1:
  for x in range(3):
    startCountdown(temp1)
    print('Descanse por 5min.')
    litleRest(temp2)
    print('Volte a focar por 25min.')
    x += 1

  for x in range(1):
    startCountdown(temp1)
    print('Descance um tempo maior.')
    x += 1
    bigRest(temp3)
    restartMens()

elif start == 2:
  print("OK, até logo")
  restartMens()
 

else:
  print("\nOpção inválida \n")
  restartMens()
       