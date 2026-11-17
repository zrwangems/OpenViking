---
type: simulink-block
title: 'LIN Pack'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'LIN'
documentation_page: 'linpack'
documentation_source_path: 'io_ref/linpack.html'
language: zh-CN
chinese_source: worker-translation
---

# LIN Pack

## 端口
```yaml
ports:
- name: in
  summary: 要打包数据的输入数据
  direction: input
- name: lin_data
  summary: 输出 LIN 数据 LIN 数据
  direction: output
```

### 输入

### **in** — 要打包数据的输入数据

接收要为 LIN 打包的数据。输入端口数量根据所选帧进行分配。端口名称分配给每个端口。
### 输出

### **lin\_data** — 输出 LIN 数据 LIN 数据

发送打包后的 LIN 数据。
## 参数
```yaml
parameters:
- name: LDF File Name
  summary: LDF 的文件路径 empty (default) | character vector | string scalar
  group: ''
  block_parameter: LDFFileName
- name: Select Frame
  summary: LIN 帧 None (default) | character vector | string scalar
  group: ''
  block_parameter: selectedFrameName
- name: Frame ID
  summary: LIN 帧 ID 1 (default) | uint8
  group: ''
  block_parameter: frameId
```

### **LDF File Name** — LDF 的文件路径 empty (default) | character vector | string scalar

提供 LDF 的文件路径。如果未设置此参数，则无法使用该模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`LDFFileName` |

### **Select Frame** — LIN 帧 `None` (default) | character vector | string scalar

从 LDF 中可用的选项中选择 LIN 帧。如果未选择 LDF，则该模块使用 `None`。

#### 编程使用

|  |
| --- |
| **模块参数**：`selectedFrameName` |

### **Frame ID** — LIN 帧 ID `1` (default) | uint8

从 LDF 中可用的选项中选择 LIN 帧 ID。如果未选择 LDF，则该模块使用 `1`。

#### 编程使用

|  |
| --- |
| **模块参数**：`frameId` |
## 所属库

Simulink Real-Time / LIN

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

通过使用 LIN 描述文件中的配置将信号打包到数据帧中

LIN Pack 模块通过使用 LIN 描述文件 (LDF) 中的配置将信号打包到数据帧中。本地互连网络 (LIN) 总线可以使用打包后的数据。LIN Pack 模块支持 LDF 版本 2.2 及更早版本。
