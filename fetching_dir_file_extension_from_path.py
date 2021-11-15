#Program to take the absolute path and print the directories,filename and extention
path = input("Please enter the full path of a file with filename: ")
path_folder = path.split('/')
dir = "/".join(path_folder[:-1])
filename = path_folder[-1]
fname_split = filename.split('.')
extension = fname_split[-1]
print ("Directory path: ",dir,"Filename is: ",filename,"Extension is: ",extension)

