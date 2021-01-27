# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# start of FO.py file operations
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# modules included in this file
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * def checkSetMode(pathToCheck, modeIn, modeToSet):
# * def deFuxDir(toDeFux):
# * def deFuxFile(toDeFux):
# * def doAHash(HASH_, stringToHash):
# * def fxDir(dirToCk):
# * def getIndexes(destDir):
# * def incIndex(indexType):
# * def PLmkdir(fullPath):
# * def putIndexes(destDir):
# * def returnPathPiecesChmod(entryPath):
# * def scanADir(rootPath):
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# other useful defines
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * PATH = os.path
# * ABSPATH = os.path.abspath
# * MOVE = shutil.move
# * STAT = os.stat
# * MKDIR = os.mkdir
# * CHMOD = os.chmod
# * HOME = f"{PATH.expanduser('~')}"
# * SUB = re.sub


import os
import re
import shutil
import pathlib as PL


import C


OSPATH = os.path


ABSPATH = os.path.abspath
CHMOD = os.chmod
HOME = f"{OSPATH.expanduser('~')}"
MKDIR = os.mkdir
MOVE = shutil.move
RENAME = os.rename
STAT = os.stat
SUB = re.sub


CODE = "CODE"
DOCS = "DOCS"
PICS = "PICS"
TEXT = "TEXT"
VIDS = "VIDS"


BLACKTAIL = "BLACKTAIL"
DIRBLACKLIST = "[a-zA-Z0-9./]+"
DIRWHITELIST = "[^a-zA-Z0-9./]+"
EXTHEAD = "EXTHEAD"
EXTTAIL = "EXTTAIL"
FILEBLACKLIST = "[a-zA-Z0-9.]+"
FILEWHITELIST = "[^a-zA-Z0-9.]+"
ISDIR = "ISDIR"
ISFILE = "ISFILE"
ISSYMLINK = "ISSYMLINK"
KNOWNFILES = "KNOWNFILES"
KNOWNFILETYPE = "KNOWNFILETYPE"
MEDIAFILES = "MEDIAFILES"
NOTKNOWNFILES = "NOTKNOWNFILES"
NOTMEDIAFILES = "NOTMEDIAFILES"
NOTUNKNOWNFILES = "NOTUNKNOWNFILES"
PATH = "PATH"
PATHHEAD = "PATHHEAD"
PATHTAIL = "PATHTAIL"
RECURSE = "RECURSE"
ROOTDIR = "ROOTDIR"
UNKNOWNFILES = "UNKNOWNFILES"
WHITEFILENAME = "WHITEFILENAME"
WHITEFULLPATH = "WHITEFULLPATH"


ILLEGALPATHS = [
	"/",
]


ILLEGALWILDCARDS = [
	"/bin/",
	"/boot/",
	"/dev/",
	"/efi/",
	"/etc/",
	"/home/",
	"/lib/",
	"/lib64/",
	"/media/",
	"/opt/",
	"/proc/",
	"/root/",
	"/run/",
	"/sbin/",
	"/srv/",
	"/sys/",
	"/tmp/",
	"/usr/",
	"/var/"
]

EXTENSIONSTYPES = {
	CODE: [
		".c",
		".C",
		".php",
		".PHP",
		".py",
		".PY",
	],
	DOCS: [
		".doc",
		".DOC",
		".ods",
		".ODS",
		".odt:,"
		".ODT:,"
		".pdf",
		".PDF",
		".xls",
		".XLS",
	],
	PICS: [
		".bmp",
		".BMP",
		".gif",
		".GIF",
		".jpeg",
		".JPEG",
		".jpg",
		".JPG",
		".png",
		".PNG",
		".webp",
		".WEBP",
	],
	TEXT: [
		".lst"
		".LST"
		".txt",
		".TXT",
	],
	VIDS: [
		".avi",
		".AVI",
		".divx",
		".DIVX",
		".flv",
		".FLV",
		".gifv",
		".GIFV",
		".m2ts",
		".M2TS",
		".m4a",
		".M4A",
		".m4v",
		".M4V",
		".mkv",
		".MKV",
		".mov",
		".MOV",
		".mp4",
		".MP4",
		".mpeg",
		".MPEG",
		".mpg",
		".MPG",
		".webm",
		".WEBM",
		".wmv",
		".WMV",
	],
}

