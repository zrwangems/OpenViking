---
type: simulink-block
title: 'MultiPlot Graph'
family: 'robust'
product_id: 'robust'
product_name: 'Robust Control Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'multiplotgraph'
documentation_source_path: 'ref/multiplotgraph.html'
language: en
---

# MultiPlot Graph

## Ports
```yaml
ports:
- name: Port_1(y)
  summary: Signal to plot scalar | vector
  direction: input
```

### Input

### **Port\_1(y)** — Signal to plot scalar | vector

Providing a scalar signal creates one plot. To create multiple subplots, combine
the signals you want to plot into a vector signal, using blocks such as:

- Mux (Simulink)
- Vector Concatenate (Simulink)
- Bus Creator (Simulink)
## Parameters
```yaml
parameters:
- name: t-min
  summary: X-axis lower limit 0 (default) | scalar | vector
  group: ''
  block_parameter: tmin
  type: scalar, vector
  default: '0'
- name: t-max
  summary: X-axis upper limit 20 (default) | scalar | vector
  group: ''
  block_parameter: tmax
  type: scalar, vector
  default: '20'
- name: y-min
  summary: Y-axis lower limit –1 (default) | scalar | vector
  group: ''
  block_parameter: ymin
  type: scalar, vector
  default: –1
- name: y-max
  summary: Y-axis upper limit 1 (default) | scalar | vector
  group: ''
  block_parameter: ymax
  type: scalar, vector
  default: '1'
- name: Plot title
  summary: Figure title empty (default) | character vector
  group: ''
  block_parameter: titleString
  type: character vector
  default: ''''''
- name: Workspace variable for export
  summary: Variable name for saving plot data multisimout (default) | character vector
  group: ''
  block_parameter: vnamesave
  type: character vector
  default: ''''''
```

### **t-min** — X-axis lower limit 0 (default) | scalar | vector

The **t-min** and **t-max** parameters set the
*x*-axis limits. To set different lower limits for each subplot,
set **t-min** to a vector of the same dimensions as the input signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `tmin` |
| **Type:** scalar, vector |
| **Default:** 0 |

### **t-max** — X-axis upper limit 20 (default) | scalar | vector

The **t-min** and **t-max** parameters set the
*x*-axis limits. To set different upper limits for each subplot,
set **t-max** to a vector of the same dimensions as the input signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `tmax` |
| **Type:** scalar, vector |
| **Default:** 20 |

### **y-min** — Y-axis lower limit –1 (default) | scalar | vector

The **y-min** and **y-max** parameters set the
*y*-axis limits. To set different lower limits for each subplot,
set **y-min** to a vector of the same dimensions as the input
signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ymin` |
| **Type:** scalar, vector |
| **Default:** –1 |

### **y-max** — Y-axis upper limit 1 (default) | scalar | vector

The **y-min** and **y-max** parameters set the
*y*-axis limits. To set different upper limits for each subplot,
set **y-max** to a vector of the same dimensions as the input
signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ymax` |
| **Type:** scalar, vector |
| **Default:** 1 |

### **Plot title** — Figure title empty (default) | character vector

Specify the title of the MATLAB figure that the block generates.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `titleString` |
| **Type:** character vector |
| **Default:** `''` |

### **Workspace variable for export** — Variable name for saving plot data `multisimout` (default) | character vector

To export the plot data to the MATLAB workspace, in the figure window, click export icon. The block exports the data to a variable with the name
you specify in this parameter. The data is saved in a `struct` array with
the following fields:

- `time` — Column vector of simulation times at which input value
  was logged.
- `signals` — Structure with sample values that contains the fields:

  - `values` — Array of sample values.
  - `dimensions` — Sample dimensions.
  - `label` — Name of signal line in model.
- `blockName` — Name of the MultiPlot Graph
  block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `vnamesave` |
| **Type:** character vector |
| **Default:** `''` |
## Libraries

Robust Control Toolbox

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2007a**

### R2023a: Block inherits upstream sample time

The **Sample time** parameter has been removed. The block now uses the
sample time of its input signal. Previously, the block resampled the input signal at the
specified sample time, or used the upstream sample time when **Sample
time** was set to –1.

### R2023a: Parameter names changed

- **Title** is now called **Plot title**.
- **Variable for Export to Workspace** is now called
  **Workspace variable for export**.

## Description

Plot results of multiple simulations

The MultiPlot Graph block displays signals in a MATLAB® figure window generated when you simulate the model. At each subsequent
simulation, the block adds a new line to the figure, cycling through seven colors. This block
allows you to view the results of multiple simulations on a single MATLAB figure. For instance, you can use the block with the Uncertain State
Space block to visualize Monte Carlo and worst-case simulation time responses.

The input signal can be scalar or vector. If the input signal is a vector, then the block
plots each component of the vector in separate axes.

To export the visible plot data to the MATLAB workspace, in the figure window, click export icon. The block exports the data in a variable having the name you
specify in the Workspace variable for export parameter.

To clear the data from all axes, in the figure window, click eraser icon.
