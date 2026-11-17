---
type: simulink-block
title: 'Simulation 3D Video Writer'
family: 'simulation-3d'
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

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条上的 **Simulation** 选项卡中，在 **Prepare** 库中，选择 **Property Inspector**。

### **Filename** — 视频文件的名称 `output.avi`（默认）| character vector | string

以 character vector 或 string scalar 形式指定视频文件的名称及文件格式。视频文件保存在模型所在的同一工作文件夹中。您还可以在指定文件名的同时指定文件路径，以将视频文件保存到特定位置。该模块支持以下文件扩展名。

| 文件扩展名 | 描述 |
| --- | --- |
| `.avi` | AVI 文件 |
| `.mj2` | Motion JPEG 2000 文件 |
| `.mp4` 或 `.m4v` | MPEG-4 文件（Windows® 7 或更高版本，或 macOS 10.7 及更高版本的系统） |

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以程序方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `Filename` |
| **值：** | `'output.avi'`（默认）| character vector | string |
| **数据类型：** | `string` |

**示例：** `set_param(gcb,"Filename","video1.avi")`

### **File action** — 如何管理视频文件 `Preserve`（默认）| `Overwrite` | character vector | string

指定如何管理视频文件。

| 选项 | 描述 |
| --- | --- |
| `Preserve` | 保护现有视频文件不被覆盖。 |
| `Overwrite` | 允许覆盖视频文件。 |

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以程序方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `FileAction` |
| **值：** | `'Preserve'`（默认）| `'Overwrite'` | character vector | string |
| **数据类型：** | `string` |

**示例：** `set_param(gcb,"FileAction","Overwrite")`

### **Recording interval (s)** — 记录时间间隔 `[0 inf]`（默认）| real positive 1-by-2 vector

以 real positive 1-by-2 vector 形式指定记录时间间隔，单位为秒。默认情况下，记录时间间隔为 3D 仿真的开始时间到结束时间。

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以程序方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `Interval` |
| **值：** | `[0 inf]`（默认）| real positive 1-by-2 vector |
| **数据类型：** | `double` |

**示例：** `set_param(gcb,"Interval","[0 inf]")`

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