EXTENSIONLOOKUP = {
	".AVI": VIDS,
	".avi": VIDS,
	".BMP": PICS,
	".bmp": PICS,
	".C": CODE,
	".c": CODE,
	".DIVX": VIDS,
	".divx": VIDS,
	".FLV": VIDS,
	".flv": VIDS,
	".GIF": PICS,
	".gif": PICS,
	".GIFV": VIDS,
	".gifv": VIDS,
	".JPEG": PICS,
	".jpeg": PICS,
	".JPG": PICS,
	".jpg": PICS,
	".LST.TXT": TEXT,
	".lst.txt": TEXT,
	".M2TS": VIDS,
	".m2ts": VIDS,
	".M4A": VIDS,
	".m4a": VIDS,
	".M4V": VIDS,
	".m4v": VIDS,
	".MKV": VIDS,
	".mkv": VIDS,
	".MOV": VIDS,
	".mov": VIDS,
	".MP4": VIDS,
	".mp4": VIDS,
	".MPEG": VIDS,
	".mpeg": VIDS,
	".MPG": VIDS,
	".mpg": VIDS,
	".PHP": CODE,
	".php": CODE,
	".PNG": PICS,
	".png": PICS,
	".PY": CODE,
	".py": CODE,
	".WEBM": VIDS,
	".webm": VIDS,
	".WEBP": PICS,
	".webp": PICS,
	".WMV": VIDS,
	".wmv": VIDS,
}


MEDIAEXTENSIONTYPES = [
	PICS,
	VIDS,
]


# for thisFileType_, theseFileExts_ in EXTENSIONSTYPES.items():
# 	for thisFileExt_ in theseFileExts_:
# 		print(f"{C.NTAB(1)}{C.DBLQT}{thisFileExt_}{C.DBLQT}: {thisFileType_}")


BLACKTAIL = "BLACKTAIL"
EXTHEAD = "EXTHEAD"
EXTTAIL = "EXTTAIL"
ISDIR = "ISDIR"
ISFILE = "ISFILE"
ISKNOWNFILETYPE = "ISKNOWNFILETYPE"
ISMEDIAFILETYPE = "ISMEDIAFILETYPE"
ISSYMLINK = "ISSYMLINK"
ISUNKNOWNFILETYPE = "ISUNKNOWNFILETYPE"
PATH = "PATH"
PATHHEAD = "PATHHEAD"
PATHTAIL = "PATHTAIL"
WHITEFULLPATH = "WHITEFULLPATH"


EMPTYENTRYPATHSTUPLE = (
	(BLACKTAIL, ""),
	(EXTHEAD, ""),
	(EXTTAIL, ""),
	(ISDIR, False),
	(ISFILE, False),
	(ISKNOWNFILETYPE, False),
	(ISMEDIAFILETYPE, False),
	(ISSYMLINK, False),
	(ISUNKNOWNFILETYPE, False),
	(PATH, ""),
	(PATHHEAD, ""),
	(PATHTAIL, ""),
	(WHITEFULLPATH, ""),
)


def EMPTYENTRYPATHSDICT():
	return dict((x, y) for x, y in EMPTYENTRYPATHSTUPLE)


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * deFuxFile
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def deFuxFile(toDeFux):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	thisWhiteTail = SUB(C.FILEWHITELIST, "", toDeFux)
	thisBlackTail = SUB(C.FILEBLACKLIST, "", toDeFux)
	return thisWhiteTail, thisBlackTail
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * deFuxDir
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def deFuxDir(toDeFux):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	thisWhiteTail = SUB(C.DIRWHITELIST, "", toDeFux)
	thisBlackTail = SUB(C.DIRBLACKLIST, "", toDeFux)
	return thisWhiteTail, thisBlackTail
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * incIndex
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def incIndex(indexType):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	if indexType == C.PICSTAIL:
		currentIndex = int(C.PICSINDEX) + 1
		C.PICSINDEX = currentIndex
	elif indexType == C.VIDSTAIL:
		currentIndex = int(C.VIDSINDEX) + 1
	if currentIndex >= C.MAXDIR:
		currentIndex = C.MINDIR
	# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
	# * currentIndex 0x000..0x1ff PICSEXTS 0x200..0x3ff VIDSEXTS 0x200 error from C.DIRLIST
	# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
	if indexType == C.PICSTAIL:
		C.PICSINDEX = currentIndex
	elif indexType == C.VIDSTAIL:
		C.VIDSINDEX = currentIndex
		currentIndex += C.MAXDIR
	return currentIndex
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * fxDir
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def fxDir(dirToCk):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	dirToCk_ = ABSPATH(dirToCk)
	TIsADir_ = OSPATH.isdir(dirToCk_)
	if not TIsADir_:
		return None
	if dirToCk_ in ILLEGALPATHS:
		return None
	for thisStub_ in ILLEGALWILDCARDS:
		isFound_ = dirToCk_.find(thisStub_)
		print(f"thisStub_ |{thisStub_}| isFound_ |{isFound_}| dirToCk_ |{dirToCk_}|{C.NEWLINE}")
		if isFound_ == 0:
			return None
	return dirToCk_ + "/"
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * use pathlib to recursively create directories
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def PLmkdir(fullPath_):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	PL.Path(fullPath_).mkdir(parents=True, exist_ok=True)
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * get the indexes from ~/.cache
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#**#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def getIndexes(destDir):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	destDir = fxDir(destDir)
	if destDir is None:
		return False
	if not PATH.isdir(destDir):
		return False
	whiteDir, blackDir = deFuxFile(destDir)
	indexNamePICS = f"{C.DIRINDEXPATH}{whiteDir}.{C.PICSTAIL}INDEX.txt"
	if PATH.isfile(indexNamePICS):
		FDIn = open(indexNamePICS, "r")
		C.PICSINDEX = int(FDIn.readline())
		FDIn.close()
	else:
		C.PICSINDEX = C.MINDIR
	indexNameVIDS = f"{C.DIRINDEXPATH}{whiteDir}.{C.VIDSTAIL}INDEX.txt"
	if PATH.isfile(indexNameVIDS):
		FDIn = open(indexNameVIDS, "r")
		C.VIDSINDEX = int(FDIn.readline())
		FDIn.close()
	else:
		C.VIDSINDEX = C.MINDIR
	return True
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


