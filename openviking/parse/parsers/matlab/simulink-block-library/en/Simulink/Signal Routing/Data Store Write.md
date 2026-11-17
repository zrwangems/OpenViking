---
type: simulink-block
title: 'Data Store Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'datastorewrite'
documentation_source_path: 'slref/datastorewrite.html'
language: en
---

# Data Store Write

## Ports
```yaml
ports:
- name: Port_1
  summary: Values to write to data store scalar | vector | matrix | N-D array
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | image
- name: IdxN
  summary: '*N*th index signal scalar | vector'
  direction: input
  data_types: int8 | int16 | int32 | uint8 | uint16
```

### Input

### **Port\_1** — Values to write to data store scalar | vector | matrix | N-D array

Values to write to the specified data store. The Data Store
Write block accepts a real or complex signal.

You can use an array of buses with a Data Store Write
block. For details about defining and using an array of buses, see Group Nonvirtual Buses in Arrays of Buses.

To assign a subset of the bus or matrix elements to the associated
data store, use the **Element Assignment** pane. The
Data Store Write block icon reflects the elements
that you specify. For details, see Accessing Specific Bus and Matrix Elements.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### **IdxN** — *N*th index signal scalar | vector

External port that specifies an index for the assignment of the
corresponding data store subelements.

#### Dependencies

To enable an external index port, on the **Element
Assignment** tab, select **Enable
indexing**. Then, in the *N*th row of
the **Index Option** table, set **Index
Option** to `Index vector
(port)` or `Starting index
(port)`.

**Data Types:** `int8` | `int16` | `int32` | `uint8` | `uint16`
## Parameters
```yaml
parameters:
- name: Data store name
  summary: Name of data store to which block writes A (default) | name of data store
  group: Parameters
  block_parameter: DataStoreName
  type: string | character vector
  values: data store name
  default: '''A'''
- name: Data store memory block
  summary: 'Data Store Memory block name Read-only: block path'
  group: Parameters
- name: Corresponding Data Store Read blocks
  summary: 'List of corresponding Data Store Read blocks Read-only: block path'
  group: Parameters
- name: Sample time
  summary: Sample time -1 (default) | scalar | vector
  group: Parameters
  block_parameter: SampleTime
  type: string | character vector
  values: scalar | vector
  default: '''-1'''
- name: Elements in the array (Signals in the bus)
  summary: Elements in associated data store string | character vector
  group: Element Assignment
  block_parameter: DataStoreElements
  type: string | character vector
  values: pound-delimited list of elements (See Specification using the command line.)
  default: ''''''
- name: Specify element(s) to assign
  summary: MATLAB expression defining the elements to assign string | character vector
  group: Element Assignment
  block_parameter: DataStoreElements
  type: string | character vector
  values: pound-delimited list of elements (See Specification using the command line.)
  default: ''''''
- name: Assigned element(s)
  summary: List of selected elements string | character vector
  group: Element Assignment
  block_parameter: DataStoreElements
  type: string | character vector
  values: pound-delimited list of elements (See Specification using the command line.)
  default: ''''''
- name: Enable indexing
  summary: Enable indexing to specify subelements of data store element to write off (default) | on
  group: Element Assignment
  block_parameter: EnableIndexing
  type: string | character vector
  values: '"off" | "on"'
  default: '''off'''
- name: Number of dimensions
  summary: Number of dimensions of data store element 1 (default) | positive integer
  group: Element Assignment
  block_parameter: NumberOfDimensions
  type: string | character vector
  values: positive integer
  default: '''1'''
- name: Index mode
  summary: Index mode One-based (default) | Zero-based
  group: Element Assignment
  block_parameter: IndexMode
  type: string | character vector
  values: '"Zero-based" | "One-based"'
  default: '''One-based'''
- name: Index Option
  summary: Index method for subelements Index vector (dialog) (default) | Select all | Index vector (port) | Starting index
    (dialog) | Starting index (port)
  group: Element Assignment
  block_parameter: IndexOptionArray
  type: string | character vector
  values: '"Select all" | "Index vector (dialog)" | "Index vector (port)" | "Starting index (dialog)" | "Starting index (port)"'
  default: '''Index vector (dialog)'''
- name: Index
  summary: Indices or starting index of subelements 1 (default) | integer | vector of integers
  group: Element Assignment
  block_parameter: IndexParamArray
  type: character vector
  values: cell array
  default: '''{ }'''
```

### Parameters

### **Data store name** — Name of data store to which block writes `A` (default) | name of data store

Specify the name of the data store to which this block writes data.
The adjacent list provides the names of Data Store Memory
blocks that exist at the same level in the model as the Data
Store Write block or at higher levels. The list also
includes all `Simulink.Signal` objects in the base and
model workspaces. To change the name, select a name from the list or
enter the name directly in the edit field.

