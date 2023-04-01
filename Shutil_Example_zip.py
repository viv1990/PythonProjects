# This module of shutil is shell utilities. This helps in extracting files , zipping files.
# Output_shutil_zip is the name of output file which is created in the same folder as this python file
# zip is the format of the output file
#Files is the folder where you have all the files that need to be zipped

import shutil
shutil.make_archive("Output_shutil_zip","zip","Files")

''' Example of real life scenarioo where you want to zip all file which are in a folder under D directory
import shutil
shutil.make_archive("D:\Important_Vivek\Important_Files_Vivek","zip","D:\Important_Vivek")
'''
'''Example of copying one file from source to destination, src, dst'''
import shutil
shutil.copy("D:\Important_Vivek\GDP_22-23.pdf",r"C:\Users\athar\OneDrive\Desktop")
