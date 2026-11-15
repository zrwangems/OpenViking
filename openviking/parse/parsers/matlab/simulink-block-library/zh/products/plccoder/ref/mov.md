---
type: simulink-block
title: 'MOV'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Memory and File Operations'
documentation_page: 'mov'
documentation_source_path: 'ref/mov.html'
language: zh-CN
chinese_source: worker-translation
---

# MOV

## 端口

### 输入

### **EnableIn** — 启用输入 off (default) | on

控制模块的执行。**EnableIn** 反映该模块之前的梯级状态。如果该模块之前的梯级状态为 false，则 **EnableIn** 为 false，模块不执行，输出也不会更新。

### **src** — 输入信号标量

要移动的值。

**数据类型：** `int8` | `int16` | `int32` | `single`

### 输出

### **EnableOut** — 启用输出 off (default) | on

默认情况下，**EnableOut** 跟随 **EnableIn** 的状态。如果模块的 **EnableIn** 输入为 false，则该模块实现的逻辑不会执行，**EnableOut** 信号被设置为 false。

### **dest** — 输出信号标量

用于存储结果的标签。

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

**R2019a 中引入**

## 描述

移动

MOV 模块实现 `MOV` 指令。当梯级条件为真时，该模块将源的一个副本移动到目标，同时保持源不变。
