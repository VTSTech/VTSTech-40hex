import sys, os, hashlib, binascii, time

from passlib.apps import custom_app_context as pwd_context
from passlib.context import CryptContext

if sys.platform.startswith('win32'):
	import msvcrt
pwd_context = CryptContext(schemes=["hex_md5", "hex_md4", "hex_sha1"])

def banner():
	print "#########################################"
	print "# VTSTech-40hex v0.1 Python Version     #"
	print "# Facebook: facebook.com/VTSTech        #"
	print "# Twitter: @VTSTech_                    #"
	print "# Web: www.VTS-Tech.org                 #"
	print "# E-mail: veritas@vts-tech.org          #"
	print "# XMPP: veritas@creep.im                #"
	print "# BTC 1VTSgzD24bjkSGdD7kvauxkxHZ4yiwhdU #"
	print "# Based on VTSTech-32hex v0.34          #"
	print "#########################################"

StartTime = time.time()
ETime = 0
silent = 1
Cracked = ""
lines = 0
linet = 0
CrkCnt = 0
cnt = ""
TotalTime = ""
LastAlgo = ""
numpass = open('passwords.dat')
num_pass = sum(1 for line in numpass)
numpass.close()
if len(sys.argv) == 1:
	banner()
	print ""
	print "Usage: VTStech-40hex.py -l hashlist.txt - List mode using hashlist.txt"
	print ""
	print "Options"
	print ""
	print "-l hashlist.txt, load target hashes from hashlist.txt"
	print "-s speed per sec updates"
	print ""
	print "Press any key to display speed/sec"
	sys.exit()
else:
	banner()
	print "Press any key to display speed/sec"
	if len(sys.argv[1]) == 2:
		if sys.argv[1] == "-l":
			target = sys.argv[2]
			hashes = open(sys.argv[2])				 
		elif sys.argv[2] == "-l":
			target = sys.argv[3]
			hashes = open(sys.argv[3])
		elif sys.argv[3] == "-l":
			target = sys.argv[4]
			hashes = open(sys.argv[4])
		if sys.argv[1] == "-s":
			silent = 0
		elif sys.argv[2] == "-s":
			silent = 0
