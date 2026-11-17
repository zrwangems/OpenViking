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
chinese_source: worker-translation
---

# Iddata Sink

## 端口
```yaml
ports:
- name: Input
  summary: iddata 对象的输入 标量 | 向量
  direction: input
  data_types: double
- name: Output
  summary: iddata 对象的输出 标量 | 向量
  direction: input
  data_types: double
```

### 输入

### **Input** — `iddata` 对象的输入 标量 | 向量

`iddata` 对象的输入，对于单输入数据指定为标量。对于具有 *Nu* 个输入的多通道数据，将 `Input` 指定为长度为 *Nu* 的向量。

**数据类型：** `double`

### **Output** — `iddata` 对象的输出 标量 | 向量

`iddata` 对象的输出，对于单输出数据指定为标量。对于具有 *Ny* 个输出的多通道数据，将 `Output` 指定为长度为 *Ny* 的向量。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: IDDATA Name
  summary: iddata 对象的名称 data（默认）| 变量名
  group: ''
- name: Sample Time
  summary: 采样时间（秒） 0.1（默认）| 有限正数
  group: ''
```

### **IDDATA Name** — `iddata` 对象的名称 `data`（默认）| 变量名

`iddata` 对象的名称，指定为 MATLAB 变量名。该对象以此名称导出到 MATLAB 工作区。

### **Sample Time** — 采样时间（秒） `0.1`（默认）| 有限正数

采样时间（秒），指定为有限正数。`iddata` 对象存储以您指定的采样时间采样的输入和输出信号。
## 所属库

System Identification Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2008a 中引入**

## 描述

将仿真数据作为 iddata 对象导出到 MATLAB 工作区

Iddata Sink 模块将仿真数据作为 `iddata` 对象导出到 MATLAB® 工作区。该对象存储以您指定的采样时间采样的输入和仿真输出信号。如果您从模型窗口仿真模型，该模块将对象导出到 MATLAB 基础工作区。如果您以编程方式仿真模型，该对象将导出到 MATLAB 调用者工作区。调用者工作区是调用当前正在运行的函数的函数的工作区。
