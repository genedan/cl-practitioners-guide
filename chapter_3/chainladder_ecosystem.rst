The Chainladder Ecosystem
=========================

Chainladder's open-source license, along with its transparent API, not only encourages users to enhance the quality
of its existing features, but also enables them to extend the package with new features and to use it as a dependency
in downstream applications. This section will highlight the nascent, but growing involvement of the actuarial community,
along with new projects that have emerged since Chainladder's inception.

Community Effort
----------------

Over the course of 6 years, X (insert number here) users have opened and closed 224 issues pertaining to bugs, usage
questions, and new features. Thanks to chainladder being hosted on an easily discoverable software development platform
(GitHub), these efforts arose organically from actuarial practitioners with an interest in open source software.

The transparency of the package, along with the social-media aspects of GitHub, facilitated discussions between
developers to improve the quality of the package. By being embedded in the broader open-source community, chainladder
continues to evolve to meet the ever-changing demands of business and technology.

Spreadsheet vs proprietary package vs “chainladder-python” package (Kenneth)
----------------------------------------------------------------------------

Benefits of why we should move towards package style tools
Nothing beats Excel for actuarial communication

Downstream Projects
-------------------

Tryangle by Balona and Richman
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tryangle is an automatic chainladder reserving framework. It provides scoring and optimisation methods based on machine learning techniques to automatically select optimal parameters to minimise reserve prediction error. Key features include optimising loss development factors, choosing between multiple IBNR models, or optimially blending these models.

FASLR: Free Actuarial System for Loss Reserving by Dan
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

FASLR is a graphical user interface that uses Chainladder as its core reserving engine. It is intended to extend the
functionality of Chainladder by enabling the user to conduct reserve studies via interactive menus, screens, and mouse
clicks. It is built on top of a relational database, adding the ability to store and retrieve the results LDF and ultimate selections.