---
type: simulink-block
title: 'KNN Search'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Cluster Analysis'
documentation_page: 'knnsearchblock'
documentation_source_path: 'knnsearchblock.html'
language: en
---

# KNN Search

## Ports
```yaml
ports:
- name: x
  summary: Query point row vector
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Idx
  summary: Indices of nearest neighbors numeric row vector | 1-by-1 cell array
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: D
  summary: Distances of nearest neighbors numeric row vector | 1-by-1 cell array
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### Input

### **x** — Query point row vector

Query point, specified as a row vector. **x** must have the same
number of columns as the number of predictor variables in the
`searcher` object specified by **Select nearest
neighbor searcher**. The columns of **x** must be in
the same order as those in the `searcher` object.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Idx** — Indices of nearest neighbors numeric row vector | 1-by-1 cell array

Indices of the nearest neighbors in the data, returned as a numeric row vector or
1-by-1 cell array.

- If you do not select **Include ties** on the **Main** tab of the Block Parameters dialog box, then the
  block returns a 1-by-*k* numeric row vector, where
  *k* is the number of nearest neighbors searched. Each column
  of the row vector contains the index of a nearest neighbor point in the data,
  ordered by increasing distance to the query point **x**.
- If you select **Include ties** on the **Main** tab of the Block Parameters dialog box, then the block
  returns a 1-by-1 cell array as a variable-size signal containing a numeric row
  vector of at least *k* indices of the closest observations in
  the data to the query point **x**. The columns of the vector
  are ordered by increasing distance to the query point.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **D** — Distances of nearest neighbors numeric row vector | 1-by-1 cell array

Distances of the nearest neighbors to the query points, returned as a numeric row
vector or 1-by-1 cell array.

- If you do not select **Include ties** on the **Main** tab of the Block Parameters dialog box, then the
  block returns a 1-by-*k* numeric row vector, where
  *k* is the number of nearest neighbors searched. Each column
  of the row vector contains the distance of a nearest neighbor point in the data
  to the query point **x**, according to the distance metric. The
  columns of the row vector are ordered by increasing distance to the query point.
- If you select **Include ties** on the **Main** tab of the Block Parameters dialog box, then the block
  returns a 1-by-1 cell array as a variable-size signal containing a numeric row
  vector of at least *k* distances of the closest observations in
  the data to the query point **x**. The columns of the vector
  are ordered by increasing distance to the query point.

#### Dependencies

To enable this port, select **Add output port for
nearest neighbor distances** in the KNN Search
block.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## Parameters
```yaml
parameters:
- name: Select nearest neighbor searcher
  summary: Nearest neighbor search method searcher (default) | ExhaustiveSearcher object | KDTreeSearcher object
  group: Main
  block_parameter: NeighborhoodSearcher
  type: workspace variable
  values: ExhaustiveSearcher object | KDTreeSearcher object
  default: '"searcher"'
- name: Add output port for nearest neighbor distances
  summary: Add second output port for nearest neighbor distances off (default) | on
  group: Main
  block_parameter: ShowOutputDistances
  type: character vector
  values: '"off" | "on"'
  default: '"off"'
- name: Number of nearest neighbors
  summary: Number of nearest neighbors 1 (default) | positive integer
  group: Main
  block_parameter: NumNeighbors
  type: positive integer
  values: single | double
  default: '1'
- name: Include ties
  summary: Flag to include all nearest neighbors off (default) | on
  group: Main
  block_parameter: IncludeTies
  type: character vector
  values: '"off" | "on"'
  default: '"off"'
- name: Distance metric
  summary: Distance metric euclidean (default) | chebychev | cityblock | minkowski | correlation | cosine | hamming | jaccard
    | mahalanobis | seuclidean | spearman
  group: Main
  block_parameter: DistanceMetric
  type: character vector
  values: '"euclidean" | "chebychev" | "cityblock" | "minkowski" | "correlation" | "cosine" | "hamming" | "jaccard" | "mahalanobis"
    | "seuclidean" | "spearman"'
  default: '"euclidean"'
