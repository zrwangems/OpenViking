---
type: simulink-block
title: 'Deep Learning HDL Single To Int8 Conversion'
family: 'deep-learning-hdl'
product_id: 'deep-learning-hdl'
product_name: 'Deep Learning HDL Toolbox'
documentation_release: R2025b
official_category: 'System Integration of Deep Learning Processor IP Core'
documentation_page: 'deeplearninghdlsingletoint8conversion'
documentation_source_path: 'ref/deeplearninghdlsingletoint8conversion.html'
language: zh-CN
chinese_source: worker-translation
---

# Deep Learning HDL Single To Int8 Conversion

## 端口

### 输入

### **Input Data** — 单精度输入数据，标量 | 向量

单精度输入数据，指定为标量或向量。

**数据类型：** `single`

### **Exponent** — 转换指数，标量

转换指数，指定为标量。必须将此输入端口连接到 Constant 模块。Constant 模块的值必须是 `getSingleToInt8ConversionExponent` 方法的输出。

**数据类型：** `int8`

### **ValidIn** — 有效信号，标量

有效信号，指定为 Boolean 标量。

**数据类型：** `Boolean`

### 输出

### **Out** — 8 位有符号整数数据，标量 | 向量

以 `int8` 数据类型标量或向量形式返回的 8 位整数数据。

**数据类型：** `int8`

### **ValidOut** — 有效信号，标量

有效信号，以 Boolean 标量形式返回。

**数据类型：** `Boolean`

## 参数

R2025b 中未记录。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024b 中引入**

## 描述

将单精度数据转换为 8 位有符号整数数据

Deep Learning HDL Single To Int8 Conversion 模块将单精度数据转换为 8 位有符号整数数据。要添加该模块，请在 MATLAB® 命令行中输入：

    open_system("dlhdlutils")
