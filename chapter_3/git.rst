Git and Version Control Management
==================

Global Information Tracker, or more commonly known as git, is a distributed version control system that can track changes within a repository, or folder. It is very commonly used by engineers or programmers to control source code versioning collaboratively. The "distributed" version control system just means that the local machines each have a local complete copy of the complete repository. That way, each team member can view, modify, and save changes to the repository without relying on a central system or impact others while they work on specific files.

There are in fact many versions of distributed source code management systems, such as Mercurial and Bazaar. These distributed version control systems help software development teams create strong workflows and hierarchies, with each developer pushing code changes to their own repository and maintainers setting a code review process to ensure only quality code is merged to the main branch, which can then be hosted on a centralized server.


Benefits of Distributed Version Control Systems
------------------------
- **Reliable backup copies**: A distributed version control system can be seen as a collection of backups. When a team member copies a repository, they create an offline backup. If the server crashes, or is in anyway jeopardized, every local copy serves as a backup. Unlike centralized systems, these distributed systems eliminates reliance on a single backup, enhancing reliability. Although some may think multiple copies waste storage space, most development involves plain text or code files, so the storage impact is minimal.

- **Flexibility for offline work**: A distributed version control system allows development activities to be performed offline, with internet needed only for committing final changes to the main repository on a server. Individual users have a local copy of the repository, enabling them to view history and make changes independently. This flexibility lets team members address issues promptly and efficiently. Having a local copy also speeds up common tasks, as developers don't need to wait for server to respond, thereby boosting productivity and reducing frustration.

- **Quicker feedback for experimentation**: A distributed version control system simplifies branching by keeping the entire repository history locally, enabling quick code implementation, experimentation, and review. Developers benefit from fast feedback and can experiment new features by comparing changes locally before merging. This can greatly reduce merge conflicts, and it allows for easy access to the full local history helps in identifying bugs, tracking changes, and reverting to previous versions.

- **Faster merging**: Distributed version control systems enable quick code merging without needing remote server communication. Unlike centralized systems, they support diverse branching strategies (such as for implementation of new features, or testing in different code environments). This accelerates delivery and boosts business value by allowing team members to focus on innovation instead of dealing with slow builds.


Git: An example of a Distributed Version Control System 
------------------------

It is important to note that git is only an example of a distributed version control system, and there are many other tools of version control systems.

It is also important to know that git does not equate to GitHub, or GitLab, despite their similar names. Git is the version control tracking system, which is a tool, that allows you to track code changes, and GitHub, GitLab, or Bitbucket are the centralized server that act as hosts to your repositories. GitHub by Microsoft and GitLab by its eponymous organization. They are each spaces for developers to work on Git projects, collaborate, and share and test their work. Both repositories are constantly evolving and have attracted user bases with millions of members.


Commonly Used Git Commands
------------------------




Basic Git Workflow
------------------------

Here is a basic overview of how Git works:

1. Create a "repository" (project) with a git hosting tool (like Bitbucket)
2. Copy (or clone) the repository to your local machine
3. Add a file to your local repo and "commit" (save) the changes
4. "Push" your changes to your main branch
5. Make a change to your file with a git hosting tool and commit
6. "Pull" the changes to your local machine
7. Create a "branch" (version), make a change, commit the change
8. Open a "pull request" (propose changes to the main branch)
9. "Merge" your branch to the main branch