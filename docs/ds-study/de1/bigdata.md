# Big Data

Traditional systems don't scale with big data. New solutions are needed like NoSQL (not only SQL).

**Relational Database**

| _Pros:_                                                                                                                                                                                                              | _Cons:_                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| - Known technology </br> - Good structure </br> - Good interface </br> - Supports concurrent access for multiple users with different permissions </br> - Multi user synchronization </br> - Query processing engine | - Scales only to medium size </br> - Cant handle over scaling </br> - Problems by using semi-structured data |

## Definition of Big Data V's

|          |                                       |
| -------- | ------------------------------------- |
| Volume   | Large amount of data                  |
| Velocity | High speed access to data             |
| Variety  | Different data sources and structures |
| Veracity | Data has different qualities          |
| Value    | Some data is more valuable than other |

### Volume (Data in Rest)

-   Scale and dimension of data is huge
-   Possibility to edit large data volumes

### Velocity (Data in Motion)

-   Speed and dynamic of incoming data is high
-   Datastreaming
-   Handling of: speed, stream, structured records creation
-   Access & delivery of data in real-time

### Variety (Data in many Forms)

-   Different Datatypes wihtout a fixed structure (images, videos, db, blogs, etc.)
-   Missing uniformity/monotony
-   Data can be highly semi-/unstructured

### Veracity (Data in Doubt)

-   Trustworthiness of data
-   Different qualities of data
-   Data consistency: trustworthiness, accuracy, etc.
-   Results only considered as probable

### Value (additional)

-   Only significant if added value can be generated from Big Data
-   New business models, products, services, etc.

## Scalability

-   Ability of a system to handle a growing amount of work by adding resources to the system

### Vertical Scaling (Up-Scaling)

!!! note

    Increasing performance and size of instance

-   Bigger and better machine
-   Seller Lock-In
-   Not many providers
-   Higher costs
-   Works well until data gets too big

### Horizontal Scaling (Out-Scaling)

!!! note

    Multiple instances working together

-   Cheaper
-   Bypass vertical scaling
-   Latency between instances
-   Network can get unseacure
-   Bandwidth is limited
-   Network is not reliable

### Cluster

!!! note

    Collection of connected nodes, based on the shared-nothing architecture

-   Network of Nodes
    -   Sharing nothing (no shared memory, no shared storage)
    -   Communication via messages
-   Distribution different tasks
    -   Data
    -   Queries
    -   Calculations
    -   Requests

## Sharding

!!! note

    Partitioning of data across multiple machines

-   Vertical Shards
-   Horizontal Shards

**Pros:**

-   Balanced workloads
-   respects physical locations
-   Uniform data distribution

**Cons:**

-   Data changes over time
-   Data conflicts (inconsistency)

### Strategies

-   Mapping Structures
    -   round-robin
    -   range
    -   hash
-   Composite Partitioning

## Replication

!!! note

    Copying data across multiple machines to provide redundancy

### Master Slave Architecture

-   One node is primary (master)
    -   only master can write
-   All other nodes are secondary (slaves)
    -   slaves can only read

### Peer to Peer Architecture

-   All nodes are equal
    -   No bottlenech/single point of failure for reads/writes
    -   Scalable
    -   Synchronization is needed
-   All nodes have same data
