---
type: simulink-block
title: 'Array Processing'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Modeling / Design Model Behavior / Iterator Subsystems'
documentation_page: 'arrayprocessing'
documentation_source_path: 'slref/arrayprocessing.html'
language: zh-CN
chinese_source: worker-translation
---

# Array Processing

## 端口

在 R2025b 中未记录。

## 参数

在 R2025b 中未记录。

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成：使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成：使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

**限制**

- 如果 Array Processing Subsystem 模块位于模型的顶层，则该模块不支持 HDL 代码生成。
- 如果模型未选择 **Enable frame to sample conversion (HDL Coder)** 模型配置参数，则 Array Processing Subsystem 模块不支持 HDL 代码生成。

## 版本历史

**在 R2024a 中引入**

## 描述

用于 Array Processing Subsystem 的控制模块

Array Processing 模块用作 Array Processing Subsystem 模块的控制模块。Array Processing Subsystem 模块将算法应用于输入矩阵的每个元素，并返回一个输出矩阵，该矩阵包含该算法针对输入矩阵每个元素的输出，类似于 `arrayfun` 函数和 For Each Subsystem 模块。

Array Processing Subsystem 模块针对大型输入矩阵（如图像数据）进行了优化。对于高性能逐元素运算（如图像处理任务），请使用 Array Processing Subsystem 模块。
