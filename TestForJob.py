FILE_PATH = 'P:\exam\\release_notes.txt'

"""
return the value [issue] Title number string for error with comment to the array
"""


def FunGitNote(arr, idx):
    title = arr[idx].replace('Title: ', '')
    for line in arr[idx:]:
        if "Issue:" in line:
            issue = line.replace('Issue: ', '').replace("\n", "")
            return f'[{issue}] {title}'


"""
return the vaule [NOTE_MISSING] commit #number @owner , Please add git notes to this commit for missing comment on git
"""


def FunWithoutGitNote(arr, index_in_array):
    note_missing = arr[index_in_array]
    for line in arr[index_in_array:]:
        if "Owner:" in line:
            owner = line.replace('Owner: ', '').replace("\n", "")
            return f'{note_missing}@{owner}, Please add git notes to this commit!'


"""
return the lines from file
"""


def load_file(path):
    with open(path, "r") as f:
        return f.readlines()


"""
print the error + title of the git notes
"""


def print_git_note(git_note):
    check_duplicate_error = ""  # array for check duplicate errors
    for error in git_note:
        if error not in check_duplicate_error:  # check for duplicate errors
            print(error)
        check_duplicate_error += error  # add the error to the array


"""
print the note missing + commit and the owner with request to add commit
"""


def print_git_without_note(git_without_note):
    check_owner_no_comment = ["chdauto", "syspdbuild",
                              "syspdbuild2"]  # owners that dont need to print the missing commit
    for no_comment in git_without_note:
        if no_comment.split("@")[1].split(",")[0] not in check_owner_no_comment:  # check for owner that dont need to print
            print(no_comment)


git_note = []  # array that contains all the errors with note
without_git_note = []  # array that contains all the missing note

file_array = load_file(FILE_PATH)  # array that contains all the lines

for num in range(len(file_array)):
    if "Title" in file_array[num]:  # check if the string Ttile is in the line
        git_note.append(FunGitNote(file_array, num))  # add the string from the function to the array
    elif "[ NOTE_MISSING ]" in file_array[num]:  # check if the string [ NOTE_MISSING ] is in the line
        without_git_note.append(FunWithoutGitNote(file_array, num))  # add the string from the function

print_git_note(git_note)
print_git_without_note(without_git_note)
