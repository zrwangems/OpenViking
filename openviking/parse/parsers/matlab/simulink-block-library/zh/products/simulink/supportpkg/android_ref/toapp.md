---
type: simulink-block
title: 'ToApp'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Advanced'
documentation_page: 'toapp'
documentation_source_path: 'supportpkg/android_ref/toapp.html'
language: zh-CN
chinese_source: worker-translation
---

# ToApp

## 端口

### 输入

### **Port\_1** — 要发送到方法 `argn` 的数据，其中 *n* 是参数数目

该模块输入要发送到 Android 应用中某个方法的数据。该数据由 **Method name** 参数指定的方法作为输入接收。模块的输入端口数目取决于输入参数数目。例如，如果将 **Number of arguments** 参数设置为 `2`，则可以将 `arg1` 和 `arg2` 作为输入参数传递给 Android 应用中的方法。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

### **Method name** — Android 应用中方法的名称 `ToAppMethod`（默认）| 字符向量

输入 Android 应用中方法的名称。

### **Number of arguments** — 方法的参数数目 `1`（默认）| `2` | `3` | `4` | `5`

选择 Android 应用中方法的参数数目。选择的参数数目将作为输入端口添加到模块。

## 所属库

Simulink Support Package for Android Devices / Advanced

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014a 中引入**

## 描述

将数据发送到应用的方法

使用 ToApp 模块将数据发送到 Android® 应用中的指定方法。该方法必须存在于默认 Activity 中。例如，假设模块输入为 `int32(ones(3,1))`，方法名称为 `ToAppFcn`。那么，Android 应用中预期的方法为：

```
public void ToAppFcn(int[] inData)
```

其中 `inData` 是包含三个元素的整数数组。

**注意**

在没有连接硬件的仿真期间，该模块不执行任何操作。有关详细信息，请参阅《模块在仿真中产生零值或不执行任何操作》。
