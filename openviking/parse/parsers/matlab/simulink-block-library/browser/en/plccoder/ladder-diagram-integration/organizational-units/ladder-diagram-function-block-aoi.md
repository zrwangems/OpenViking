---
type: simulink-block
title: 'Ladder Diagram Function Block (AOI)'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Organizational Units'
documentation_page: 'functionblockaoi'
documentation_source_path: 'ref/functionblockaoi.html'
language: en
---

# Ladder Diagram Function Block (AOI)

## Ports

### Input

### **EnableIn** — Enable Input off (default) | on

The **EnableIn** port controls the execution of the block and
reflects the rung state preceding the block. If the rung state preceding the block is
false, the **EnableIn** signal is set to false, the block does not
execute the custom logic, and the outputs are not updated.
### Output

### **EnableOut** — Enable Output off (default) | on

If the **EnableIn** input to the block is false, the custom
logic implemented by the block is not executed and the **EnableOut**
signal is set to false. If **EnableIn** is true and the custom
instruction executes, the **EnableOut** signal is set to true.

## Parameters

### Inputs and Outputs

### **Function Block Name** — Name of AOI FB (default) | character vector

Name of the AOI function block that you want to create. The Rockwell Automation® Studio 5000 IDE must support the ladder logic instruction name.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PLCPOUName` |
| **Type**: character vector |
| **Value**: character vector |
| **Default**: `'FB'` |

### **Block Data Tag** — Name of the AOI instance D (default) | character vector

Name of the AOI instance that you want to generate code for or the instance name
for the imported AOI instruction. The Rockwell Automation Studio 5000 IDE must support the ladder logic instruction name.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PLCOperandTag` |
| **Type**: character vector |
| **Value**: character vector |
| **Default**: `'D'` |

### **Variable Table** — Open AOI variable table Boolean

Button that opens the AOI variable table.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PLCEditVariableSS` |
| **Type**: button |

### **Logic Routine** — Open AOI ladder logic Boolean

Button that opens the ladder logic routine to implement the AOI ladder
logic.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PLCEditPOU` |
| **Type**: button |

### **Allow EnableInFalse Routine** — Enable `EnableInFalse` routine ladder logic Boolean

Check box that you select to enable the ladder logic inside the
`EnableInFalse` routine.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PLCAllowEnableInFalse` |
| **Type**: check-box |

### **EnableInFalse Routine** — Open `EnableInFalse` routine ladder logic Boolean

Button that opens the ladder logic routine to implement the AOI
`EnableInFalse` ladder logic.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PLCEditEnableInFalse` |
| **Type**: button |

### **Allow Prescan Routine** — Enable `Prescan` routine ladder logic Boolean

Check box that you select to enable the ladder logic inside the
`Prescan` routine.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PLCAllowPrescan` |
| **Type**: check-box |

### **Prescan Routine** — Open `Prescan` routine ladder logic Boolean

Button that opens the ladder logic routine to implement the AOI
`Prescan` ladder logic.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PLCEditPrescan` |
| **Type**: button |

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Ladder Diagram Function Block (AOI)

The Ladder Diagram function block is a standalone, organizational unit. Use this block in
the absence of a general hierarchy of controller, task, program, and ladder diagram. It is
also called an AOI block. The Ladder Diagram function block consists of a ladder diagram and
function block variables. The function block variables represent the function variables used
in the ladder diagram and provide information about its data types, size, and initial
value.
