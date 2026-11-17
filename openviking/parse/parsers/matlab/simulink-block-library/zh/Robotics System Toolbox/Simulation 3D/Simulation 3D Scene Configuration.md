---
type: simulink-block
title: 'Simulation 3D Scene Configuration'
family: 'simulation-3d'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Simulation 3D'
documentation_page: 'simulation3dsceneconfiguration'
documentation_source_path: 'ref/simulation3dsceneconfiguration.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Scene Configuration

## 端口

在 R2025b 中未记录。

## 参数

### 场景

#### 场景选择

### **Scene source** — 场景的来源 `Default Scenes`（默认）| `RoadRunner` | `Unreal Executable` | `Unreal Editor`

要在其中进行仿真的场景的来源，指定为表中选项之一。

| 选项 | 描述 |
| --- | --- |
| `Default Scenes` | 在 **Scene name** 参数中指定的一个默认预构建场景中进行仿真。 |
| `RoadRunner` | 在 RoadRunner 场景中进行仿真。要导入 RoadRunner 场景，请在 **Project** 参数中指定相应文件。 |
| `Unreal Executable` | 在属于 Unreal Engine 可执行文件的场景中进行仿真。在 **Project name** 参数中指定该可执行文件。在 **Scene** 参数中指定场景。选择此选项可在已打包为可执行文件的自定义场景中进行仿真，以获得更快的仿真速度。 |
| `Unreal Editor` | 在属于 Unreal Engine 项目（`.uproject`）文件且已在 Unreal® Editor 中打开的场景中进行仿真。在 **Project** 参数中指定项目文件。在开发自定义场景时选择此选项。通过点击 **Open Unreal Editor**，您可以在 Simulink 和 Unreal Editor 中进行协同仿真，并根据仿真结果修改场景。 |

### **Scene name** — 预构建 3D 场景的名称 `Empty scene`（默认）| `Blank scene` | `Curved road` | `Straight road` | `Offroad pit mining scene` | `Construction site scene`

要在其中进行仿真的预构建 3D 场景的名称，指定为这些选项之一。有关场景的详细信息，请参阅其列出的对应参考页。

- `Blank scene` – 空白场景（Simulink 3D Animation）
- `Curved road` – 弯曲道路（Simulink 3D Animation）
- `Empty scene` – 空场景（Simulink 3D Animation）
- `Straight road` – 直行道路（Simulink 3D Animation）
- `Offroad pit mining scene` – 越野露天矿场景。您可以通过附加功能安装程序中的可选安装访问此场景。
- `Construction site scene` – 建筑工地场景。您可以通过附加功能安装程序中的可选安装访问此场景。

#### 依赖关系

要启用此参数，请将 **Scene source** 设置为 `Default Scenes`。

### **Project name** — Unreal Engine 可执行文件的名称 `VehicleSimulation.exe`（默认）| 有效的可执行文件名

Unreal Engine 可执行文件的名称，指定为有效的可执行项目文件名。您可以浏览该文件，也可以使用反斜杠指定项目文件的完整路径。要指定从此文件进行仿真的场景，请使用 **Scene** 参数。

默认情况下，**Project name** 设置为 `VehicleSimulation.exe`，该文件位于 MATLAB® 搜索路径上。

**注意**

如果选择使用与当前 MATLAB 版本不兼容的 Unreal Engine 版本构建的自定义 Unreal 可执行文件，则会收到以下错误消息之一：

- `"Incompatible version of 3D Simulation engine:
  Undefined"`：适用于为 R2023b 之前 MATLAB 版本构建的 Unreal 可执行文件
- `"Incompatible version of 3D Simulation engine: 23.2.0"`：
  适用于为 MATLAB R2023b 或更高版本构建的 Unreal 可执行文件

要解决这些错误，您必须迁移 Unreal 项目，并在安装最新支持包后重新构建可执行文件。有关详细信息，请参阅 How Unreal Engine Simulation for Robots Works。

**示例：** `C:\Local\WindowsNoEditor\AutoVrtlEnv.exe`

#### 依赖关系

要启用此参数，请将 **Scene source** 设置为 `Unreal Executable`。

### **Select ASAM OpenDRIVE file** — 指定 ASAM OpenDRIVE® 文件 `off`（默认）| `on`

指定 ASAM OpenDRIVE 文件。选择模块参数 **Select ASAM OpenDRIVE file** 以指定 ASAM OpenDRIVE 文件。

