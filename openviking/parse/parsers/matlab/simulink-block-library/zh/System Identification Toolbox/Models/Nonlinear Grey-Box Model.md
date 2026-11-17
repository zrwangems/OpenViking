---
type: simulink-block
title: 'Nonlinear Grey-Box Model'
family: 'ident'
product_id: 'ident'
product_name: 'System Identification Toolbox'
documentation_release: R2025b
official_category: 'Models'
documentation_page: 'nonlineargreyboxmodel'
documentation_source_path: 'ref/nonlineargreyboxmodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Nonlinear Grey-Box Model

## 端口

R2025b 中未记录。

## 参数

**IDNLGREY model**
:   MATLAB® 工作区中 `idnlgrey` 变量的名称。

**Initial state**
:   将初始状态指定为以下之一：

    - `'z'`：指定为零，对应于从静止开始的系统。
    - `'m'`：指定模型的内部初始状态。
    - 大小等于 `idnlgrey` 对象中状态数的向量。
    - 初始状态结构体数组。有关创建此结构体的信息，请在 MATLAB 命令窗口中键入 `help idnlgrey/sim`。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2008a 中引入**

## 描述

在 Simulink 软件中仿真非线性灰箱模型

仿真非线性灰箱（`idnlgrey`）模型系统。

### 输入

模型的输入信号。

### 输出

模型的输出信号。
