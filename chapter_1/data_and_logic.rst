Data And Logic
==============

Practicing actuaries are managing more complex system and workflow everyday, especially in reserving. While reserving in of itself is a complex topic, many actuaries prefers routine workflow that is intuitive and easy to manage.

This paper discusses practical considerations on the analytical and workflow structure of setting an unpaid claim estimate. Literature abounds on actuarial methods and assumptions used to tackle specific reserving issues, but there is very little research into the best practices of managing actuarial reserving workflows. Today, management teams of companies increasingly desire

1.	Faster speed in end-to-end analysis,
2.	Lower cost in running a reserving shop, and
3.	More detailed insight into the drivers of loss experience

These pressures continue to shape the evolution of reserving against a backdrop of technology advancements that are outpacing advancements in actuarial reserving processes.  They point to the need to scale up the reserving function to meet the needs of the business.

At the heart of our recommendation for scaling up a reserving function is the establishment of standards that improve the ability to scale. Standards are used throughout a variety of industries to establish common language, seamlessly integrate different technologies, and improve interoperability where possible. We propose a standard for data management of the loss triangle along with a standard for building actuarial models with an explicit declaration of model assumptions.

Our belief is that these standards can improve the efficacy of a reserving function by preserving traditional techniques and standards of practice while simultaneously enabling a foundation for more advanced data and modeling needs.  These standards are borne out of the idea that a separation of concerns is a good thing for scaling up the complexity of a workflow.


===========================================
Should Data and Business Logic be Separate?
===========================================

The actuarial profession is used to working with spreadsheets. The CAS technology survey consistently shows Microsoft Excel as the dominant tool used in actuarial work. Indeed for a large swath of actuarial problems, spreadsheets are fantastic tool.  According to the ASTIN 2016 Non-Life Reserving Practices Survey, the plurality of practitioners worldwide use spreadsheet software for meeting reserving obligations.

Spreadsheets differ from traditional software applications in that they generally promote interdependence between the data and business logic. Because of this, there is no difference between cells with raw data and cells with formulae.  At a small enough scale, this is easy to reason about making spreadsheets great for simple models, prototypes, when working with small data sets.

Because of the interdependence between data and logic, spreadsheet complexity tends to grow at a faster pace than analytical complexity. Most spreadsheet functions are designed to reference static cells and ranges.  Changes to the shape of data often mean a manual update of references is inevitable.

The desire to decouple data and business logic is compelling. Updating a spreadsheet business logic to accommodate another year or quarter of data becomes tedious, prone to error, and is an inefficient use of actuarial time in the long run.  Actuaries have developed tips and tricks to avoid this including using combinations of formulas such as OFFSET/MATCH to generate dynamic ranges. This is a sound approach, but not without trade-offs.  First, the spreadsheet becomes substantially more difficult to audit and debug. Second, spreadsheets take a hit on performance with dynamic formula. Volatile functions, like OFFSET and INDIRECT are difficult for Excel to optimize due to their dynamic nature. Lastly, complex formulas require robust documentation, and often, important detail can be lost in communication.

Visual Basic for Applications (VBA) and PowerPivot backend are excellent extensions for Microsoft Excel that naturally address some of these concerns. The inclusion of LAMBDA functions, dynamic arrays and tables with Structured References are also moves towards improving the scalability of spreadsheets. These are welcome advancements in capabilities that allow for much better chances for scale.  However, the fact that data and logic are co-mingled really make it difficult to use spreadsheets as software. The separation of data and logic is a defining difference between spreadsheets and software with the latter having much more scalable virtues.

Shareability is another key requirements to a software-oriented approach to actuarial work. Every company has their own implementation of spreadsheets with much of the same basic functionality, albeit with lots of variation. As a profession that adheres to standards of practice, its natural for commonalities in approaches to be used throughout industry. Yet spreadsheets are not shared in the public domain with as much frequency as software packages.  This is because of the co-mingled nature of data and logic as well as the approach to designing spreadsheets which is often emphasizes practical and actuarial aspects rather than emphasizing quality and reusability of work product.

