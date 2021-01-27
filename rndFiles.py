#!/usr/bin/python


import subprocess as SP
import os


import C
import FO




def __main__(argv):
	C.setOptions(argv)
	# print(f"argv |{argv}|{C.NEWLINE}")
	C.OPTIONSDICT[C.ROOTDIR] = FO.ABSPATH(C.OPTIONSDICT[C.ROOTDIR])
	print(f"C.OPTIONSDICT |{C.OPTIONSDICT}|{C.NEWLINE}")
	C.OPTIONSDICT[C.ROOTDIR] = FO.fxDir(C.OPTIONSDICT[C.ROOTDIR])
	print(f"C.OPTIONSDICT |{C.OPTIONSDICT}|{C.NEWLINE}")
	if C.OPTIONSDICT[C.ROOTDIR] is None:
		C.doError(f"illegal directory selected{C.NEWLINE}argv |{argv}|{C.NEWLINE}")
		C.exit(-1)
	dirList_ = FO.scanADir(C.OPTIONSDICT[C.ROOTDIR], C.OPTIONSDICT[FO.RECURSE])
	with open(f"{C.OPTIONSDICT[C.ROOTDIR]}__UNRENAME__.zsh", "tw") as FDOut:
		for thisEntry_ in dirList_:
			if thisEntry_[FO.ISMEDIAFILETYPE] is True and C.OPTIONSDICT[FO.MEDIAFILES] is True:
				hashedName_ = C.doAHash(C.OPTIONSDICT[C.HASHER], f"{thisEntry_[FO.PATH]}")
				allNewFilename_ = f"{thisEntry_[FO.PATHHEAD]}/{hashedName_}{thisEntry_[FO.EXTTAIL].lower()}"
				if C.OPTIONSDICT[C.TRIALRUN] is True:
					print(f"mv {C.DBLQT}{thisEntry_[FO.PATH]}{C.DBLQT} {C.DBLQT}{allNewFilename_}{C.DBLQT}{C.NEWLINE}")
				else:
					FO.RENAME(thisEntry_[FO.PATH], allNewFilename_)
				FDOut.write(f"mv {C.DBLQT}{allNewFilename_}{C.DBLQT} {C.DBLQT}{thisEntry_[FO.PATH]}{C.DBLQT}{C.NEWLINE}")
			elif thisEntry_[FO.ISKNOWNFILETYPE] is True and C.OPTIONSDICT[FO.KNOWNFILES] is True:
				hashedName_ = C.doAHash(C.OPTIONSDICT[FO.HASHER], f"{thisEntry_[FO.PATH]}")
				allNewFilename_ = f"{thisEntry_[FO.PATHHEAD]}/{hashedName_}{thisEntry_[FO.EXTTAIL.lower()]}"
				if C.OPTIONSDICT[C.TRIALRUN] is True:
					print(f"mv {C.DBLQT}{thisEntry_[FO.PATH]}{C.DBLQT} {C.DBLQT}{allNewFilename_}{C.DBLQT}{C.NEWLINE}")
				else:
					FO.RENAME(thisEntry_[FO.PATH], allNewFilename_)
				FDOut.write(f"mv {C.DBLQT}{allNewFilename_}{C.DBLQT} {C.DBLQT}{thisEntry_[FO.PATH]}{C.DBLQT}{C.NEWLINE}")
			elif thisEntry_[FO.ISUNKNOWNFILETYPE] is True and C.OPTIONSDICT[FO.UNKNOWNFILES] is True:
				hashedName_ = C.doAHash(C.OPTIONSDICT[FO.HASHER], f"{thisEntry_[FO.PATH]}")
				allNewFilename_ = f"{thisEntry_[FO.PATHHEAD]}/{hashedName_}{thisEntry_[FO.EXTTAIL].lower()}"
				if C.OPTIONSDICT[C.TRIALRUN] is True:
					print(f"mv {C.DBLQT}{thisEntry_[FO.PATH]}{C.DBLQT} {C.DBLQT}{allNewFilename_}{C.DBLQT}{C.NEWLINE}")
				else:
					FO.RENAME(thisEntry_[FO.PATH], allNewFilename_)
				FDOut.write(f"mv {C.DBLQT}{allNewFilename_}{C.DBLQT} {C.DBLQT}{thisEntry_[FO.PATH]}{C.DBLQT}{C.NEWLINE}")


if __name__ == "__main__":
	__main__(C.argv)


#
#
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# end of rndFiles.py
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
