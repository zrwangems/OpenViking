---
type: simulink-block
title: 'Custom Instruction'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Custom PLC Instruction'
documentation_page: 'custominstruction'
documentation_source_path: 'ref/custominstruction.html'
language: zh-CN
chinese_source: worker-translation
---

# Custom Instruction

## 端口

### 输入

### **EnableIn** — 使能输入 off（默认） | on

**EnableIn** 端口控制模块的执行，并且还反映模块之前的梯级状态。如果模块之前的梯级状态为 false，则 **EnableIn** 信号设置为 false，模块不执行自定义逻辑，并且输出不会更新。

### **src** — 输入信号 scalar

输入到 Custom Instruction 模块的输入信号。

**数据类型：** `int8` | `int16` | `int32` | `single`

### 输出

### **EnableOut** — 使能输出 off（默认） | on

如果模块的 **EnableIn** 输入为 false，则模块实现的自定义逻辑不会执行，并且 **EnableOut** 信号设置为 false。如果 **EnableIn** 为 true 并且自定义指令执行，则 **EnableOut** 信号设置为 true。

## 参数

### 输入和输出

### **指令名称** — 用户定义梯形图逻辑指令的名称 sampleBlock（默认） | character vector

要创建的梯形图逻辑指令的名称。Rockwell Automation® Studio 5000 IDE 必须支持该梯形图逻辑指令名称。

### **输入数量** — 模块的输入信号数量 1（默认） | scalar

为您的自定义梯形图逻辑指令所需的模块输入信号数量。

#### 编程用法

|  |
| --- |
| **模块参数**：`NumInputs` |
| **类型**：scalar |
| **值**：scalar |
| **默认值**：`1` |

**数据类型：** `int8` | `int16` | `int32` | `single`

### **输入类型** — 输入信号的数据类型 `{{'SINT', 'INT','DINT','REAL'}}`（默认） | character vector

输入信号的数据类型，指定为元胞数组。对于多个输入信号，将数据类型指定为每个信号的元胞数组的逗号分隔列表。例如，如果有两个具有相同数据类型的输入信号，则将 **输入类型** 指定为 `{{'SINT','INT','DINT','REAL'},{'SINT','INT','DINT','REAL'}}`。

#### 编程用法

|  |
| --- |
| **模块参数**：`InputTypeList` |
| **类型**：cell array |
| **值**：cell array |
| **默认值**：`{{'SINT','INT','DINT','REAL'}}` |

**数据类型：** `character vector`

### **输出数量** — 模块的输出信号数量 1（默认） | scalar

来自用户定义 Custom Instruction 模块的输出信号数量。

#### 编程用法

|  |
| --- |
| **模块参数**：`NumOutputs` |
| **类型**：scalar |
| **值**：scalar |
| **默认值**：`1` |

**数据类型：** `int8` | `int16` | `int32` | `single`

### **输出类型** — 输出信号的数据类型 `{{'SINT', 'INT','DINT','REAL'}}`（默认） | character vector

输出信号的数据类型，指定为元胞数组。如果有多个输出信号，将数据类型指定为每个信号的元胞数组的逗号分隔列表。例如，如果有两个具有相同数据类型的输出信号，则将 **输出类型** 指定为 `{{'SINT','INT','DINT','REAL'},{'SINT','INT','DINT','REAL'}}`。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutputTypeList` |
| **类型**：cell array |
| **值**：cell array |
| **默认值**：`{{'SINT','INT','DINT','REAL'}}` |

**数据类型：** `character vector`

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2020a 中引入**

## 描述

创建自定义梯形图逻辑指令

Custom Instruction 模块为梯形图模型实现用户定义指令。当梯级条件为 true 时，模块执行指定的自定义逻辑。您可以将这些指令保存在名为 `plcuserlib.slx` 的用户定义库中。您还可以通过使用保存在 `plcuserlib.slx` 库中的自定义模块，导入、仿真和导出梯形图逻辑指令。
