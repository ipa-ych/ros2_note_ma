import os
import subprocess

def git_push():
    # Change directory to your local Git repository
    os.chdir("/home/nhg-yc/Desktop/Notes")

    # Add all files to staging area
    subprocess.run(["git", "add", "."])

    # Commit changes
    subprocess.run(["git", "commit", "-m", "Automatic commit"])

    # Push changes to GitHub
    subprocess.run(["git", "push", "origin", "master"])  # Assuming master branch

if __name__ == "__main__":
    git_push()
