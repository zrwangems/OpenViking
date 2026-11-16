---
type: simulink-block
title: 'DBSCAN Clusterer'
family: 'radar'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'dbscanclusterer'
documentation_source_path: 'ref/dbscanclusterer.html'
language: en
---

# DBSCAN Clusterer

## Ports

### Input

### **X** — Input data *N*-by-*P* real-valued matrix

Input data, specified as a real-valued
*N*-by-*P* matrix, where *N* is
the number of data points to cluster. *P* is the number of feature
dimensions. The DBSCAN algorithm can cluster any type of data with appropriate
**Minimum number of points in a cluster** and **Cluster
threshold epsilon** settings.

**Data Types:** `double`

### **Update** — Enable automatic update of epsilon `false` (default) | `true`

Enable automatic update of the epsilon estimate, specified as
`false` or `true`.

- When `true`, the epsilon threshold is first estimated as
  the average of the knees of the *k-NN* search curves. The
  estimate is then added to a buffer of size *L*, set by the
  **Length of cluster threshold epsilon history** parameter.
  The final value of epsilon is calculated as the average of the
  *L*-length epsilon history buffer. If **Length of
  cluster threshold epsilon history** is set to one, the estimate is
  memory-less. Memory-less means that each epsilon estimate is immediately used
  and no moving-average smoothing occurs.
- When `false`, a previous epsilon estimate is used.
  Estimating epsilon is computationally intensive and not recommended for large
  data sets.

#### Dependencies

To enable this port, set the **Source of cluster threshold
epsilon** parameter to `Auto` and set the
**Maximum number of points for 'Auto' epsilon** parameter.

**Data Types:** `Boolean`

### **AmbLims** — Ambiguity limits 1-by-2 real-valued vector (default) | 2-by-2 real-valued matrix

Ambiguity limits, specified as a 1-by-2 real-valued vector or 2-by-2 real-valued
matrix. For a single ambiguity dimension, specify the limits as a 1-by-2 vector
*[MinAmbiguityLimitDimension1,MaxAmbiguityLimitDimension1]*. For
two ambiguity dimensions, specify the limits as a 2-by-2 matrix
*[MinAmbiguityLimitDimension1, MaxAmbiguityLimitDimension1;
MinAmbiguityLimitDimension2,MaxAmbiguityLimitDimension2]*.

Clustering can occur across boundaries to ensure that ambiguous detections are
appropriately clustered for up to two dimensions. The ambiguous columns of the input
port data `X` are defined using the **Indices of ambiguous
dimensions** parameter. The **AmbLims** parameter defines
the minimum and maximum ambiguity limits in the same units as used in the
**Indices of ambiguous dimensions** columns of the input data
`X`.

#### Dependencies

To enable this port, select the **Enable disambiguation of
dimensions** check box.

**Data Types:** `double`
### Output

### **Idx** — Cluster indices *N*-by-1 integer-valued column vector

Cluster indices, returned as an *N*-by-1 integer-valued column
vector. Cluster IDs represent the clustering results of the DBSCAN algorithm. A value
equal to '-1' implies a DBSCAN noise point. Positive `Idx` values
correspond to clusters that satisfy the DBSCAN clustering criteria.

#### Dependencies

To enable this port, set the **Define outputs for Simulink
block** parameter to `Index` or
`Index and ID`.

**Data Types:** `double`

### **Clusters** — Alternative cluster IDs 1-by-*N* integer-valued row vector

Alternative cluster IDs, returned as a 1-by-*N* row vector of
positive integers. Each value is a unique identifier indicating a hypothetical target
cluster. This argument contains unique positive cluster IDs for all points including
noise. In contrast, the `Idx` output argument labels noise points
with '–1'. Use this output as input to Phased Array System Toolbox™ blocks such as Range Estimator and Doppler Estimator.

#### Dependencies

To enable this port, set the **Define outputs for Simulink
block** parameter to `Cluster ID` or
`Index and ID`.

**Data Types:** `double`

## Parameters

### **Define outputs for Simulink block** — Type of cluster data output `Index and ID` (default) | `Cluster ID` | `Index`

Type of cluster data output, specified as:.

- `Index and ID` –- Enables the `Idx`
  and `Clusters` output ports.
- `Cluster ID` –- Enables the
  `Clusters` output port only.
- `Index` –- Enables the `Idx` output
  port only.

### **Source of cluster threshold epsilon** — Epsilon source `Property` (default) | `Auto`

Epsilon source for cluster threshold:

- `Property` — Epsilon is obtained from the
  **Cluster threshold epsilon** parameter.
- `Auto` — Epsilon is estimated automatically using a
  k-nearest neighbor (*k*-NN) search. The search is calculated with
  *k* ranging from one less than the value of **Minimum
  number of points in a cluster** to one less than the value of
  **Maximum number of points for 'Auto' epsilon**. The
  subtraction of one is needed because the neighborhood of a point includes the
  point itself.

