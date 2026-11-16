---
type: simulink-block
title: 'CLR'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Memory and File Operations'
documentation_page: 'clr'
documentation_source_path: 'ref/clr.html'
language: zh-CN
chinese_source: worker-translation
---

# CLR

## 端口

### 输入

### **EnableIn** — 启用输入 off (默认) | on

控制模块的执行。**EnableIn** 反映模块之前的梯级状态。如果模块之前的梯级状态为 false，则 **EnableIn** 为 false，模块不执行，且输出不会更新。

### 输出

### **EnableOut** — 启用输出 off (默认) | on

默认情况下，**EnableOut** 跟随 **EnableIn** 的状态。如果模块的 **EnableIn** 输入为 false，则不执行该模块实现的逻辑，并将 **EnableOut** 信号设置为 false。

## 参数

### **Data To Clear** — 操作数数据 A (默认) | boolean

指定要清除的数据位。数据位以 `tags` 格式指定。在梯形图中，标签（变量）用于表示输入、输出和内部存储器，并具有诸如 `Data Type`、`Initial Value` 和 `size` 等属性。要更改 `Data To Clear` 的属性，请在 Ladder Diagram Program 模块中打开 **Program Variables** 表。

#### 编程用法

|  |
| --- |
| **模块参数**: `PLCOperandTag` |
| **类型**: character vector |
| **值**: character vector |
| **默认值**: `'A'` |

## 所属库

未在 R2025b 中记录。

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019a 中引入**

## 描述

清除

CLR 模块实现 `CLR` 梯形图逻辑指令。当梯级条件为 true 时，该模块清除 `Data To Clear` 标签中指定的位。
