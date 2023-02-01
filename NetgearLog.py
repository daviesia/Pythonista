def formatLine(line):
     # Reformat line to make it look nicer.
     
     return(". "+line)

def main():

    with open("test.txt") as f:
        with open("out.txt", "w") as f1:
            for line in f:
                fline=formatLine(line)
                f1.write(fline)
            
    print("Done...")


if __name__ == '__main__':
	main()
