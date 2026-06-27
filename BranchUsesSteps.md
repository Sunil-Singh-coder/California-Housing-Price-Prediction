# hello this is by branch in this branch we changes perform and after all commit we merge them
# in avoid conflict 

# 🌿 Git Branch Notes

## What is a Branch?

A branch is a separate workspace in Git where developers can work on new features without affecting the main project.

Example:

```
master
│
├── login-feature
├── payment-feature
└── profile-feature
```

---

## Why Use Branches?

* Work on new features safely.
* Fix bugs without affecting the main code.
* Multiple developers can work together.
* Keep the `master` (or `main`) branch stable.

---

## Common Commands

### Check Current Branch

```bash
git branch
```

### Create a New Branch

```bash
git branch login-feature
```

### Create and Switch

```bash
git switch -c login-feature
```

### Switch Branch

```bash
git switch master
```

### Commit Changes

```bash
git add .
git commit -m "Added login feature"
```

### Merge Branch

```bash
git switch master
git merge login-feature
```

### Delete Branch

```bash
git branch -d login-feature
```

### Push Branch

```bash
git push origin login-feature
```

### Pull Latest Code

```bash
git pull origin master
```

---

## Merge Conflict

A merge conflict occurs when two branches modify the **same line** of the **same file**.

---

## How to Avoid Merge Conflicts

* Pull the latest code before starting work.
* Create a separate branch for every feature.
* Commit changes regularly.
* Avoid editing the same line as another developer.
* Merge changes frequently.

---

## Do NOT Do These

* ❌ Don't work directly on `master`.
* ❌ Don't keep uncommitted changes for a long time.
* ❌ Don't forget to pull the latest code.
* ❌ Don't use `git push --force` unless necessary.

---

## Important Note

A branch becomes different **only after a commit**.

If you create a file but **do not commit it**, it may still appear when switching branches because it is an uncommitted change.

---

## Basic Workflow

```
master
   │
Create Branch
   │
Write Code
   │
git add .
git commit
   │
git pull origin master
   │
git merge master (if needed)
   │
Switch to master
   │
git merge feature-branch
```

---

## Interview Tip

In professional projects, developers create a **new branch for every feature or bug fix**, test their changes, and then merge them into the `master` (or `main`) branch.
