---
type: simulink-block
title: 'Mapped Core Engine'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Combustion Engine Components / Core Engine'
documentation_page: 'mappedcoreengine'
documentation_source_path: 'ref/mappedcoreengine.html'
language: en
---

# Mapped Core Engine

## Ports

### Input

### ***`<TrqCmd>`*** — Engine load `TrqCmd` (default)

Engine load, *L*. Examples of engine load include:

- Commanded torque

- Commanded indicated mean effective pressure (IMEP) in the
  engine cylinder

- Normalized cylinder air mass

- Injected fuel mass

#### Dependencies

To specify an engine load port name, on the
**Configuration** tab, enter a name in the
**Load input port name** parameter
field.

### ***`<EngSpd>`*** — Engine speed `EngSpd` (default)

Engine speed, *N*.

#### Dependencies

To specify an engine load port name, on the
**Configuration** tab, enter a name in the
**Speed input port name** parameter
field.

### ***`<EngTemp>`*** — Engine temperature `EngTemp` (default)

Engine temperature, *T*.

#### Dependencies

To create the engine temperature input port name, select
**Input engine temperature** parameter
field.

To specify an engine load port name, on the
**Configuration** tab, enter a name in the
**Temperature input port name** parameter
field.
### Output

### ***`<EngTrq>`*** — Power `EngTrq` (default)

Engine power, Tbrake.

#### Dependencies

- To create this port, on the
  **Configuration** tab, select
  **Power**.
- To specify the port name, on the
  **Power** tab, enter a name in the
   **Power output port name**
  parameter field.

### ***`<IntkAirMassFlw>`*** — Air mass flow `IntkAirMassFlw` (default)

Engine air mass flow, m˙intk.

#### Dependencies

- To create this port, on the
  **Configuration** tab, select
  **Air**.
- To specify the port name, on the
  **Air** tab, enter a name in the
   **Air output port name** parameter
  field.

### ***`<FuelMassFlw>`*** — Fuel flow `FuelMassFlw` (default)

Engine fuel flow, m˙fuel.

#### Dependencies

- To create this port, on the
  **Configuration** tab, select
  **Fuel**.
- To specify the port name, on the
  **Fuel** tab, enter a name in the
  **Fuel output port name** parameter
  field.

### ***`<ExhManGasTemp>`*** — Exhaust temperature `ExhManGasTemp` (default)

Engine exhaust temperature, Texh.

#### Dependencies

- To create this port, on the
  **Configuration** tab, select
  **Temperature**.
- To specify the port name, on the
  **Temperature** tab, enter a name
  in the **Temperature output port name**
  parameter field.

### ***`<Bsfc>`*** — Efficiency `Bsfc` (default)

Brake-specific fuel consumption (BSFC), *Eff*.

#### Dependencies

- To create this port, on the
  **Configuration** tab, select
  **Efficiency**.
- To specify the port name, on the
  **Efficiency** tab, enter a name in
  the **Efficiency output port name**
  parameter field.

### ***`<EoHC>`*** — Hydrocarbon emissions `EoHC` (default)

Hydrocarbon emissions, *HC*.

#### Dependencies

- To create this port, on the
  **Configuration** tab, select
  **HC**.
- To specify the port name, on the
  **HC** tab, enter a name in the
  **HC output port name** parameter
  field.

### ***`<EoCO>`*** — Carbon monoxide emissions `EoCO` (default)

Carbon monoxide emissions, *CO*.

#### Dependencies

- To create this port, on the
  **Configuration** tab, select
  **CO**.
- To specify the port name, on the
  **CO** tab, enter a name in the
  **CO output port name** parameter
  field.

### ***`<EoNOx>`*** — Nitric oxide and nitrogen dioxide emissions `EoNOx` (default)

Nitric oxide and nitrogen dioxide emissions,
*NOx*.

#### Dependencies

- To create this port, on the
  **Configuration** tab, select
  **NOx**.
- To specify the port name, on the
  **NOx** tab, enter a name in the
  **NOx output port name** parameter
  field.

### ***`<EoCO2>`*** — Carbon dioxide emissions `EoCO2` (default)

Carbon dioxide emissions, *CO2*.

#### Dependencies

- To create this port, on the
  **Configuration** tab, select
  **CO2**.
