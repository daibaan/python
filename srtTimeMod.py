#!/usr/bin/python
"""modify timestamps of an srt file with given offset & acceration factor"""

import sys
import re

def hms2sec(hms):
	hms = hms.split(":")
	(h,m,s) = (int(float(hms[0]))), int(float(hms[1])), float(hms[2])
	sec = h*3600+m*60+s
	#print "<<< sec=", sec
	return sec

def sec2hms(sec):
	if sec<0: sec=0
	ss = sec % 60
	hh = sec /3600
	mm = sec / 60 % 60
	ms = (ss-int(ss))*1000
	print "%s %d:%d:%d %d" % (sec,hh,mm,ss,ms)
	return "%02d:%02d:%02d,%03d" % (hh, mm, ss, ms)

# srtFileName, timeOffset, timeAcceration
def srtTimeMod(srt,tos,tacc):
	srtTimePat = "(\d\d:\d\d:\d\d),(\d\d\d)"
	with open(srt, "r") as f:
		for line in f:
			mo=re.match("^"+srtTimePat+"(.*)"+srtTimePat+"(.*)", line)
			if mo != None:
				s1 = hms2sec(mo.groups()[0] + "." + mo.groups()[1])
				s2 = hms2sec(mo.groups()[3] + "." + mo.groups()[4])
				hms1 = sec2hms((s1+tos)*tacc)
				hms2 = sec2hms((s2+tos)*tacc)
				print "%s%s%s%s" % (hms1, mo.groups()[2], hms2, mo.groups()[5])
			else:
				print line,

def srtTime2hms(srtTime):
	hmsMatch = re.match("^(\d\d:\d\d:\d\d),(\d\d\d)", srtTime)
	hms = hms2sec(hmsMatch.groups()[0] + "." + hmsMatch.groups()[1])
	return hms

def anaModRequired(s0,m0,s1,m1):
	print s0,m0,s1,m1
	[hmss0, hmsm0] = [srtTime2hms(s0), srtTime2hms(m0)]
	[hmss1, hmsm1] = [srtTime2hms(s1), srtTime2hms(m1)]
	tos0 = hmsm0-hmss0
	tos1 = hmsm1-hmss1
	tacc = 1+(tos1-tos0)/(hmss1-tos0)
	#print tos0,tos1,tacc
	return tos0,tacc

def main():
	[srt,tos,tacc] = [ "v.srt", -12, 1.04270]
	[srt,tos,tacc] = [ "s.srt", -17.5, 1]
	[srt,tos,tacc] = [ "12yearsaslaveweb72-G.srt", -5.7, 1]
	[srt,tos,tacc] = [ "12yearsaslaveweb72-G.srt", -5.2, 0.9991]

	if len(sys.argv) == 4:
		'''srtFile timeOffset timeAccelerationFactor'''
		[arg0,srt,tos,tacc] = sys.argv
		[tos,tacc] = [float(tos),float(tacc)]
	if len(sys.argv) == 6:
		'''srtFile srtTime0 actualTime0 srtTime1 actualTime1'''
		[arg0,srt,s0,m0,s1,m1] = sys.argv
		[tos,tacc] = anaModRequired(s0,m0,s1,m1)

	srtTimeMod(srt,tos,tacc)
	
# :!p.py 12yearsaslaveweb72-G.srt -5.2, 0.9991
# :!p.py 12yearsaslaveweb72-G.srt 00:01:08,154 00:01:02,897 02:05:06,500 02:04:54,548
if __name__ == '__main__':
	main()
