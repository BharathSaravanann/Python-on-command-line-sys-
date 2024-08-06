import sys
import numpy as np

def main():

    script=sys.argv[0]
    action=sys.argv[1]
    if action not in ["--min","--max","--mean"]:
        action = "--mean"
        filenames=sys.argv[1:]
    else:
        filenames=sys.argv[2:]

    if len(filenames)<0:
        process(sys.stdin,action)
    else:
        for filename in filenames:
            process(filename,action)

def process(filename,action):
    data=np.loadtxt(fname=filename,delimiter=",")
    if action == "--mean":
        values=np.mean(data,axis=0)
    elif action == "--min":
        values=np.amin(data,axis=0)
    elif action == "--max":
        values=np.amax(data,axis=0)

    for value in values:
        print(value)

if __name__ == "__main__":
    main()
