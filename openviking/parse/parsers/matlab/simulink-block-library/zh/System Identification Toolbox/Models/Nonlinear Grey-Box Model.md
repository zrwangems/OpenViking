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
chinese_source: official
---

# Nonlinear Grey-Box Model

## 端口

R2025b 官方文档未提供。

## 参数

**IDNLGREY model**
:   `idnlgrey` 变量在 MATLAB® 工作区中的名称。

**初始状态**
:   初始状态应为以下之一：

    - `'z'`:指定零，这对应于系统从静止开始。
    - `'m'`:指定模型的内部初始状态。
    - 大小等于 `idnlgrey` 对象中状态数量的向量。
    - 初始状态结构体数组。要了解创建此结构的信息，请在 MATLAB 命令行窗口中输入 `help idnlgrey/sim`。

## 所属库

R2025b 官方文档未提供。

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2008a 中推出**

## 描述

在 Simulink 软件中仿真非线性灰箱模型

仿真非线性灰箱 (`idnlgrey`) 模型的系统。

### 输入

模型的输入信号。

### 输出

模型的输出信号。
