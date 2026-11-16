---
type: simulink-block
title: 'Iddata Source'
family: 'ident'
product_id: 'ident'
product_name: 'System Identification Toolbox'
documentation_release: R2025b
official_category: 'Data Preparation / Represent Data'
documentation_page: 'iddatasource'
documentation_source_path: 'ref/iddatasource.html'
language: zh-CN
chinese_source: worker-translation
---

# Iddata Source

## 端口

### Output

### **Input** — 存储在 `iddata` 对象中的输入数据 标量 | 向量

存储在 `iddata` 对象中的输入数据，对于单输入数据，返回为标量；对于具有 *Nu* 个输入的多通道数据，返回为长度为 *Nu* 的向量。如果 `z` 是 `iddata` 对象，则在仿真时间 *t* 时此端口的输出为 *t* 时刻的 `z.InputData`。如果 *t* 大于 `z.SamplingInstants(end)`（即 `z` 中的最大时间），则对于每个输入通道，输入数据返回为 `0`。

**数据类型：** `double`

### **Output** — 存储在 `iddata` 对象中的输出数据 标量 | 向量

存储在 `iddata` 对象中的输出数据，对于单输出数据，返回为标量；对于具有 *Ny* 个输出的多通道数据，返回为长度为 *Ny* 的向量。如果 `z` 是 `iddata` 对象，则在仿真时间 *t* 时此端口的输出为 *t* 时刻的 `z.OutputData`。如果 *t* 大于 `z.SamplingInstants(end)`（即 `z` 中的最大时间），则对于每个输出通道，输出数据返回为 `0`。

**数据类型：** `double`

## 参数

### **IDDATA object** — 要导入的时域数据 `iddata(1,1)`（默认）| `iddata` 对象

要导入的时域数据，指定为在 MATLAB 工作区中创建的 `iddata` 对象。`iddata` 对象必须仅包含一个实验。对于多实验 `iddata` 对象 `z`，要为实验编号 `kexp` 指定 `iddata` 对象，请将 **IDDATA object** 指定为 `getexp(z,kexp)`。

### **Start time** — `iddata` 对象中信号的起始时间 `-1`（默认）| 非负实数标量

`iddata` 对象中信号的起始时间，指定为 `-1` 或非负实数标量。默认值 `-1` 表示此起始时间与 Simulink 模型的起始时间匹配。要将信号的起始时间指定为与 `iddata` 对象的起始时间相同，请将 **Start time** 设置为 `data.Tstart`，其中 `data` 是 `iddata` 对象。

## 所属库

System Identification Toolbox

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

导入存储在 MATLAB 工作区中 iddata 对象内的时域数据

Iddata Source 模块导入存储在 MATLAB® 工作区中 `iddata` 对象内的输入-输出时域数据。您可以使用此模块导入数据，以在 Simulink® 中仿真模型。