### **Cluster threshold epsilon** — Cluster neighborhood size `10.0` (default) | positive scalar | positive real-valued 1-by-*P* row vector

Cluster neighborhood size for a search query, specified as a positive scalar or
real-valued 1-by-*P* row vector. *P* is the number of
clustering dimensions in the input data `X`.

Epsilon defines the radius around a point inside which to count the number of
detections. When epsilon is a scalar, the same value applies to all clustering feature
dimensions. You can specify different epsilon values for different clustering dimensions
by specifying a real-valued 1-by-*P* row vector. Using a row vector
creates a multi-dimensional ellipse search area, which is useful when the data columns
have different physical meanings such as range and Doppler.

### **Minimum number of points in a cluster** — Minimum number of points required for cluster `3` (default) | positive integer

Minimum number of points required for a cluster, specified as a positive integer.
This parameter defines the minimum number of points in a cluster when determining
whether a point is a core point.

### **Maximum number of points for 'Auto' epsilon** — Maximum number of points required for cluster `10` (default) | positive integer

Maximum number of points in a cluster, specified as a positive integer. This
property is used to estimate epsilon when the object performs a *k*-NN
search.

#### Dependencies

To enable this parameter, set the **Source of cluster threshold
epsilon** parameter to `Auto`.

### **Length of cluster threshold epsilon history** — Length of cluster threshold epsilon history `10` (default) | positive integer

Length of the stored cluster threshold epsilon history, specified as a positive
integer. When set to one, the history is memory-less. Then, each epsilon estimate is
immediately used and no moving-average smoothing occurs. When greater than one, the
epsilon value is averaged over the history length specified.

**Example:** `5`

**Data Types:** `double`

### **Enable disambiguation of dimensions** — Turn on disambiguation `off` (default) | `on`

Check box to enable disambiguation of dimensions, specified as
`false` or `true`. When checked, clustering occurs
across boundaries defined by the values in the input port `AmbLims`
at execution. Ambiguous detections are appropriately clustered. Use the
**Indices of ambiguous dimensions** parameter to specify those column
indices of `X` in which ambiguities can occur. Up to two ambiguous
dimensions are permitted. Turning on disambiguation is not recommended for large data
sets.

**Data Types:** `Boolean`

### **Indices of ambiguous dimensions** — Indices of ambiguous dimensions `1` (default) | positive integer | 1-by-2 vector of positive integers

Indices of ambiguous dimensions, specified as a positive integer or 1-by-2 vector of
positive integers. This property specifies the column indices of the input port data
`X` in which disambiguation can occur. A positive integer
corresponds to a single ambiguous dimension in the input data matrix
`X`. A 1-by-2 length row vector of indices corresponds to two
ambiguous dimensions. The size and order of **Indices of ambiguous
dimensions** must be consistent with the `AmbLims` input
port value.

**Example:** `[3 4]`

#### Dependencies

To enable this parameter, select the **Enable disambiguation of
dimensions** check box.

**Data Types:** `double`

### **Simulate using** — Block simulation method `Interpreted Execution` (default) | `Code Generation`

Block simulation, specified as `Interpreted Execution` or `Code
Generation`. If you want your block to use the MATLAB® interpreter,
choose `Interpreted Execution`. If you want
your block to run as compiled code, choose `Code Generation`.
Compiled code requires time to compile but usually runs faster.

Interpreted execution is useful when you are developing and tuning a model. The block runs the
underlying System object™ in MATLAB. You can change and execute your model quickly. When you are satisfied
with your results, you can then run the block using `Code
Generation`. Long simulations run faster with generated code than in
interpreted execution. You can run repeated executions without recompiling, but if you
change any block parameters, then the block automatically recompiles before
execution.

This table shows how the **Simulate using** parameter affects the overall
simulation behavior.

When the Simulink model is in `Accelerator` mode, the block mode specified
using **Simulate using** overrides the simulation mode.

**Acceleration Modes**

|  |  |  |  |
| --- | --- | --- | --- |
| Block Simulation | Simulation Behavior | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | The block executes using the MATLAB interpreter. | The block executes using the MATLAB interpreter. | Creates a standalone executable from the model. |
| `Code Generation` | The block is compiled. | All blocks in the model are compiled. |

For more information, see Choosing a Simulation Mode (Simulink).

## Libraries

Radar Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

## Description

Cluster detections

Cluster data using the density-based spatial clustering of applications with noise
(DBSCAN) algorithm. The DBSCAN Clusterer block can cluster any type of data.
The block can also solve for the clustering threshold (epsilon) and can perform data
disambiguation in two dimensions.
