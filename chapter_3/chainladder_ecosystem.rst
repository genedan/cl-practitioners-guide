The Chainladder Ecosystem
=========================

Chainladder's open-source license, along with its transparent API, not only encourages users to enhance the quality
of its existing features, but also enables them to extend the package with new features and to use it as a dependency
in downstream applications. This section will highlight the nascent, but growing involvement of the actuarial community,
along with new projects that have emerged since Chainladder's inception.

Community Effort
----------------

Over the course of 6 years, X (insert number here) users have opened and closed 224 issues pertaining to bugs, usage
questions, and new features. Thanks to chainladder being hosted on an easily discoverable software development platform,GitHub, these efforts arose organically from actuarial practitioners with an interest in open source software.

The transparency of the package, along with the social-media aspects of GitHub, facilitated discussions between
developers from all over the world to improve the quality of the package. By being embedded in the broader open-source community, chainladder
continues to evolve to meet the ever-changing demands of business and technology.

Downstream Projects
-------------------
Here are well known projects that depend on chainladder-python.

Tryangle by Balona and Richman
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tryangle is an automatic chainladder reserving framework. It provides scoring and optimisation methods based on machine learning techniques to automatically select optimal parameters to minimise reserve prediction error. Key features include optimising loss development factors, choosing between multiple IBNR models, or optimially blending these models.

FASLR: Free Actuarial System for Loss Reserving by Dan
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

FASLR is a graphical user interface that uses Chainladder as its core reserving engine. It is intended to extend the
functionality of Chainladder by enabling the user to conduct reserve studies via interactive menus, screens, and mouse
clicks. It is built on top of a relational database, adding the ability to store and retrieve the results LDF and ultimate selections.


Proprietary Tools vs Open-Source Packages
----------------------------------------------------------------------------

The CAS conducts an annual technology survey, and the responses to the question “In which of the following tools do you plan to increase your proficiency in the next 12 months?” speak for themselves. Respondents are overwhelmingly interested in advancing skills that utilize open-source concepts; the top three choices (R, Python, and SQL) are all open-source tools. Even though the respondents might not consider if a project is open-source or not as the most important criteria, there is a certain appeal to open-source tools that make them popular and attractive.

While we recognize the attractiveness of continuing to use spreadsheet as the primary actuarial tool, there are many benefits to open-source tools.

-  Advantages:

   -  **Cost**: Open-source tools are cost-effective because they are
      typically free to use, making them accessible to individuals and
      organizations with limited financial budgets.
   -  **Permissive**: Open-source licenses often allow for extensive
      freedom in how the software is used, modified, and distributed,
      enabling diverse and innovative applications. They often have
      standardized licenses. We can finally leave our lawyers out of it.
   -  **Transparent**: Open-source tools provide transparency into their
      codebase, fostering trust and enabling users to verify security,
      functionality and privacy. Reproducibility: Because these tools
      are transparent, anyone will be able to reproduce and replicate
      the results published by someone else.
   -  **Flexible**: Open-source tools can be customized and adapted to
      suit specific needs, making them versatile for a wide range of
      applications and industries. In fact, most open-source tools are
      utilized because of their flexibility.
   -  **Direct access to developers**: Users of open-source tools often
      have direct access to the developer community, facilitating quick
      issue resolution and collaboration. There’s no need to go through
      helpdesks and wait for your tickets to be rerouted by customer
      service agents that have little to no clue what you are asking
      for.
   -  **Speed**: Open-source tools are generally faster, especially for
      making complex calculations or running simulations.
   -  **Source of ideas and talent**: Open-source projects attract
      talent from around the world, fostering innovation and generating
      new ideas that benefit the entire community.
   -  **Democratic**: Open-source tools can promote an inclusive and
      democratic development model, where contributions and decisions
      are made by a global community rather than a single entity.
   -  **Pull requests**: Open-source projects encourage collaboration
      through pull requests, which are requests that can be made when an
      independent developer wants their code or contribution “pulled”
      into the main project’s code repository. This allows anyone to
      contribute by fixing bugs or implementing new features to the
      project.
   -  **Fork**: In the event of a disagreement, for example, when a pull
      request is rejected, the ability to fork open-source projects
      allows users to create new versions of the software, promoting
      diversity and competition in the development ecosystem.