#### 依赖关系

当您将 `Scene Source` 设置为 `Unreal Executable` 或 `Unreal Engine` 时，此参数可用。

**数据类型：** `Boolean`

### **Scene** — 来自可执行文件的场景名称 `/Game/Maps/EmptyScene`（默认）| 有效场景名称的路径

来自 **Project name** 参数所指定可执行文件的场景名称，指定为有效场景名称的路径。

当您将 Unreal Engine 项目中的场景打包到可执行文件时，Unreal Editor 会将场景保存到可执行文件内的内部文件夹中。默认场景位于路径 `/Game/Maps`。因此，您必须在场景名称前加上 `/Game/Maps`。请使用正斜杠指定此路径。对于文件名，不要指定 `.umap` 扩展名。例如，如果要进行仿真的可执行文件中的场景名为 `myScene.umap`，则应将 **Scene** 指定为 `/Games/Maps/myScene`。

或者，您可以在相应的 Unreal Engine 项目中浏览该场景。这些场景通常保存到项目的 `Content/Maps` 子文件夹中。此子文件夹包含项目中的所有场景。这些场景的扩展名为 `.umap`。选择您已打包到 **File** name 参数所指定可执行文件中的某个场景。使用反斜杠并为场景指定 `.umap` 扩展名。

默认情况下，**Scene** 设置为 `/Game/Maps/EmptyScene`，这是来自 **Project name** 参数所指定默认 `VehicleSimulation.exe` 可执行文件中的场景。

**示例：** `/Game/Maps/scene1`,
`C:/Local/myProject/Content/Maps/scene1.umap`

#### 依赖关系

要启用此参数，请将 **Scene source** 设置为 `Unreal Executable`。

### **Project** — Unreal Engine 项目文件或 RoadRunner 文件的名称 有效的项目文件名

Unreal Engine 项目文件或 RoadRunner 文件的名称，指定为有效的项目文件名。您可以浏览该文件，也可以使用反斜杠指定文件的完整路径。文件名不得包含空格。

要在 Unreal Editor 中仿真来自 Unreal Engine 项目文件的场景，请点击 **Open Unreal Editor**。如果您已经打开了 Unreal Editor 会话，则此按钮处于禁用状态。

要运行仿真，请在 Simulink 中点击 **Run**。在 Unreal Editor 中点击 **Play** 之前，请等待 Diagnostic Viewer 窗口显示以下确认消息：

```
In the Simulation 3D Scene Configuration block, you set the scene source to 'Unreal Editor'.
In Unreal Editor, select 'Play' to view the scene.
```

此消息确认 Simulink 已在 Unreal Engine 3D 环境中实例化场景 actor，包括车辆和相机。如果在 Diagnostic Viewer 窗口显示此确认消息之前点击 **Play**，Simulink 可能不会在 Unreal Editor 中实例化这些 actor。

要仿真 RoadRunner 场景，您可以导入 Filmbox (`.fbx`)、Universal Scene Description (USD)、RoadRunner scene (`.rrscene`) 或 RoadRunner scenario (`.rrscenario`) 格式的文件。

- 要仿真 Filmbox (`.fbx`) 格式的场景，请浏览到包含导出的 RoadRunner 场景文件的文件夹，并指定 `.fbx` 文件。
- 要仿真 Universal Scene Description (USD) 格式的场景，请浏览到包含导出的 RoadRunner 场景文件的文件夹，并选择 `.usd`、`.usdc` 或 `.usda` 文件。从 USD 文件导入的 actor 与碰撞检测不兼容。
- 要仿真 RoadRunner scene 或 scenario (`.rrscene` 或 `.rrscenario`) 格式的场景，请浏览到包含 RoadRunner 文件的文件夹，并选择相应文件。在仿真之前，您必须使用 `roadrunnerSetup` 函数配置 RoadRunner 与 MATLAB 的集成。

  - 在 MATLAB Command Window 中输入 `roadrunnerSetup` 函数。
  - 将打开 RoadRunner Setup 对话框。
  - 指定 **RoadRunner Project Folder** 和 **RoadRunner Installation Folder** 位置。

**注意**

Linux® 不支持 USD 以及 RoadRunner scene 或 scenario (`.rrscene` 或 `.rrscenario`) 文件导入。

#### 依赖关系

#### 场景参数

