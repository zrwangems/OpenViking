---
type: simulink-block
title: 'LEQ'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Math, Logical, and Comparison Operations'
documentation_page: 'leq'
documentation_source_path: 'ref/leq.html'
language: zh-CN
chinese_source: worker-translation
---

# LEQ

## 端口

### 输入

### **EnableIn** — 使能输入 off（默认） | on

控制模块的执行。**EnableIn** 反映模块之前的梯级状态。如果模块之前的梯级状态为 false，则 **EnableIn** 为 false，模块不执行，并且输出不会更新。

### **srcA** — 第一个输入信号标量

要对照 `srcB` 测试的值。

**数据类型：** `int8` | `int16` | `int32` | `single`

### **srcB** — 第二个输入信号标量

要对照 `srcA` 测试的值。

**数据类型：** `int8` | `int16` | `int32` | `single`
### 输出

### **EnableOut** — 使能输出 off（默认） | on

如果模块的 **EnableIn** 输入为 false，则模块实现的逻辑不会执行，并且 **EnableOut** 信号设置为 false。如果 **EnableIn** 为 true，那么当 `srcA` 小于或等于 `srcb` 时，**EnableOut** 信号设置为 true。

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

小于或等于

LEQ 模块实现 `LEQ` 指令。当梯级条件为 true 时，模块验证源 A 处的值是否小于或等于源 B 处的值。
