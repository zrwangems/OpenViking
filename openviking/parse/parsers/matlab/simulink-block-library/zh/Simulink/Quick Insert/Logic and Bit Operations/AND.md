---
type: simulink-block
title: 'AND'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Quick Insert / Logic and Bit Operations'
documentation_page: 'and'
documentation_source_path: '../plccoder/ref/and.html'
language: zh-CN
chinese_source: worker-translation
---

# AND

## 端口

### 输入

### **EnableIn** — 使能输入 off（默认）| on

控制模块的执行。**EnableIn** 反映模块之前的梯级状态。如果模块之前的梯级状态为 false，则 **EnableIn** 为 false，模块不执行，输出也不更新。

### **srcA** — 第一个输入信号 标量

按位 AND 运算的第一个输入信号。如果数据类型为 `single`（`REAL`——梯形图逻辑等效），输入值将转换为 `int32`（`DINT`——梯形图逻辑等效）。`int8, int16`（`SINT,INT`——梯形图逻辑等效）数据类型通过在高位填充 0 转换为 `int32`（`DINT`——梯形图逻辑等效）。

**数据类型：** `int8` | `int16` | `int32` | `single`

### **srcB** — 第二个输入信号 标量

按位 AND 运算的第二个输入信号。如果数据类型为 `single`（`REAL`——梯形图逻辑等效），输入值将转换为 `int32`（`DINT`——梯形图逻辑等效）。`int8, int16`（`SINT,INT`——梯形图逻辑等效）数据类型通过在高位填充 0 转换为 `int32`（`DINT`——梯形图逻辑等效）。

**数据类型：** `int8` | `int16` | `int32` | `single`
### 输出

### **EnableOut** — 使能输出 off（默认）| on

默认情况下，**EnableOut** 跟随 **EnableIn** 的状态。如果模块的 **EnableIn** 输入为 false，则模块实现的逻辑不执行，**EnableOut** 信号设置为 false。

### **dest** — 输出信号 标量

按位 AND 运算的输出信号。如果数据类型为 `single`（`REAL`——梯形图逻辑等效），结果 `int32`（`DINT`——梯形图逻辑等效）将转换为 `REAL`（`single`——梯形图逻辑等效）。

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

按位 AND

AND 模块实现 `AND` 梯形图逻辑指令。当梯级条件为 true 时，模块对源 A 的值与源 B 的值执行按位 AND 运算。该运算的结果可在目标端口（`dest`）处获得。
