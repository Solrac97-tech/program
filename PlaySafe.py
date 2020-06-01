import os
import sys

banner = """
			 ----------------------------------
                          \____________PlaySafe__________/
                              since: june 1 2020
                              -------------------------
                              | Author: Solrac97-tech |
			      | coder : Carlx         |
                              | Member: Tommy         |
                              |         Melvin        |
                              -------------------------
"""

menu = """
	[99] back to list
	[100] Exit
       """
def Sniff():
	print(banner)
	print("     [01] shellphish")
	sniff = raw_input("[PlaySafe]-> ")
	if sniff == "01" or sniff == "1":
		shell()
	else:
		restart_program()

def badbug():
	print(banner)
	print("     [01] Malicious")
	badbug = raw_input("[PlaySafe]-> ")
	if badbug == "01" or badbug == "1":
		malware()
	else:
		restart_program()


def malware():
	print(banner)
	print("installing Malicious..........")
	print("Anang lelasam ngena nyak")
	os.system("git clone https://github.com/TheReaper167/Malicious.git")
	returntomenu_option()

def shell():
	print(banner)
	print("Installing Shellphish.........")
	print("Relax dan jangan biadap!!")
	os.system("git clone https://github.com/thelinuxchoice/shellphish.git")
       	returntomenu_option()

def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()


def returntomenu_option():
	print(menu)
	back = input("[PlaySafe]-> : ")
	if back == "99":
		restart_program()
	elif back == "100":
		sys.exit()
	else:
		print("\nRestart to Menu")
                restart_program()




def main():
	os.system("clear")
	print(banner)
	print("     [01] Snorf and Sniff")
	print("     [02] BadBug")
	get_tool =  raw_input("[PlaySafe]-> ")
	if get_tool == "1" or get_tool == "01":
		Sniff()
	elif get_tool == "2" or get_tool == "02":
		badbug()
	else:
		restart_program()
if __name__ == "__main__":
	main()