In the context of open-source software, reserving capabilities can be developed with much more rigor than any one company’s spreadsheet implementation. Widely used open-source software logic is tested in the public domain. Usage of software by multiple people in multiple companies substantially feeds back into the quality of the work product. A 2009 meta-analysis found that over 90 percent of reviewed spreadsheets contain errors.  While software is not immune to errors, the expected volume of errors within a piece of software reduces as the user base of that software increases. This is particularly beneficial for actuarial teams in smaller firms without the resources to test and maintain bespoke spreadsheet applications.

Another benefit to a software-oriented approach to reserving is reusability. By design, the business logic is intended to support a variety of different use cases whether that be for start-up companies with limited history, long-tenured companies with decades of data.

Specialized reserving software exists to deal with a lot of these scalability issues already mentioned. There are several reserving software available and these applications are often vetted by well-funded teams of actuaries and software developers and are an excellent choice for scaling up enterprise reserving.  However these applications's source code is not open, so auditing the internal calculations can be challenging, or even impossible.  Furthermore, modifications of software are generally closed to customers with niche needs.  In other words, clients must work with the developers for feature enhancements, and cannot make modification to the product that they had purchased themselves.

Increases in analytical sophistication has consequences for the complexity of data, process, and workflow of a reserving work product. Contrasted against the discipline of software development, which has tools and capabilities to manage these complexities, there is a compelling argument that scaling analytical sophistication should warrant closer alignment and even adoption of software development capabilities. Software development is often subject to strict requirements to ensure a high quality output. This often includes:

*	Version control: Logic version control systems, such as git, track logic changes over time, allowing developers to manage different versions that ensure consistency, collaboration, and history tracking. In the context of analytical complexity, this allows for efficiently managing different versions of analysis and can benefit scenario testing, prototyping, and general collaboration on an analysis.
*	Computational environments: Environments are distinct setups for software development that allow for variations on set-up to include different technologies or different versions of the same technology. In the context of analytical complexity, this ensures reproducibility of results.
*	Testing: Software testing validates functionality, performance, and security in an automated fashion. In the context of analytical complexity, ensuring a component of a broader analysis works consistently provides assurances that evolution of an analysis does not unwittingly introduce errors.

The software development life cycle treats these capabilities as first-class citizens. The usage of these capabilities directly facilitates a higher quality work product at scale. None of these is particularly easy to use or accomplish when logic is maintained in spreadsheet software. This is in part driven by the lack of separation between data and business logic.

If the reader is comfortable with the notion that data and business logic should be separate, let’s discuss how the chainladder-python package, the most popular open-source actuarial software on GitHub, approaches the topic of data and business logic standards.

==================================================
A Standard for Data: The Multidimensional Triangle
==================================================

Tidy data is a standard way of mapping the meaning of a dataset to its structure. A dataset is messy or tidy depending on how rows, columns and tables are matched up with observations, variables and types. 

In tidy data:

#.	Each variable is a column; each column is a variable.
#.	Each observation is a row; each row is an observation.
#.	Each value is a cell; each cell is a single value.

Tidy data makes it easy for an analyst or a computer to extract needed variables because it provides a standard way of structuring a dataset.  The basic triangle is not considered tidy data. A single variable, say losses paid, spans multiple rows. A single observation, say accident year, spans multiple columns. Data shaped as a basic triangle contains rows representing a time-dependent cohort of loss data. This is commonly the accident period, but could be report period as well as policy period. Cohorts are reviewed at regular intervals to elucidate the loss development process. In its simplest form, a triangle may look like the following:

.. ipython:: python

   import chainladder as cl
   cl.load_sample('raa')

