---
subtitle: Decision Trees
---

# What is Clustering analysis?

Finding groups of objects such that objects that belong to the same group are more "similar" to each other than objects belonging to different groups.

- Inter-cluster distances are maximized
- Intra-cluster distances are minimized

![Clustering (or Clustering Analysis)](img/clustering/Immagine7.png)

# What is NOT Clustering analysis?

Supervised classification

* It assumes classes to be known

Segmentation

* Partitioning students alphabetically by last name
* The partitioning rule is given

Querying a database

* The selection and grouping criteria are given

How many clusters?

# Cluster notion can be ambiguous

![How many clusters?](img/clustering/Immagine8.png)

# Cluster notion can be ambiguous

::::{.columns}
:::{.column width="33%"}
![2](img/clustering/Immagine9.png)
:::
:::{.column width="33%"}
![4](img/clustering/Immagine10.png)
:::
:::{.column width="33%"}
![6](img/clustering/Immagine11.png)
:::
::::

# Type of clustering

A clustering is a set of clusters. We distinguish between:

__Partitioning clustering__: a division of objects into non-overlapping subsets (clusters). Each object belongs exactly to a cluster.

![Partitioning clustering](img/clustering/Immagine12.png)

__Hierarchical clustering__: a set of nested clusters organized as a hierarchical tree

![Hierarchical clustering and dendrogram](img/clustering/Immagine13.png)


# Further cluster classification

__Exclusive vs non-exclusive__

* In a non-exclusive clustering, points can belong to multiple clusters.
* Useful for representing border points and points belonging to several classes

__Fuzzy vs non-fuzzy__

* In a fuzzy clustering, a point belongs to all clusters with a weight between 0 and 1.
* For each point, weights sum up to 1.

__Partial vs complete__

* In a partial clustering, some points may not belong to any of the clusters.

__Heterogeneous vs homogeneous__

* In a heterogeneous cluster, clusters can have very different sizes, shapes, and densities

# Cluster types: Well-Separated

Well-Separated Cluster:

* A cluster is a set of points such that each point in the cluster is closer (more similar to) any other point in the cluster than any other point that does not belong to the cluster.

![Well-Separated Clusters](img/clustering/Immagine14.svg)


# Cluster types: Center-based

Center-based

* A cluster is a set of points such that a point in the cluster is closer (or more similar) to the "center" of the cluster, rather than to the center of each other cluster
* Cluster center is called the centroid if it is computed as the average of all the cluster's points, or the medoid if it is computed as the "more representative" cluster point

![4 center-based clusters](img/clustering/Immagine15.svg)


# Cluster types: Contiguity-Based

Contiguous cluster (Nearest neighbor or Transitive)

* A cluster is a set of points such that a point in a cluster is closer (or more similar) to one or more other points in the cluster than to any point not in the cluster

![8 contiguous clusters](img/clustering/Immagine16.svg)

# Cluster types: Density-Based

Density-based

* A cluster is a dense region of points, which is separated by low-density regions from other regions of high density.

* Used when the clusters are irregular or twisted, and when noise and outliers are present.

![6 density-based clusters](img/clustering/Immagine17.svg)

# Cluster types: Conceptual cluster

Clusters with shared properties or in which the shared property derives from the whole set of points (that models a particular concept)

* Specific techniques are needed to express the underlying concept.

![2 overlapped circles](img/clustering/Immagine18.svg)

# K-means Clustering

Partitional clustering approach

- Number of clusters, K, must be specified
- Each cluster is associated with a centroid (center point)
- Each point is assigned to the cluster with the closest centroid

```
function kmeans(k, points) is
    // Initialize centroids
    centroids ← list of k starting centroids
    converged ← false

    while converged == false do
        // Create empty clusters
        clusters ← list of k empty lists

        // Assign each point to the nearest centroid
        for i ← 0 to length(points) - 1 do
            point ← points[i]
            closestIndex ← 0
            minDistance ← distance(point, centroids[0])
            for j ← 1 to k - 1 do
                d ← distance(point, centroids[j])
                if d < minDistance THEN
                    minDistance ← d
                    closestIndex ← j
            clusters[closestIndex].append(point)

        // Recalculate centroids as the mean of each cluster
        newCentroids ← empty list
        for i ← 0 to k - 1 do
            newCentroid ← calculateCentroid(clusters[i])
            newCentroids.append(newCentroid)

        // Check for convergence
        if newCentroids == centroids THEN
            converged ← true
        else
            centroids ← newCentroids

    return clusters
```