### **Scene view** — 显示场景的虚拟相机放置位置 `Scene Origin`（默认）| `Custom` | 车辆名称 | `sim3d` actor 名称 | 视点名称

配置虚拟相机的放置位置，以设置在仿真期间显示场景的视点。**Scene view** 参数列表会填充模型中车辆和 actor 模块的所有 **Name** 参数值，以及您创建的任何其他自定义视点。如果向模型添加 Simulation 3D Scene Configuration 模块，虚拟相机将保持在场景原点。要将相机重新定位到自定义视点或跟随车辆或 actor，请更新此参数。

下表列出了当模型中不包含车辆模块、actor 模块或自定义视点时，**Scene view** 参数选项。

| 选项 | 描述 |
| --- | --- |
| `Custom` | - 创建自定义视点。此选项会启用以下参数。  - **Name**   - **Translation**   - **Rotation** - 点击 **Save Viewpoint** 以创建该视点。 - 在自由相机模式下查看场景。相机移动使用世界坐标系。 |
| `Scene Origin` | - 将视点设置在场景原点。 - 在自由相机模式下查看场景。相机移动使用世界坐标系。 |

下表列出了当模型中包含车辆模块、actor 模块或自定义视点时，额外的选项。

| 选项 | 描述 |
| --- | --- |
| 车辆名称 | - 将虚拟相机附加到模型中选定的车辆模块。 - 您只能更改相机围绕车辆的位置。 |
| `sim3d` actor 名称 | - 将虚拟相机附加到模型中选定的 Simulation 3D Actor 模块。 - 此选项会启用以下参数，以设置相机相对于 actor 原点的位置。  - **Viewer relative translation [X, Y, Z]     (m)**   - **Viewer relative rotation [Roll, Pitch, Yaw]     (deg)** |
| 视点名称 | - 将视点设置为选定的视点名称。此选项还会启用以下参数。  - **Name**   - **Translation**   - **Rotation** - 点击 **Save Viewpoint** 以更新视点。 - 点击 **Delete Viewpoint** 以移除视点。 - 在自由相机模式下查看场景。相机移动使用世界坐标系。 |

**场景控制**

当 **Scene view** 设置为 `Scene Origin` 或 `Custom` 时，您可以在仿真期间使用键盘和鼠标控制在场景中导航，以更改相机位置。您也可以在仿真暂停时更改相机位置。

要在 3D 环境中导航，请使用以下键盘快捷键。

| 键盘快捷键 | 相机控制 |
| --- | --- |
| **W** | 向前移动。 |
| **Shift+W** | 沿向前方向更快移动。 |
| **S** | 向后移动。 |
| **Shift+S** | 沿反向更快移动。 |
| **A** | 向左移动。 |
| **Shift+A** | 向左侧更快移动。 |
| **D** | 向右移动。 |
| **Shift+D** | 向右侧更快移动。 |
| **E** | 向上移动。 |
| **Shift+E** | 沿向上方向更快移动。 |
| **Q** | 向下移动。 |
| **Shift+Q** | 沿向下方向更快移动。 |
| 鼠标滚轮 | 控制相机与光标点之间的距离。 |
| **Shift**+鼠标滚轮 | 相机移动更快。 |
| 鼠标右键单击并拖动 | 围绕光标点旋转。 |
| **O** | 将相机附加到光标点下的 actor。 |
| 鼠标左键单击并拖动 | 相机附加到 actor 后，围绕该 actor 旋转。 |
| **P** | 从 actor 分离相机。 |
| **L** | 记录当前视点并在场景上显示 `Location saved`。 |
| **1 to 9** | 访问已存储的视点（如果有）。 |
| **Tab** | 在场景中的所有车辆和仿真开始时的视点之间按正向循环切换视图。 |
| **Shift+Tab** | 在场景中的所有车辆和仿真开始时的视点之间按反向循环切换视图。 |
| **I** | 在屏幕上切换键盘快捷键的显示。按一次显示，再按一次隐藏。 |

**车辆视图**

当 **Scene view** 设置为车辆名称时，在仿真期间，您可以更改相机围绕车辆的位置。您还可以在仿真期间按 **Tab** 将视图设置为某辆车。

要平滑更改相机视图，请使用以下键盘快捷键。

