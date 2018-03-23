import os
def rename_files():
	
	# 1- Get files name from a given folder
	# os.listdir() will get you everything that is in a directory "files & directories"
	# r stands for rawpack 
	# tells python [take this string as it is, and don't interpret it any other way]

	message_path = r"E:\Mini-Project\Secret Message\prank";
	file_list = os.listdir(message_path)

	# print(file_list)

	saved_path = os.getcwd()

	print("Current Working Directory is " + saved_path)

	os.chdir(message_path)

	# 2- for each file name, rename it
	for file_name in file_list:
		# print("Old Name : " + file_name)
		# print("New Name : " + file_name.translate(None,'0123456789'))
		os.rename(file_name, file_name.translate(None,'0123456789'))

	os.chdir(saved_path)

rename_files()