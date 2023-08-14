import os
import subprocess
from tkinter import Tk, Label, Entry, Button, filedialog

def browse_files():
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, 'end')
    file_entry.insert(0, file_path)

def git_push():
    file_path = file_entry.get()
    repo_path = repo_entry.get()
    commit_msg = commit_entry.get()

    os.chdir(repo_path)
    subprocess.run(['git', 'add', file_path])
    subprocess.run(['git', 'commit', '-m', commit_msg])
    subprocess.run(['git', 'push'])

root = Tk()
root.title("Git Push App")

Label(root, text="File:").grid(row=0, column=0, sticky="e")
file_entry = Entry(root, width=50)
file_entry.grid(row=0, column=1)
Button(root, text="Browse", command=browse_files).grid(row=0, column=2)

Label(root, text="Repo Path:").grid(row=1, column=0, sticky="e")
repo_entry = Entry(root, width=50)
repo_entry.grid(row=1, column=1)

Label(root, text="Commit Message:").grid(row=2, column=0, sticky="e")
commit_entry = Entry(root, width=50)
commit_entry.grid(row=2, column=1)

Button(root, text="Push", command=git_push).grid(row=3, column=1, pady=10)

root.mainloop()