| 键盘快捷键 | 相机视图 | |
| --- | --- | --- |
| **1** | 左后方 | 示意图显示与相机视图对应的编号按键命令     查看动画 GIF  相机视图的动画 GIF |
| **2** | 后方 |
| **3** | 右后方 |
| **4** | 左侧 |
| **5** | 内部 |
| **6** | 右侧 |
| **7** | 左前方 |
| **8** | 前方 |
| **9** | 右前方 |
| **0** | 俯视 |

有关其他相机控制，请使用以下键盘快捷键。

| 键盘快捷键 | 相机控制 |
| --- | --- |
| **Tab** | 在场景中的所有车辆之间循环切换视图。  查看动画 GIF  场景中所有车辆之间循环切换视图的动画 GIF |
| 鼠标滚轮 | 控制相机与车辆之间的距离。  查看动画 GIF  相机距离控制的动画 GIF |
| **L** | 打开或关闭相机滞后效果。启用滞后效果后，相机视图包括：  - 位置滞后，基于车辆平移加速度 - 旋转滞后，基于车辆旋转速度  此滞后可改进整体车辆加速度和旋转的可视化。  查看动画 GIF  相机滞后效果的动画 GIF |
| **F** | 打开或关闭自由相机模式。启用自由相机模式后，您可以使用鼠标更改相机的俯仰角和偏航角。此模式允许您围绕车辆旋转相机。  查看动画 GIF  自由相机模式的动画 GIF |

### **Name** — 自定义视点的名称 `custom`（默认）| character array | string scalar

*自 R2025a 起*

将自定义视点的名称指定为 character array 或 string scalar。

**示例：** `View1`

#### 依赖关系

要启用此参数，请将 **Scene view** 设置为 `Custom`。

**数据类型：** `char` | `string`

### **Translation** — 视点平移 `[0 0 0]`（默认）| real 1-by-3 vector

*自 R2025a 起*

将视点平移 (*x*,*y*,*z*) 指定为 real 1-by-3 vector，单位为 m。

#### 依赖关系

要启用此参数，请将 **Scene view** 设置为 `Custom`。

**数据类型：** `double`

### **Rotation** — 视点旋转 `[0 0 0]`（默认）| real 1-by-3 vector

*自 R2025a 起*

将视点旋转 (*roll*, *pitch*, *yaw*) 指定为 real 1-by-3 vector，单位为 deg。

#### 依赖关系

要启用此参数，请将 **Scene view** 设置为 `Custom`。

**数据类型：** `double`

### **Viewer relative translation [X, Y, Z] (m)** — 相对于 actor 的视点平移 `[0 0 0]`（默认）| real 1-by-3 vector

*自 R2025a 起*

将相对于 `sim3d` actor 原点的视点平移 (*x*,*y*,*z*) 指定为 real 1-by-3 vector，单位为 m。

#### 依赖关系

要启用此参数，请将 **Scene view** 设置为 `sim3d` actor 名称。

**数据类型：** `double`

### **Viewer relative rotation [Roll, Pitch, Yaw] (deg)** — 相对于 actor 的视点旋转 `[0 0 0]`（默认）| real 1-by-3 vector

*自 R2025a 起*

将相对于 `sim3d` actor 原点的视点旋转 (*roll*, *pitch*, *yaw*) 指定为 real 1-by-3 vector，单位为 deg。

#### 依赖关系

要启用此参数，请将 **Scene view** 设置为 `sim3d` actor 名称。

**数据类型：** `double`

### **采样时间** — 可视化引擎的采样时间 `.02`（默认）| real positive scalar

可视化引擎的采样时间 *Ts*，指定为 real positive scalar。单位为 seconds。

可视化引擎的图形帧率是采样时间的倒数。例如，如果 **采样时间** 为 `1/60`，则可视化引擎求解器会尝试达到 60 frames per second 的帧率。但是，实时图形帧率通常较低，原因包括显卡性能和模型复杂度等因素。

默认情况下，从可视化引擎接收数据的模块继承此采样率。

### 天气

### **覆盖场景天气** — 用于控制场景天气和太阳位置的选项 `off`（默认）| `on`

选择是否在仿真期间控制场景天气和太阳位置。使用启用的参数更改太阳位置、云、雾、雨和雪。

此表总结了特定一天中时间的太阳位置设置。

