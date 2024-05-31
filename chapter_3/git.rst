Git and Version Control Management
====================================

Global Information Tracker, or more commonly known as git, is a distributed version control system that can track changes within a repository, or folder. It is very commonly used by engineers or programmers to control source code versioning collaboratively. The "distributed" version control system just means that the local machines each have a local complete copy of the complete repository. That way, each team member can view, modify, and save changes to the repository without relying on a central system or impact others while they work on specific files.

There are in fact many versions of distributed source code management systems, such as Mercurial and Bazaar. These distributed version control systems help software development teams create strong workflows and hierarchies, with each developer pushing code changes to their own repository and maintainers setting a code review process to ensure only quality code is merged to the main branch, which can then be hosted on a centralized server.


Benefits of Distributed Version Control Systems
------------------------------------------------------------------------
- **Reliable backup copies**: A distributed version control system can be seen as a collection of backups. When a team member copies a repository, they create an offline backup. If the server crashes, or is in anyway jeopardized, every local copy serves as a backup. Unlike centralized systems, these distributed systems eliminates reliance on a single backup, enhancing reliability. Although some may think multiple copies waste storage space, most development involves plain text or code files, so the storage impact is minimal.

- **Flexibility for offline work**: A distributed version control system allows development activities to be performed offline, with internet needed only for confirming final changes to the main repository on a server. Individual users have a local copy of the repository, enabling them to view history and make changes independently. This flexibility lets team members address issues promptly and efficiently. Having a local copy also speeds up common tasks, as developers don't need to wait for server to respond, thereby boosting productivity and reducing frustration.

- **Quicker feedback for experimentation**: A distributed version control system simplifies branching by keeping the entire repository history locally, enabling quick code implementation, experimentation, and review. Developers benefit from fast feedback and can experiment new features by comparing changes locally before merging. This can greatly reduce merge conflicts, and it allows for easy access to the full local history helps in identifying bugs, tracking changes, and reverting to previous versions.

- **Faster merging**: Distributed version control systems enable quick code merging without needing remote server communication. Unlike centralized systems, they support diverse branching strategies (such as for implementation of new features, or testing in different code environments). This accelerates delivery and boosts business value by allowing team members to focus on innovation instead of dealing with slow builds.


Git: An Example of a Distributed Version Control System 
------------------------------------------------------------------------

It is important to note that git is only an example of a distributed version control system, and there are many other tools of version control systems.

It is also important to know that git does not equate to GitHub, or GitLab, despite their similar names. Git is the version control tracking system, which is a tool, that allows you to track code changes, and GitHub, GitLab, or Bitbucket are the centralized server that act as hosts to your repositories. GitHub by Microsoft and GitLab by its eponymous organization. They are each spaces for developers to work on Git projects, collaborate, and share and test their work. Both repositories are constantly evolving and have attracted user bases with millions of members.


Commonly Used Git Commands
------------------------------------------------------------------------

There are many git commands, however, a practicing actuary might be able to get by with just knowing a few. Let's explore some of the popular commands and how it might can relate to how an actuary that use a centralized folder sharing system for collaboration.

:code:`git clone`: The :code:`git clone` command downloads existing source code from a remote repository (e.g., GitHub), creating an identical copy of the latest project version on your local computer. This is similar to copying all the files (including folders) from your shared drive to your local machine.

:code:`git commit -m "commit message"`: Once we reach a certain point in development, we want to "save" our changes . :code:`git commit` is like setting a checkpoint in the development process which you can go back to later if needed. Note that a commit message is required for a commit, this message ideally should be descriptive in documenting what we have developed or changed in the source code. For example, useful messages might look like, "capping all large losses at $250k", or "setting the reinsurance quota share to 25%". For a traditional actuary, this can be very similar to "saving as", but in the git world.

:code:`git branch <branch-name>`: Branches are very important when it comes to version control systems. By using branches, several developers are able to work in parallel on the same project simultaneously. We can use the :code:`git branch` command for creating, listing and deleting branches. Think of branching as creating a road marker, which represents an independent line of development. Do you want to find out what the indication would look like with a different trend? Or how the a-priori change with a different development patterns? These are all great use cases of branches. We mark the roads where we deviate from the main road, so we know what changes are made subsequently, before committing these changes as to the main road.

:code:`git checkout <name-of-your-branch>`: To work on a branch, we need to first be on that branch. We use :code:`git checkout` mostly for switching from one branch to another. But we can also use it for checking out specific files and commits. Did another analyst update something that you need on another branch? We can get on that branch by checking it out. Or was there a new piece of code that was developed that we need to bring in? We can checkout the specific file that way.

:code:`git status`: How do we know what the current branch looks like as we work it over time? The :code:`git status` command gives us all the necessary information about the current branch. We can know if the current branch is up-to-date. Whether there are files that had bee created, modified, or deleted. Whether there are files staged (ready to be committed), unstaged (not ready to be committed) or untracked (git doesn't care about these files). Whether there is anything to commit, push or pull.

:code:`git add <files>`: From :code:`git status`, we can see a list of files that aren't tracked (or unstaged) by default. We can add the files that we stagged for commit by using :code:`git add`. For traditional practitioners, this is very similar to preparing a list of files that we are ready to deploy to a centralized shared-folder.

:code:`git push`: After adding and committing the changes, the next thing you want to do is send the changes to the remote server. :code:`git push` uploads all committed changes to the remote repository. Remember that unless we push the changes to the server, all changes made so far had only been for our local copy.

:code:`git pull`: :code:`git pull` is the opposite of :code:`git push`, where we download updates from the remote server.

:code:`git revert`: Sometimes we need to undo the changes that we've made. There are various ways to undo our changes locally or remotely, but we must carefully use these commands to avoid unwanted deletions.

:code:`git merge`: When we have completed development in our branch and everything works fine, the final step is merging the branch with the "main" branch. This is done with the :code:`git merge` command. :code:`git merge` basically integrates the experimental or developmental branch with all of its commits back to the main branch. It's important to remember that you first need to be on the specific branch that you want to merge with your feature branch.

There are many more git commands that might become useful for very specific use cases, but by understanding the basic commands above should allow you to have a basic understanding of how git works.
