---
type: simulink-block
title: 'NOP'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Program Control'
documentation_page: 'nop'
documentation_source_path: 'ref/nop.html'
language: zh-CN
chinese_source: worker-translation
---

# NOP

## 端口

### 输入

### **EnableIn** — 启用输入 off（默认） | on

控制模块的执行。**EnableIn** 反映模块之前的梯级状态。如果模块之前的梯级状态为 false，则 **EnableIn** 为 false，模块不执行，输出也不会更新。

### 输出

### **EnableOut** — 启用输出 off（默认） | on

当模块执行时，它会自动将 **EnableOut** 设置为 false。这会禁用梯级上的所有后续模块。

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

无操作

NOP 模块实现 `NOP` 函数。该模块充当占位符。它在 enable 或 disable 时不执行任何操作。
