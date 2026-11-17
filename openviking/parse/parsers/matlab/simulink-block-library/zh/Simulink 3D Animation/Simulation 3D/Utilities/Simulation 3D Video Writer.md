---
type: simulink-block
title: 'Simulation 3D Video Writer'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Simulation 3D / Utilities'
documentation_page: 'simulation3dvideowriter'
documentation_source_path: 'simulation3dvideowriter.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Video Writer

## 端口

R2025b 中未记录。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Filename** — 视频文件名称 `output.avi`（默认）| 字符向量 | 字符串

以字符向量或字符串标量形式指定视频文件的名称及文件格式。视频文件保存在与模型保存位置相同的工作文件夹中。您也可以同时指定文件路径和文件名，以将视频文件保存到特定位置。该模块支持以下文件扩展名。

| 文件扩展名 | 描述 |
| --- | --- |
| `.avi` | AVI 文件 |
| `.mj2` | Motion JPEG 2000 文件 |
| `.mp4` 或 `.m4v` | MPEG-4 文件（Windows® 7 或更高版本，或 macOS 10.7 及更高版本的系统） |

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `Filename` |
| **值**：| `'output.avi'`（默认）| 字符向量 | 字符串 |
| **Data Types:** | `string` |

**Example:** `set_param(gcb,"Filename","video1.avi")`

### **File action** — 如何管理视频文件 `Preserve`（默认）| `Overwrite` | 字符向量 | 字符串

指定如何管理视频文件。

| 选项 | 描述 |
| --- | --- |
| `Preserve` | 保护现有视频文件不被覆盖。 |
| `Overwrite` | 允许覆盖视频文件。 |

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `FileAction` |
| **值**：| `'Preserve'`（默认）| `'Overwrite'` | 字符向量 | 字符串 |
| **Data Types:** | `string` |

**Example:** `set_param(gcb,"FileAction","Overwrite")`

### **Recording interval (s)** — 记录时间间隔 `[0 inf]`（默认）| 实数正 1×2 向量

以实数正 1×2 向量形式指定记录时间间隔，单位为秒。默认情况下，记录时间间隔为 3D 仿真的开始时间到结束时间。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `Interval` |
| **值**：| `[0 inf]`（默认）| 实数正 1×2 向量 |
| **Data Types:** | `double` |

**Example:** `set_param(gcb,"Interval","[0 inf]")`

## 所属库

Simulink 3D Animation / Simulation 3D / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2025a 中引入**

## 描述

将 3D 仿真捕获为视频文件

Simulation 3D Video Writer 将 3D 仿真捕获为视频文件，每步一帧。