- name: Covariance matrix
  summary: Covariance matrix for Mahalanobis distance metric Computed using data in searcher (default) | Customized
  group: Main
  block_parameter: CovarianceMatrix
  type: positive definite matrix
  values: '"Computed using data in searcher" | "Customized"'
  default: '"Computed using data in searcher"'
- name: Scale
  summary: Scale parameter value for standardized Euclidean distance metric Standard deviation of data in searcher (default)
    | Customized
  group: Main
  block_parameter: Scale
  type: nonnegative numeric row vector
  values: '"Standard deviation of data in searcher" | "Customized"'
  default: '"Standard deviation of data in searcher"'
- name: P
  summary: Exponent for Minkowski distance metric 2 (default) | positive integer
  group: Main
  block_parameter: MinkExp
  type: positive integer
  values: positive integer
  default: '2'
- name: Integer rounding mode
  summary: Rounding mode for fixed-point operations Floor (default) | Ceiling | Convergent | Nearest | Round | Simplest |
    Zero
  group: Data Types
  block_parameter: RndMeth
  type: character vector
  values: '"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"'
  default: '"Floor"'
- name: Saturate on integer overflow
  summary: Method of overflow action off (default) | on
  group: Data Types
  block_parameter: SaturateOnIntegerOverflow
  type: character vector
  values: '"off" | "on"'
  default: '"off"'
- name: Lock output data type setting against changes by the fixed-point tools
  summary: Prevention of fixed-point tools from overriding data type off (default) | on
  group: Data Types
  block_parameter: LockScale
  type: character vector
  values: '"off" | "on"'
  default: '"off"'
- name: Index data type
  summary: 'Data type of index output Inherit: auto (default) | double | single | half | int8 | uint8 | int16 | uint16 | int32
    | uint32 | int64 | uint64 | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: Data Types
  block_parameter: IndicesDataTypeStr
  type: character vector
  values: '"Inherit: auto" | "double" | "single" | "half" | "int8" | "uint8" | "int16" | "uint16" | "int32" | "uint32" | "int64"
    | "uint64" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "<data type expression>"'
  default: '"Inherit: auto"'
- name: Index data type Minimum
  summary: Minimum of index output [] (default) | scalar
  group: Data Types
  block_parameter: IndicesOutMin
  type: scalar
  values: '"[]" | scalar'
  default: '"[]"'
- name: Index data type Maximum
  summary: Maximum of index output [] (default) | scalar
  group: Data Types
  block_parameter: IndicesOutMax
  type: scalar
  values: '"[]" | scalar'
  default: '"[]"'
- name: Distance data type
  summary: 'Data type of distance output Inherit: auto (default) | double | single | half | int8 | uint8 | int16 | uint16
    | int32 | uint32 | int64 | uint64 | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: Data Types
  block_parameter: DistanceDataTypeStr
  type: character vector
  values: '"Inherit: auto" | "double" | "single" | "half" | "int8" | "uint8" | "int16" | "uint16" | "int32" | "uint32" | "int64"
    | "uint64" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "<data type expression>"'
  default: '"Inherit: auto"'
- name: Distance data type Minimum
  summary: Minimum of distance output [] (default) | scalar
  group: Data Types
  block_parameter: DistanceOutMin
  type: scalar
  values: '"[]" | scalar'
  default: '"[]"'
- name: Distance data type Maximum
  summary: Maximum of distance output [] (default) | scalar
  group: Data Types
  block_parameter: DistanceOutMax
  type: scalar
  values: '"[]" | scalar'
  default: '"[]"'
