---
type: simulink-block
title: 'JMP'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Program Control'
documentation_page: 'jmp'
documentation_source_path: 'ref/jmp.html'
language: zh-CN
chinese_source: worker-translation
---

# JMP

## 端口

### 输入

### **EnableIn** — 使能输入 off（默认）| on

控制模块的执行。**EnableIn** 反映该模块之前的梯级状态。如果该模块之前的梯级状态为 false，则 **EnableIn** 为 false，模块不执行，并且输出不会更新。
### 输出

### **EN** — 使能输出 off（默认）| on

默认情况下，**EnableOut** 跟随 **EnableIn** 的状态。如果该模块的 **EnableIn** 输入为 false，则模块实现的逻辑不会执行，并且 **EnableOut** 信号设置为 false。

## 参数

### **跳转到标签** — 标签的名称 L（默认）| character vector

指定关联 `LBL` 指令的名称。

#### 编程使用

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

跳转

JMP 模块实现 `JMP` 梯形图逻辑指令。当梯级条件为 true 时，该模块跳过一部分梯形图逻辑，梯级执行将移动到由标签模块引用的模块。跳转模块只能跳过其后的梯级。该模块不支持向后跳转。
