import datetime
from os import listdir
from os.path import isfile, join, splitext

#print date-time in nice format
today = str(datetime.date.today())
today.replace("-","_")

# Check for files in the folder
folder = "\\\\atlas-fs.atlas.uiuc.edu\\atlas\\admin\\Malice UIIntegrate\\Survey\\AIDESurveys\\AIDE1\\Data\\20130521"
onlyfiles = [f for f in listdir(folder) if isfile(join(folder,f)) and splitext(f)[1] == ".csv" and "AIDE" in f]

# Create a file to hold all lines in all CSVs
combined = open(folder + "\\combined_" + today + ".csv","w")
allData = []
for f in onlyfiles:
    filePath = folder + "\\" + f
    data = open(filePath,"r")
    if f == onlyfiles[0]:
        for line in data.readlines():
            combined.write(line)
    else:
        fileData = data.readlines()
        del fileData[0]
        for line in fileData:
            combined.write(line)  
    data.close()
combined.close()
