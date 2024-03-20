“The first draft of anything is shit.” ― Ernest Hemingway

# Chapter 1
- Data Management Principles
  - (John) primarily the separation of data and modeling
    - Database management
      - In-memory (“RAM”)
          - (John) Sparse matrix
      - Long-term memory data storage (“Disk”)
          - (Gene) database architecture discussion
- (John) Implementation philosophy
  - reproducible workflow
- (Kenneth) Open-source tools  benefits and disadvantages


# Chapter 2
- Improvements
    - Unified dataset (without having to use multiple datasets across examples)
    - CLRD (Casualty loss reserves database)
        - Make adjustments
        - Quarterly “grain”
- (Kenneth) Tutorial/Guides
    - Jupyter-NB use Pydoc to convert
    - Sections
      - Working with Triangles
      - Triangle Development
      - Extending the Tail Factors
      - Applying Deterministic Models
        - Chain-ladder
        - Bornhutter-Ferguson
        - Expected Loss
        - Cape Cod
      - Applying Stochastic Models
        - Mack’s Chain-ladder
        - Shapland’s ODP model
- (Gene) Ideas to streamline workflow
    - Package-style workflow
    - Classes
    - Redeploy in new projects
        - How to keep good “results” of existing projects to reuse or share

# Chapter 3
- Spreadsheet vs proprietary package vs “chainladder-python” package
    - Benefits of why we should move towards package style tools
    - Nothing beats Excel for actuarial communication
        - The gap between Excel vs open-source package result
- Dependencies
    - Tryangle by Balon and Richman
    - FASLR by Dan
    - 
