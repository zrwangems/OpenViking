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
language: zh-CN
chinese_source: worker-translation
---

# Ladder Diagram Function Block (AOI)

## 端口

### 输入

### **EnableIn** — 使能输入 off（默认）| on

**EnableIn** 端口控制模块的执行，并反映模块之前的梯级状态。如果模块之前的梯级状态为 false，则 **EnableIn** 信号设置为 false，模块不执行自定义逻辑，并且输出不会更新。
### 输出

### **EnableOut** — 使能输出 off（默认）| on

如果模块的 **EnableIn** 输入为 false，则不执行该模块实现的自定义逻辑，并且 **EnableOut** 信号设置为 false。如果 **EnableIn** 为 true 且自定义指令执行，则 **EnableOut** 信号设置为 true。

## 参数

### 输入和输出

### **功能块名称** — AOI FB 的名称（默认）| character vector

要创建的 AOI 功能块的名称。Rockwell Automation® Studio 5000 IDE 必须支持该梯形图逻辑指令名称。

#### 编程用法

|  |
| --- |
| **模块参数**：`PLCPOUName` |
| **类型**：character vector |
| **值**：character vector |
| **默认**：`'FB'` |

### **模块数据标签** — AOI 实例的名称 D（默认）| character vector

要为其生成代码的 AOI 实例的名称，或导入的 AOI 指令的实例名称。Rockwell Automation Studio 5000 IDE 必须支持该梯形图逻辑指令名称。

#### 编程用法

|  |
| --- |
| **模块参数**：`PLCOperandTag` |
| **类型**：character vector |
| **值**：character vector |
| **默认**：`'D'` |

### **变量表** — 打开 AOI 变量表 Boolean

用于打开 AOI 变量表的按钮。

#### 编程用法

|  |
| --- |
| **模块参数**：`PLCEditVariableSS` |
| **类型**：button |

### **逻辑例程** — 打开 AOI 梯形图逻辑 Boolean

用于打开梯形图逻辑例程以实现 AOI 梯形图逻辑的按钮。

#### 编程用法

|  |
| --- |
| **模块参数**：`PLCEditPOU` |
| **类型**：button |

### **允许 EnableInFalse 例程** — 启用 `EnableInFalse` 例程的梯形图逻辑 Boolean

选中此复选框可启用 `EnableInFalse` 例程内部的梯形图逻辑。

#### 编程用法

|  |
| --- |
| **模块参数**：`PLCAllowEnableInFalse` |
| **类型**：check-box |

### **EnableInFalse 例程** — 打开 `EnableInFalse` 例程的梯形图逻辑 Boolean

用于打开梯形图逻辑例程以实现 AOI `EnableInFalse` 梯形图逻辑的按钮。

#### 编程用法

|  |
| --- |
| **模块参数**：`PLCEditEnableInFalse` |
| **类型**：button |

### **允许 Prescan 例程** — 启用 `Prescan` 例程的梯形图逻辑 Boolean

选中此复选框可启用 `Prescan` 例程内部的梯形图逻辑。

#### 编程用法

|  |
| --- |
| **模块参数**：`PLCAllowPrescan` |
| **类型**：check-box |

### **Prescan 例程** — 打开 `Prescan` 例程的梯形图逻辑 Boolean

用于打开梯形图逻辑例程以实现 AOI `Prescan` 梯形图逻辑的按钮。

#### 编程用法

|  |
| --- |
| **模块参数**：`PLCEditPrescan` |
| **类型**：button |

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

Ladder Diagram Function Block (AOI)

Ladder Diagram 功能块是一个独立的组织单元。在没有控制器、任务、程序和梯形图的通用层级结构时，可使用此模块。它也称为 AOI 块。Ladder Diagram 功能块由梯形图以及功能块变量组成。功能块变量表示梯形图中使用的功能变量，并提供有关其数据类型、大小和初始值的信息。
