# IECSE-ML-Winter-19

## The winter Machine Learning project of IECSE 2019

**Instructions:**

- Clone the IECSE ML Winter Project repository
```git clone https://github.com/whopriyam/IECSE-ML-Winter-19.git```

- Initialize a repository in the directory(this is just for information, you won't need this for any task) ```git init <Project Name>```

- Type ```cd IECSE-ML-Winter-19```

- Create a new branch with your name using the command ```git checkout -b <branch-name>```, with branch name in format ```<first-name>"-"<last-name>. eg.- git checkout -b Priyam-Basu.```

- All commits should be made to your own branch, **Never commit to master.** To prevent this always check what branch you're on before committing any changes, command to check current branch ```git branch```, command to checkout(change to) a branch, ```git checkout <branch-name>```.

- To pull solutions after they are uploaded to master, change branch to master and do a git pull.
```git checkout master```
```git pull origin master```

- Steps to submit your code.
* Add files to be committed using the command ```git add .``` (the "." after add means all files in the current directory will be added)
* Add a descriptive commit message for the same. Command- ```git commit -m "<msg>"```.
Format - ```Task #<task-no.> : description```. Mention any errors or issues in the code in the commit message, if any.

- Finally, push your code. command - ```git push origin <branch-name>``` <br>
**Note:** While pushing your code, the above git command might ask your GitHub Id and password, enter the same, and then after successful verification only will git push your branch onto GitHub

``` 
git checkout -b Priyam-Basu
git checkout Priyam-Basu	// to make sure you are in your own branch
git add .	// adds all files and subfolders to be committed in the current directory
git commit -m "Task #0: description"
git push origin Priyam-Basu 
```

- All solutions will be uploaded to master.

- All tasks will be posted on the [wiki](https://github.com/whopriyam/IECSE-ML-Winter-19/wiki).