When compiling a model that contains this block, the software searches
the model upwards from the level of the block for a Data Store
Memory block having the specified data store name. If the
software does not find such a block, it searches the model workspace and
the MATLAB® workspace for a `Simulink.Signal` object
that has the same name. If the software finds a `Signal`
object, it creates a hidden Data Store Memory block at
the root level of the model with the properties specified by the
`Signal` object and an initial value set to an array
of zeros. The dimensions of that array are inherited from the
`Dimensions` property of the
`Signal` object.

If the software finds neither the Data Store Memory
block nor the `Signal` object, it halts the compilation
and issues an error. See Symbol Resolution for more
information about the search path.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DataStoreName` |
| **Type**: string | character vector |
| **Values**: data store name |
| **Default**: `'A'` |

### **Data store memory block** — Data Store Memory block name Read-only: block path

This parameter is read-only.

This field lists the Data Store Memory block that
initialized the store to which this block writes.

### **Corresponding Data Store Read blocks** — List of corresponding Data Store Read blocks Read-only: block path

This parameter is read-only.

This field lists the path to all Data Store Read blocks
with the same data store name as this block that are in the same
subsystem or in any subsystem below it in the model hierarchy. Click any
entry in this list to highlight the corresponding block in your
model.

### **Sample time** — Sample time `-1` (default) | scalar | vector

The sample time, which controls when the block writes to the data
store. A value of `-1` indicates that the sample time
is inherited. See Specify Sample Time
for more information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: string | character vector |
| **Values**: scalar | vector |
| **Default**: `'-1'` |

### Element Assignment

### **Elements in the array (Signals in the bus)** — Elements in associated data store string | character vector

List of elements in the associated data store. For data stores with
arrays, you can write the whole data store, or you can assign one or
more elements to the whole data store. For data stores with a bus data
type, you can expand the tree to view and select the bus elements. The
list displays the maximum dimensions for each element in
parentheses.

If **Enable indexing** is not selected, select an
element and use one of the following approaches:

- Click **Select>>** to display that
  element and all its subelements in the **Selected
  element(s)** list.
- Use the **Specify element(s) to assign** edit
  box to specify the subelements that you want to select for
  writing. Then click
  **Select>>**.

To select multiple elements, repeat the above procedure for each
element.

Alternatively, you can select **Enable indexing**,
then select a single element and specify the subelements dynamically
using the **Index Option** parameter.

To refresh the display and reflect modifications to the array or bus
used in the data store, click **Refresh**.

#### Dependencies

The prompt for this section (**Elements in the
array** or **Signals in the bus**)
depends on the type of data in the data store.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DataStoreElements` |
| **Type**: string | character vector |
| **Values**: pound-delimited list of elements (See Specification using the command line.) |
| **Default**: `''` |

### **Specify element(s) to assign** — MATLAB expression defining the elements to assign string | character vector

Enter a MATLAB expression to define the specific element that you want to
write, then click **Select>>** to add the
element to the **Assigned element(s)** table. Repeat to
select additional elements.

For example, for a data store named `DSM` that has
maximum dimensions of `[3,5]`, you could enter
expressions such as `DSM(2,4)` or `DSM([1
3],2)` in the edit box. See Accessing Specific Bus and Matrix Elements.

To apply the element selection, click **OK** or
**Apply**.

#### Dependencies

The **Specify element(s) to assign** edit box
appears only if **Enable indexing** is not
selected.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DataStoreElements` |
| **Type**: string | character vector |
| **Values**: pound-delimited list of elements (See Specification using the command line.) |
| **Default**: `''` |

### **Assigned element(s)** — List of selected elements string | character vector

Elements that you select for assignment. The Data Store
Write block icon displays an input port for each element
that you specify.

To change the order of bus or matrix elements in the list, select the
element in the list and click **Up** or
**Down**. Changing the order of the elements in
the list changes the order of the ports. To remove an element, click
**Remove**.

#### Dependencies

To enable this parameter, clear **Enable
indexing**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DataStoreElements` |
| **Type**: string | character vector |
| **Values**: pound-delimited list of elements (See Specification using the command line.) |
| **Default**: `''` |

### **Enable indexing** — Enable indexing to specify subelements of data store element to write `off` (default) | `on`

Select this parameter to enable indexing similar to that used by the
Assignment block,
whereby you can dynamically specify indices of subelements to write by
using one or more index input ports, as well as specifying indices by
using the block dialog. A Data Store Write block can
write to only a single element of a data store (that is, a single signal
in a bus) when this parameter is selected. To write to multiple elements
of a data store using dynamic indexing, use multiple Data Store
Write blocks.

Clear this parameter to disable Assignment block-style
indexing. You can select multiple data store elements to write, but you
can specify which subelements to write only by using the block
dialog.