This standard view of a loss triangle is an important structure for actuarial work. (Possibly make some references to the notation used in Monograph 4 which has a formal notation for describing a loss triangle.

On its own, it is a useful structure for performing analysis, but the lack of tidy structure makes it more challenging to derive more complex insights.  For example, actuaries seldom look at a single triangle to formulate an opinion on unreported claims. Actuaries will often have a suite of triangles, many of which are arithmetic combinations of other triangles to inform their analysis.  Such triangles include:

*	Paid vs incurred loss data.
*	Loss vs loss adjustment expense data.
*	Reported, open and closed claim count data.
*	Exposure-based triangles for auditable exposures.
*	Reserve groupings that reflect homogenous groupings of a heterogeneous book of business.

The suite of triangles available to an actuary tend to vary along two aspects – quantitative (e.g. reported count, paid loss) and qualitative groupings (e.g. line of business, jurisdiction). These different groupings are often called measures and dimensions in data modeling.

The multidimensional triangle aims to blend the need for a suite of triangles and the benefits of tidy data.  So as to differentiate between the conventional definition of a triangle and a multidimensional triangle, we will refer to the multidimensional triangle as a `Triangle`. Rather than considering each unique triangle as its own independent messy data, a single observation of a `Triangle` is a conventional triangle. A suite of conventional triangles can be laid out in tidy format in a table of triangles where each cell of the table is a conventional triangle. It can look like this:

.. image:: https://chainladder-python.readthedocs.io/en/latest/_images/triangle_graphic.PNG

Here, `index` includes the qualitative properties of the observation, and `column` contains the quantitative properties.

Though tidy data finds its roots in R, tidy concepts apply to all tables of data and can be queried by any dataframe library syntax. Because of the implementation of chainladder-python in the Python programming language, the syntax for working with a `Triangle` follows Python’s most widely used dataframe library, pandas. Treating a suite of triangles as a tidy dataframe substantially enhances the diagnostic capabilities of the practitioner as it allows for exposition of data manipulation used by pandas while preserving access to the untidy traditional loss triangle format.

With the pandas API, we can filter our data, perform aggregations across groups, derive new quantitative measures, and apply basic arithmetic to our suite of triangles.

`Triangle` is not just used for selecting development patterns, it becomes a query tool for diagnostic insights into the reserve setting process. For example, the ratio of a closed count triangle to a reported count triangle yields a triangle of closure rates. A ratio of paid losses to case incurred losses yields a view into changes into paid patterns relative to incurred patterns. Arithmetic of triangles is so common in practice that it should follow the simple syntax of the arithmetic of columns in a table.

While a tidy format substantially expands on the capabilities of loss reserving data, not all use-cases can be supported by treating a basic loss triangle as an atomic unit of data.  Accessing origins, development lags, and diagonals is also a common need for actuaries. This is akin to needing to access detailed components of other complex data type such as strings and dates.  Most dataframe libraries including pandas have solved for this level of access. To access these granular components of a triangle, the multidimensional triangle also borrows from the accessor capabilities of pandas. In pandas, parsing a broader text field for key pieces of information is handled by exposing the `str` object of a text column. Doing date manipulation is handled by exposing the `dt` object. As an extension of this approach, the `Triangle` exposes `origin`, `development` and `valuation` accessors to access data which allows for expanded query capabilities such as a comparative view of age-to-age factors of one development lag or run-off of claims activity over the subsequent diagonal.

Being able to manipulate a suite of triangles as a dataframe using a syntax broadly adopted by the pandas community not only allows for rapid exploration of reserving data, but also reinforces skills more broadly used across the Python data ecosystem. The trade-off of tidy vs untidy data structures is substantially diminished through the exposition of accessors.

========================================================
A Standard for Modeling: Borrowing from Machine Learning
========================================================

Estimation of an unpaid claim analysis is informed by three sources:

#.	Data: This is typically a suite of triangles and was discussed in the previous section.
#.	Reserving Models: Often referred to as actuarial methods. The practitioner decides which methods are appropriate for the analysis at hand. The choice of model inherently has model risk and actuaries will typically use several models to reduce this risk.
#.	Assumptions: The practitioner determines a set of assumptions to parameterize each reserving model and may include how to average age-to-age factors, whether to include an exogenous tail calculation, etc.

Models and assumptions are related, but are not the same thing. In the domain of machine learning, practitioners are equipped with a diverse array of algorithms or methods. However, each algorithm comes with its own set of assumptions and requires the tuning of specific hyperparameters to effectively guide the model's convergence toward a solution. In short, assumptions are model dependent.

Taking inspiration from scikit-learn, the most popular machine learning library in Python, we can explore how general purpose modeling standards can be applied to reserving. scikit-learn includes a suite of Machine Learning estimators that range anywhere from data prep (e.g. PCA, OneHotEncoding) to classification (e.g. RandomForestClassifier, K-neighbors), to regression (e.g. LinearRegression, ElasticNet), to clustering (e.g. K-means).

The chainladder-python package uses the scikit-learn estimator as the foundation to model construction. Similar to scikit-learn, actuaries use a variety of techniques and algorithms to model unpaid claim estimates. These can span a variety of use cases including:

#.	Selecting loss development factors (`Development`, `ClarkLDF`, `DevelopmentConstant`)
#.	Extrapolating tail factors (`TailCurve`, `TailBondy`)
#.	Triangle data adjustment (`ParallelogramOLF`, `BerquistSherman`)
#.	Developing unpaid claim estimates (`Chainladder`, `BornhuetterFerguson`, `CapeCod`)

Model selection is a starting point for an analysis, how the model behaves can be altered through the usage of hyperparameters. For example, scikit-learn’s ElasticNet estimator includes the following hyperparamters to influence how the model behaves (alpha, l1_ratio, fit_intercept, precompute, max_iter, copy_X, tol, warm_start, positive, random_state, selections).  A key property of these hyperparameters is that they can be set prior to the fitting of the estimator to any data.  This is similar to assumption setting where an actuary may want to influence how development factors are calculated. The Development estimator has the following hyperparameters to aid in assumption setting (n_periods, average, sigma_interpolation, drop, drop_high, drop_low, preserve, drop_valuation, drop_above, drop_below, fillna, groupby). `n_periods` would indicate the number of diagonals from a triangle to be used in selecting loss development. `average` allows for selection between ‘simple’, volume’ and ‘regression’. Each of these can be varied for each development lag and are specified before fitting the estimator to a Triangle.

Analytical workflows are more complex than just fitting single estimators. Scikit-learn accommodates chaining separate algorithms together to support more complex workflows. It’s entirely reasonable to perform PCA on data before pushing it into a KNeighbors classifier. Chaining algorithms together is possible in chainladder and is facilitated through the use of composite estimators called `Pipeline`s.

As is the case with the suite of machine learning estimators, not all of use-cases are intended to develop unpaid claims estimates in isolation. An actuary may want to perform a basic chainladder projection on a Berquist-Sherman adjusted set of triangles.  It is also common to see a single set of development factors being used across both a multiplicative Chainladder and a Bornhuetter-Ferguson approach.  Separating techniques into composable estimators allows for reuse. As a practitioner, one can declare individual estimators and use those to create a `Pipeline` that describe a reserving process.

An example reserving `Pipeline` might be declared as follows:

.. ipython:: python

   import chainladder as cl

   cl.Pipeline(
       steps=[
         ('sample', cl.BootstrapODPSample(random_state=42)),
         ('dev', cl.Development(average='volume')),
         ('tail', cl.TailCurve(curve='exponential')),
         ('model', cl.Chainladder())
       ]
   )

It’s clear to see that this is a volume-weighted chainladder model with a tail factor set using exponential curve fitting. Further, this model will resample the `Triangle` it receives using overdispersed poisson bootstrapping to provide a simulated set of reserve estimates.

Some advantages of this approach:

#.	It is declared independent of the data it will be used on.
#.	The models used are explicit: `BootstrapODPSample`, `Development`, `TailCurve` and `Chainladder`.
#.	The assumptions used are also explicit: `random_state=42`, `average='volume'`, `curve='exponential'`.

These estimators also benefit from standardized models results. When performing an unpaid claim analysis, the actuary is seldom only interested in the ultimate unpaid claim amount. Projecting ultimates automatically produces IBNR and Run-Off expectations. These are standard outputs regardless of whether the practitioner uses a `CapeCod` method or a `Benktander` method. Such outputs allow for further diagnostic development such as duration and cashflow analysis and calendar period performance against prior expectations.

Leveraging the modeling framework of scikit-learn allows the practitioner and library maintainers to capitalize on lessons learned in analytical workflow management from the machine learning community. Additionally, the framework reinforces skills more broadly used across the Python data ecosystem.

The primary goals of the chainladder-python library are inherently to manage analytical complexity. It does so by exposing a code-based API to the practitioner. This enables the usage of many software development facilities that support scaling up complexity. By leveraging the syntax standards of the most popular data manipulation package (pandas) and machine learning package (scikit-learn), chainladder-python is designed to remove as much friction from the learning process as possible.


