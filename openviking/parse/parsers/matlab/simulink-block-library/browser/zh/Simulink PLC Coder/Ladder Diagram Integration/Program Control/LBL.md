---
type: simulink-block
title: 'LBL'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Program Control'
documentation_page: 'lbl'
documentation_source_path: 'ref/lbl.html'
language: zh-CN
chinese_source: worker-translation
---

# LBL

## 端口

### 输入

### **EnableIn** — 启用输入 off（默认）| on

控制模块的执行。**EnableIn** 反映该模块之前的梯级状态。如果该模块之前的梯级状态为 false，**EnableIn** 为 false，则模块不执行，输出也不会更新。

### 输出

### **EN** — 启用输出 off（默认）| on

默认情况下，**EnableOut** 跟随 **EnableIn** 的状态。如果模块的 **EnableIn** 输入为 false，则该模块实现的逻辑不会执行，并且 **EnableOut** 信号设置为 false。

## 参数

### **Label** — 标签名称 L（默认）| character vector

指定 `LBL` 的名称。

#### 程序化使用

|  |
| --- |
| **模块参数**: `PLCLabelTag` |
| **类型**: character vector |
| **值**: character vector |
| **默认值**: `'L'` |

## 所属库

未在 R2025b 中记录。

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019a 中引入**

## 描述

标签

LBL 模块实现 `LBL` 梯形图逻辑指令。此模块与 JMP 模块一起使用。梯级执行会跳转到由 LBL 模块引用的模块。LBL 应是梯级中的第一条指令。
