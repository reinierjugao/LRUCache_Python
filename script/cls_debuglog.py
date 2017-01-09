import os
import datetime
import __main__

class debuglog(object):
    def __init__(self):
        self.enabled = None
        # default log name will be the name of the top most script
        self.logpath = os.path.splitext(__main__.__file__)[0] + '.log'
        # default max log size is 1M
        self.maxsize = 1048576
        self.pid = str(os.getpid())


    def getcurdate(self):
        """
        " sets self.curdate variable for use
        """
        self.curdate = str(datetime.datetime.now())


    def generatemsg(self, msg):
        """
        " generates message with timestamp and process id
        """
        self.getcurdate()
        return self.curdate + ' [' + self.pid + ']: ' + msg + '\n'


    def truncatelog(self):
        """
        " Checks if size of file is larger than maxsize and truncates
        " NOTE: Alternate method of truncating log file would be to read
        "       data from the original file into a single buffer then
        "       write the buffer back to the original file, replacing
        "       all of its original content. The downside of this is that
        "       we would have to store half of the self.maxsize value into memory
        "       (assuming that we only want to preserve half of original file's
        "       max allowed size to minimize the number of times we would 
        "       need to truncate)
        """

        if not os.path.exists(self.logpath):
           return

        # check log size if we need to truncate
        logsize = os.path.getsize(self.logpath)
        if logsize < self.maxsize:
            return

        # truncate file
        logmsg = 'Truncated file'

        # create temporary file by appending .temp to original filename
        lftemp = self.logpath + '.temp'
        newlf = open(lftemp, 'w')
        newlf.write(self.generatemsg(logmsg))
                
        seekpos = logsize - (self.maxsize / 2)
        lf = open(self.logpath, 'rb')
        lf.seek(seekpos)
        
        # ignore the first line since it will most likely be incomplete
        lf.readline()

        # gets each line from original file and writes to temp file
        for chunk in lf:
            newlf.write(chunk)
            newlf.close

        # delete original file and rename temp file
        os.remove(self.logpath)
        os.rename(lftemp, self.logpath)


    def writelog(self, msg):
        """
        " Use this function to write to the log file
        """

        if not self.enabled:
            return

        if self.logpath == '':
            return

        self.truncatelog()
  
        lf = open(self.logpath, 'aw+')
        lf.write(self.generatemsg(msg))
        lf.close


