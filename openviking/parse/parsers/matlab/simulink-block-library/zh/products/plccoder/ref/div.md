---
type: simulink-block
title: 'DIV'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Math, Logical, and Comparison Operations'
documentation_page: 'div'
documentation_source_path: 'ref/div.html'
language: zh-CN
chinese_source: worker-translation
---

# DIV

## 端口

### 输入

### **EnableIn** — 使能输入 off (默认) | on

控制模块的执行。**EnableIn** 反映模块之前的梯级状态。如果模块之前的梯级状态为 false，则 **EnableIn** 为 false，模块不执行且输出不会更新。

### **srcA** — 第一个输入信号（标量）

除法运算的第一个输入信号。

**数据类型：** `int8` | `int16` | `int32` | `single`

### **srcB** — 第二个输入信号（标量）

除法运算的第二个输入信号。

**数据类型：** `int8` | `int16` | `int32` | `single`
### 输出

### **EnableOut** — 使能输出 off (默认) | on

默认情况下，**EnableOut** 跟随 **EnableIn** 的状态。如果模块的 **EnableIn** 输入为 false，则模块实现的逻辑不会执行，并且 **EnableOut** 信号设置为 false。

### **dest** — 输出信号（标量）

除法运算产生的输出信号。

**数据类型：** `int8` | `int16` | `int32` | `single`

## 参数

R2025b 中未记录。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

将一个输入除以另一个输入

DIV 模块实现 `DIV` 梯形逻辑指令。当梯级条件为 true 时，模块将源 A（`srcA`）处的被除数除以源 B（`srcB`）处的除数，并将结果输出到目标（`dest`）。

**注意**

如果执行除以零运算，则在代码生成期间会生成一条 `"Divide by zero detected"` 诊断消息。
