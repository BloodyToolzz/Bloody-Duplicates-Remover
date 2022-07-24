import os

from pystyle import *
from time import sleep as stfu
from console.utils import set_title

def cls():
        os.system('cls' if os.name == "nt" else "clear")

def pause():
        os.system('pause >nul')

banner = '''
██████╗ ██╗      ██████╗  ██████╗ ██████╗ ██╗   ██╗                          
██╔══██╗██║     ██╔═══██╗██╔═══██╗██╔══██╗╚██╗ ██╔╝                          
██████╔╝██║     ██║   ██║██║   ██║██║  ██║ ╚████╔╝                           
██╔══██╗██║     ██║   ██║██║   ██║██║  ██║  ╚██╔╝                            
██████╔╝███████╗╚██████╔╝╚██████╔╝██████╔╝   ██║                             
╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝    ╚═╝                             
                                                                             
██████╗ ██╗   ██╗██████╗ ██╗     ██╗ ██████╗ █████╗ ████████╗███████╗███████╗
██╔══██╗██║   ██║██╔══██╗██║     ██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔════╝
██║  ██║██║   ██║██████╔╝██║     ██║██║     ███████║   ██║   █████╗  ███████╗
██║  ██║██║   ██║██╔═══╝ ██║     ██║██║     ██╔══██║   ██║   ██╔══╝  ╚════██║
██████╔╝╚██████╔╝██║     ███████╗██║╚██████╗██║  ██║   ██║   ███████╗███████║
╚═════╝  ╚═════╝ ╚═╝     ╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚══════╝
                                                                             
██████╗ ███████╗███╗   ███╗ ██████╗ ██╗   ██╗███████╗██████╗                 
██╔══██╗██╔════╝████╗ ████║██╔═══██╗██║   ██║██╔════╝██╔══██╗                
██████╔╝█████╗  ██╔████╔██║██║   ██║██║   ██║█████╗  ██████╔╝                
██╔══██╗██╔══╝  ██║╚██╔╝██║██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗                
██║  ██║███████╗██║ ╚═╝ ██║╚██████╔╝ ╚████╔╝ ███████╗██║  ██║                
╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝                
Simple duplicates remover for .txt files.
'''
cls()
print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(banner)))

set_title("Bloody Duplicate Remover | Made By: Bloody | Input Text File")
inpt = Write.Input('Input text file name (e.g. input.txt) ', Colors.rainbow, interval=0.008)
set_title("Bloody Duplicate Remover | Made By: Bloody | Input Output Text File")
oupt = Write.Input('Output file name (e.g. output.txt) ', Colors.rainbow, interval=0.008)
cls()
print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(banner)))

if __name__ == '__main__':
	f = open(oupt, 'w+')
	flag = False
	set_title("Bloody Duplicate Remover | Made By: Bloody | Processing . . .")
	Write.Print('[?] Processing . . .\n\n', Colors.red_to_yellow, interval=0)
	stfu(2)
	with open(inpt) as fp:
		for line in fp:
			for temp in f:
				if temp == line:
					flag = True
					Write.Print('\n[+] Finding Duplicates . . .\n', Colors.red_to_yellow, interval=0)
					Write.Print('[-] Duplicate Found! | ', Colors.green_to_white, interval=0)
					Write.Print(f'{line}', Colors.rainbow, interval=0)
					Write.Print('[+] Removing Duplicate . . .\n', Colors.red_to_yellow, interval=0)
					Write.Print('[+] Duplicate Removed!\n', Colors.green_to_white, interval=0)
					break
			if flag == False:
				f.write(line)
			elif flag == True:
				flag = False
			f.seek(0)
		f.close()
		stfu(1)
		set_title("Bloody Duplicate Remover | Made By: Bloody | Finished!")
Write.Print('\nSuccessfully removed all duplicates!\n', Colors.green_to_white, interval=0)
Write.Print('Thanks for using my tools <3\n', Colors.red_to_yellow, interval=0.1)
Write.Print('Press any key to continue . . .', Colors.green_to_white, interval=0)
pause()