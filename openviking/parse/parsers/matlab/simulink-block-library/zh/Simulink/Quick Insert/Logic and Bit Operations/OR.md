---
type: simulink-block
title: 'OR'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Quick Insert / Logic and Bit Operations'
documentation_page: 'or'
documentation_source_path: '../plccoder/ref/or.html'
language: zh-CN
chinese_source: worker-translation
---

# OR

## 端口

### 输入

### **EnableIn** — 启用输入 off (default) | on

控制模块的执行。**EnableIn** 反映该模块之前的梯级状态。如果该模块之前的梯级状态为 false，则 **EnableIn** 为 false，该模块不执行，且输出不会更新。

### **srcA** — 第一个输入信号标量

按位 OR 运算的第一个输入信号。如果数据类型为 `single`（`REAL` – 梯形逻辑等效），则输入值会转换为 `int32`（`DINT` – 梯形逻辑等效）。`int8, int16`（`SINT,INT` – 梯形逻辑等效）数据类型会通过用 0 填充高位转换为 `int32`（`DINT` – 梯形逻辑等效）。

**数据类型：** `int8` | `int16` | `int32` | `single`

### **srcB** — 第二个输入信号标量

按位 OR 运算的第二个输入信号。如果数据类型为 `single`（`REAL` – 梯形逻辑等效），则输入值会转换为 `int32`（`DINT` – 梯形逻辑等效）。`int8, int16`（`SINT,INT` – 梯形逻辑等效）数据类型会通过用 0 填充高位转换为 `int32`（`DINT` – 梯形逻辑等效）。

**数据类型：** `int8` | `int16` | `int32` | `single`
### 输出

### **EnableOut** — 启用输出 off (default) | on

默认情况下，**EnableOut** 跟随 **EnableIn** 的状态。如果到该模块的 **EnableIn** 输入为 false，则该模块实现的逻辑不执行，且 **EnableOut** 信号设置为 false。

### **dest** — 输出信号标量

按位 OR 运算产生的输出信号。如果数据类型为 `single`（`REAL` – 梯形逻辑等效），则所得的 `int32`（`DINT` – 梯形逻辑等效）会转换为 `REAL`（`single` – 梯形逻辑等效）。

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

按位 OR

OR 模块实现 `OR` 梯形逻辑指令。
当梯级条件为 true 时，该模块对源 A 处的值与源 B 处的值执行按位 OR 运算。此运算的结果在目标端口（`dest`）处提供。