| 一天中的时间 | 设置 | Unreal Editor 环境 |
| --- | --- | --- |
| 午夜 | **太阳高度角**：-90  **太阳方位角**：180 | 午夜道路 |
| 北部日出 | **太阳高度角**：0  **太阳方位角**：180 | 日出道路 |
| 正午 | **太阳高度角**：90  **太阳方位角**：180 | 正午道路 |

此表总结了特定云条件的设置。

| 云条件 | 设置 | Unreal Editor 环境 |
| --- | --- | --- |
| 晴朗 | **云不透明度**：0 | 晴朗天空的道路 |
| 厚重 | **云不透明度**：85 | 多云天空的道路 |
| 厚重 | **启用体积云**：Selected  **云覆盖**：50  **云层高度**：6 | 体积云道路 |

此表总结了特定雾条件的设置。

| 雾条件 | 设置 | Unreal Editor 环境 |
| --- | --- | --- |
| 无 | **雾密度**：0 | 无雾道路 |
| 浓重 | **雾密度**：100 | 浓雾道路 |

此表总结了特定雨条件的设置。

| 雨条件 | 设置 | Unreal Editor 环境 |
| --- | --- | --- |
| 小雨 | **云不透明度**：10  **雨密度**：25 | 小雨的城市场景 |
| 大雨 | **云不透明度**：10  **雨密度**：80 | 大雨的城市场景 |

此表总结了特定雪条件的设置。

| 雪条件 | 设置 | Unreal Editor 环境 |
| --- | --- | --- |
| 大雪 | **雪密度**：50 | 大雪的道路场景 |

#### 太阳

### **太阳方位角** — 从南到太阳光线水平投影的方位角 `90`（默认）| 介于 `0` 和 `360` 之间的任意值

水平面中从南到太阳光线水平投影测量的方位角，单位为 deg。

太阳高度角（垂直箭头）和太阳方位角（水平箭头）的示意图

使用 **太阳高度角** 和 **太阳方位角** 参数控制场景中的一天中的时间。例如，要指定北部日出，将 **太阳高度角** 设置为 0 deg，将 **太阳方位角** 设置为 180 deg。

#### 依赖项

要启用此参数，请选择 **覆盖场景天气**。

### **太阳高度角** — 太阳与地平线之间的高度角 `40`（默认）| 介于 `-90` 和 `90` 之间的任意值

垂直平面中太阳光线与光线水平投影之间的高度角，单位为 deg。

太阳高度角（垂直箭头）和太阳方位角（水平箭头）的示意图

使用 **太阳高度角** 和 **太阳方位角** 参数控制场景中的一天中的时间。例如，要指定北部日出，将 **太阳高度角** 设置为 0 deg，将 **太阳方位角** 设置为 180 deg。

#### 依赖项

要启用此参数，请选择 **覆盖场景天气**。

### **启用地理空间太阳** — 用于启用地理空间太阳的选项 `off`（默认）| `on`

选中此复选框以启用地理空间太阳。启用地理空间太阳可用于仿真极点附近或昼夜长度差异悬殊位置的条件。

#### 依赖项

要启用此参数，请选择 **覆盖场景天气**。

### **纬度** — 地球上地理位置的纬度 `0`（默认）| scalar

地球上地理位置的纬度，指定为 scalar，单位为 deg。

#### 依赖项

要启用此参数，请选择 **覆盖场景天气** 和 **启用地理空间太阳**。

### **经度** — 地球上地理位置的经度 0（默认）| scalar

地球上地理位置的经度，指定为 scalar，单位为 deg。

#### 依赖项

要启用此参数，请选择 **覆盖场景天气** 和 **启用地理空间太阳**。

### **日期 (YYYY-MM-DD)** — 日期 2023-01-01（默认）| integer

日期，指定为 `YYYY-MM-DD` 格式的 integer。

#### 依赖项

要启用此参数，请选择 **覆盖场景天气** 和 **启用地理空间太阳**。

### **时间 (HH:MM:SS)** — 时间 `10:30:00`（默认）| integer

时间，指定为 `HH:MM:SS` 格式的 integer。

#### 依赖项

要启用此参数，请选择 **覆盖场景天气** 和 **启用地理空间太阳**。

### **时区** — 时区 `-5.0`（默认）| 介于 `-12.0` 和 `12.0` 之间的任意值

时区指定与 Coordinated Universal Time (UTC) 或 Greenwich Mean Time (GMT) 的小时偏移量。

#### 依赖项

