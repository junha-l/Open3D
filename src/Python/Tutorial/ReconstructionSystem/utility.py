import sys
from os import listdir
from os.path import isfile, join, splitext


def parse_argument(argument, query):
	if query in argument:
		query_idx = argument.index(query)
		if query_idx + 1 <= len(argument):
			return argument[query_idx + 1]
	return False


def parse_argument_int(argument, query):
	return int(parse_argument(argument, query))


def get_file_list(path, extension=None):
	if extension is None:
		file_list = [path + f for f in listdir(path) if isfile(join(path, f))]
	else:
		file_list = [path + f for f in listdir(path)
				if isfile(join(path, f)) and splitext(f)[1] == extension]
	file_list.sort()
	return file_list


def initialize_opencv():
	opencv_installed = True
	try:
		import cv2
	except ImportError:
		pass
		print('OpenCV is not detected. Using Identity as an initial')
		opencv_installed = False
	if opencv_installed:
		print('OpenCV is detected. Using ORB + 5pt algorithm')
	return opencv_installed
