# Package Management

Reserve studies apply algorithms to manipulate data. These algorithms can be written as Excel formulas, 
as a sequence of statements in a script, a collection of functions and classes in a package, or in a variety 
of other ways. The aim of this section is to promote the organization of these algorithms into packages, 
of which both the R and Python versions of Chainladder are examples. We will start by following what an actuary 
interested in applying programming on the job might do as they begin to learn their language of preference, 
by applying simple Python statements to an input triangle. We will then describe the problems the actuary may face 
when doing so and the motivations towards organizing their code into higher levels of abstraction - that is, 
functions, classes, and packages - designed to solve such problems.

# Algorithms Stored as a Sequence of Statements

# Algorithms Encapsulated as Functions

# Algorithms Organized into Classes

# Algorithms Organized into Packages

# Sharing Code Between Team Members

As a project increases in scope and visibility, there will be a time when the maintainer will need to share code with others or invite others to work on it.

## Reasons for sharing code

- Promote visibility within or beyond their organization
- Need to grant access to other departments, such as IT to assist in deployment and maintenance
- The project scope has grown so that more people need to be core contributors, such as new direct reports in an expanding team
- The project has become useful and other people want to use it  

## Non-recommended Methods for Sharing Code

The following methods for sharing code are not recommended but may have been used in the past prior to the rise of repository hosting providers. Because these methods are not optimal and come with many downsides, but can still be used to share code, it may be difficult to convince IT or upper management to provide proper tools or adopt industry best practices (source control hosted on a repository provider), since you may be told that as long these get the job done, you will need to put up with whatever inconveniences they may carry. Our goal is to clearly articulate these downsides in the hopes that you can overcome the communicative barrier at work.

### Email

Why you shouldn't share code this way:

- Companies may forbid attachments with certain code extensions (.py, .R).
- If you shared your code and latter make an update, you will need to send a new file. If your colleague also made their own update, they will need to manually inspect your new version and their version and hope that they didn't make any errors in doing so.

Communicative barriers:

If you bring these points up to upper management, you may receive the counterargument since there are often workarounds 

### Shared Folders

Perhaps you've gotten your department to adopt version control and have also been provided a shared drive to place your project.

Why you shouldn't share code this way:

- Poor integration with project management software: As a project grows in size, you will want start using tools to manage the project. This includes things like issue tracking, CI/CD, and automated testing. There are well-known commercial products such as GitHub, Azure DevOps, and Atlassian which provide such features out-of-the box, in addition to hosting code repositories on either an on-premises server or in the cloud. 
- Merge conflicts: Leaving an editable set of code on a shared drives opens the possibility of having uncommitted edits if people choose to edit the shared drive version of the code rather than locally and then pushing their code to a centralized hosting provider. This type of workflow will lead to conflicting versions of code across team members, which will be extremely difficult to reconcile if the project is large.


### Physical Media

At this time of writing, we would find this situation to be rare, but you never know what you might find at companies,
even today.  It is common for companies to lock down the ability of their employees to put data onto physical media
for security reasons, such as protecting data and intellectual property. For this reason alone, attempting to share 
code this way is not recommended. Another reason would be the inconvenience of physical media compared to 
Intra-/Internet transfer capabilities that we would hope would exist at most companies.

## Using a version control system

It doesn't take long for practitioner who is interested in code to independently arrive at the conclusion that some
form of version management is needed. Even with the absence of code, practitioners who work primarily with spreadsheets
will recognize the importance of preserving prior versions of their work so that they may be revisited later. For 
example, if one were to update a spreadsheet model, it may still be necessary to preserve a version of the model prior
to the update in order to answer questions from stakeholders as to why the prior model produced the numbers it did 
at the time it was used.

It has been the authors' experience that actuarial departments will develop their own practices when it comes to
managing prior versions of actuarial work. Such practices may involve appending spreadsheet names with some kind of 
suffix, e.g., "v1", "v2", etc., and inserting a sheet that includes a changelog with a verbal description of material
changes between spreadsheet versions, and who was responsible for those changes.

While such practices are well-intentioned, and indeed solve many problems that actuaries encounter, they come with
shortcomings and lack features that version control systems used in software have already solved and implemented.

One such shortcoming arises when the progression of complex actuarial projects is not monolithically linear. Imagine 
a large model embedded in a spreadsheet. The actuary decides to call this first version "v1." Later on, 

## Hosting

### Repository Hosting Providers

## Workflow

**Insert Diagram Here** Diagram between local contributors, data, hosting provider, downstream systems/applications

# Extensibility