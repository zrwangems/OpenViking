---
type: simulink-block
title: 'Point Cloud Viewer'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'pointcloudviewer'
documentation_source_path: 'ref/pointcloudviewer.html'
language: zh-CN
chinese_source: worker-translation
---

# Point Cloud Viewer

## 端口

### 输入

### **Location** — 三维坐标空间中点的位置 矩阵 | 数组

三维坐标空间中点的位置，指定为：

- 用于三维点云的 *M*×3 矩阵或
  *M*×*N*×3 数组。
- 用于三维点云序列的 *M*×3×*T* 或
  *M*×*N*×3×*T*
  数组，其中 *T* 是点云序列中三维点云的总数。

每个数组指定点云中点的 *x*、*y*
和 *z* 坐标，但无组织点云和有组织点云的格式有所不同。

- 对于无组织点云，必须将 **Location**
  指定为 *M*×3 或
  *M*×3×*T* 数组，其中
  *M* 是点的总数，每一行提供点的
  *xyz* 坐标。
- 对于有组织点云，必须将 **Location** 指定为
  *M*×*N*×3 或 *M*×*N*×3×*T* 数组，
  其中 *M*×*N* 是点的总数，
  数组的第三维提供对应点的 *x*、
  *y* 和 *z* 坐标。投影相机（如 Kinect 或激光雷达传感器）将
  点存储为有组织点云。有组织点云以类似图像或视频结构的
  二维或三维点阵列形式排列。

**数据类型：** `single` | `double` | `uint8` | `uint16`

### **Color** — 点云颜色 `[]`（默认）| 矩阵 | 数组

点云颜色，指定为：

- 用于三维点云的 *M*×3 矩阵或
  *M*×*N*×3 数组。
- 用于三维点云序列的 *M*×3×*T* 或
  *M*×*N*×3×*T*
  数组，其中 *T* 是点云序列中三维点云的总数。

对于无组织点云，指定为
*M*×3 矩阵或 *M*×3×*T*
数组，每一行指定点云数据中一个点的 RGB 颜色三元组。
对于有组织点云，指定为
*M*×*N*×3 或
*M*×*N*×3×*T* 数组，
第三维的每个通道指定点云数据中对应点的 RGB 颜色三元组。可以为所有
点指定相同颜色，也可以为每个点指定不同颜色。

- 对于 `single` 或 `double` 数据类型，
  必须将 **Color** RGB 值指定在 [0, 1] 范围内。
- 对于 `uint8` 数据类型，必须将
  **Color** RGB 值指定在 [0, 255] 范围内。
- 对于 `uint16` 数据类型，必须将
  **Color** RGB 值指定在 [0, 65535] 范围内。

**注意**

**Color** 端口的输入必须与 **Location** 端口的输入具有相同的维度和
数据类型。

#### 依赖关系

要启用此端口，请选择 **File** > **Location and Color Port** 参数。

**数据类型：** `single` | `double` | `uint8` | `uint16`

### **Intensity** — 灰度强度 `[]`（默认）| 向量 | 矩阵 | 数组

*自 R2025a 起*

每个点的灰度强度，指定为：

- 用于无组织点云的 *M*×1 向量或
  用于有组织点云的 *M*×*N* 矩阵。
- 用于无组织点云序列的 *M*×1×*T* 数组或
  用于有组织点云序列的
  *M*×*N*×*T* 数组。*T* 是点云序列中三维点云的总数。

**注意**

**Intensity** 端口的输入必须与 **Location** 端口的输入具有相同的数据类型。

#### 依赖关系

要启用此端口，请选择 **File** > **Location and Intensity Port** 参数。

**数据类型：** `single` | `double` | `uint8` | `uint16`

## 参数

### File

### **Open at Start of Simulation** — 在仿真开始时打开 Point Cloud Viewer 窗口 `on`（默认）| `off`

选择此参数可在仿真开始时显示 Point Cloud Viewer 窗口。清除此参数可防止
Point Cloud Viewer 窗口在仿真开始时打开。

### **Location Port** — 启用点位置作为输入 `on`（默认）| `off`

选择此参数可启用 **Location** 端口以输入三维点云坐标。如果选择此参数，
**Location and Color Port** 和 **Location and Intensity
Port** 参数会自动清除。

### **Location and Color Port** — 启用点位置和颜色作为输入 `off`（默认）| `on`

选择此参数可同时启用 **Location** 和
**Color** 输入端口。如果选择此参数，
**Location Port** 和 **Location and Intensity
Port** 参数会自动清除。

### **Location and Intensity Port** — 启用点位置和强度作为输入 `off`（默认）| `on`

*自 R2025a 起*

选择此参数可同时启用 **Location** 和
**Intensity** 输入端口。如果选择此参数，
**Location Port** 和 **Location and Color Port**
参数会自动清除。

### File > Configuration > Edit > Core

Point Cloud Viewer Configuration 对话框使您能够更改图形用户界面 (GUI) 的行为和
外观。

- 要打开 Configuration 对话框并编辑参数，请选择 **File** > **Configuration** > **Edit**。

Configuration 对话框中的 **Core** 选项卡列出了 GUI 的常规
设置。

- 在 **Core** 选项卡中，选择 `General UI`
  并点击 **Properties** 以打开 General UI Properties 对话框。

### **Display the full path** — 在标题栏中显示源数据的完整路径 `off`（默认）| `on`

选择此参数可在 Point Cloud Viewer 窗口的标题栏中显示模型名称和源数据的完整路径。
如果清除此参数，窗口将显示缩短的名称。

### Tools > Point Cloud Information