def putIndexes(destDir):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	destDir = fxDir(destDir)
	if destDir is None:
		return False
	whiteStr, blackStr = deFuxFile(destDir)
	indexNamePICS = f"{C.DIRINDEXPATH}{whiteStr}.{C.PICSTAIL}INDEX.txt"
	FDOut = open(indexNamePICS, "w")
	FDOut.write(f"{C.PICSINDEX}\n")
	FDOut.flush()
	FDOut.close()
	indexNameVIDS = f"{C.DIRINDEXPATH}{whiteStr}.{C.VIDSTAIL}INDEX.txt"
	FDOut = open(indexNameVIDS, "w")
	FDOut.write(f"{C.VIDSINDEX}\n")
	FDOut.flush()
	FDOut.close()
	return True
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# * checkSetMode
# *#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def checkSetMode(pathToCheck, modeIn, modeToSet):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	return
	if modeIn != modeToSet:
		# print(f"dir chmod {pathToCheck} {modeIn:03o}  ==>  {modeToSet:03o}")
		CHMOD(pathToCheck, modeToSet)
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# returnPathPiecesChmod
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def returnPathPiecesChmod(entryPath_):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	thisPath_ = entryPath_.path
	thisPathHead_, thisPathTail_ = OSPATH.split(thisPath_)
	thisIsSymlink_ = entryPath_.is_symlink()
	thisIsDir_ = entryPath_.is_dir(follow_symlinks=False)
	thisIsFile_ = entryPath_.is_file(follow_symlinks=False)
	thisExtHead_, thisExtTail_ = OSPATH.splitext(thisPath_)
	thisMode_ = entryPath_.stat()[0] & 0o777
	if thisIsDir_:
		thisWhiteTail_, thisBlackTail_ = deFuxDir(thisPathTail_)
		thisWhiteFullPath_ = thisPathHead_ + "/" + thisWhiteTail_
		checkSetMode(thisPath_, thisMode_, 0o777)
	if thisIsFile_:
		thisWhiteTail_, thisBlackTail_ = deFuxFile(thisPathTail_)
		thisWhiteFullPath_ = thisPathHead_ + "/" + thisWhiteTail_.lower()
		checkSetMode(thisPath_, thisMode_, 0o666)
	if thisExtTail_ in EXTENSIONLOOKUP and thisIsFile_ is True:
		thisIsKnownFileType_ = True
		thisIsUnknownFiletype = False
	else:
		thisIsKnownFileType_ = False
		thisIsUnknownFiletype = True
	thisIsMediaFiletype_ = False
	for thisFileType_ in MEDIAEXTENSIONTYPES:
		if thisExtTail_ in EXTENSIONSTYPES[thisFileType_] and thisIsFile_ is True:
			thisIsMediaFiletype_ = True
	return {
		BLACKTAIL: thisBlackTail_,
		EXTHEAD: thisExtHead_,
		EXTTAIL: thisExtTail_,
		ISDIR: thisIsDir_,
		ISFILE: thisIsFile_,
		ISKNOWNFILETYPE: thisIsKnownFileType_,
		ISMEDIAFILETYPE: thisIsMediaFiletype_,
		ISSYMLINK: thisIsSymlink_,
		ISUNKNOWNFILETYPE: thisIsUnknownFiletype,
		PATH: thisPath_,
		PATHHEAD: thisPathHead_,
		PATHTAIL: thisPathTail_,
		WHITEFULLPATH:  thisWhiteFullPath_,
	}
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰


# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# scanADir
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
def scanADir(rootPath_, recurse_):
	# fold here ⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱⟱
	listToRtn_ = []
	with os.scandir(rootPath_) as dirEntries_:
		for entry_ in dirEntries_:
			thisEntryData_ = returnPathPiecesChmod(entry_)
			listToRtn_.append(thisEntryData_)
			if thisEntryData_[ISDIR] is True and recurse_ is True:
				addToListToRtn = scanADir(thisEntryData_[PATH], recurse_)
				for thisEntry_ in addToListToRtn:
					listToRtn_.append(thisEntry_)
	return listToRtn_
	# fold here ⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰⟰

#
#
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# end of FO.py
# #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
