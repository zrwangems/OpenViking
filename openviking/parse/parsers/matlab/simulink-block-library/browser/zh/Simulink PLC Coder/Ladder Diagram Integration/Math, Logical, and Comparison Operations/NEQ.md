---
type: simulink-block
title: 'NEQ'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Math, Logical, and Comparison Operations'
documentation_page: 'neq'
documentation_source_path: 'ref/neq.html'
language: zh-CN
chinese_source: worker-translation
---

# NEQ

## 端口

### 输入

### **EnableIn** — 使能输入 off (默认) | on

控制该模块的执行。**EnableIn** 反映该模块之前的梯级状态。如果该模块之前的梯级状态为 false，则 **EnableIn** 为 false，模块不执行，输出也不更新。

### **srcA** — 第一个输入信号标量

要与 `srcB` 进行比较测试的值。

**数据类型：** `int8` | `int16` | `int32` | `single`

### **srcB** — 第二个输入信号标量

要与 `srcA` 进行比较测试的值。

**数据类型：** `int8` | `int16` | `int32` | `single`

### 输出

### **EnableOut** — 使能输出 off (默认) | on

如果该模块的 **EnableIn** 输入为 false，则该模块实现的逻辑不执行，且 **EnableOut** 信号设置为 false。如果 **EnableIn** 为 true，则当 `srcA` 不等于 `srcb` 时，**EnableOut** 信号设置为 true。

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

不等于

NEQ 模块实现 `NEQ` 指令。当梯级条件为 true 时，该模块验证源 A 处的值是否不等于源 B 处的值。
