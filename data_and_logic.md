*“The first draft of anything is shit.”*
― Ernest Hemingway

# Should Data and Business Logic be separate?
The actuarial profession is used to working with spreadsheets. The CAS technology survey consistently shows Microsoft Excel as the dominant tool used in actuarial work. Indeed for a large swath of actuarial problems, spreadsheets are fantastic tool.  However, it is apparent that spreadsheets are routinely abused.

Spreadsheets differ from traditional software applications in that it generally promotes interdependence between the data and the business logic. Data and logic are comingled as there is no difference between cells and ranges with raw data and cells with formulae.  At a small enough scale, this is easy to reason about making spreadsheets great for simple models, prototypes, and small data sets.

Because of the interdependence between data and logic spreadsheet complexity tends to grow at a faster pace than analytical complexity. Most spreadsheet functions are designed to reference static cells and ranges.  Changes to the shape of data typically requires updates to static range references in business logic.

The desire to decouple data and business logic is compelling. Updating a spreadsheet business logic to accommodate another year or quarter of data becomes tedious and is an inefficient use of actuarial time in the long run.  Actuaries have developed tips and tricks to avoid this including using combinations of offset/match to generate dynamic ranges. This is a sound approach, but not without trade-offs.  First, the spreadsheet becomes substantially more difficult to audit and debug. Second, spreadsheets take a hit on performance with dynamic formula. Volatile functions, like OFFSET and INDIRECT are both difficult for Excel to optimize due to their dynamic nature and difficult to debug.

Visual Basic for Applications and PowerPivot backend are excellent extensions for Microsoft Excel that naturally address some of these concerns. The inclusion of LAMBDA functions to promote reusability is also a nice step. Dynamic arrays and Tables with Structured References also allow for variable length datasets. These are welcome advancements in spreadsheet capabilities that allow for much better chances for scale.  However, the fact that data and logic are comingled really make it difficult to use spreadsheets as software.

Shareability is a key benefit to a software-oriented approach to actuarial work. Every company has their own implementation of spreadsheets with much of the same basic functionality. As a profession that adheres to standards of practice, its natural for commonalities in approaches to be used throughout industry. Yet spreadsheets are not shared in the public domain with as much frequency as software packages.  This is because of the comingled nature of data, often proprietary, and logic as well as the approach to designing spreadsheets which is often emphasizes practical and actuarial aspects rather than emphasizing quality software aspects of the work product.  

In the context of open-source software, reserving capabilities can be developed with much more rigor than any one company’s spreadsheet implementation. Open-source software logic is tested in the public domain. The greater usage the software by multiple people in multiple companies substantially feeds back into the quality of the work product. A survey on randomly sampled spreadsheets  shows that 80% contain some error and 30% contain material errors (cite something).

Another benefit to a software-oriented approach to reserving is reusability. By design, the business logic is intended to support a variety of different use cases whether that be for start up companies with limited history, long-tenured companies with decades of data.

Specialized reserving software exists to deal with a lot of these scalability issues. There are several and these applications are often vetted by well-funded teams of actuaries and software developers and are an excellent choice for scaling up enterprise reserving.  However these applications are not open so auditing the internal calculations is challenging.

Reproducibility of results - Mention something about code allowing for code-supported workflows (version control, environments, unit testing, etc) that have been show to scale well for very complex projects.

If the reader is comfortable with the notion that data and business logic should be separate, let’s discuss how the chainladder-python package approaches the topic of data and business logic.

## A standard for data: The multidimensional triangle
Tidy data is a standard way of mapping the meaning of a dataset to its structure. A dataset is messy or tidy depending on how rows, columns and tables are matched up with observations, variables and types. In tidy data:
1.	Each variable is a column; each column is a variable.
2.	Each observation is a row; each row is an observation.
3.	Each value is a cell; each cell is a single value.

The basic triangle is not considered tidy data. A single variable spans multiple rows. A single variable, say loss paid spans multiple rows. A single observation, say accident year, spans multiple columns. Tidy data allows the practitioner to conduct analysis, generate meaningful visualizations, and uncover actionable insights more efficiently.
Data shaped as a basic triangle contains rows representing a time-dependent cohort of loss data. This is commonly accident period, but could be report period as well as policy period. Cohorts are reviewed at regular intervals to elucidate the loss development process. In its simplest form, a triangle may look like the following:
```python
cl.load_sample(‘raa’)
```
Possibly make some references to the notation used in Monograph 4.

Actuaries seldom look at a single triangle to formulate an opinion on unpaid claims. Actuaries will often have a suite of triangles, many of which are arithmetic combinations of other triangles to inform their analysis.  Such triangles include:
•	Paid vs incurred loss data
•	Loss vs loss adjustment expense data.
•	Reported, open and closed claim count data.
•	Exposure-based triangles which support development frequency, loss cost and loss ratio triangles.
•	Reserve groupings that reflect homogenous groupings of a heterogeneous book of business.

The suite of triangles available to an actuary tend to vary along two aspects – quantitative (i.e. reported count, paid loss) and qualitative groupings (e.g. line of business, jurisdiction). These different groupings are often called measures and dimensions.

The multidimensional triangle aims to blend the need for a suite of triangles and the benefits of tidy data.  So as to differentiate between the conventional definition of a triangle and a multidimensional triangle, we will refer to the latter as a Triangle. Rather than considering each unique triangle as its own independent messy data, a single observation of a Triangle is a conventional triangle. A suite of conventional triangles can be laid out in tidy format in a “dataframe” of triangles where each cell of the dataframe is a conventional triangle.

Though tidy data finds its roots in R, the concept applies to all dataframe libraries. Because of the implementation of chainladder-python in the Python programming language, the syntax for working with a Triangle follows python’s most widely used dataframe library, pandas. Treating a suite of triangles as a tidy dataframe substantially enhances the diagnostic capabilities of the practitioner.

Filters/Aggregations - Mention something about filters, groupby, agg funcs with examples.

Arithmetic - Triangles are not just used for selecting development patterns, they are also a good diagnostic tool. Often the relationship between multiple triangles provides insights into formulating actuarial analysis. For example, the ratio of a closed count triangle to a reported count triangle yields a triangle of closure rates. A ratio of paid losses to case incurred losses yields a view into changes into paid patterns relative to incurred patterns. 

Arithmetic of triangles is so common in practice that it should be as effortless as arithmetic of integers or floating point numbers. That is, arithmetic combinations of triangles with other triangles or with scalars should be available to the practitioner.

Include some brief examples of arithmetic.

Being able to manipulate a suite of triangles as a dataframe using a syntax broadly adopted by the pandas community not only allows for rapid exploration of reserving data, but also reinforces skills more broadly used across the python data ecosystem.

 


## A standard for modeling: Borrowing from machine learning 
Producing reserve estimates generally requires three things. 
1.	Data – This is typically our suite of triangles and was discussed in the previous section
2.	Reserving Models  - Often referred to as actuarial methods. The practitioner decides which methods are appropriate for the analysis at hand
3.	Assumptions – The practitioner determines a set of assumptions to parameterize reserving models.
Models and assumptions are related, but also not the same thing. This is very apparent in the machine learning world where practitioners have different algorithms or methods available to them, but each of the algorithms has a set of assumptions or hyperparameters to tune how the model converges to an answer. 

Taking inspiration from scikit-learn, the most popular machine learning library in python, we can...

Standardized models means standardized results – Producing ultimates automatically produces IBNR, and Run-Off expectations.


Efficiency/performance topics – do we really want to get into these?
*	In-memory (“RAM”)
*	(John) Sparse matrix