- To specify the port name, on the
  **CO2** tab, enter a name in the
  **CO2 output port name** parameter
  field.

### ***`<EoPm>`*** — Particulate matter emissions `EoPm` (default)

Particulate matter emissions, *PM*.

#### Dependencies

- To create this port, on the
  **Configuration** tab, select
  **PM**.
- To specify the port name, on the
  **PM** tab, enter a name in the
  **PM output port name** parameter
  field.

## Parameters

#### Configuration

### **Engine Type** — Type of engine image `Compression-ignition (CI)` (default) | `Spark-ignition (SI)`

Type of mapped internal combustion engine image to use in the
block.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `EngineType` |
| **Values:** | `Compression-ignition (CI)` (default) | `Spark-ignition (SI)` |
| **Data Types:** | `character vector` |

### **Load input port name** — Name `TrqCmd` (default)

Engine load input port name.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `rowVarName` |
| **Values:** | `TrqCmd` (default) |
| **Data Types:** | `character vector` |

### **Breakpoints for load input** — Breakpoints `vector`

Breakpoints for engine load input.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `rowbreakpoints` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Speed input port name** — Name `EngSpd` (default)

Speed input port name.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `colVarName` |
| **Values:** | `EngSpd` (default) |
| **Data Types:** | `character vector` |

### **Breakpoints for speed input** — Breakpoints `vector`

Breakpoints for engine speed input.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `colbreakpoints` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

### **Temperature input port name** — Name `EngTemp` (default)

Temperature input port name.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `TmpVarName` |
| **Values:** | `EngTemp` (default) |
| **Data Types:** | `character vector` |

#### Dependencies

To enable this parameter, select **Input engine temperature**.

### **Breakpoints for temperature input** — Breakpoints `[233.15 273.15 373.15]` (default) | `vector`

Breakpoints for engine temperature input.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Tmpbreakpoints` |
| **Values:** | `[233.15 273.15 373.15]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, select **Input engine temperature**.

### **Output Configuration** — Create output ports `on` (default) | `off`

Create the output ports.

#### Dependencies

The table summarizes the output ports that are created for each
**Output** parameter selection.

| Output Selection | Creates Port | Creates Tab |
| --- | --- | --- |
| **Power** | `EngTrq` | **Power** |
| **Air** | `IntkAirMassFlw` | **Air** |
| **Fuel** | `FuelMassFlw` | **Fuel** |
| **Temperature** | `ExhManGasTemp` | **Temperature** |
| **Efficiency** | `Bsfc` | **Efficiency** |
| **HC** | `EoHC` | **HC** |
| **CO** | `EoCO` | **CO** |
| **NOx** | `EoNOx` | **NOx** |
| **CO2** | `EoCO2` | **CO2** |
| **PM** | `EoPm` | **PM** |

#### Power

### **Power output port name** — Power `EngTrq` (default)

Power output port name.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Name1` |
| **Values:** | `EngTrq` (default) |
| **Data Types:** | `character vector` |

#### Dependencies

To create this parameter, on the **Configuration**
tab, select **Power**.

### **Power table** — Power `array`

Power table.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Name1_z` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, on the **Configuration**
tab, select **Power**.

#### Air

### **Air output port name** — Air `IntkAirMassFlw` (default)

Air mass flow output port name.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Name2` |
| **Values:** | `IntkAirMassFlw` (default) |
| **Data Types:** | `character vector` |

#### Dependencies

To create this parameter, on the **Configuration**
tab, select **Air**.

### **Air table** — Air `array`

Air mass flow table.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Name2_z` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, on the **Configuration**
tab, select **Air**.

#### Fuel

### **Fuel output port name** — Fuel `FuelMassFlw` (default)

Fuel output port name.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Name3` |
| **Values:** | `FuelMassFlw` (default) |
| **Data Types:** | `character vector` |

#### Dependencies

To create this parameter, on the **Configuration**
tab, select **Fuel**.

### **Fuel table** — Fuel `array`

Fuel table.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Name3_z` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, on the **Configuration**
tab, select **Fuel**.

#### Temperature

### **Temperature output port name** — Temperature `ExhManGasTemp` (default)