But of course, there are benefits to proprietary actuarial softwares, here are some of the weakness-es of open-source tools:

   -  **Skills**: Open-source tools can be more complex, necessitating a
      more significant up-front investment of time and effort to master
      compared to some commercial alternatives, especially if you need
      to customize the tools for your specific needs.
   -  **Familiarity**: Open-source tool projects are often foreign to
      many users, both in terms of its understanding the raw source code
      and accessing their results. This sometimes create additional
      friction between business units.
   -  **Compatibility**: Compatibility issues may arise when integrating
      open-source tools with existing legacy systems, potentially
      causing disruptions and additional development efforts.
   -  **Usage restrictions**: Some organizations may have cybersecurity
      policies or government regulatory constraints that limit the use
      of open-source tools, potentially hindering their adoption.
   -  **Limited resources**: Open-source projects may experience
      irregular maintenance or even abandonment due to their limited
      resources, this can leave users with outdated or unsupported
      software and potential security vulnerabilities.
   -  **Intellectual property & licenses**: Users sometimes need to be
      aware of the various open source licenses and the associated
      permissions and requirements and how they would impact their
      company intellectual property. For example, the General Public
      License (GPL) requires derivative works to be distributed under
      GPL terms, which means the derivative works must be open-sourced
      as well.

While there are many other elements to consider when choosing the
product that suits your analytics needs, these are generally the main
consideration between open-source and proprietary tools when all else
being equal.

The Powerful Microsoft Excel
----------------------------------------------------------------------------

The authors recognize the usefulness of spread-sheet tools such as Microsoft Excel. Excel is widely used in the actuarial profession due to its versatility, accessibility, and rich feature set tailored for financial and actuarial analysis. Here is a detailed look at why actuaries might prefer Excel over other scripting tools like Python, R, or MATLAB:

1. **User-Friendly Interface**

Excel offers a graphical user interface that is highly intuitive and accessible even to those with minimal programming experience. This makes it easier for actuaries to manipulate data, perform calculations, and visualize results without the need for extensive coding knowledge.

2. **Real-Time Data Visualization**

Excel provides robust tools for creating charts and graphs that update in real time as data changes. This is particularly useful for actuaries who need to present data in a way that is easy to understand and interpret for stakeholders who may not have a technical background.

3. **Widespread Adoption and Familiarity**

Excel is a standard tool in most business environments, including insurance and financial services. This widespread adoption means that sharing files, collaborating on projects, and integrating with other business processes is streamlined, reducing the friction that might arise with less familiar or more specialized tools.

4. **Built-in Financial Functions**

Excel comes equipped with numerous built-in functions that are specifically designed for financial and actuarial calculations, such as NPV, IRR, and various amortization functions. This pre-built functionality can save time and reduce errors compared to coding similar functions from scratch in a scripting language.

5. **Pivot Tables and Data Analysis**

Actuaries often deal with large datasets. Excel's pivot tables allow for dynamic summarization and analysis of data, enabling actuaries to quickly extract insights without needing to write complex scripts.

6. **Integration with Other Microsoft Products**

Excel integrates seamlessly with other Microsoft Office products like Word and PowerPoint, making it easier to transfer data and results into reports or presentations. This compatibility is especially useful in corporate environments where Microsoft Office is the norm.

7. **Dependency by Other Teams**

Excel integrates well with many other products, and as such, many of the downstream work product demands that the actuaries feed them the result in Excel. 

8. **Excel Add-Ins and Tools**

There are numerous add-ins available for Excel that enhance its capabilities, some of which are specifically designed for actuarial work. Tools like @RISK or the Excel add-in for SQL Server bring advanced statistical and stochastic modeling capabilities right into the spreadsheet.

9. **Macro and VBA Support**

For more complex or repetitive tasks, Excel supports macros and VBA (Visual Basic for Applications), allowing actuaries to automate their workflows. While VBA does require some programming skills, it is generally considered more accessible than more complex programming languages used in other statistical tools.

Final Remarks
----------------------------------------------------------------------------

(Need to close out the paper)