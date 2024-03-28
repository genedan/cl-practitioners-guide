*“The first draft of anything is shit.”*
― Ernest Hemingway

# Should Data and Business Logic be separate?
The actuarial profession is used to working with spreadsheets. The CAS technology survey consistently shows Microsoft Excel as the dominant tool used in actuarial work. Indeed for a large swath of actuarial problems, spreadsheets are fantastic tool.  However, it is apparent that spreadsheets are routinely abused.

Spreadsheets differ from traditional software applications in that they generally promote interdependence between the data and the business logic. Data and logic are comingled as there is no difference between cells and ranges with raw data and cells with formulae.  At a small enough scale, this is easy to reason about making spreadsheets great for simple models, prototypes, and small data sets.

Because of the interdependence between data and logic spreadsheet complexity tends to grow at a faster pace than analytical complexity. Most spreadsheet functions are designed to reference static cells and ranges.  Changes to the shape of data typically requires updates to static range references in business logic.

The desire to decouple data and business logic is compelling. Updating a spreadsheet business logic to accommodate another year or quarter of data becomes tedious and is an inefficient use of actuarial time in the long run.  Actuaries have developed tips and tricks to avoid this including using combinations of formulas such as OFFSET/MATCH to generate dynamic ranges. This is a sound approach, but not without trade-offs.  First, the spreadsheet becomes substantially more difficult to audit and debug. Second, spreadsheets take a hit on performance with dynamic formula. Volatile functions, like OFFSET and INDIRECT are difficult for Excel to optimize due to their dynamic nature and difficult to debug.

Visual Basic for Applications and PowerPivot backend are excellent extensions for Microsoft Excel that naturally address some of these concerns. The inclusion of LAMBDA functions to promote reusability is also a nice step. Dynamic arrays and Tables with Structured References also allow for variable length datasets. These are welcome advancements in spreadsheet capabilities that allow for much better chances for scale.  However, the fact that data and logic are comingled really make it difficult to use spreadsheets as software. The separation of data and logic is a defining difference between software and spreadsheets.

Shareability is a key benefit to a software-oriented approach to actuarial work. Every company has their own implementation of spreadsheets with much of the same basic functionality. As a profession that adheres to standards of practice, its natural for commonalities in approaches to be used throughout industry. Yet spreadsheets are not shared in the public domain with as much frequency as software packages.  This is because of the comingled nature of data, often proprietary, and logic as well as the approach to designing spreadsheets which is often emphasizes practical and actuarial aspects rather than emphasizing quality software aspects of the work product.  

In the context of open-source software, reserving capabilities can be developed with much more rigor than any one company’s spreadsheet implementation. Open-source software logic is tested in the public domain. The greater usage the software by multiple people in multiple companies substantially feeds back into the quality of the work product. A survey on randomly sampled spreadsheets shows that 80% contain some error and 30% contain material errors (cite something).  Software is not immune to errors. However, the expected volume of errors within a piece of software reduces as the user base of that software increases. This is particularly beneficial for actuarial teams in smaller firms 

Another benefit to a software-oriented approach to reserving is reusability. By design, the business logic is intended to support a variety of different use cases whether that be for start-up companies with limited history, long-tenured companies with decades of data.

Specialized reserving software exists to deal with a lot of these scalability issues. There are several and these applications are often vetted by well-funded teams of actuaries and software developers and are an excellent choice for scaling up enterprise reserving.  However these applications are not open so auditing the internal calculations is challenging.  Software modifications are generally closed to customers with niche needs.

Analytical complexity as measured by the data, process, and work flow complexity of an analytical deliverable is a natural byproduct of increasing analytical sophistication. The ability to scale-up reserving sophistication safely and efficiently is a topic that is very seldom broached in actuarial literature. Contrasted against the discipline of software development which has developed standards and suites of capabilities to manage software complexity, there is a compelling argument that analytical complexity should warrant far more attention than it currently receives. Software development is often subject to strict requirements to ensure a high quality output. This often includes:
•	Version control – Logic version control systems such as git track logic changes over time, allowing developers to manage different versions ensuring consistency, collaboration, and history tracking. In the context of analytical complexity, this allows for efficiently managing different versions of analysis and can benefit scenario testing, prototyping, and general collaboration on an analysis.
•	Computational environments – Environments are distinct setups for software development that allow for variations on set-up to include different technologies or different versions of the same technology. In the context of analytical complexity, this ensures reproducibility of results.
•	Testing – Software testing validates functionality, performance, and security in an automated fashion. In the context of analytical complexity, ensuring a component of a broader analysis works consistently provides assurances that evolution of an analysis does not unwittingly introduce errors.
The software development life cycle treats these capabilities as first-class citizens. The usage of these capabilities directly facilitates a higher quality work product at scale. None of these is particularly easy to use or accomplish when logic is maintained in spreadsheet software. This is in part driven by the lack of separation between data and business logic.

