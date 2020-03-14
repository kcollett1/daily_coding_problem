class file_system:
    def __init__(self) -> None:
        self.dirs    = [] # list of first level dirs, of type str
        self.subdirs = [] # list of list of second level subdirs within each first level dir, of type file_system
        self.files   = [] # list of list of files in each first level dir, of type str

    def __init__(self, filesys_str: str) -> None:
        if not filesys_str:
            __init__()
            return

        self.dirs    = [] # list of first level dirs, of type str
        self.subdirs = [] # list of list of second level subdirs within each first level dir, of type file_system
        self.files   = [] # list of list of files in each first level dir, of type str

        dir_ct   = -1 # num of first level dirs - 1 (for indexing purposes)
        lines    = filesys_str.split('\n')
        line     = 0
        numlines = len(lines)

        while line < numlines:
            currline = lines[line] # just for ease of typing, can take this out if needed

            # if first level dir, add to list of dirs in this fs object, go on to next line
            if currline[:1] != '\t':
                self.dirs.append(currline)
                self.subdirs.append([])
                self.files.append([])
                dir_ct += 1
                line   += 1
                continue

            # else if a file in current dir, add it to file list for current dir
            if '.' in currline:
                self.files[dir_ct].append(currline[1:])
                line += 1
                continue

            # else must be a subdir within current dir
            # put together string for this subdir until next string at this level is reached
            # removing one \t from start of each string, and adding \n between each
            # increasing line var and then adding subdir fs object to self.subdirs list
            subfs_str = currline[1:]
            line     += 1
            while line < numlines and lines[line][1:2] == '\t':
                subfs_str += '\n' + lines[line][1:]
                line      += 1
            self.subdirs[dir_ct].append(file_system(subfs_str))

    def longest_path(self) -> int:
        if not self.dirs: return 0

        max_len = 0
        for ctr, dir_name in enumerate(self.dirs):
            path_len = len(dir_name) + 1 # path length starts with this dir name + '/'
            # check all files in this dir
            max_fn = max([0] + [len(fn) for fn in self.files[ctr]])
            if max_fn > 0 and path_len + max_fn > max_len: max_len = path_len + max_fn
            for sd in self.subdirs[ctr]:
                max_sdlen = sd.longest_path()
                if max_sdlen > 0 and path_len + max_sdlen > max_len:
                    max_len = path_len + max_sdlen

        return max_len

    def printfilesys(self) -> str:
        return '' # can do this for fun if wanted after, not really necessary FIXME

test_filesys_str = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
test_filesys = file_system(test_filesys_str)
print('longest path in:')
print(test_filesys_str)
#print(test_filesys.printfilesys(), ':')
print('   ', test_filesys.longest_path())
print('\n')

test_filesys_str = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" 
test_filesys = file_system(test_filesys_str)
print('longest path in:')
print(test_filesys_str)
#print(test_filesys.printfilesys(), ':')
print('   ', test_filesys.longest_path())
print('\n')

test_filesys_str = "dir\n\tsubdir1\n\tsubdir2"
test_filesys = file_system(test_filesys_str)
print('longest path in:')
print(test_filesys_str)
#print(test_filesys.printfilesys(), ':')
print('   ', test_filesys.longest_path())
