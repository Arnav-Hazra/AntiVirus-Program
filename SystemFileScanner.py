import glob
import time
import sys, os

os_name = sys.platform
partitionen = []
directori = []
files = []

def partitions(sfsFolder):
    global partitionen
    big = 65

    if "win" in os_name:
        for i in range(26):
            try:
                if glob.glob(str(chr(big + i)) + ":\\"):
                    #print("Successfully found partition: " + str(chr(big + i)))
                    partitionen.append(str(chr(big + i)) + ":\\")
            except:
                continue
        return indeces(sfsFolder)
    if "win" not in os_name:
        return indeces(sfsFolder)
    
def indeces(sfsFolder):
    global directori
    global files
    
    if "win" in os_name:
        directori2 = glob.glob("\\*")
    else:
        directori2 = glob.glob("//*")
    directori_tmp = []
    x = 1

    if "win" in os_name:
        for ind in range(len(partitionen)):
            #print(partitionen[ind])
            while directori2 != []:
                directori2 = glob.glob(partitionen[ind] + "\\*"*x)
                for i in range(len(directori2)):
                    directori.append(directori2[i])
                x += 1
            x = 1

        for i in range(len(directori)):
            if "." in directori[i]:
                files.append(directori[i])
        for i in range(len(directori)):
            if not os.path.isfile(directori[i]):
                directori_tmp.append(directori[i])
        directori = directori_tmp
        i = 0
        f = open(sfsFolder, "w")
        for i in range(len(files)):
            f.write(files[i] + "\n")
        f.close()
        time.sleep(3)

    if "win" not in os_name:
        while directori2 != []:
            directori = glob.glob("//*" * x)
            for i in range(len(directori2)):
                directori.append(directori2[i])
            x += 1
        x = 1

        for i in range(len(directori)):
            if "." in directori[i]:
                files.append(directori[i])
        for i in range(len(directori)):
            if not os.path.isfile(directori[i]):
                directori_tmp.append(directori[i])
        directori = directori_tmp
        i = 0
        f = open(sfsFolder, "w")
        for i in range(len(files)):
            f.write(files[i] + "\n")
        f.close()
        time.sleep(3)