要启用此参数，请选择 **覆盖场景天气** 和 **启用地理空间太阳**。

### **夏令时** — 用于启用夏令时的选项 `off`（默认）| `on`

选中此复选框以启用夏令时。

#### 依赖项

要启用此参数，请选择 **覆盖场景天气** 和 **启用地理空间太阳**。

#### 云

### **云速度** — Unreal Editor Cloud Speed global actor target value `1`（默认）| 介于 `-100` 和 `100` 之间的任意值

对应于 Unreal Editor **Cloud Speed** global actor target value 的参数。对于正值，云从西向东移动；对于负值，云从东向西移动。

Unreal Editor 中的 Cloud Opacity 和 Cloud Speed 设置

使用 **云不透明度** 和 **云速度** 参数控制场景中的云。

#### 依赖项

要启用此参数，请选择 **覆盖场景天气**。

### **云不透明度** — Unreal Editor Cloud Opacity global actor target value `10`（默认）| 介于 `0` 和 `100` 之间的任意值

对应于 Unreal Editor **Cloud Opacity** global actor target value 的参数，单位为 percent。零表示无云场景。

Unreal Editor 中的 Cloud Opacity 和 Cloud Speed 设置

使用 **云不透明度** 和 **云速度** 参数控制场景中的云。

#### 依赖项

要启用此参数，请选择 **覆盖场景天气**。

### **启用体积云** — 用于启用体积云的选项 `off`（默认）| `on`

选中此复选框以启用体积云。

#### 依赖项

要启用此参数，请选择 **覆盖场景天气**。

### **云覆盖** — Unreal Editor Cloud Density global target value `1.0`（默认）| 介于 `0` 和 `100` 之间的任意值

对应于 Unreal Editor **Cloud Density** global actor target value 的参数，单位为 percent。

Unreal Editor 中的云覆盖设置

使用 **云覆盖** 参数控制场景中的云。

#### 依赖项

要启用此参数，请选择 **覆盖场景天气** 和 **启用体积云**。

### **云层高度** — Unreal Editor Layer Bottom Altitude global actor target value `6`（默认）| 介于 `5` 和 `20` 之间的任意值

对应于 Unreal Editor **Layer Bottom Altitude** global actor target value 的参数，单位为 km。

Unreal Editor 中的云高度设置

#### 依赖项

要启用此参数，请选择 **覆盖场景天气** 和 **启用体积云**。

#### 雾

### **雾密度** — Unreal Editor Set Fog Density 和 Set Start Distance target values `0`（默认）| 介于 `0` 和 `100` 之间的任意值

对应于 Unreal Editor **Set Fog Density** 和 **Set Start Distance** target values 的参数，单位为 percent。

Unreal Editor 中的 Set Fog Density 设置

#### 依赖项

要启用此参数，请选择 **覆盖场景天气**。

#### 雨

### **雨密度** — Unreal Editor local actor controlling rain density, wetness, rain puddles, and ripples `0`（默认）| 介于 `0` 和 `100` 之间的任意值

对应于 Unreal Editor local actor 的参数，该 actor 控制雨密度、湿度、雨洼和涟漪，单位为 percent。

Unreal Editor 中用于控制雨密度的设置。左侧的 Get Components by Class 激活或停用雨密度设置。右侧的雨效果控制湿度、雨洼和涟漪等设置。

使用 **云不透明度** 和 **雨密度** 参数控制场景中的雨。

#### 依赖项

要启用此参数，请选择 **覆盖场景天气**。

### **启用相机镜头上的雨滴** — 用于启用相机镜头上雨滴的选项 `off`（默认）| `on`

选中此复选框以启用相机镜头上的雨滴。

Unreal Editor 中的云高度设置

#### 依赖项

要启用此参数，请选择 **覆盖场景天气**。

#### 雪

### **雪密度** — Unreal Editor global actor controlling snow density `0`（默认）| 介于 `0` 和 `100` 之间的任意值

此参数对应于控制雪密度的 Unreal Editor global actor，单位为 percent。

Unreal Editor 中的云高度设置

#### 依赖项

要启用此参数，请选择 **覆盖场景天气**。

## 所属库

Offroad Autonomy Library / Simulation 3D Aerospace Blockset / Animation / Simulation 3D Automated Driving Toolbox / Simulation 3D Robotics System Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Environment UAV Toolbox / Simulation 3D Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Core

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