# Convergence and optimality

::::{.columns}
:::{.column width="33%"}
![Original points and natural clusters](img/clustering/Immagine20.svg)
:::
:::{.column width="33%"}
![Optimal clusters](img/clustering/Immagine19.svg)
:::
:::{.column width="33%"}
![Sub-ottimal clusters](img/clustering/Immagine21.svg)
:::
::::

# Convergence to optimality

![Convergence to optimality](img/clustering/Immagine22.svg)

# K-means Clustering: details

Initial centroids are often chosen randomly.

* Clusters produced vary from one run to another.

The centroid is (typically) the mean of the points in the cluster.

- *Closeness* is measured by Euclidean distance, cosine similarity, correlation, etc.

K-means will converge for common similarity measures mentioned above, and most of the convergence happens in the first few iterations.

* The algorithm can converge to sub-optimal
* Often, the stopping condition is relaxed to "Until relatively few points change clusters."

Algorithm complexity is $O(n \cdot K \cdot I \cdot d )$

* $n$ = number of points, $K$ = number of clusters, $I$ = number of iterations, $d$ = number of attributes

# Evaluating k-means clusters

The most common measure is the Sum of Squared Error (SSE)

* For each point, the error is the distance to the nearest cluster
* To get SSE, we square these errors and sum them.

$SSE = \sum_{i=1}^K\sum_{x \in C_i} dist(x, m_i)^2$

* $x$ is a data point in cluster $C_i$ and $m_i$ is the representative point for cluster $C_i$
* The centroid  $m_i$ that minimizes the SSE when  $dist$ is the Euclidean distance is the average of the cluster points.

$m_i = \frac{1}{|C_i|} \sum_{x \in C_i} x$

One easy way to reduce SSE is to increase  $K$, the number of clusters.

* A good clustering with a smaller $K$ can have a lower SSE than a poor clustering with a higher $K$

# Convergence and optimality

There is only a finite number of ways to partition  $n$ records into  $k$ groups. So there is only a finite number of possible configurations in which all the centers are centroids of the points they possess.

If the configuration changes in an iteration, the distortion must be improved. So every time the configuration changes, it must lead to a state never visited before

* The reassignment of records to centroids is done based on smaller distances
* The calculation of the new centroids minimizes the value of SSE for the cluster

Therefore, the algorithm must stop due to the unavailability of further configurations to visit.

It is not necessarily true that the final configuration is the one that has the minimum value of SSE, as shown in the following slide.

# Convergence to sub-optimality

![Convergence to sub-optimality](img/clustering/Immagine23.svg)

# Importance of Choosing Initial Centroids

If there are real $K$ clusters, the probability of choosing a centroid from each cluster is very limited.

* Assuming the clusters have the same cardinality  $n$ :

