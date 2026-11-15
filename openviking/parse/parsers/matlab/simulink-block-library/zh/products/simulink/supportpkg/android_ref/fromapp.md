---
type: simulink-block
title: 'FromApp'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Advanced'
documentation_page: 'fromapp'
documentation_source_path: 'supportpkg/android_ref/fromapp.html'
language: zh-CN
chinese_source: worker-translation
---

# FromApp

## 端口

### 输出

### **Data** — 方法返回的数据 numeric array

该模块输出由 **Method name** 参数指定的方法所返回的数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Size** — 方法返回的数据大小 numeric scalar

该模块输出由 **Method name** 参数指定的方法所返回数据的大小。

**数据类型：** `double`

## 参数

### **Method name** — 方法名称 `'FromAppMethod'`（默认）| character array

输入 Android 应用中方法的名称。

### **Return type** — 方法返回的元素的数据类型 `uint8`（默认）| `int8` | `uint16` | `int16` | `uint32` | `int32` | `single` | `double`

选择由 **Method name** 参数指定的方法所返回元素的数据类型。

### **Data size (N)** — 方法返回的数据元素数 `32`（默认）|

输入方法每次运行时返回给模块的数据元素数。

### **Sample time** — 采样时间间隔 `0.1`（默认）| nonnegative scalar

指定模块读取 Android 应用中方法的频率。

**注意**

**Sample time** 的值越小，处理器需要在更短时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

Simulink Support Package for Android Devices / Advanced

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2014a 中引入**

## 描述

从应用的方法接收数据

使用 FromApp 模块从 Android® 应用中的方法接收数据。代码生成完成后，您可以修改生成的代码，以配置 **Method name**、**Data type** 和 **Data size (N)** 参数，使其与方法相匹配。

例如，考虑一个方法 `public int[] FromAppFcn()`，该方法每次运行时发送三个数据元素，这些元素的数据类型为 `int32`。在这种情况下，设置以下参数值。

- 将 **Method name** 设置为 `FromAppFcn`
- 将 **Data size** 设置为 `3`
- 将 **Data type** 设置为 `int32`

Android 应用中的方法必须发送此模块可以接受的数据类型。

**注意**

在未连接硬件的情况下进行仿真时，此模块不执行任何操作。有关详细信息，请参阅模块在仿真中产生零值或不执行任何操作。
