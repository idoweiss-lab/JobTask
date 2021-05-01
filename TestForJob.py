def FunGitNote(arr , IndexInArray):
    Title = FileArray[IndexInArray].replace('Title: ', '')
    for line in arr[IndexInArray:]:
        if("Issue:" in line):
           issue = line.replace('Issue: ','')
           issue = issue.replace("\n", "")
           return "["+issue+"]"+ " " + Title

def FunWithoutGitNote(arr , IndexInArray):
    NoteMissing = FileArray[num]
    for line in arr[IndexInArray:]:
        if("Owner:" in line):
           owner = line.replace('Owner: ','')
           owner = owner.replace("\n", "")
           return NoteMissing + "@"+owner+ " , Please add git notes to this commit!"

CheckDuplicateEror = ""
CheckOwnerNoCommaent = ["chdauto", "syspdbuild", "syspdbuild2"]
GitNote = []
WithoutGitNote = []
FileArray = []
f = open("P:\exam\\release_notes.txt", "r")
for line in f:
   FileArray.append(line)
ArrayLen = len(FileArray)
for num in range(ArrayLen):
    if("Title" in FileArray[num]):
        GitNote.append(FunGitNote(FileArray,num))
    elif ("[ NOTE_MISSING ]" in FileArray[num]):
        WithoutGitNote.append(FunWithoutGitNote(FileArray,num))
for Error in GitNote:
    if(Error not in CheckDuplicateEror):
        print(Error)
    CheckDuplicateEror += Error
for NoComment in WithoutGitNote:
    if(NoComment.split("@")[1].split(" ,")[0] not in CheckOwnerNoCommaent):
        print(NoComment)

