---
type: simulink-block
title: 'SUB'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Math, Logical, and Comparison Operations'
documentation_page: 'sub'
documentation_source_path: 'ref/sub.html'
language: zh-CN
chinese_source: worker-translation
---

# SUB

## 端口

### 输入

### **EnableIn** — 使能输入 off（默认）| on

控制模块的执行。**EnableIn** 反映模块之前的梯级状态。如果模块之前的梯级状态为 false，则 **EnableIn** 为 false，模块不执行，输出也不会更新。

### **srcA** — 第一个输入信号（标量）

减法运算的第一个输入信号。

**数据类型：** `int8` | `int16` | `int32` | `single`

### **srcB** — 第二个输入信号（标量）

减法运算的第二个输入信号。

**数据类型：** `int8` | `int16` | `int32` | `single`
### 输出

### **EnableOut** — 使能输出 off（默认）| on

默认情况下，**EnableOut** 跟随 **EnableIn** 的状态。如果该模块的 **EnableIn** 输入为 false，则不执行该模块实现的逻辑，并将 **EnableOut** 信号设置为 false。

### **dest** — 输出信号（标量）

减法运算产生的输出信号。

**数据类型：** `int8` | `int16` | `int32` | `single`

## 参数

在 R2025b 中未记录。

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

输入相减

SUB 模块实现 `SUB` 梯形图逻辑指令。当梯级条件为 true 时，该模块从源 A（`srcA`）中减去源 B（`srcB`），并将结果输出到目标（`dest`）。
