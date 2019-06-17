#!/usr/bin/python3
import os
import subprocess

def list_nonpdf():
	years = ['OPDC2009','OPDC2010','OPDC2011','OPDC2012','OPDC2013','OPDC2014','OPDC2015','OPDC2016','OPDC2017','OPDC2018'];
	for year in years:
		directory = "../" + year + "/";
		for fn in os.listdir(directory):
			if fn[-4:] != '.pdf':
#			if fn[-4:] == '.tif':
				print "\n" + directory + fn;
#				print directory + fn[:-4] + ".pdf";
#				os.system("img2pdf -o "+directory+fn[:-4]+".pdf "+directory+fn)
#				os.system("convert "+directory+fn+" -quality 100 "+directory+fn[:-4]+".pdf")
#				subprocess.call(["git", "add", directory+fn[:-4]+".pdf"])
#				subprocess.call(["git", "rm", directory+fn])

def strip_nonalphanumeric(astring):
#	astring = astring.replace("_", "");
	astring = astring.replace("-", "");
	astring = astring.replace(",", "");
	astring = astring.replace("(", "");
	astring = astring.replace(")", "");
	astring = astring.replace("&", "");
	astring = astring.replace("!", "");
	astring = astring.replace("\"", "");
	astring = astring.replace(" ", "");
	return astring;

#def fix_2010():
#	directory = "../OPDC2011/"
#	sid = 1;
#	for fn in os.listdir(directory):
#		if sid < 10: 
#			sids = "E00" + str(sid);
#		elif sid < 100: 
#			sids = "E0" + str(sid);
#		elif sid < 1000: 
#			sids = "E" + str(sid);
	#	if "__" not in fn: 
	#		sid += 1;
	#		continue
#		name_title_idx = ;
#		name = fn[0:name_title_idx];
#		title = fn[name_title_idx+2:];
#		name = strip_nonalphanumeric(name);
#		name = name.replace(".", "");
#		title = strip_nonalphanumeric(title);
#		title = title.replace("...", "");
#		newfn = directory + sids + "_" + name + "_" + title;
#		oldfn = directory + fn;
#		print newfn;
#		subprocess.call(["git", "mv", oldfn, newfn])
#		sid += 1;

#def fix_2017():
#	directory = "../" + "OPDC2017/"
#	for fn in os.listdir(directory):
#		newfn = directory + "E0" + fn[0] + fn[1] + "_" + fn[3].upper() + fn[4:];
#		oldfn = directory + fn;
#		subprocess.call(["git", "mv", oldfn, newfn])

#def fix_2018():
#	directory = "../" + "OPDC2018/"
#	for fn in os.listdir(directory):
#		if fn[3] == "_":
#			newfn = directory + "E0" + fn[1] + fn[2] + "_" + fn[4:];
#			oldfn = directory + fn;
#			subprocess.call(["git", "mv", oldfn, newfn])

def fix_2019():
	directory = "../" + "OPDC2019/"
	for fn in os.listdir(directory):
		if fn[4] == "_":
			#newfn = directory + "E0" + fn[1] + fn[2] + "_" + fn[4:];
			newfn = directory + fn;
			newfn = strip_nonalphanumeric(newfn);
			print newfn;
			oldfn = directory + fn;
			#print oldfn;
			subprocess.call(["mv", oldfn, newfn])
			#subprocess.call(["git", "mv", oldfn, newfn])

if __name__ == '__main__':
#	fix_2019()
	list_nonpdf()
