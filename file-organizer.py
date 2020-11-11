import glob, os, shutil  

source_directory=r"C:\Users\siddi\Downloads"
destination_directory=r"D:\\"
os.chdir(source_directory)
base_extension = "pdf" 
file_extension_prefix = "**."
file_extension = file_extension_prefix + base_extension

#Create a list of files matching the pattern. If file is empty do nothing
files_list = glob.glob(file_extension)
if len(files_list) == 0:
    print( f"No file of type .{base_extension} present in dir {source_directory}" )

else:
    print( f"{str(len(files_list))} Files of type {base_extension} found" ) 

    # Change directory to destination folder
    os.chdir(destination_directory) 
    #MYDIR = ("images")
    CHECK_FOLDER = os.path.isdir(base_extension)

    # If folder doesn't exist, then create it.
    if not CHECK_FOLDER:
        os.makedirs(base_extension)
        print(  f"created folder : {base_extension}"    )
    else:
        print(  f"{base_extension} folder already exists."  )

    for file in files_list:
        print( f"Moving File : {file}" )
        os.chdir(source_directory)         
        shutil.move(file, destination_directory + base_extension)

        # TODO 
        # Error handling when file name exist in the destination folder
        # Create a bash script to accept user inputs for source and destination directory

