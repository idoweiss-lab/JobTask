FILE_PATH = 'P:\exam\\release_notes.txt'

'''
return the value [issue] Title number string for error with comment to the array
'''
def FunGitNote(arr , IndexInArray):
    Title = FileArray[IndexInArray].replace('Title: ', '')
    for line in arr[IndexInArray:]:
        if("Issue:" in line):
           issue = line.replace('Issue: ','')
           issue = issue.replace("\n", "")
           return "["+issue+"]"+ " " + Title
"""
return the vaule [NOTE_MISSING] commit #number @owner , Please add git notes to this commit for missing comment on git
"""
def FunWithoutGitNote(arr , IndexInArray):
    NoteMissing = FileArray[num]
    for line in arr[IndexInArray:]:
        if("Owner:" in line):
           owner = line.replace('Owner: ','')
           owner = owner.replace("\n", "")
           return NoteMissing + "@"+owner+ " , Please add git notes to this commit!"

"""
return the lines from file
"""
def load_file(path):
    with open(path, "r") as f:
        return f.readlines()

"""
print the error + title of the git notes
"""
def summarize_git_note(git_note):
    CheckDuplicateEror = ""  # array for check duplicate errors
    for Error in GitNote:
        if (Error not in CheckDuplicateEror):  # check for duplicate errors
            print(Error)
        CheckDuplicateEror += Error  # add the error to the array

"""
print the note missing + commit and the owner with request to add commit
"""
def summarize_git_without_note(git_without_note):
    CheckOwnerNoComment = ["chdauto", "syspdbuild", "syspdbuild2"]#owners that dont need to print the missing commit
    for NoComment in WithoutGitNote:
        if (NoComment.split("@")[1].split(" ,")[0] not in CheckOwnerNoComment):  # check for owner that dont need to print
            print(NoComment)


GitNote = []#array that contains all the errors with note
WithoutGitNote = []#array that contains all the missing note
FileArray = []#array that contains all the lines

FileArray = load_file(FILE_PATH)

ArrayLen = len(FileArray)

for num in range(ArrayLen):
    if("Title" in FileArray[num]):#check if the string Ttile is in the line
        GitNote.append(FunGitNote(FileArray,num))#add the string from the function to the array
    elif ("[ NOTE_MISSING ]" in FileArray[num]):#check if the string [ NOTE_MISSING ] is in the line
        WithoutGitNote.append(FunWithoutGitNote(FileArray,num))#add the string from the function

summarize_git_note(GitNote)
summarize_git_without_note(WithoutGitNote)