$P=\frac{\# ways of choosing a centroid by cluster}{\# ways of choosing K centroids}=\frac{(n)^K \cdot K!}{(n \cdot K)^K}=\frac{K!}{K^K}$

* $K$ = 10, probability is 10!/1010 = 0.00036

Sometimes the centroids will reposition themselves correctly, sometimes not...

# 10 clusters example

![Starting with clusters with 2 centroids and clusters with 0 centroids](img/clustering/Immagine24.svg)

# 10 clusters example

![Starting with clusters with 2 centroids and clusters with 0 centroids](img/clustering/Immagine25.svg)

# 10 clusters example

![Starting with a couple of clusters with 3 centroids and couple of clusters with 1 centroids](img/clustering/Immagine26.svg)

# 10 clusters example

![Starting with a couple of clusters with 3 centroids and couple of clusters with 1 centroids](img/clustering/Immagine27.svg)

# Solution to the problems induced by the choice of initial centroids

Run the algorithm several times with different initial centroids.

* It can help, but the probability is not on our side!

Perform a sampling of the points and use a hierarchical clustering technique to identify $k$ initial centroids.

Select more than $k$ initial centroids and then select from these to use

* The selection criterion is to keep those more "separated."

Use post-processing techniques to eliminate the identified erroneous cluster.

Bisecting K-means

* Less affected by the problem

# Handling empty clusters

The K-means algorithm can determine empty clusters if, during the assignment phase, no element is assigned to a centroid.

* This case can cause a high SSE as one of the clusters is not "used."

Different strategies are possible to identify an alternative centroid.

* Choose the item that most contributes to the value of SSE

* Choose an item of the cluster with the highest SSE. Normally, this causes the cluster to split into two clusters that include the closest elements.

# Handling empty clusters

![Handling empty clusters](img/clustering/Immagine28.svg)

# Handling outlier

The goodness of clustering can be negatively influenced by the presence of outliers that tend to "shift" the cluster centroids, so that to reduce the increase in the SSE, they determine

* Since SSE is the square of a distance, the far points heavily affect its value

Outliers, if identified, can be eliminated during pre-processing.

* Outlier concepts depend on the application domain

# K-means: limits

The k-means algorithm does not achieve good results when natural clusters have:

* Different sizes
* Different density
* Non-globular shape
* Data contains outliers

# K-means limits: different dimension

The value of SSE leads to the identification of centroids to have clusters of the same size if the clusters are not well-separated

::::{.columns}
:::{.column width="50%"}
![Unclustered points & natural clusters](img/clustering/14-Clustering_43.png)
:::
:::{.column width="50%"}
![K-means (3 Cluster)](img/clustering/14-Clustering_42.png)
:::
::::

# K-means limits: different density

More dense clusters lead to smaller intra-cluster distances, so less dense areas require more medians to minimize the total value of SSE.

::::{.columns}
:::{.column width="50%"}
![Unclustered points & natural clusters](img/clustering/14-Clustering_44.png)
:::
:::{.column width="50%"}
![K-means (3 Cluster)](img/clustering/14-Clustering_45.png)
:::
::::

# K-means limits: non-globular shape

SSE is based on an Euclidean distance that does not take into account the shape of objects

::::{.columns}
:::{.column width="50%"}
![Unclustered points & natural clusters](img/clustering/14-Clustering_47.png)
:::
:::{.column width="50%"}
![K-means (2 Cluster)](img/clustering/14-Clustering_46.png)
:::
::::

# K-means: possible solutions

Use a higher $k$ value, thus identifying portions of clusters.

The definition of "natural" clusters then requires a technique to bring together the identified clusters.

::::{.columns}
:::{.column width="50%"}
![Unclustered points & natural clusters](img/clustering/14-Clustering_48.png)
:::
:::{.column width="50%"}
![K-means (10 Cluster)](img/clustering/14-Clustering_49.png)
:::
::::

# K-means: possible solutions

Use a higher $k$ value, thus identifying portions of clusters.

The definition of "natural" clusters then requires a technique to bring together the identified clusters.

::::{.columns}
:::{.column width="50%"}
![Unclustered points & natural clusters](img/clustering/14-Clustering_51.png)
:::
:::{.column width="50%"}
![K-means (10 Cluster)](img/clustering/14-Clustering_50.png)
:::
::::

# K-means: possible solutions

Use a higher $k$ value, thus identifying portions of clusters.

The definition of "natural" clusters then requires a technique to bring together the identified clusters.

::::{.columns}
:::{.column width="50%"}
![Unclustered points & natural clusters](img/clustering/14-Clustering_53.png)
:::
:::{.column width="50%"}
![K-means (10 Cluster)](img/clustering/14-Clustering_52.png)
:::
::::

# Choosing K: the elbow method

It consists of executing k-means several times with increasing values for k

* SSE value will decrease
* $k < #NaturalCluster$: SSE includes inter-cluster distances
* $k >= #NaturalCluster$: SSE includes intra-cluster distances
* The "elbow" occurs when SSE starts decreasing more slowly since it is generated only by intra-cluster distances

![The elbow method](img/clustering/14-Clustering_54.png)

# Exercise

Draw the cluster partitioning and the approximate position of the centroids chosen by the k-means algorithm, assuming that:

* The points are equally distributed
* The distance function is SSE
* The value of $k$ is shown below the figures

![K=2, K=3, K=3, K=2, K=3](img/clustering/14-Clustering_55.png)

# Hierarchical Clustering

Produces a set of nested clusters organized as a hierarchical tree

Can be visualized as a dendrogram

* A tree-like diagram that records the sequences of merges or splits

Different values on the Y-axis correspond to different clusterings.

* Higher Y-axis values imply fewer clusters with more items

![Handling empty clusters](img/clustering/Immagine29.svg)

# Hierarchical Clustering: pros and cons

Pros:

* The cluster number must not be defined a priori
    * The desired number of clusters can be obtained by 'cutting' the dendrogram to the appropriate level
* It can identify a taxonomy (hierarchical classification) of concepts
    * The most similar elements will be fused before the less similar elements

Cons:

* Once a decision is made (merge), it can no longer be canceled
* In many configurations, it is sensitive to noise and outliers
* A global optimization function is missing

# Hierarchical Clustering approaches

There are two approaches to building a hierarchical clustering.

* Agglomerative:
  * Start with the points as individual clusters
  * At each step, merge the closest pair of clusters until only one cluster (or $k$ clusters) is left
* Divisive:
  * Start with one, all-inclusive cluster
  * At each step, split a cluster until each cluster contains an individual point (or there are $k$ clusters)

Traditional hierarchical algorithms use a similarity or distance matrix.

* A  $n \cdot n$ matrix storing the similarities/distances between pairs of points/clusters

# Hierarchical Clustering algorithms

The basic algorithm is straightforward.

```
Compute the proximity matrix
Let each data point be a cluster
Repeat
    Merge the two closest clusters
    Update the proximity matrix
Until only a single cluster remains
```

The key operation is the computation of the proximity of two clusters.

* Different approaches to defining the distance between clusters distinguish the different algorithms

# Hierarchical Clustering flow

Start with clusters of individual points and a proximity matrix.

![Proximity matrix](img/clustering/Immagine30.svg)

# Hierarchical Clustering flow

After some merging steps, we have some clusters.

![Proximity matrix](img/clustering/Immagine31.svg)

# Merging step

We want to merge the two closest clusters (C2 and C5) and update the proximity matrix.

* The affected cells are only those related to C2 and C5

![Proximity matrix](img/clustering/Immagine32.svg)

# Inter-Cluster Distances

![Inter-Cluster Distances](img/clustering/Immagine33.svg)

- MIN or Single link
- MAX or Complete link
- Group Average
- Centroid's distance
- Other methods driven by an objective function
    - Ward's Method uses squared error

# Inter-Cluster Distances

__MIN or Single link__: is the minimum distance between two cluster points

![MIN or Single link](img/clustering/Immagine34.svg)

# Inter-Cluster Distances

__MAX or Complete link__: is the maximum distance between all cluster points

![MAX or Complete link](img/clustering/Immagine35.svg)

# Inter-Cluster Distances

__Group Average__: is the average distance between all the cluster points

![Group Average](img/clustering/Immagine36.svg)

# Inter-Cluster Distances

__Centroids distance__

![Centroids distance](img/clustering/Immagine37.svg)

# Hierarchical clustering: MIN

::::{.columns}
:::{.column width="33%"}
|  | p1 | p2 | p3 | p4 | p5 | p6 |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| p1 | 0.00 | 0.24 | 0.22 | 0.37 | 0.34 | 0.23 |
| p2 | 0.24 | 0.00 | 0.15 | 0.20 | 0.14 | 0.25 |
| p3 | 0.22 | 0.15 | 0.00 | 0.15 | 0.28 | 0.11 |
| p4 | 0.37 | 0.20 | 0.15 | 0.00 | 0.29 | 0.22 |
| p5 | 0.34 | 0.14 | 0.28 | 0.29 | 0.00 | 0.39 |
| p6 | 0.23 | 0.25 | 0.11 | 0.22 | 0.39 | 0.00 |
:::
:::{.column width="33%"}
![Dendrogram](img/clustering/Immagine38.svg)
:::
:::{.column width="33%"}
![Clustering](img/clustering/Immagine39.svg)
:::
::::

After step 2: $Dist(\{3,6\}, \{2,\5})=min(dist(\{2,3\}), dist(\{2,6\}), dist(\{5,3\}), dist(\{5,6\})) = min(0.15,0.25,0.28,0.39)=0.15$

# MIN: pros and cons

It allows for managing non-spherical clusters too.

::::{.columns}
:::{.column width="50%"}
![](img/clustering/14-Clustering_59.png)
:::
:::{.column width="50%"}
![](img/clustering/14-Clustering_60.png)
:::
::::

It is subject to outliers and noise.

::::{.columns}
:::{.column width="50%"}
![](img/clustering/14-Clustering_62.png)
:::
:::{.column width="50%"}
![](img/clustering/14-Clustering_61.png)
:::
::::

# Hierarchical clustering: MAX

::::{.columns}
:::{.column width="33%"}
|  | p1 | p2 | p3 | p4 | p5 | p6 |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| p1 | 0.00 | 0.24 | 0.22 | 0.37 | 0.34 | 0.23 |
| p2 | 0.24 | 0.00 | 0.15 | 0.20 | 0.14 | 0.25 |
| p3 | 0.22 | 0.15 | 0.00 | 0.15 | 0.28 | 0.11 |
| p4 | 0.37 | 0.20 | 0.15 | 0.00 | 0.29 | 0.22 |
| p5 | 0.34 | 0.14 | 0.28 | 0.29 | 0.00 | 0.39 |
| p6 | 0.23 | 0.25 | 0.11 | 0.22 | 0.39 | 0.00 |
:::
:::{.column width="33%"}
![Dendrogram](img/clustering/Immagine40.svg)
:::
:::{.column width="33%"}
![Clustering](img/clustering/Immagine41.svg)
:::
::::

After step 2...

- $Dist(\{3,\6}, \{4 \})=max(dist(\{3,4\}), dist(\{6,4\})) = max(0.15,0.22)=0.22$
- $Dist(\{3,\6}, \{2,5\})=max(dist(\{3,2\}), dist(\{3,5\}), dist(\{6,2\}) dist(\{6,5\})) = max(0.15,0.25,0.28,0.39)=0.39$
- $Dist(\{3,\6}, \{1 \})=max(dist(\{3,1\}), dist(\{6,1\})) = max(0.22,0.23)=0.23$

# MAX: pros and cons

Less affected by noise

::::{.columns}
:::{.column width="50%"}
![](img/clustering/14-Clustering_65.png)
:::
:::{.column width="50%"}
![](img/clustering/14-Clustering_64.png)
:::
::::

It tends to separate large clusters.

Favor globular clusters

::::{.columns}
:::{.column width="50%"}
![](img/clustering/14-Clustering_66.png)
:::
:::{.column width="50%"}
![](img/clustering/14-Clustering_67.png)
:::
::::


# Hierarchical clustering: Group Average

The similarity between two clusters is the average of the similarity of the cluster pairs of points.

$proximity(c_i, c_j) = \frac{1}{|c_i| \cdot |c_j|} \sum_{p \in c_i} \sum_{q \in c_j} proximity(p, q)$

It is a compromise between MIN and MAX.

* PROs: less affected by noise than MIN
* CONS: Biased towards globular clusters

# Hierarchical clustering: Group Average

::::{.columns}
:::{.column width="33%"}
|  | p1 | p2 | p3 | p4 | p5 | p6 |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| p1 | 0.00 | 0.24 | 0.22 | 0.37 | 0.34 | 0.23 |
| p2 | 0.24 | 0.00 | 0.15 | 0.20 | 0.14 | 0.25 |
| p3 | 0.22 | 0.15 | 0.00 | 0.15 | 0.28 | 0.11 |
| p4 | 0.37 | 0.20 | 0.15 | 0.00 | 0.29 | 0.22 |
| p5 | 0.34 | 0.14 | 0.28 | 0.29 | 0.00 | 0.39 |
| p6 | 0.23 | 0.25 | 0.11 | 0.22 | 0.39 | 0.00 |
:::
:::{.column width="33%"}
:::
:::{.column width="33%"}
![Clustering](img/clustering/Immagine43.svg)
:::
::::

After step 3...

- $Dist(\{3,6,4\}, \{1 \}) = (0.22+0.37+0.23)/(3 \cdot 1) = 0.28$
- $Dist(\{2,5 \}, \{1 \}) = (0.2357+0.3421)/(2 \cdot 1) = 0.2889$
- $Dist(\{3,6,4\}, \{2,5\}) =(0.15+0.28+0.25+0.39+0.20+0.29)/(3\cdot 2) = 0.26$

# Hierarchical clustering: Ward's Method

Similarity of two clusters is based on the increase in squared error when two clusters are merged.

* Similar to group average if the distance between points is the distance squared

- PROS: Less susceptible to noise and outliers
 CONS: Biased towards globular clusters

It uses the same objective function as the K-means algorithm.

* It can be used to initialize k-means: since it allows identifying the correct value of $k$ and an initial subdivision of the points
    * Please note that, due to not being able to cancel the choices made, the solutions found by the hierarchical methods are often sub-optimal.

# Hierarchical clustering: Comparison

![Comparison](img/clustering/Immagine44.svg)

# Hierarchical clustering: computational complexity

Space: $O(N^2)$ is the space occupied by the proximity matrix when the number of points is $N$

Time: $O(N^3)$

* $N$ steps are needed to build the dendrogram. At each step, the proximity matrix must be updated and read
* Prohibitive for large datasets

# Hierarchical clustering: exercise

Given the following similarity matrix, represent the dendrograms deriving from the hierarchical clustering obtained by

* Single link
* Complete link

| simil | p1 | p2 | p3 | p4 | p5 |
| :-: | :-: | :-: | :-: | :-: | :-: |
| p1 | 1.00 | 0.10 | 0.41 | 0.55 | 0.35 |
| p2 | 0.10 | 1.00 | 0.64 | 0.47 | 0.98 |
| p3 | 0.41 | 0.64 | 1.0 | 0.44 | 0.85 |
| p4 | 0.55 | 0.47 | 0.44 | 1.00 | 0.76 |
| p5 | 0.35 | 0.98 | 0.85 | 0.76 | 1.00 |

# DBSCAN

DBSCAN is a density-based approach

* Density = number of points within a specified radius ($Eps$)
* A point is a __core point__ if it has at least a specified number of points ($MinPts$) within $Eps$
  * These are points that are within a cluster
* A __border point__ is not a core point, but is in the neighborhood (i.e., within a $Eps$ radius) of a core point
* A __noise point__ is any point that is not a core point or a border point

# DBSCAN: Core, Border, and Noise Points

![DBSCAN](img/clustering/14-Clustering_69.png)

# DBSCAN algorithm

// Input:Dataset $D, MinPts, Eps$
// Output set of cluster $C$

1. Label points in $D$ as core, border or noise
1. Drop all noise points
1. Assign to cluster ci the core points with a distance < $Eps$ from one of the other points assigned to the same cluster
1. Assign border points to one of the clusters that the corresponding core points belong to

# DBSCAN: Core, Border, and Noise Points

$Eps = 10$, $MinPts = 4$

::::{.columns}
:::{.column width="50%"}
![Original points](img/clustering/14-Clustering_70.png)
:::
:::{.column width="50%"}
![Point types: core, border and noise](img/clustering/14-Clustering_71.png)
:::
::::

# DBSCAN: pros and cons

Pro

* Resistant to noise
* It can generate clusters with different shapes and sizes

Cons

* Data with high dimensionality
  * The key point is to properly define the density (i.e., choosing $Eps$ and $MinPts$)
  * Does not handle dataset variable density

::::{.columns}
:::{.column width="33%"}
![$MinPts$ = 4, $Eps=9.92$](img/clustering/Immagine45.svg)
:::
:::{.column width="33%"}
![](img/clustering/Immagine46.svg)
:::
:::{.column width="33%"}
![$MinPts$ = 4, $Eps = 9.75$](img/clustering/Immagine47.svg)
:::
::::

# DBSCAN: choosing Eps and MinPts

The idea is that for points in a cluster, their kth nearest neighbors are at roughly the same distance.

Noise points have the kth nearest neighbor at a farther distance.

So, plot the sorted distance of every point to its kth nearest neighbor.

* $Eps$ value is given by the y-axis in $p$
* $MinPts$ value is given by  $k$
* The result depends on the value of $k$, but the trend of the curve remains similar for reasonable values of $k$
* A value of $k$ normally used for two-dimensional datasets is 4

![](img/clustering/14-Clustering_73.png)

# Cluster validity

For supervised classification techniques, there are several measures to evaluate the validity of the results based on the comparison between the known labels of the test set and those calculated by the algorithm.

* Accuracy, precision, recall

This is not the case of clustering. So why evaluate clustering validity?

* To avoid finding patterns in noise
* To compare clustering algorithms
* To compare two sets of clusters
* To compare two clusters

# Cluster validity

![](img/clustering/Immagine48.svg)

# Validity measures

Numerical measures that are applied to judge various aspects of cluster validity are classified into the following three types.

* Internal Index: Used to measure the goodness of a clustering structure without respect to external information.
  * Sum of Squared Error (SSE)
* External Index: Used to measure the extent to which cluster labels match externally supplied class labels.
  * Entropy
* Relative Index: Used to compare two different clusterings or clusters.
  * Often an external or internal index is used for this function, e.g., SSE or entropy

# Internal measures

Cluster Cohesion: Measures how closely related the objects in a cluster are.

* Example: SSE

Cluster Separation: Measure how distinct or well-separated a cluster is from other clusters

* Example: Squared Error

* Cohesion is measured by the __W__ithin cluster __S__um of __S__quares (WSS or SSE)

$SSE = WSS = \sum_{i=1}\sum_{x \in C_i} dist(x, m_i)^2$

* Separation is measured by the __B__etween cluster __S__um of __S__quares (BSS)

$BSS = \sum_{i=1} |C_i| \cdot dist(m_i, m)^2$

# Internal Measures: Cohesion and Separation

Cohesion and separation can be calculated both for graph-based representations...

* Cohesion is the sum of the weights of the arcs between the nodes belonging to a cluster
* The separation is the sum of the weights of the arcs between the nodes belonging to distinct clusters

![Cohesion vs Separation](img/clustering/Immagine49.svg)

- $cohesion(C_i) = \sum_{u,v \in C_i} proximity(u,v)$
- $separation(C_i, C_j) = \sum_{u \in C_i, v \in C_j} proximity(u,v)$

# Internal Measures: Cohesion and Separation

... both for representations based on centroids

* Cohesion is the sum of the weights of the arcs between the nodes belonging to a cluster $C_i$ and the relative centroid $m_i$
* The separation is the sum of the weights of the arches between the centroids

![](img/clustering/Immagine50.svg)

- $cohesion(C_i) = \sum_{u \in C_i} proximity(u, m_i)$
- $separation(C_i, C_j) = proximity(m_i, m_j)$

# Measuring Cluster Validity Via Correlation

Two matrices are used.

* *Proximity* Matrix
  * Distance matrix between elements
* *Incidence* Matrix
  * One row and one column for each data point
  * An entry is 1 if the associated pair of points belongs to the same cluster
  * An entry is 0 if the associated pair of points belongs to different clusters

Compute the correlation between the two matrices.

High correlation indicates that points that belong to the same cluster are close to each other.

Not a good measure for some density or contiguity-based clusters (such as those obtained with density-based algorithms or contiguity measures)

* In this case, the distances between the points are not correlated with their membership in the same cluster

# Measuring Cluster Validity Via Correlation

Correlation between the incidence matrix and the proximity matrix on the result of the k-means algorithm on two different data sets.

* The correlation is negative because at small distances in the proximity matrix, they correspond to large values (1) in the incidence matrix
* Obviously, if the distance matrix had been used instead of the similarity matrix, the correlation would have been positive

![Corr = -0.9235 vs Corr = -0.5810](img/clustering/Immagine51.svg)

# Measuring Cluster Validity Via Correlation

The visualization is obtained by ordering the similarity matrix based on the groupings defined by the clusters.

![Cluster Validity Via Correlation](img/clustering/Immagine52.svg)

# Measuring Cluster Validity Via Correlation

If the data is uniformly distributed, the matrix is more "shaded."

![K-means](img/clustering/Immagine53.svg)

![DBSCAN](img/clustering/Immagine54.svg)

![Complete link](img/clustering/Immagine55.svg)

# Exercise

Associate similarity matrices with the data set

::::{.columns}
:::{.column width="50%"}
![](img/clustering/14-Clustering_89.png)
:::
:::{.column width="350%"}
![](img/clustering/14-Clustering_88.png)
:::
::::

# Cophenetic distance

The previous measures represent validity indices for partitioning clustering algorithms.

In the case of hierarchical clustering, a measure often used is the cophenetic distance, that is, given two elements, it is the proximity to which they are placed together by an agglomerative clustering algorithm.

* In the underlying dendrogram, the pairs of points (3,4), (6,4) have a distance of 0.15 because the clusters to which they belong are merged at that value of the proximity matrix

Calculating the cophenetic distance for all pairs of points, we obtain a matrix that allows us to calculate the CoPhenetic Correlation Coefficient (CPCC)

* The term Cophenetic comes from biology: phenetics (Greek: phainein – to appear), also known as taximetrics, is an attempt to classify organisms based on overall similarity, usually in morphology or other observable traits, regardless of their phylogeny or evolutionary relation.
* The CPCC is the correlation index between the cophenetic distance matrix and the dissimilarity matrix of the points
* A high correlation indicates that the clustering algorithm has respected the dissimilarity between the elements

::::{.columns}
:::{.column width="50%"}
| Distance | CPCC |
| :-: | :-: |
| Single link | 0.44 |
| Complete link | 0.63 |
| Group average | 0.66 |
| Ward's | 0.64 |
:::
:::{.column width="50%"}
![Ward's](img/clustering/Immagine56.svg)
:::
::::

# Statistical framework for clustering validation

Internal measures often return measurements that must be interpreted.

* _Is a value of 10 good or bad?_

Statistics can provide a suitable methodology for assessing the goodness of a measurement.

* We are looking for non-random patterns, so the more "atypical" the result we get, the more likely it is to represent a non-random pattern in the data
* Therefore, the idea is to compare the value of the measure with that obtained from random data.
  * If the value of the measure obtained on the data is unlikely for random data, then clustering is valid

The issue of interpreting the measure value is less pressing when comparing the results of two clusters.

# Cluster in random data

::::{.columns}
:::{.column width="50%"}
![Original random points](img/clustering/Immagine57.svg)
:::
:::{.column width="50%"}
![K-means](img/clustering/Immagine58.svg)
:::
::::

::::{.columns}
:::{.column width="50%"}
![DBSCAN](img/clustering/Immagine59.svg)
:::
:::{.column width="50%"}
![Complete Link](img/clustering/Immagine60.svg)
:::
::::

# Clustering Tendency

One obvious way to check whether a dataset has clusters is to cluster it

* Clustering algorithms will still find clusters in the data

* There could be types of clusters not identified by the chosen algorithm

Alternatively, statistical indices, such as the Hopkins statistic, could be used to estimate how evenly distributed the data are

* Applicable mainly with low dimensionality and in Euclidean spaces

# Clustering Tendency: Hopkins statistic

Given a dataset $Q$ of $n$ real points, we generate a dataset $P$ of $m$ points ($m$ << $n$) by randomly distributing them in the data space.

For each point $p_i \in P$, the distance $u_i$ from the point to its nearest-neighbor in the real dataset $Q$ is calculated.

Other $m$ points from the real dataset $q_i \in Q$ are sampled, and for each of them, the distance $w_i$ from the point to its nearest-neighbor in the real dataset $Q$ is calculated.
The Hopkins statistic is defined as:

$H = \frac{\sum_{i=1}^{m} u_i}{\sum_{i=1}^{m} u_i + \sum_{i=1}^{m} w_i}$

* If the distance to the nearest neighbor is about the same for both generated and sampled points, then $H \approx 0.5$. Then the data set has a random distribution.
* If $H \approx 1$ (very small values of $w_i$) the data are well clustered
* If $H \approx 0$ (very small values of $u_i$), the data are evenly distributed (equally spaced).

# Clustering Tendency: Hopkins statistic

![Hopkins statistic](img/clustering/Immagine61.svg)

# Clustering Tendency: Hopkins statistic

![Hopkins statistic](img/clustering/Immagine62.svg)

# Clustering Tendency: Hopkins statistic

![Hopkins statistic](img/clustering/Immagine63.svg)

# Clustering Tendency: Hopkins statistic

![Hopkins statistic](img/clustering/Immagine64.svg)

# Clustering Tendency: Hopkins statistic

![Hopkins statistic](img/clustering/Immagine65.svg)


# External measures for clustering validation

External information is usually the class labels of the objects on which clustering is performed.

* They allow you to measure the correspondence between the computed label of the cluster and the class label

If class labels are available, why perform clustering?

* Compare the results of different clustering techniques

* Evaluate the possibility of automatically obtaining an otherwise manual classification

Two approaches are possible.

* Classification-oriented: evaluate the extent to which clusters contain objects belonging to the same class

  * Entropy, purity, F-measure

* Similarity-oriented: they measure how often two objects that belong to the same cluster belong to the same class

  * They use similarity measures for binary data: Jaccard

# External measures for clustering validation: Entropy and Purity

Entropy: for each cluster $i$ let $p_{ij} = \frac{m_{ij}}{m_i}$ the probability that a member of cluster $i$ belongs to class $j$

* $m_i = $ # of objects in cluster $i$
* $m_{ij} = $ # of objects of class $j$ in cluster $i$

Cluster $i$ entropy is $e_i$ while whole clustering entropy is $e$


- $e_i = - \sum_{j=1}^{L} p_{ij} \cdot log_2(p_{ij})$
- $e = -\sum_{i=1}^{K} \frac{m_i}{m} \cdot e_i$
    - $L=$# class $K=$# clusters

Purity is computed as:

* $p_i$ measures how "strong" the relationship is between cluster and class
  * It is minimal when the points belonging to the cluster are equally distributed among the classes

- $p_i = max_j(p_{ij})$
- $p = \sum_{i=1}^{K} \frac{m_i}{m} \cdot p_i$

# A final comment

> " _The validation of clustering structures is the most difficult and frustrating part of cluster analysis. Without a strong effort in this direction, cluster analysis will remain a black art accessible only to those true believers who have experience and great courage."
>
> cit. Algorithms for Clustering Data, Jain and Dubes

