try:
    stream = open("file.txt", "rt")
    # Processing goes here.
    stream.close()
except Exception as exc:
    print("Cannot open the file:", exc)
    print(exc.errno)
    exit(1)