```

### Main

### **Select nearest neighbor searcher** — Nearest neighbor search method `searcher` (default) | `ExhaustiveSearcher` object | `KDTreeSearcher` object

Specify the name of a workspace variable that contains an `ExhaustiveSearcher` or `KDTreeSearcher` object.

**Note**

The software uses the default settings for all parameters that you can specify
in the Block Parameters dialog box. The parameters in the dialog box override those
of the searcher object.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NeighborhoodSearcher` |
| **Type:** workspace variable |
| **Values:** `ExhaustiveSearcher` object | `KDTreeSearcher` object |
| **Default:** `"searcher"` |

### **Add output port for nearest neighbor distances** — Add second output port for nearest neighbor distances `off` (default) | `on`

Select the check box to include the second output port **D** in
the KNN Search block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowOutputDistances` |
| **Type:** character vector |
| **Values:** `"off" | "on"` |
| **Default:** `"off"` |

### **Number of nearest neighbors** — Number of nearest neighbors `1` (default) | positive integer

Specify the number of nearest neighbors to find in the data for the query
point.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumNeighbors` |
| **Type:** positive integer |
| **Values:** `single` | `double` |
| **Default:** `1` |

### **Include ties** — Flag to include all nearest neighbors `off` (default) | `on`

If you do not select **Include ties** on the **Main** tab of the Block Parameters dialog box, then the block
selects the observation with the smallest index among the observations that have the
same distance from the query point.

If you select **Include ties**:

- The block output includes all nearest neighbors whose distances are equal to
  the *k*th smallest distance in the output arguments. If more
  than five nearest neighbors have equal distance to the *k*th
  smallest distance, the block output includes only the first five nearest
  neighbors with the smallest index values.
- The **Idx** and **D** block outputs are
  1-by-1 cell arrays where each cell contains a vector of at least
  *k* indices and distances, respectively. The columns in the
  vectors are ordered by increasing distance to the query point.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IncludeTies` |
| **Type:** character vector |
| **Values:** `"off" | "on"` |
| **Default:** `"off"` |

### **Distance metric** — Distance metric `euclidean` (default) | `chebychev` | `cityblock` | `minkowski` | `correlation` | `cosine` | `hamming` | `jaccard` | `mahalanobis` | `seuclidean` | `spearman`

Specify the distance metric used to find nearest neighbors in the data to the
query point.

For both `ExhaustiveSearcher` and `KDTreeSearcher` objects, the block supports these distance metrics.

| Value | Description |
| --- | --- |
| `"chebychev"` | Chebychev distance (maximum coordinate difference) |
| `"cityblock"` | City block distance |
| `"euclidean"` | Euclidean distance |
| `"minkowski"` | Minkowski distance. The default exponent is 2. You can specify a different exponent in the Block Parameters dialog box. |

For an `ExhaustiveSearcher` object, the block also supports these
distance metrics.

| Value | Description |
| --- | --- |
| `"correlation"` | One minus the sample linear correlation between observations (treated as sequences of values) |
| `"cosine"` | One minus the cosine of the included angle between observations (treated as row vectors) |
| `"hamming"` | Hamming distance, which is the percentage of coordinates that differ |
| `"jaccard"` | One minus the Jaccard coefficient, which is the percentage of nonzero coordinates that differ |
| `"mahalanobis"` | Mahalanobis distance, computed using a positive definite covariance matrix. The block computes the covariance matrix from the data in the `searcher` object, by default. You can specify a customized covariance matrix in the Block Parameters dialog box. |
| `"seuclidean"` | Standardized Euclidean distance. Each coordinate difference between the query point **x** and the data is scaled by dividing by the corresponding element of the standard deviation computed from the data. You can specify a different scaling method in the Block Parameters dialog box. |
| `"spearman"` | One minus the sample Spearman's rank correlation between observations (treated as sequences of values) |

**Note**

- The distance metric setting overrides the `Distance`
  property of the specified `searcher` object.
- The KNN Search block does not support the
  `"fasteuclidean"` or `"fastseuclidean"`
  distance metric (see Distance Metrics).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DistanceMetric` |