**Note**

Do not select **Enable indexing** if the
associated data store contains only a single, scalar element.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `EnableIndexing` |
| **Type**: string | character vector |
| **Values**: `"off"` | `"on"` |
| **Default**: `'off'` |

### **Number of dimensions** — Number of dimensions of data store element `1` (default) | positive integer

Number of dimensions of selected data store element. You must
explicitly indicate this number.

#### Dependencies

To enable this parameter, select **Enable
indexing**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumberOfDimensions` |
| **Type**: string | character vector |
| **Values**: positive integer |
| **Default**: `'1'` |

### **Index mode** — Index mode `One-based` (default) | `Zero-based`

Select the indexing mode. If `One-based` is
selected, an index of 1 specifies the first element of the input vector.
If `Zero-based` is selected, an index of 0
specifies the first element of the input vector.

#### Dependencies

To enable this parameter, select **Enable
indexing**.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `IndexMode` |
| **Type:** string | character vector |
| **Values:** `"Zero-based"` | `"One-based"` |
| **Default:** `'One-based'` |

### **Index Option** — Index method for subelements `Index vector (dialog)` (default) | `Select all` | `Index vector (port)` | `Starting index (dialog)` | `Starting index (port)`

Define, by dimension, how the subelements of the selected data store
element are to be indexed. From the list, select:

| Menu Item | Action |
| --- | --- |
| `Select all` | Disables the **Index** column. All subelements are assigned. |
| `Index vector (dialog)` | Enables the **Index** column. Enter a vector containing the indices of subelements to be assigned values. |
| `Index vector (port)` | Disables the **Index** column. The relevant index port defines the indices of subelements to be assigned values. |
| `Starting index (dialog)` | Enables the **Index** column. Enter the starting index of the range of subelements to be assigned values. The size of the range is inherited from the size of relevant dimension of the input data signal. |
| `Starting index (port)` | Disables the **Index** column. The relevant index port defines the starting index of the range of elements to be assigned values. The size of the range is inherited from the size of relevant dimension of the input data signal. |

The **Index** column is displayed as relevant.

#### Dependencies

To enable this parameter, select **Enable
indexing**.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `IndexOptionArray` |
| **Type:** string | character vector |
| **Values:** `"Select all"` | `"Index vector (dialog)"` | `"Index vector (port)"` | `"Starting index (dialog)"` | `"Starting index (port)"` |
| **Default:** `'Index vector (dialog)'` |

### **Index** — Indices or starting index of subelements `1` (default) | integer | vector of integers

If the **Index Option** is `Index vector
(dialog)`, enter a vector containing the indices of
each subelement to write.

If the **Index Option** is `Starting
index (dialog)`, enter the starting index of the range
of subelements to write.

#### Dependencies

To enable this parameter, select **Enable
indexing** and set **Index Option**
for the dimension to `Index vector
(dialog)` or `Starting index
(dialog)`.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `IndexParamArray` |
| **Type:** character vector |
| **Values:** cell array |
| **Default:** `'{ }'` |
## Libraries

Simulink / Signal Routing

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2024a: Data Store Write Block Supports Indexing for Symbolic Indexing

The Data Store Write block now supports indexing when the Data Store Memory block uses
symbolic dimensions.

## Description

Write data to data store

The Data Store Write block copies the value at its input to the named
data store. Each write operation performed by a Data Store Write block
writes over the data store or a selected portion thereof and replaces the previous
contents.

The data store to which this block writes is determined by the location of the
Data Store Memory block or signal object that defines the data store.
For more information, see Data Stores and Data Store Memory. The size of the data
store is set by the signal object or the Data Store Memory block that
defines and initializes the data store. Each Data Store Write block that
writes to that data store can write up to the amount of data in the data store.

More than one Data Store Write block can write to the same data store.
However, if two Data Store Write blocks attempt to write to the same data
store during the same simulation step, results are unpredictable.

Obtaining correct results from data stores requires ensuring that data store reads and
writes occur in the expected order. For details, see Order Data Store Access and Data Store Diagnostics.

You can log the values of a local or global data store data variable for all the steps
in a simulation. For details, see Log Data Stores.

You can select a Data Store Read, Data Store Write, or
Data Store Memory block to highlight blocks related to it. To show a
related block in an open diagram or new tab, pause on the ellipsis that appears after
selection. Then, select Related Blocks  from the action bar. When multiple blocks correspond
to the selected block, a list of related blocks opens. You can filter the list of
related blocks by entering a search term in the text box. After you select a related
block from the list, window focus goes to the open diagram or new tab that shows the
related block.

**Element Assignment** tab is not supported when the Data
Store Write block writes to a Data Store Memory block with
the **Dimensions** parameter value set to `Inf`. In
other words, the data store is set to accept unbounded variable-size signals.
