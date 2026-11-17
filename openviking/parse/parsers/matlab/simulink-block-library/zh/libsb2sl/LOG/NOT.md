---
type: simulink-block
title: 'NOT'
family: 'libsb2sl'
product_id: 'libsb2sl'
product_name: 'libsb2sl'
documentation_release: R2025b
official_category: 'LOG'
documentation_page: 'not'
documentation_source_path: '../plccoder/ref/not.html'
language: zh-CN
chinese_source: worker-translation
---

# NOT

## 端口

### 输入

### **EnableIn** — 使能输入 off（默认）| on

控制模块的执行。**EnableIn** 反映模块之前的梯级状态。如果模块之前的梯级状态为 false，则 **EnableIn** 为 false，模块不执行，输出也不会更新。

### **src** — 输入信号 标量

要对其执行按位 NOT 运算的输入信号。如果数据类型为 `single`（`REAL`——梯形图逻辑等效类型），则输入值转换为 `int32`（`DINT`——梯形图逻辑等效类型）。`int8, int16`（`SINT,INT`——梯形图逻辑等效类型）数据类型通过在高位填充 0 转换为 `int32`（`DINT`——梯形图逻辑等效类型）。

**数据类型：** `int8` | `int16` | `int32` | `single`
### 输出

### **EnableOut** — 使能输出 off（默认）| on

默认情况下，**EnableOut** 跟随 **EnableIn** 的状态。如果模块的 **EnableIn** 输入为 false，则模块实现的逻辑不执行，**EnableOut** 信号设置为 false。

### **dest** — 输出信号 标量

按位 NOT 运算产生的输出信号。如果数据类型为 `single`（`REAL`——梯形图逻辑等效类型），则结果 `int32`（`DINT`——梯形图逻辑等效类型）转换为 `REAL`（`single`——梯形图逻辑等效类型）。

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

按位 NOT

NOT 模块实现 `NOT` 梯形图逻辑指令。当梯级条件为 true 时，模块对源处的值执行按位 NOT 运算。此运算的结果可在目标端口（`dest`）处获得。