Point Cloud Information 对话框显示有关输入点云
序列的信息。此信息包括 **Source type**、**Source
名称**、**帧大小**、**源数据类型**
和 **Display data type**。

### View

### **Bring All Point Cloud Viewer Windows Forward** — 将所有 Point Cloud Viewer 窗口置于显示前端 `off`（默认）| `on`

选择此参数可将所有 Point Cloud Viewer 窗口置于前端，
位于所有其他已打开窗口的前面。

### **Simulation Toolbar** — 显示仿真工具栏 `on`（默认）| `off`

选择此参数可在 Point Cloud Viewer
窗口上显示仿真工具栏。

仿真工具栏

要使用仿真工具栏执行相关操作，请按下表所述选择
相应功能。

| 功能 | 描述 |
| --- | --- |
| Run | 启动仿真，并查看点云序列。 |
| Step Forward | 启动仿真，查看点云序列的一帧，然后暂停。 |
| Stop | 停止仿真。 |
| Highlight Simulink Block | 在 Simulink 模型中以蓝色背景高亮显示 Point Cloud Viewer 模块。 |
| Snapshot (Freeze Display) | 冻结 Point Cloud Viewer 窗口，使您能够使用 **File** 菜单中的 **Print** 或 **Print Preview** 选项对窗口进行截图。 **注意** 取消选择此选项可将 Point Cloud Viewer 窗口从冻结状态恢复到活动状态。 |
| Settings | 在 Point Cloud Viewer 窗口上启用 **Settings** 窗格。 |
| Colorbar *(自 R2025a 起)* | 在 Point Cloud Viewer 窗口中查看颜色条。 默认情况下，Point Cloud Viewer 窗口不显示颜色条。要查看颜色条，请点击仿真工具栏上的 **Colorbar**。要隐藏颜色条，请再次点击 **Colorbar**。 **依赖关系** 要启用此参数，请选择 **File** > **Location Port** 或 **File** > **Location and Intensity Port** 参数。 |

### **Status Bar** — 显示状态栏 `on`（默认）| `off`

选择此参数可在 Point Cloud Viewer 窗口上显示状态栏。
位于 Point Cloud Viewer 窗口底部的状态栏显示有关点云序列的以下信息。

- 维度
- 组织
- 仿真期间窗口的状态
- 当前帧的时间戳

### **Highlight Simulink Block** — 高亮显示 Point Cloud Viewer 模块 `off`（默认）| `on`

在 Simulink 模型中以蓝色高亮显示 Point Cloud Viewer 模块。

### 仿真

要访问此参数，请在 Point
Cloud Viewer 窗口中选择 **Simulation** 菜单。

### **Run** — 查看整个点云序列 `off`（默认）| `on`

选择此参数可启动仿真，并从第一帧到最后一帧连续查看点云序列。
您也可以通过点击仿真工具栏上的 **Run** 来执行此操作。

### **Continue** — 继续查看点云序列 `off`（默认）| `on`

选择此参数可继续查看点云序列直到最后一帧。要启用 **Continue** 参数，
请通过点击仿真工具栏上的 **Step Forward** 来启动仿真。

### **Stop** — 停止查看点云序列 `off`（默认）| `on`

选择此参数可停止点云序列的显示。您也可以
通过点击仿真工具栏上的 **Stop** 来执行此操作。

### **Drop Frames to Improve Performance** — 降低输入点云序列的帧率 `on`（默认）| `off`

选择此参数可降低输入流式点云序列的帧率，以提高仿真的性能。如果清除此参数，
模块将在仿真期间显示输入点云序列信号中的每一帧。

## 所属库

Computer Vision Toolbox / Sinks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023a 中引入**

### R2025a：使用强度值可视化点云数据

该模块现在支持 **Intensity** 输入端口，以使用强度值可视化流式点云数据。要启用此端口，请选择 **File** > **Location and Intensity Port** 参数。

### R2025a：查看点云数据的颜色条

您现在可以通过选择仿真工具栏上的 **Colorbar** 按钮来查看颜色条。当您选择 **File** > **Location Port** 或 **File** > **Location and Intensity Port** 参数时，此按钮可用。

### R2025a：在坐标轴完整范围内查看点云

该模块现在会根据输入点云数据自动调整默认坐标轴范围。自动调整使您能够在坐标轴的完整范围内查看点云。

## 描述

可视化流式点云数据序列

Point Cloud Viewer 模块创建一个 Point Cloud Viewer 窗口，用于显示
从 Microsoft® Kinect® 或激光雷达传感器等设备流式传输的三维点云数据序列。
Point Cloud Viewer 模块还在 Point Cloud Viewer
窗口中提供仿真控制，以播放、暂停和逐步浏览流式点云数据序列。

点云查看器窗口

### Point Cloud Viewer 的功能

- 播放控制 — 使用 **Run**、**Step Forward** 和
  **Stop** 按钮控制点云序列的流式播放。
- 设置坐标轴范围 — 通过设置 *x*、*y* 和 *z* 轴
  范围来限制三维点云数据的显示。
- 设置背景颜色 — 设置查看器窗口的背景颜色，以在其上显示点云数据。
- 垂直轴方向控制 — 将点云数据的垂直轴方向设置为向上为正或向下为正。
- 视图平面控制 — 设置视图平面以更改点云数据的视角。
- 分析点云数据 — 使用 Point Cloud Viewer 窗口坐标轴工具栏上的 **Data
  Tips** 选项检查点云数据。
- 查看颜色条 — 使用仿真工具栏上的 **Colorbar** 按钮在 Point Cloud Viewer 窗口中查看颜色条。