Temperature output port name.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Name4` |
| **Values:** | `ExhManGasTemp` (default) |
| **Data Types:** | `character vector` |

#### Dependencies

To create this parameter, on the **Configuration**
tab, select **Temperature**.

### **Temperature table** — Temperature `array`

Temperature table.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Name4_z` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, on the **Configuration**
tab, select **Temperature**.

#### Efficiency

### **Efficiency output port name** — Efficiency `Bsfc` (default)

Efficiency output port name.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Name5` |
| **Values:** | `Bsfc` (default) |
| **Data Types:** | `character vector` |

#### Dependencies

To create this parameter, on the **Configuration**
tab, select **Efficiency**.

### **Efficiency table** — Efficiency `array`

Efficiency table.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Name5_z` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, on the **Configuration**
tab, select **Efficiency**.

#### HC

### **HC output port name** — Hydrocarbon `EoHC` (default)

Hydrocarbon output port name.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Name6` |
| **Values:** | `EoHC` (default) |
| **Data Types:** | `character vector` |

#### Dependencies

To create this parameter, on the **Configuration**
tab, select **HC**.

### **HC table** — Hydrocarbon `array`

Hydrocarbon table.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Name6_z` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, on the **Configuration**
tab, select **HC**.

#### CO

### **CO output port name** — Carbon dioxide `EoCO` (default)

Carbon monoxide output port name.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Name7` |
| **Values:** | `EoCO` (default) |
| **Data Types:** | `character vector` |

#### Dependencies

To create this parameter, on the **Configuration**
tab, select **CO**.

### **CO table** — Carbon dioxide `array`

Carbon dioxide table.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Name7_z` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, on the **Configuration**
tab, select **CO**.

#### NOx

### **NOx output port name** — Nitric oxide *NO* and nitrogen dioxide *NO2* `EoNOx` (default)

NOx output port name. NOx is nitric oxide *NO* and
nitrogen dioxide *NO2*.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Name8` |
| **Values:** | `EoNOx` (default) |
| **Data Types:** | `character vector` |

#### Dependencies

To create this parameter, on the **Configuration**
tab, select **NOx**.

### **NOx table** — Nitric oxide *NO* and nitrogen dioxide *NO2* `array`

NOx emissions table. NOx is nitric oxide *NO* and
nitrogen dioxide *NO2*.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Name8_z` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, on the **Configuration**
tab, select **NOx**.

#### CO2

### **CO2 output port name** — Carbon dioxide `EoCO2` (default)

Carbon dioxide output port name.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Name9` |
| **Values:** | `EoCO2` (default) |
| **Data Types:** | `character vector` |

#### Dependencies

To create this parameter, on the **Configuration**
tab, select **CO2**.

### **CO2 table** — Carbon dioxide `array`

Carbon dioxide table.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Name9_z` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, on the **Configuration**
tab, select **CO2**.

#### PM

### **PM output port name** — Particulate matter `EoPm` (default)

Particulate matter output port name.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Name10` |
| **Values:** | `EoPm` (default) |
| **Data Types:** | `character vector` |

#### Dependencies

To create this parameter, on the **Configuration**
tab, select **PM**.

### **PM table** — Particulate matter `array`

Particulate matter table.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Name10_z` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, on the **Configuration**
tab, select **PM**.

## Libraries

Powertrain Blockset / Propulsion / Combustion Engine Components / Core Engine

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Steady-state core engine model using lookup tables

The Mapped Core Engine block implements a steady-state core engine
model using power, air mass flow, fuel flow, exhaust temperature, efficiency, and
emission performance lookup tables. You can use the block for:

- Hardware-in-the-loop (HIL) engine control design.
- Vehicle-level fuel economy and performance simulations.

The block enables you to specify lookup tables for these engine characteristics. The
lookup tables are functions of engine load, *L*, and engine speed
*N*. If you select **Input engine
temperature**, the tables are also a function of engine temperature,
*T*.

- Power
- Air
- Fuel
- Temperature
- Efficiency
- Emissions

  - Hydrocarbon (HC)
  - Carbon monoxide (CO)
  - Nitric oxide and nitrogen dioxide (NOx)
  - Carbon dioxide (CO2)
  - Particulate matter (PM) emissions

To bound the Mapped Core Engine block output, the block does not
extrapolate the lookup table data.
