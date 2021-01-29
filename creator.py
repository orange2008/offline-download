import json
import sys
print("Creator.")
ff = {}
while 1:
    try:
        s = input("Save as: ")
        u = input("URL: ")
        ff["/home/gdrive/" + str(s)] = str(u)
    except KeyboardInterrupt:
        print("Saving..")
        fp = open("config.json", 'w')
        json.dump(ff, fp)
        break

sys.exit(0)
