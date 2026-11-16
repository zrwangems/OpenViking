---
type: simulink-block
title: 'MUL'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Math, Logical, and Comparison Operations'
documentation_page: 'mul'
documentation_source_path: 'ref/mul.html'
language: zh-CN
chinese_source: worker-translation
---

# MUL

## 端口

### 输入

### **EnableIn** — 使能输入 off（默认）| on

控制模块的执行。**EnableIn** 反映该模块之前的梯级状态。如果该模块之前的梯级状态为 false，**EnableIn** 为 false，模块不执行，输出也不更新。

### **srcA** — 第一个输入信号标量

乘法运算的第一个输入信号。

**数据类型：** `int8` | `int16` | `int32` | `single`

### **srcB** — 第二个输入信号标量

乘法运算的第二个输入信号。

**数据类型：** `int8` | `int16` | `int32` | `single`
### 输出

### **EnableOut** — 使能输出 off（默认）| on

默认情况下，**EnableOut** 跟随 **EnableIn** 的状态。如果到模块的 **EnableIn** 输入为 false，则模块实现的逻辑不执行，并且 **EnableOut** 信号设置为 false。

### **dest** — 输出信号标量

乘法运算产生的输出信号。

**数据类型：** `int8` | `int16` | `int32` | `single`

## 参数

未在 R2025b 中记录。

## 所属库

未在 R2025b 中记录。

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019a 中引入**

## 描述

输入相乘

MUL 模块实现 `MUL` 梯形逻辑指令。当梯级条件为 true 时，该模块将源 A（`srcA`）处的被乘数与源 B（`srcB`）处的乘数相乘，并将结果输出到目标（`dest`）。
