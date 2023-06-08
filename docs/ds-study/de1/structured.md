# Structured Data

## Save Data

| Flat Files                                   | Relational Systems            |
| -------------------------------------------- | ----------------------------- |
| easy to read, write, analyze                 | well defined structure        |
| no optimsed access                           | well structured and organized |
| inconsistent, concurrent, integrity problems | metadata in form of schema    |
|                                              | multiple users simultaneously |
|                                              | good Query processing         |

## OLTP vs OLAP

**OLTP** - Online Transaction Processing

**OLAP** - Online Analytical Processing

### OLTP

| Advantages        | Usage             |
| ----------------- | ----------------- |
| Many small writes | Ecommerce         |
| Real time         | Booking Systems   |
| Fast              | Bank Transactions |
| Efficient         | Consumer Goods    |

### OLAP

| Advantages                        | Usage                       |
| --------------------------------- | --------------------------- |
| Analysis of large Amounts of Data | Complex Business Questions  |
| Different Data Sources            | BI Systems                  |
| Aggregations                      | Data Warehouse Environments |
| Multidimensional Data             |                             |

### Comparision

| OLTP                                      | OLAP                                  |
| ----------------------------------------- | ------------------------------------- |
| Includes Day to Day Transactions          | Includes historical Transactions      |
| OLTP is used by DB Professionals          | OLAP is used by Managers and Analysts |
| To keep running the business              | to analyze the business               |
| Focus on Data                             | Focus on Information                  |
| ER Diagram                                | Star/Snowflake Schema                 |
| Highly detailed with flat relational Data | Aggregated, Multidimensional Data     |
| Around 1000 Users                         | Around 100 Users                      |
| Amount of Record access: 10               | Amount of Record access: 1 Mio        |
| DB Size: 100MB - 100GB                    | DB Size: 100GB - 100TB                |

## OLAP Operations

!!! info

    Operations to transform & analyze multidimensional Data Cubes

### Pivoting / Rotation

Cube rotation at Dimensions change, analysis from different perspectives. Perspectives

![Pivoting & Rotation](./images/pivot-rotate.png)

### Roll-up / Drill-down

**Roll-up** - Aggregation of detailed Data (Dimension Reduction)

**Drill-down** - Breakdown of aggregated Data (Dimension Enlargement)

![Roll-up & Drill-down](./images/drill-roll.png)

### Slice / Dice

**Slice** - Selection of one slice of a Dimension

**Dice** - Selection of one or more slices of multiple Dimensions

![Slice & Dice](./images/slice-dice.png)

## ROLAP, MOLAP, HOLAP

**MOLAP** - Multidimensional OLAP: Datawarehouse is a proprietary system, tailored for multi-dimensional data
manipulations

**ROLAP** - Relational OLAP: Multi-dimensional data mapped onto tables, and manipulations
mapped onto relational queries

**HOLAP** - Hybrid OLAP: Relational systems extended with specific OLAP functionalities

## Data Warehouse

!!! info

    Repository of integrated Data which manages multiple Data Sources

![Data Warehouse](./images/data-warehouse.png){ loading=lazy }

**Characteristics of a Data Warehouse**

-   Collection of Data to support Management's Decision Making Process
-   Subject oriented (Product, Customer, Sales, Revenue, etc.)
-   Integrated (from heterogeneous Data Sources)
-   Time Variant (historical Point of View)
-   Non-volatile (Data is never removed when new Data is added)
-   Data Warehouse is seperate from Operational Database

**Types of Data Warehouses**

-   Information Processing

    -   Data Processing in Data Warehouse
    -   Simple Statistics

-   Analytical Processing

    -   Supports analytical Processing
    -   Slice & Dice, Drill-down, Roll-up, etc.

-   Data Mining
    -   hidden Patterns, unknown Correlations, etc.
    -   Classification, Prediction, etc.

### Data Warehouse Modelling

| **Qualitative**                             | **Quantitative**                          |
| ------------------------------------------- | ----------------------------------------- |
| Category Attributes                         | Summary Attributes (Subject of Analysis)  |
| Data as navigation Structure (Drillpahts)   | Cells of Data Cubes (Dimensions as Edges) |
| Modeled as Term Hierarchies with Dimensions |                                           |

**Dimensions**

-   Describes a view of Measures
-   Orthogonal Structure for Data Space

**Dimensional Hierarchies**

-   Nodes für classification Hierarchies
-   Classification Level describes granularity of Data
-   Representation of Dimensions via classification Schema

**Simple Hierarchies**

```mermaid
graph LR
  TOP --> country --> city --> store
```

-   Higher Hierarchy Level contains aggregated Values of lower Level

**Parallel Hierarchies**

```mermaid
graph LR
	TOP --> year
	TOP --> week

	year --> quarter
    quarter --> month
	month --> day
	week --> day
```

-   Multiple independent Grouping Options

**Dimension Table**

-   ID for classification Node
-   Characteristic Attributes (Brand, Producer, Title, etc.)
-   Foreign Key (for direct Parent Hierarchy Level)

**Fact Table**

-   Foreign Keys (referencing bottom-level Category of each Dimension)
-   Set of all Foreign Keys (= **Composite Primary Key**)

### Star Schema

-   Avoiding Joins over multiple Tables
-   Denormalized Schema (Data Redundancy)
-   One Dimension Table per Dimension

