from datetime import datetime

def reformatDateTime(DTString):
    # Reformat the time stamp to ISO (YYYY-MM-DD HH:MM:SS)
    timeStamp = datetime.strptime(DTString, "%b %d %Y %H:%M:%S")

    timeString=timeStamp.strftime("%Y-%m-%d %H:%M:%S")
    return (timeString)

def main():

    with open("Data/NetgearLogIn.txt") as f:
        with open("Data/NetgearLogOut.txt", "w") as f1:
            for line in f:
                # Extract date and tiem stamp.
                splitLine = (line.split(","))
                monthDay = splitLine[-2]
                logYear = splitLine[-1]
                monthDay = monthDay.strip()
                logYear = logYear.strip()
                
                # Reformat date and time
                stringDate = (reformatDateTime(monthDay + " " + logYear))
                
                # Put the timestamp at the start of
                # the line and write it out to the
                # new log file.
                fline=(stringDate+" "+splitLine[0])
                f1.write(fline+"\n")

    print("Done...")


if __name__ == '__main__':
    main()