md5 = CryptContext(schemes=["hex_md5"],)
sha = CryptContext(schemes=["hex_sha1"],)
md4 = CryptContext(schemes=["hex_md4"],)
numhash = open(target)
num_hash = sum(1 for line in numhash)
print ""
print num_pass,"passwords,", num_hash,"hashes loaded."
print ""
TotalPass = (num_pass * num_hash) * 8
numhash.close()
hashes = open(target)
for lineh in hashes:
	passwd = open("passwords.dat")	
	CurrHash = lineh
	CurrTime = time.time()
	TotalTime = CurrTime - StartTime
	if sys.platform.startswith('win32'):
			while msvcrt.kbhit():
				msvcrt.getch()
				progress = str(cnt),chr(47),str(TotalPass)
				pcnt = "(",str(round(float(float(cnt) / float(TotalPass))*100,2)),"%)"
				duration = str(round(TotalTime,2)),"s"
				print "Elapsed:",''.join(duration),"Progess:",''.join(progress),''.join(pcnt),"Speed:", round((cnt / TotalTime),2),"Hash/s"
	if ((CurrTime - ETime)  > 60) or ((CurrTime - ETime) == CurrTime):
		if (TotalTime > 1):
			if silent == 0:
				progress = str(cnt),chr(47),str(TotalPass)
				pcnt = "(",str(round(float(float(cnt) / float(TotalPass))*100,2)),"%)"
				duration = str(round(TotalTime,2)),"s"
				print "Elapsed:",''.join(duration),"Progess:",''.join(progress),''.join(pcnt),"Speed:", round((cnt / TotalTime),2),"Hash/s"
		ETime = CurrTime
	for linep in passwd:
		lines += 1
		CurrPass = linep
		CurrHash = CurrHash.strip(chr(13))
		CurrHash = CurrHash.strip(chr(10))
		CurrHash = CurrHash.strip(chr(34))
		CurrPass = CurrPass.strip(chr(13))
		CurrPass = CurrPass.strip(chr(10))
		CurrPass = CurrPass.strip(chr(34))
		sha1 = sha.encrypt(CurrPass)
		sha12x = sha.encrypt(sha1)
		sha13x = sha.encrypt(sha12x)
		sha14x = sha.encrypt(sha13x)
		sha15x = sha.encrypt(sha14x)
		sha16x = sha.encrypt(sha15x)
		shamd5 = sha.encrypt(md5.encrypt(CurrPass))
		shamd4 = sha.encrypt(md4.encrypt(CurrPass))
		cnt = (lines * 8)
		CurrTime = time.time()
		TotalTime = CurrTime - StartTime
		if sha1 == CurrHash:
			Algo = "SHA1"
			Cracked = sha1,":",CurrPass
			if LastAlgo == Algo:
				print ''.join(Cracked)
			else:
				print "Encryption Method: ",Algo
				print ''.join(Cracked)
				LastAlgo = Algo
				CrkCnt = CrkCnt + 1		
			break
			break	
		elif sha12x == CurrHash:
			Algo = "Double SHA1"
			Cracked = sha12x,":",CurrPass
			if LastAlgo == Algo:
				print ''.join(Cracked)
			else:
				print "Encryption Method: ",Algo
				print ''.join(Cracked)				
				LastAlgo = Algo
				CrkCnt = CrkCnt + 1		
			break
			break	
		elif sha13x == CurrHash:
			Algo = "Triple SHA1"
			Cracked = sha13x,":",CurrPass
			if LastAlgo == Algo:
				print ''.join(Cracked)
			else:
				print "Encryption Method: ",Algo
				print ''.join(Cracked)	
				LastAlgo = Algo
				CrkCnt = CrkCnt + 1		
			break
			break	
		elif sha14x == CurrHash:
			Algo = "Quadruple SHA1"
			Cracked = sha14x,":",CurrPass
			if LastAlgo == Algo:
				print ''.join(Cracked)
			else:
				print "Encryption Method: ",Algo
				print ''.join(Cracked)	
				LastAlgo = Algo
				CrkCnt = CrkCnt + 1		
			break
			break	
		elif sha15x == CurrHash:
			Algo = "Quintuple SHA1"
			Cracked = sha15x,":",CurrPass
			if LastAlgo == Algo:
				print ''.join(Cracked)
			else:
				print "Encryption Method: ",Algo
				print ''.join(Cracked)	
				LastAlgo = Algo
				CrkCnt = CrkCnt + 1		
			break
			break	
		elif sha16x == CurrHash:
			Algo = "Hextuple SHA1"
			Cracked = sha16x,":",CurrPass
			if LastAlgo == Algo:
				print ''.join(Cracked)
			else:
				print "Encryption Method: ",Algo
				print ''.join(Cracked)	
				LastAlgo = Algo
				CrkCnt = CrkCnt + 1		
			break
			break	
		elif shamd5 == CurrHash:
			Algo = "SHA(MD5())"
			Cracked = md5sha1,":",CurrPass
			if LastAlgo == Algo:
				print ''.join(Cracked)
			else:
				print "Encryption Method: ",Algo
				print ''.join(Cracked)	
				LastAlgo = Algo
				CrkCnt = CrkCnt + 1		
			break
			break	
		elif shamd4 == CurrHash:
			Algo = "SHA(MD4())"
			Cracked = md5sha1,":",CurrPass
			if LastAlgo == Algo:
				print ''.join(Cracked)
			else:
				print "Encryption Method: ",Algo
				print ''.join(Cracked)	
				LastAlgo = Algo
				CrkCnt = CrkCnt + 1		
			break
			break	
print ""
print ""
DidWeWin = "Recovered: ",str(CrkCnt),"/",str(num_hash)," (",str(round(float(CrkCnt) / float(num_hash)*100,2)),"%)"
progress = str(cnt),chr(47),str(TotalPass)
pcnt = "(",str(round(float(float(cnt) / float(TotalPass))*100,2)),"%)"
duration = str(round(TotalTime,2)),"s"
print ''.join(DidWeWin)
print ""
print "Elapsed time:",''.join(duration),"Progess:",''.join(progress),''.join(pcnt),"Speed:", round((cnt / TotalTime),2),"Hash/s"
print "Recovery complete."
sys.exit()