![Star Schema](./images/star-schema.png){ loading=lazy }

### Snowflake Schema

-   Mapping of Classification (seperate Tables for each Dimension/Level/Classification)
-   Normalized Schema (avoiding Update Anomalies, Redundancy, etc.)

![Snowflake Schema](./images/snowflake-schema.png){ loading=lazy }

### Star vs Snowflake Schema

|                                     | Star Schema                                | Snowflake Schema                 |
| ----------------------------------- | ------------------------------------------ | -------------------------------- |
| **Normalization & Data Redundancy** | denromalized, redundant Data in Dim Tables | fully normalized Dim Tables      |
| **Query Complexity**                | simple Queries                             | complex Queries                  |
| **Query Performance**               | faster                                     | slower                           |
| **Disk Space**                      | more Storage                               | less Storage                     |
| **Data Integrity Issues**           | might occur                                | less likely                      |
| **Setup / Maintenance**             | easier Setup, harder Maintenance           | harder Setup, easier Maintenance |

## Data Lake

!!! info

    Collection of many Data and Data Sources (structured, unstructured, semi-structured)

| Data Warehouse                                                                                                          | Data Lake                                                                       |
| ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Stores **structured Data** that has been extracted, transformed and loaded from various Sources                         | Stores **raw, unstructured or semi-structured Data** from various Sources       |
| Data is stored in a **predefined Schema** with a Structure                                                              | Data is stored in its **native Format** without a predefined Schema/Structure   |
| Designed for **complex Queries** and **generating Reports**                                                             | Designed for **storing** and **processing** large volumes of Data               |
| Provides a centralized/organized approach to Data Storage                                                               | Provides a flexible/scalable approach to Data Storage                           |
| **Data Processing** is performed before **Data Load into Warehouse**, can be **time-consuming and ressource-intensive** | **Data Processing** is performed **on an as-needed basis**, more agile/scalable |
| Optimized for **BI** and **Analytics**                                                                                  | Optimized for **Data Exploration**, **Machine Learning** and advanced Analytics |
| Data is already cleaned and processed                                                                                   | Requires additional processing and cleaning                                     |
| **Schema on Write**                                                                                                     | **Schema on Read**                                                              |
| Higher cost of storage                                                                                                  | Lower cost of storage                                                           |

## Data Mart

!!! info

    Subset of Data Warehouse, optimized for specific Domain Operations: optimized Data Model (special Views, Data Subsets, etc.)

## Extract, Transform, Load (ETL)

Process of extracting Data from Source Systems and bringing it into Data Warehouse

### Extract

**Batch Processing**

-   Creates batches of defined size/time interval
-   Needs space for buffering

**Real-Time Processing**

-   Processes Data Item by Item continuously
-   Each Item is only processed once

**Synchron Notification**

-   Source pushes each Data update to Data Warehouse

**Asynchron Notification**

-   Periodic
    -   Source generates Extracts on regular Basis
    -   Data Warehouse prompts for updates on regular Basis
-   Event-Driven
    -   Data Warehouse prompts for updates (e.g. end of Month)
-   Query-Driven
    -   Data Warehouse prompts for updates before each new Data access

**Type of Data**

-   Snapshots (Source delivers complete Data Set each Time)
-   Logs (Source delivers each update Operation)
-   Netlogs (Source delivers Net Updates)

### Transform

-   Data gets restructured to make it compliant for Data Warehouse (Data, Schema, etc.)

### Load

**Record Based Loading**

-   Trigger, Indices and Constraints can remain active
-   No long Table/DB Locks

**Bulk Loading**

-   Is used mostly for special Context
-   Complete DB/Table Locks
-   Ignores Triggers and Constraints checks
-   Needs Checkpoints for Resuming

### ETL vs ELT

**ELT** - Extract, Load, Transform: Variant of ETL, where Data is loaded into Data Warehouse first, and then transformed with SQL (similar like Data Lage with on-demand Processing)

## Profiling

!!! info

    Content Analysis before Staging Area

**Content & Structure Analysis**

-   Data Types
-   Value Ranges
-   Distribution/Variance
-   Null Values
-   Cardinality
-   Patterns (e.g. Dates, Names, etc.)

**Dependencie Analysis** Analysis betweend different Attributes and Relations

-   Functional Dependencies (Primary Key Candidates)
-   Integrity Constraints

**Overlap Analysis**

-   Redundancy
-   Foreign Key Relationships

## Data Cleansing

!!! info

    Cleaning, normalizing, tokenizing, discretizing, standardizing, etc. of the Data

**Normalization & Standardization**

-   Discretization (categorizing) numerical Values
-   Domain specific Transformations (e.g. Adresses, Name Formats, St. to Street, etc.)

### Missing Values

!!! info

    Treating Null Values, Distortions/Noisiness (Biases)

**Recognition**

-   Simple Analysis (e.g. amount of Null Values, frequency, etc)
-   Order Analysis (e.g. no Values in a specific Range)
-   Multilated Data (e.g. ignoring Values in a specific Range)
-   Recognition (e.g. Analysis of Data Distribution, Domain Knowledge, etc.)

**Treatment**

-   Unbiased Estimators (mean, median, standard deviation, etc.)
-   Attribute Relationships (correlation, etc.)
-   Statistical Techniques (linear regression, neural networks, etc.)