| **Type:** character vector |
| **Values:** `"euclidean" | "chebychev" | "cityblock" | "minkowski" | "correlation" | "cosine" | "hamming" | "jaccard" | "mahalanobis" | "seuclidean" | "spearman"` |
| **Default:** `"euclidean"` |

### **Covariance matrix** — Covariance matrix for Mahalanobis distance metric `Computed using data in searcher` (default) | `Customized`

The block computes the covariance matrix from the data in the
`searcher` object, by default. You can specify a customized
covariance matrix by selecting `Customized` and entering a
positive definite matrix in the **Customized matrix** box.

**Note**

This setting overrides the `DistParameter` property of the
specified `searcher` object.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CovarianceMatrix` |
| **Type:** positive definite matrix |
| **Values:** `"Computed using data in searcher"` | `"Customized"` |
| **Default:** `"Computed using data in searcher"` |

#### Dependencies

To enable this parameter, set **Distance Metric** to
`"mahalanobis"`.

### **Scale** — Scale parameter value for standardized Euclidean distance metric `Standard deviation of data in searcher` (default) | `Customized`

The block computes the scale parameter value from the data in the
`searcher` object, by default. You can specify a customized scale
parameter value by selecting `Customized` and entering a
nonnegative numeric row vector in the **Customized scale** text box.
The row vector must have the same number of columns as the number of predictor
variables in the `searcher` object. When the block computes the
standardized Euclidean distance, each coordinate of the data is scaled by the
corresponding element of `Scale`, as is the query point.

**Note**

This setting overrides the `DistParameter` property of the
specified `searcher` object.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Scale` |
| **Type:** nonnegative numeric row vector |
| **Values:** `"Standard deviation of data in searcher"` | `"Customized"` |
| **Default:** `"Standard deviation of data in searcher"` |

#### Dependencies

To enable this parameter, set **Distance Metric** to
`"seuclidean"`.

### **P** — Exponent for Minkowski distance metric `2` (default) | positive integer

Specify the exponent for the Minkowski distance metric. For the default case of *P* = 2, the Minkowski distance gives the Euclidean distance. For the
special case of *P* = 1, the Minkowski distance gives the city block distance. For the
special case of *P* = ∞, the Minkowski distance gives the Chebychev distance.

**Note**

This setting overrides the `DistParameter` property of the
specified `searcher` object.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MinkExp` |
| **Type:** positive integer |
| **Values:** `positive integer` |
| **Default:** `2` |

#### Dependencies

To enable this parameter, set **Distance Metric** to
`"minkowski"`.

### Data Types

#### Fixed-Point Operational Parameters

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations. For more information, see Rounding Modes (Fixed-Point Designer).

Block parameters always round to the nearest representable value. To control the
rounding of a block parameter, enter an expression into the mask field using a
MATLAB® rounding function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RndMeth` |
| **Type:** character vector |
| **Values:** `"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"` |
| **Default:** `"Floor"` |

### **Saturate on integer overflow** — Method of overflow action `off` (default) | `on`

Specify whether overflows saturate or wrap.

| Action | Rationale | Impact on Overflows | Example |
| --- | --- | --- | --- |
| Select this check box (`on`). | Your model has possible overflow, and you want explicit saturation protection in the generated code. | Overflows saturate to either the minimum or maximum value that the data type can represent. | The maximum value that the `int8` (signed 8-bit integer) data type can represent is 127. Any block operation result greater than this maximum value causes overflow of the 8-bit integer. With the check box selected, the block output saturates at 127. Similarly, the block output saturates at a minimum output value of –128. |
| Clear this check box (`off`). | You want to optimize the efficiency of your generated code.  You want to avoid overspecifying how a block handles out-of-range signals. For more information, see Troubleshoot Signal Range Errors (Simulink). | Overflows wrap to the appropriate value that the data type can represent. | The maximum value that the `int8` (signed 8-bit integer) data type can represent is 127. Any block operation result greater than this maximum value causes overflow of the 8-bit integer. With the check box cleared, the software interprets the value causing the overflow as `int8`, which can produce an unintended result. For example, a block result of 130 (binary 1000 0010) expressed as `int8` is –126. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SaturateOnIntegerOverflow` |
| **Type:** character vector |
| **Values:** `"off" | "on"` |
| **Default:** `"off"` |

### **Lock output data type setting against changes by the fixed-point tools** — Prevention of fixed-point tools from overriding data type `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data type
you specify for the block. For more information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LockScale` |
| **Type:** character vector |
| **Values:** `"off" | "on"` |
| **Default:** `"off"` |

#### Data Type

### **Index data type** — Data type of index output `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the **Idx** output. The type can be
inherited, specified directly, or expressed as a data type object such as
`Simulink.NumericType`.

