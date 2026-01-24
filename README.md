<h3>Hello 👋 I'm Ruslan Project manager here my GIT – Short Report💻</h3>

![Header](https://github.com/WhiteRichMan/WhiteRichMan/blob/main/assets/animef.gif)

# Software-Development
# GIT – Short Report


**Language:** Python  
**IDE:** VS Code  
**Git server:** GitHub / GitLab  

This report describes all required Git operations performed using a local project and a remote repository.
All actions were done using both terminal and IDE Git tools.

---

## a) Create remote repository
A remote repository was created on GitHub/GitLab.  
It is used to store the project online.

---

## b) Clone the empty repository
The remote repository was cloned to the local machine.

Command used:

git clone <repo-url>

## c) Create empty local project

An empty Python project was created inside the cloned repository.

---

## d) Commit the whole project

The initial project structure was saved to Git history.

**Commands used:**

git add .
git commit -m "Initial empty project"

<p align="center">
  <img src="screen1.png" width="300">
</p>

----

## e) Add simple code (create table)

Simple Python code was added to create a table (list).

table = [0] * 10
print(table)

<p align="center">
  <img src="Screen2.png">
</p>

---

## f) Commit changes

The added code was saved as a new commit.

**Command used:**

git commit -am "Create table"


<p align="center">
  <img src="Screen3.png">
</p>

---

## g) Initialize table with random values

The table was filled with random numbers.

import random
table = [random.randint(0, 99) for _ in range(10)]
print(table)


<p align="center">
  <img src="Screen5.png">
</p>

---

## h) Commit changes

The changes were committed.

**Command used:**

git commit -am "Initialize table with random values"


<p align="center">
  <img src="Screen4.png">
</p>

---

## i) Sort table elements

Sorting of table elements was added.

table.sort()
print(table)


<p align="center">
  <img src="Screen4.png">
</p>

---

## j) Commit changes

Sorting functionality was committed.

**Command used:**

git commit -am "Sort table elements"


<p align="center">
  <img src="Screen5.png">
</p>

---

## k) Look at code history

Commit history was checked.

**Command used:**

git log


<p align="center">
  <img src="Screen6.png">
</p>

---

## l) Look at code annotations

Line-by-line code history was checked.

**Command used:**

git blame funvtional.py


<p align="center">
  <img src="Screen7.png">
</p>

---

## m) Checkout different revisions

Different versions of the project were checked.

**Commands used:**

git checkout <commit-id>
git checkout main


<p align="center">
  <img src="Screen8.png">
</p>

---

## n) Add changes without commit

The code was modified but not committed.

---

## o) Revert last changes

Uncommitted changes were reverted.

**Command used:**

git restore main.py


<p align="center">
  <img src="Screen9.png">
</p>

---

## p) Push project to remote repository

All commits were uploaded to the remote repository.

Command used:

git push origin main

<p align="center">
  <img src="Screen10.png">
</p>

---

## r) Delete local project and repository

The local project and repository were removed.

<p align="center">
  <img src="Screen11.png">
</p>

---

## s) Clone project again from remote repository

The project was cloned again from the remote repository.

**Command used:**

git clone <repo-url>

<p align="center">
  <img src="Screen12.png">
</p>

---

## t) Create tag and switch between tag and main

A tag was created to mark a project version and switching was tested.

**Commands used:**

git tag v1.0
git checkout v1.0
git checkout main

<p align="center">
  <img src="Screen13.png">
</p>

---

## u) Create new branch from main

A new branch was created from the main branch.

**Commands used:**

git branch improvement
git checkout improvement

---

## w) Switch to branch

Work was continued in the new branch.

**Command used:**

git checkout improvement

---

## x) Improve code in branch

The sorting algorithm was improved in the branch.

table = sorted(table, reverse=True)
print(table)

**Command used:**

git commit -am "Improve sorting algorithm"

---

## y) Merge branch into master

Changes from the branch were merged into the main branch.

**Commands used:**

git checkout main
git merge improvement

<p align="center">
  <img src="Screen14.png">
</p>
---

## z) Share repository with a friend

Repository URL was shared and access permissions were granted.

---

## z1) Produce conflict

A conflict was produced when two users edited the same file.

---

## z2) Solve conflict and push solution

The conflict was resolved manually and pushed to the remote repository.

**Commands used:**

git add .
git commit -m "Resolve merge conflict"
git push

---

## z3) Send repository URL to teacher

The repository URL and short report were sent to the teacher by e-mail.
Teacher access to the repository was enabled.

---

## Additional Git commands used
git status
git branch
git tag
git pull


<h2>Languages for tasks🌐 </h2>

![Python](https://img.shields.io/badge/-Python-grey?style=for-the-badge&logo=Python)