### R2025a: 将 USD 和 RoadRunner 场景或 scenario 文件导入 Unreal Engine 仿真环境

您可以导入以下 RoadRunner 场景文件：

- Universal Scene Description（`.usd`、`.usdc` 和 `.usda`）文件
- RoadRunner 场景或 scenario（`.rrscene` 或 `.rrscenario`）文件

要指定场景源，请将 **场景源** 参数设置为 `RoadRunner`。然后，在 **项目** 参数中，指定对应的 RoadRunner 场景文件。

### R2025a: 创建 3D 环境的多个视图

您可以使用 **场景视图** 参数中的 `Custom` 选项创建自定义视点。此选项会启用以下参数。

- **名称**
- **平移**
- **旋转**

您可以保存视点，以使用视点名称填充 **场景视图** 参数列表。选择该视点以设置场景的视图。您还可以编辑或删除该视点。

### R2025a: 设置相对于 `sim3d` actor 的场景视图

您可以将 **场景视图** 参数设置为模型中包含的 Simulation 3D Actor 模块的 **名称** 参数。此选项会启用以下参数，以设置相机相对于 actor 原点的位置。

- **查看器相对平移 [X, Y, Z] (m)**
- **查看器相对旋转 [Roll, Pitch, Yaw] (deg)**

### R2025a: 安装其他场景

除了默认场景之外，您还可以下载并安装 Unreal Engine 环境中可用于 3D 仿真的任何预构建 3D 场景。

要选择和下载场景，请点击 **Install**。安装场景后，MATLAB 会重新启动。现在您可以从 **场景视图** 参数列表中选择已安装的场景。

### R2024a: 新增可用于仿真其他天气条件的参数

使用新的天气参数仿真其他天气条件。

| 天气 | 参数 |
| --- | --- |
| **太阳** | - **启用地理空间太阳** - **纬度** - **经度** - **日期** - **时间** - **夏令时** |
| **云** | - **启用体积云** - **云覆盖** - **云层高度** |
| **雨** | - **启用相机镜头上的雨滴** |
| **雪** | - **雪密度** |

### R2023b: 将 RoadRunner Scene 导入 Unreal Engine 仿真环境

使用 Simulation 3D Scene Configuration 模块导入 RoadRunner 场景并在该场景中进行仿真。要指定场景源，请将 **场景源** 参数选择为 `RoadRunner`。然后，在 **项目** 参数中，指定对应于 RoadRunner 场景的 Filmbox `(.fbx)` 文件。有关示例，请参阅 Import RoadRunner Scene into Unreal Engine Using Simulink (Simulink 3D Animation)。

### R2023b: 用于查看虚拟世界的相机视图改进

使用 Simulation 3D Scene Configuration 模块从位于自定义视点的相机查看虚拟世界。要设置自定义视点，请将 **场景视图** 选择为 `Custom`，并设置 **初始查看器平移** 和 **初始查看器旋转** 值。您还可以使用键盘快捷键和鼠标控件在虚拟世界场景中导航。

## 描述

3D 仿真环境的场景配置

**注意**

使用 Simulation 3D Scene Configuration 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Scene Configuration 模块实现了一个 3D 仿真环境，该环境使用 Epic Games® 的 Unreal Engine® 进行渲染。它将 3D 仿真环境与 Simulink 集成，以便您可以查询车辆周围的世界，并虚拟测试感知、控制和规划算法。使用此模块，您还可以控制太阳位置和场景的天气条件。有关更多详细信息，请参阅 Sun Position and Weather。

**提示**

Simulation 3D Scene Configuration 模块必须在向 3D 环境发送数据的模块之后执行，并在从 3D 环境接收数据的模块之前执行。要验证此类模块的执行顺序，请右键点击这些模块并选择 **属性**。然后，在 **常规** 选项卡上，确认以下 **优先级** 设置：

- 对于向 3D 环境发送数据的模块，**优先级** 必须设置为 `-1`，以便这些模块可以在 3D 环境接收数据之前准备好其数据。
- 对于模型中的 Simulation 3D Scene Configuration 模块，**优先级** 必须设置为 `0`。
- 对于从 3D 环境接收数据的模块，**优先级** 必须设置为 `1`，以便 3D 环境可以在这些模块接收数据之前准备好数据。

有关执行顺序的更多信息，请参阅 How Unreal Engine Simulation for Robots Works。