Click the **Show data type assistant**
button  to display the **Data Type Assistant**,
which helps you set the data type attributes. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IndicesDataTypeStr` |
| **Type**: character vector |
| **Values**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"Inherit: auto"` |

### **Index data type Minimum** — Minimum of index output `[]` (default) | scalar

Specify the minimum value of the **Idx** output range that
Simulink® checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as software-in-the-loop (SIL) mode or external mode. For more information,
  see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Index data type Minimum** parameter does not saturate
or clip the actual **Idx** output signal. To do so, use the
Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IndicesOutMin` |
| **Type**: scalar |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Index data type Maximum** — Maximum of index output `[]` (default) | scalar

Specify the maximum value of the **Idx** output range that
Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as software-in-the-loop (SIL) mode or external mode. For more information,
  see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Index data type Maximum** parameter does not saturate
or clip the actual **Idx** output signal. To do so, use the
Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `IndicesOutMax` |
| **Type**: scalar |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Distance data type** — Data type of distance output `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the distance (**D**) output. The type
can be inherited, specified directly, or expressed as a data type object such as
`Simulink.NumericType`.

Click the **Show data type assistant**
button  to display the **Data Type Assistant**,
which helps you set the data type attributes. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DistanceDataTypeStr` |
| **Type**: character vector |
| **Values**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"Inherit: auto"` |

**Note**

Fixed-point data types are not supported for the Spearman distance
metric.

#### Dependencies

To enable this parameter, select **Add output port for nearest
neighbor distances** on the **Main** tab of the Block
Parameters dialog box.

### **Distance data type Minimum** — Minimum of distance output `[]` (default) | scalar

Specify the minimum value of the distance (**D**) output range
that Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as software-in-the-loop (SIL) mode or external mode. For more information,
  see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Distance data type Minimum** parameter does not
saturate or clip the actual **D** output signal. To do so, use
the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DistanceOutMin` |
| **Type**: scalar |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

#### Dependencies

To enable this parameter, select **Add output
port for nearest neighbor distances** on the **Main**
tab of the Block Parameters dialog box.

### **Distance data type Maximum** — Maximum of distance output `[]` (default) | scalar

Specify the maximum value of the distance (**D**) output range
that Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as software-in-the-loop (SIL) mode or external mode. For more information,
  see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Distance data type Maximum** parameter does not
saturate or clip the actual **D** output signal. To do so, use
the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DistanceOutMax` |
| **Type**: scalar |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

#### Dependencies

To enable this parameter, select **Add output
port for nearest neighbor distances** on the **Main**
tab of the Block Parameters dialog box.
## Libraries

Statistics and Machine Learning Toolbox / Neighborhood Searcher

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2023b**

## Description

Find k -nearest neighbors using searcher object

The KNN Search block finds the nearest neighbors in the data to a query
point using a nearest neighbor searcher object (`ExhaustiveSearcher` or `KDTreeSearcher`).

Import a trained searcher object containing observation data into the block by specifying
the name of a workspace variable that contains the object. The input port
**x** receives a query point, and the output port **Idx**
returns the indices of the *k*-nearest neighbor points in the data. The
optional output port **D** returns the distances between the query point and
the nearest neighbor points.
