---
type: simulink-block
title: 'Iddata Sink'
family: 'ident'
product_id: 'ident'
product_name: 'System Identification Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'iddatasink'
documentation_source_path: 'ref/iddatasink.html'
language: zh-CN
chinese_source: official
---

# Iddata Sink

## 端口

### 输入

### **Input** — `iddata` 对象的输入 标量 | 向量

`iddata` 对象的输入，指定为单输入数目据的标量。对于具有 *Nu* 输入的多通道数据，将 `Input` 指定为长度为 *Nu* 的向量。

**数据类型:** `double`

### **Output** — `iddata` 对象的输出 标量 | 向量

`iddata` 对象的输出，指定为单输出数目据的标量。对于具有 *Ny* 输出的多通道数据，将 `Output` 指定为长度为 *Ny* 的向量。

**数据类型:** `double`

## 参数

### **IDDATA Name** — `iddata` 对象的名称 `data` (默认) | 变量名称

`iddata` 对象的名称，指定为 MATLAB 变量名称。该对象以此名称导出到 MATLAB 工作区。

### **采样时间** — 采样时间（以秒为单位） `0.1` (默认) | 有限正数

以秒为单位的采样时间，指定为有限正数。`iddata` 对象存储在您指定的采样时间采样的输入和输出信号。

## 所属库

System Identification Toolbox

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2008a 中推出**

## 描述

将仿真数据作为 iddata 对象导出到 MATLAB 工作区

Iddata Sink 模块将仿真数据作为 `iddata` 对象导出到 MATLAB® 工作区。该对象存储在您指定的采样时间采样的输入和仿真输出信号。如果您从模型窗口仿真您的模型，则该模块会将对象导出到 MATLAB 基础工作区。如果您以编程方式仿真模型，则对象将被导出到 MATLAB 调用方工作区。调用方工作区是调用当前正在运行的函数的函数的工作区。
