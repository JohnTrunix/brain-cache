# Git

Git is a version control system for tracking changes in computer files and coordinating work on those files among multiple people.

!!! note

    VS Code has a built-in Git support. You can use it to manage your repositories without using the command line.

## Most used commands

**Get latest changes from remote repository:**

```bash
git pull
```

!!! note

    Use `--rebase` flag to rebase local changes on top of remote changes.

**Add new file to index:**

```bash
git add <file>
```

!!! note

    You can add all files in current directory with `git add .` or `git add -a`

!!! danger

    `-f` flag is used to force all files to be added to the index also if they are ignored by `.gitignore` file.

**Commit changes:**

```bash
git commit -a -m "Commit message"
```

!!! note

    You can use `git commit -a` to commit all changes in tracked files.

    If you want to commit only a specific file, you can use `git commit -a <file> -m "Commit message"`

## Other useful commands

!!! note

    To leave the vim editor, type `:q` and press enter.

**Show status of tracked files:**

```bash
git status
```

**Show changes in tracked files:**

```bash
git diff
```

**Show changes/tracked/untracked of local files:**

```bash
git status
```

**Show commit history:**

```bash
git log
```

??? note "git log options"

    You can also filter the log:

    | Command | Description |
    | --- | --- |
    | `--author=<author>` | Show commits by author |
    | `--grep=<string>` | Show commits with message containing string |
    | `--since=<date>` | Show commits after date |
    | `--until=<date>` | Show commits before date |
    | `--oneline` | Show commits in one line |
    | `--graph` | Show commits as a graph |

## branch

**Create new branch:**

```bash
git branch <branch name>
```

**Switch to branch:**

```bash
git checkout <branch name>
```

**Merge branch into main:**

```bash
git checkout <main branch>
git merge <branch name>
```

## staging

This is the area where you see tracked files that are not yet committed.

## Init git & push to remote origin

```bash
git init
```

```bash
git add .
```

```bash
git commit -m "Initial commit"
```

```bash
git remote add origin <remote repository url>
```

```bash
git push -u origin master
```
