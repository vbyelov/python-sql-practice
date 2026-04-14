try:
    stream = open("fi1le.txt", "rt")
    # Processing goes here.
    stream.close()
except Exception as exc:
    print("Cannot open the file:", exc)
    print(exc.errno)
    for i in exc:
        print(i)