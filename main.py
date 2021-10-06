#
# if __name__ == '__main__':
#
#
#
#     import os
#     def soldier(path, dictionary_file, format):
#         os.chdir(path)
#         i = 1
#         files = os.listdir(path)
#
#
#         with open(dictionary_file) as f :
#             filelist = f.read().split("\n")
#
#         for dictionary_file in files :
#             if dictionary_file not in filelist:
#                 os.rename(dictionary_file, files.capitalize())
#
#         if os.path.splitext(dictionary_file)[1] == format:
#             os.rename((dictionary_file, f"{i}{format}"))
#             i = i + 1
#
#
# need = str(input("Please Enter the three things here each seperated by a (,) symbol\n"
#                      "Order Should be like this : path, dictionary file, format\n"))
#
#
# names = need.split(",")[0]
# path = [0]
# dictionary_file =[1]
# format =[2]
#
# soldier(path,dictionary_file,format)
#
print("Your Task Was Completed")
#
# # print(type(names))
#
# print(os.getcwd())


# Oh soldier Prettify my Folder

# path, dictionary file, format

# def soldier("C://", "harry.txt", "jpg")

print("Hello Welcome to My Programme [Oh soldier Prettify my Folder] \n"
	            "Please Mention the Following things \n"
            "A Directory - from where we will find the folder\n"
            "A File- in which the names should be there containing the folder that you don't want to rename\n"
            "A format- from which we will use that format to change their name from 1 to the number of files of that format\n"
            "Please Enter to Continue")
space = input()


soldier(r"C:\Users\Sony\OneDrive\Pictures\Screenshots",
        r"E:\Python\Pycharm\PyCharm Community Edition 2020.2.2\Project\name12.txt", ".png" )