If the reader is comfortable with the notion that data and business logic should be separate, let’s discuss how the chainladder-python package approaches the topic of data and business logic.

## A standard for data: The multidimensional triangle

Tidy data is a standard way of mapping the meaning of a dataset to its structure. A dataset is messy or tidy depending on how rows, columns and tables are matched up with observations, variables and types. In tidy data:
1.	Each variable is a column; each column is a variable.
2.	Each observation is a row; each row is an observation.
3.	Each value is a cell; each cell is a single value.

Tidy data allows the practitioner to conduct analysis, generate meaningful visualizations, and uncover actionable insights more efficiently.  The basic triangle is not considered tidy data. A single variable, say loss paid spans multiple rows. A single observation, say accident year, spans multiple columns. Data shaped as a basic triangle contains rows representing a time-dependent cohort of loss data. This is commonly accident period, but could be report period as well as policy period. Cohorts are reviewed at regular intervals to elucidate the loss development process. In its simplest form, a triangle may look like the following:
```python
cl.load_sample(‘raa’)
```
This standard view of a loss triangle is an important structure for actuarial work. (Possibly make some references to the notation used in Monograph 4 which has a formal notation for describing a loss triangle.

On its own, it is a useful structure for performing analysis, but the lack of tidy structure makes it more challenging to derive more complex insights.  For example, actuaries seldom look at a single triangle to formulate an opinion on unpaid claims. Actuaries will often have a suite of triangles, many of which are arithmetic combinations of other triangles to inform their analysis.  Such triangles include:
•	Paid vs incurred loss data
•	Loss vs loss adjustment expense data.
•	Reported, open and closed claim count data.
•	Exposure-based triangles for auditable exposures
•	Reserve groupings that reflect homogenous groupings of a heterogeneous book of business.

The suite of triangles available to an actuary tend to vary along two aspects – quantitative (e.g. reported count, paid loss) and qualitative groupings (e.g. line of business, jurisdiction). These different groupings are often called measures and dimensions in data modeling.

The multidimensional triangle aims to blend the need for a suite of triangles and the benefits of tidy data.  So as to differentiate between the conventional definition of a triangle and a multidimensional triangle, we will refer to the latter as a Triangle. Rather than considering each unique triangle as its own independent messy data, a single observation of a Triangle is a conventional triangle. A suite of conventional triangles can be laid out in tidy format in a “dataframe” of triangles where each cell of the dataframe is a conventional triangle.

Though tidy data finds its roots in R, the concept applies to all dataframe libraries. Because of the implementation of chainladder-python in the Python programming language, the syntax for working with a Triangle follows python’s most widely used dataframe library, pandas. Treating a suite of triangles as a tidy dataframe substantially enhances the diagnostic capabilities of the practitioner as it allows for exposition of data manipulation used by pandas while preserving access to the untidy traditional loss triangle format.

Useful practitioner tips when creating triangles
-	Push as much granularity of measures and dimensions into the triangle as possible to allow for aggregate views on demand. Individual claim and policy level information is ideal.
-	Stack premium/exposure based records and loss-based records vertically to maintain.


With the pandas API, we can do filters/aggregations - Mention something about filters, groupby, agg funcs with examples. 


Arithmetic - Triangles are not just used for selecting development patterns, they are also a good diagnostic tool. Often the relationship between multiple triangles provides insights into formulating actuarial analysis. For example, the ratio of a closed count triangle to a reported count triangle yields a triangle of closure rates. A ratio of paid losses to case incurred losses yields a view into changes into paid patterns relative to incurred patterns. Arithmetic of triangles is so common in practice that it should be as effortless as arithmetic of integers or floating point numbers. That is, arithmetic combinations of triangles with other triangles or with scalars should be available to the practitioner.

Accessing origins, development lags, and diagonals is also a common need for actuaries. This is a barrier to treating a triangle like a single indivisible cell in a broader dataframe. To access these granular components of a triangle, the multidimensional triangle also borrows from the accessor capabilities of pandas. Pandas allows for deeper access to a datatype through accessor objects. These are most typically used with text and date data. For example, parsing a broader text field for key pieces of information is handled by exposing the `str` object of a text column. Doing date manipulation is handled by exposing the `dt` object. The multidimensional triangle exposes `origin`, `development` and `valuation` accessors to access data akin to the more traditional view of a triangle without sacrificing the 

Being able to manipulate a suite of triangles as a dataframe using a syntax broadly adopted by the pandas community not only allows for rapid exploration of reserving data, but also reinforces skills more broadly used across the python data ecosystem. The trade-off of tidy vs untidy data structures is substantially diminished through the exposition of accessors.



## A standard for modeling: Borrowing from machine learning 
Developing an unpaid claim analysis generally requires consideration for three things:
1.	Data – This is typically our suite of triangles and was discussed in the previous section
2.	Reserving Models - Often referred to as actuarial methods. The practitioner decides which methods are appropriate for the analysis at hand. The choice of model inherently has model risk and actuaries will typically use several models to reduce this risk.
3.	Assumptions – The practitioner determines a set of assumptions to parameterize reserving models.

We’ve already explored data through the multidimensional triangle. Models and assumptions are related, but are not the same thing. This is very apparent in the machine learning world where practitioners have different algorithms or methods available to them, but each of the algorithms has a set of assumptions or hyperparameters to tune how the model converges to an answer. 

Taking inspiration from scikit-learn, the most popular machine learning library in python, we can explore how general purpose modeling standards can be applied to reserving. Scikit-learn includes a suite of Machine Learning estimators that range anywhere from data prep (PCA, OneHotEncoding) to classification (RandomForestClassifier, Kneighbors), to regression (LinearRegression, ElasticNet), to clustering (Kmeans). 


The chainladder-python package uses the scikit-learn estimator as the foundation to model construction. Similar to scikit-learn, actuaries use a variety of techniques and algorithms to model unpaid claim estimates. These can span a variety of use cases including:
1.	Selecting loss development factors (Development, ClarkLDF, DevelopmentConstant)
2.	Extrapolating tail factors (TailCurve, Bondy)
3.	Prepping triangle data (ParallelogramOLF, BerquistSherman)
4.	Developing unpaid claim estimates (Chainladder, BornhuetterFerguson)


Model selection is a starting point for an analysis, how the model behaves can be altered through the usage of hyperparameters. For example, scikit-learn’s ElasticNet estimator includes the following hyperparamters to influence how the model behaves (alpha, l1_ratio, fit_intercept, precompute, max_iter, copy_X, tol, warm_start, positive, random_state, selections.  A key property of these hyperparameters is that they can be set prior to the fitting of the estimator to any data.  This is similar to assumption setting where an actuary may want to influence how development factors are calculated. The Development estimator has the following hyperparameters to aid in assumption setting (n_periods, average, sigma_interpolation, drop, drop_high, drop_low, preserve, drop_valuation, drop_above, drop_below, fillna, groupby). `n_periods` would indicate the number of diagonals from a triangle to be used in selecting loss development. `average` allows for selection between ‘simple’, volume’ and ‘regression’. Each of these can be varied for each development lag and are specified before fitting the estimator to a Triangle.


Analytical workflows are more complex than just fitting single estimators. Scikit-learn accommodates chaining separate algorithms together to support more complex workflows. It’s entirely reasonable to perform PCA on data before pushing it into a KNeighbors classifier. Chaining algorithms together is facilitated through the use of Pipeline estimators.

As is the case with the suite of machine learning estimators, not all of these use cases are intended to develop unpaid claims estimates in isolation. An actuary may want to perform a basic chainladder projection on a berquist-sherman adjusted set of triangles.  It is also common to see a single set of development factors being used across both a multiplicative Chainladder and a BornHuetterFerguson approach. Separating techniques into composable estimators allows for reuse. As a practitioner, one can declare individual estimators and use those to create composite estimators that describe a reserving process.


These estimators also benefit from standardized models results. When performing an unpaid claim analysis, the actuary is seldom only interested in the ultimate unpaid claim amount. Projecting ultimates automatically produces IBNR, and Run-Off expectations. These are standard outputs regardless of whether the practitioner uses a CapeCod method or a Benktander method. Such outputs allow for further diagnostic development such as duration and cashflow analysis and calendar period performance against prior expectations.


Leveraging the modeling framework of scikit-learn allows the practitioner and library maintainers to capitalize on lessons learned in analytical workflow management from the machine learning community. Additionally, the framework reinforces skills more broadly used across the python data ecosystem.


The primary goals of the chainladder-python library are inherently to manage analytical complexity. It does so by exposing a code-based API to the practitioner. This enables the usage of many software development facilities that support scaling up complexity. By leveraging the syntax standards of the most popular data manipulation package (pandas) and machine learning package (scikit-learn), chainladder-python is designed to remove as much friction from the learning process as possible.



