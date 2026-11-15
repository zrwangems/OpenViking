---
type: simulink-block
title: 'Deep Learning HDL Int8 To Single Conversion'
family: 'deep-learning-hdl'
product_id: 'deep-learning-hdl'
product_name: 'Deep Learning HDL Toolbox'
documentation_release: R2025b
official_category: 'System Integration of Deep Learning Processor IP Core'
documentation_page: 'deeplearninghdlint8tosingleconversion'
documentation_source_path: 'ref/deeplearninghdlint8tosingleconversion.html'
language: zh-CN
chinese_source: worker-translation
---

# Deep Learning HDL Int8 To Single Conversion

## 端口

### 输入

### **Input Data** — 8 位有符号整数数据标量 | 向量

指定为 `int8` 数据类型的标量或向量的 8 位有符号整数数据。

**数据类型：** `int8`

### **Exponent** — 转换指数标量

转换指数，指定为标量。必须将此输入端口连接到 Constant 模块。Constant 模块的值必须是 `getInt8ToSingleConversionExponent` 方法的输出。

**数据类型：** `int8`

### **ValidIn** — 有效信号标量

有效信号，指定为 Boolean 标量。

**数据类型：** `Boolean`
### 输出

### **Out** — 单精度数据标量 | 向量

单精度数据，返回为 `single` 数据类型的标量或向量。

**数据类型：** `single`

### **ValidOut** — 有效信号标量

有效信号，返回为 Boolean 标量。

**数据类型：** `Boolean`

## 参数

在 R2025b 中未记录。

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2024b 中引入**

## 描述

将 8 位有符号整数数据转换为单精度数据

Deep Learning HDL Int8 To Single Conversion 模块将 8 位有符号整数数据转换为单精度数据。要添加该模块，请在 MATLAB® 命令行中输入：

```
open_system("dlhdlutils")
```
