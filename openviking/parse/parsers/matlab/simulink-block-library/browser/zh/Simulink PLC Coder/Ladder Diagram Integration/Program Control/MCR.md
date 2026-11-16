---
type: simulink-block
title: 'MCR'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Program Control'
documentation_page: 'mcr'
documentation_source_path: 'ref/mcr.html'
language: zh-CN
chinese_source: worker-translation
---

# MCR

## 端口

### 输入

### **EnableIn** — 使能输入 off（默认）| on

控制模块的执行。**EnableIn** 反映该模块之前的梯级状态。如果该模块之前的梯级状态为 false，则 **EnableIn** 为 false，模块不执行，并且输出不会更新。
### 输出

### **EnableOut** — 使能输出 off（默认）| on

当模块执行时，它会自动将 **EnableOut** 设置为 false。这会禁用该梯级上所有后续模块。

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

主控复位

MCR 模块实现 `MCR` 指令。该模块模拟一个主控继电器，可以选择性地禁用一段梯级。
