#!/usr/bin/python3
import os, time, sys
def cpu_frequency_linux():
	while True:
		os.system('clear')
		os.system('grep MHz /proc/cpuinfo')
		time.sleep(1)
		os.system('clear')

def cpu_information_windows():
	while True:
		os.system("cls")
		os.system("wmic cpu list brief")
		time.sleep(1)
def cpu_information_linux():
	while True:
		os.system("clear")
		os.system("lscpu")
		time.sleep(1)
systemtype = sys.platform
if systemtype == 'win32':
	cpu_information_windows()
elif systemtype == 'linux' or systemtype == 'cygwin' or systemtype == 'darwin':
	os.system("figlet -f slant CPU Information")
	chinf = int(input("What information you want to collect? [1] Infomation about CPU [2] CPU frequency : "))
	if chinf == 1:
		cpu_information_linux()
	elif chinf == 2:
		cpu_frequency_linux()
	else:
		print("You write incorrect number!")
		time.sleep(1)
		quit()
