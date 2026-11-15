---
type: simulink-block
title: 'Ladder Diagram Subroutine'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Organizational Units'
documentation_page: 'subroutine'
documentation_source_path: 'ref/subroutine.html'
language: zh-CN
chinese_source: worker-translation
---

# Ladder Diagram Subroutine

## 端口

### 输入

### **EnableIn** — 使能输入 off（默认） | on

控制模块的执行。**EnableIn** 反映该模块之前的梯级状态。如果该模块之前的梯级状态为 false，则 **EnableIn** 为 false，模块不会执行，并且输出不会更新。
### 输出

### **EnableOut** — 使能输出 off（默认） | on

默认情况下，**EnableOut** 跟随 **EnableIn** 的状态。如果模块的 **EnableIn** 输入为 false，则模块实现的逻辑不会执行，且 **EnableOut** 信号设置为 false。

## 参数

### **例程名称** — 例程的名称 R（默认） | character vector

指定梯形图逻辑子例程的名称。

#### 编程用法

|  |
| --- |
| **模块参数**: `PLCPOUName` |
| **类型**: character vector |
| **值**: character vector |
| **默认值**: `'R'` |

### **例程逻辑** — 打开梯形图逻辑 boolean

用于打开梯形图逻辑子例程的按钮。

#### 编程用法

|  |
| --- |
| **模块参数**: `PLCOpenRoutine` |
| **类型**: 按钮 |

## 所属库

未在 R2025b 中记录。

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019a 中引入**

## 描述

Ladder Diagram Subroutine

Ladder Diagram Subroutine 允许您创建并定义命名的梯形图逻辑例程。您可以通过点击此模块的模块参数菜单下的 `Routine Logic` 按钮，编辑由该子例程实现的逻辑。
