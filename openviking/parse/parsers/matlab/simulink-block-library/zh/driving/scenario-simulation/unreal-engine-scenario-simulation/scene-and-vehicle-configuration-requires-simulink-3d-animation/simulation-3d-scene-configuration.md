---
type: simulink-block
title: 'Simulation 3D Scene Configuration'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'Scenario Simulation / Unreal Engine Scenario Simulation / Scene and Vehicle Configuration (requires Simulink 3D Animation)'
documentation_page: 'simulation3dsceneconfiguration'
documentation_source_path: 'ref/simulation3dsceneconfiguration.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Scene Configuration

## 端口

R2025b 中未记录。

## 参数

### 场景

#### 场景选择

### **Scene source** — 场景来源 `Default Scenes` (默认) | `RoadRunner` | `Unreal Executable` | `Unreal Editor`

要在其中进行仿真的场景的来源，指定为表中的一个选项。

| 选项 | 描述 |
| --- | --- |
| `Default Scenes` | 在 **Scene name** 参数中指定的一个默认预构建场景中进行仿真。 |
| `RoadRunner` | 在 RoadRunner 场景中进行仿真。要导入 RoadRunner 场景，请在 **Project** 参数中指定相应的文件。 可以使用以下文件格式。  - Filmbox (`.fbx`) 文件。 - Universal Scene Description (`.usd`、`.usdc` 和   `.usda`) 文件。 - RoadRunner 场景或 scenario (`.rrscene` 或   `.rrscenario`) 文件。 |
| `Unreal Executable` | 在属于 Unreal Engine 可执行文件的场景中进行仿真。在 **Project name** 参数中指定可执行文件。在 **Scene** 参数中指定场景。  选择此选项可在已打包为可执行文件以加快仿真的自定义场景中进行仿真。 |
| `Unreal Editor` | 在属于 Unreal Engine 项目 (`.uproject`) 文件并在 Unreal® Editor 中打开的场景中进行仿真。在 **Project** 参数中指定项目文件。  在开发自定义场景时选择此选项。通过点击 **Open Unreal Editor**，可以在 Simulink 和 Unreal Editor 中进行联合仿真，并根据仿真结果修改场景。 |

### **Scene name** — 预构建 3D 场景的名称 `Empty Grass` | `Straight road` | `Curved road` | `US city block` | `Large parking lot` | 已安装场景名称

指定要在其中进行仿真的预构建 3D 场景的名称。此参数列出默认场景和当前可用的场景。还可以按需安装其他场景。安装场景后，**Scene name** 参数列表将填充所有可用场景名称。有关场景的详细信息，请参阅其列出的对应参考页。

这些是默认场景选项。

- `Empty Grass` — 空草地
- `Straight road` — 直路
- `Curved road` — 弯路
- `US city block` — 美国城市街区
- `Large parking lot` — 大型停车场

这些是可以安装的场景。有关其他场景的详细信息，请参阅 Unreal Engine 环境中用于仿真的 3D 场景。

- `Parking lot` — 停车场
- `Double lane change` — 双车道变换
- `Open surface` — 开放路面
- `US highway` — 美国高速公路
- `Virtual Mcity` — 虚拟 Mcity
- `ZalaZONE Smart City` — ZalaZONE 汽车试验场智能城市

要安装新场景：

1. 点击 **Install**。
2. 在 Add-on installer 对话框中，选择要安装的场景。
3. 要下载并安装场景，请点击 **Next** 并按照提示操作。安装场景后，MATLAB® 将重新启动。

安装后，可以从 **Scene name** 参数列表中选择新场景。

Unreal Engine 项目 Automated Driving Toolbox 接口包含这些场景的可自定义版本。有关自定义场景的详细信息，请参阅 Customize Unreal Engine Scenes for Automated Driving。

#### 依赖关系

要启用此参数，请将 **Scene source** 设置为 `Default Scenes`。

### **Project name** — Unreal Engine 可执行文件的名称 `VehicleSimulation.exe` (默认) | 有效的可执行文件名

Unreal Engine 可执行文件的名称，指定为有效的可执行项目文件名。您可以浏览该文件，或使用反斜杠指定项目文件的完整路径。要指定此文件中要进行仿真的场景，请使用 **Scene** 参数。

默认情况下，**Project name** 设置为 `VehicleSimulation.exe`，该文件位于 MATLAB 搜索路径中。

**注意**

如果选择使用与当前 MATLAB 版本不兼容的 Unreal Engine 版本构建的自定义 Unreal 可执行文件，将收到以下错误消息之一：

- `"Incompatible version of 3D Simulation engine: Undefined"`：对于为 R2023b 之前的 MATLAB 版本构建的 Unreal 可执行文件
- `"Incompatible version of 3D Simulation engine: 23.2.0"`：对于为 MATLAB R2023b 或更高版本构建的 Unreal 可执行文件

要解决这些错误，必须迁移 Unreal 项目，并使用已安装的最新支持包重新构建可执行文件。有关详细信息，请参阅 How Unreal Engine Simulation for Automated Driving Works。

**示例：** `C:\Local\WindowsNoEditor\AutoVrtlEnv.exe`

#### 依赖关系

要启用此参数，请将 **Scene source** 设置为 `Unreal Executable`。

### **Select ASAM OpenDRIVE file** — 指定 ASAM OpenDRIVE® 文件 `off` (默认) | `on`

指定 ASAM OpenDRIVE 文件。选择模块参数 **Select ASAM OpenDRIVE file** 以指定 ASAM OpenDRIVE 文件。如果要使用 Simulation 3D Vision Detection Generator 模块对自定义场景执行任何车道检测应用，则需要 ASAM OpenDRIVE 文件。

#### 依赖关系

当 `Scene Source` 设置为 `Unreal Executable` 或 `Unreal Engine` 时，此参数可用。

**数据类型：** `Boolean`

### **Scene** — 可执行文件中的场景名称 `/Game/Maps/HwStrght` (默认) | 有效场景名称的路径

由 **Project name** 参数指定的可执行文件中的场景名称，指定为有效场景名称的路径。

将场景从 Unreal Engine 项目打包到可执行文件时，Unreal Editor 会将场景保存到可执行文件内的内部文件夹中。此文件夹位于路径 `/Game/Maps`。因此，必须在场景名称前加上 `/Game/Maps`。必须使用正斜杠指定此路径。对于文件名，不要指定 `.umap` 扩展名。例如，如果要进行仿真的可执行文件中的场景名为 `myScene.umap`，请将 **Scene** 指定为 `/Game/Maps/myScene`。

或者，可以在相应的 Unreal Engine 项目中浏览该场景。这些场景通常保存到项目的 `Content/Maps` 子文件夹中。此子文件夹包含项目中的所有场景。场景具有扩展名 `.umap`。选择已打包到 **Project name** 参数指定的可执行文件中的其中一个场景。使用反斜杠并为场景指定 `.umap` 扩展名。

默认情况下，**Scene** 设置为 `/Game/Maps/HwStrght`，这是 **Project name** 参数指定的默认 `VehicleSimulation.exe` 可执行文件中的场景。此场景对应于预构建的 **Straight Road** 场景。

**示例：** `/Game/Maps/scene1`

**示例：** `C:\Local\myProject\Content\Maps\scene1.umap`

#### 依赖关系

要启用此参数，请将 **Scene source** 设置为 `Unreal Executable`。

### **Project** — Unreal Engine 项目文件或 RoadRunner 文件的名称 有效的项目文件名

Unreal Engine 项目文件或 RoadRunner 文件的名称，指定为有效的项目文件名。您可以浏览该文件，或使用反斜杠指定文件的完整路径。文件名不能包含空格。

要在 Unreal Editor 中仿真 Unreal Engine 项目文件中的场景，请点击 **Open Unreal Editor**。如果已经打开了 Unreal Editor 会话，则此按钮处于禁用状态。

要运行仿真，请在 Simulink 中点击 **Run**。在 Unreal Editor 中点击 **Play** 之前，请等待 Diagnostic Viewer 窗口显示以下确认消息：

```
In the Simulation 3D Scene Configuration block, you set the scene source to 'Unreal Editor'.
In Unreal Editor, select 'Play' to view the scene.
```

此消息确认 Simulink 已在 Unreal Engine 3D 环境中实例化场景 actor，包括车辆和摄像机。如果在 Diagnostic Viewer 窗口显示此确认消息之前点击 **Play**，Simulink 可能不会在 Unreal Editor 中实例化 actor。

要仿真 RoadRunner 场景，可以导入 Filmbox (`.fbx`)、Universal Scene Description (USD)、RoadRunner 场景 (`.rrscene`) 或 RoadRunner scenario (`.rrscenario`) 格式的文件。

- 要仿真 Filmbox (`.fbx`) 格式的场景，请浏览包含导出的 RoadRunner 场景文件的文件夹，并指定 `.fbx` 文件。可以使用 Export Using CARLA Filmbox (RoadRunner) 中的 **CARLA Filmbox** 选项导出 RoadRunner 场景。此选项会将以下三个文件导出到一个文件夹：

  - Filmbox (`.fbx`) 文件
  - ASAM OpenDrive (`.xodr`) 文件
  - XML (`.rrdata.xml`) 文件
- 要仿真 Universal Scene Description (USD) 格式的场景，请浏览包含导出的 RoadRunner 场景文件的文件夹，并选择 `.usd`、`.usdc` 或 `.usda` 文件。从 USD 文件导入的 actor 与碰撞检测不兼容。要以 USD 格式导出 RoadRunner 场景，请参阅 Export to USD (RoadRunner)。
- 要仿真 RoadRunner 场景或 scenario (`.rrscene` 或 `.rrscenario`) 格式的场景，请浏览包含 RoadRunner 文件的文件夹，并选择相应的文件。在仿真之前，必须使用 `roadrunnerSetup` (RoadRunner) 函数配置 RoadRunner 与 MATLAB 的集成。

  - 在 MATLAB 命令窗口中输入 `roadrunnerSetup` 函数。
  - 将打开 RoadRunner Setup 对话框。
  - 指定 **RoadRunner Project Folder** 和 **RoadRunner Installation Folder** 位置。

有关导出和仿真 RoadRunner 场景的详细信息，请参阅 Simulate in RoadRunner Scene (Simulink 3D Animation)。

**提示**

Simulation 3D Camera 和 Simulation 3D Lidar 中的语义分割使用 XML (`.rrdata.xml`) 文件。ASAM OpenDRIVE (`.xodr`) 文件提供对象数据和车道真值数据，供 Simulation 3D Vision Detection Generator 生成检测。当您将 Filmbox (`.fbx`) 或 Universal Scene Description (USD) 文件指定为 **Project** 参数时，请检查 XML (`.rrdata.xml`) 和 ASAM OpenDRIVE (`.xodr`) 文件是否在同一文件夹中。

**注意**

Linux® 上不支持 USD 和 RoadRunner 场景或 scenario (`.rrscene` 或 `.rrscenario`) 文件导入。

#### 依赖关系

要启用此参数，请将 **Scene source** 设置为 `Unreal Editor` 或 `RoadRunner`。

#### 场景参数

### **Scene view** — 显示场景的虚拟摄像机的位置 `Scene Origin` (默认) | `Custom` | 车辆名称 | `sim3d` actor 名称 | 视点名称

配置虚拟摄像机的位置，以设置仿真期间显示场景的视点。**Scene view** 参数列表将填充模型中所有车辆和 actor 模块的 **Name** 参数值，以及您创建的任何其他自定义视点。如果向模型添加 Simulation 3D Scene Configuration 模块，虚拟摄像机将保持在场景原点。要将摄像机重新定位到自定义视点或跟随车辆或 actor，请更新此参数。

下表列出了模型不包含车辆模块、actor 模块或自定义视点时 **Scene view** 参数的选项。

| 选项 | 描述 |
| --- | --- |
| `Custom` | - 创建自定义视点。此选项启用以下参数。  - **Name**   - **Translation**   - **Rotation** - 点击 **Save Viewpoint** 创建视点。 - 在自由摄像机模式下查看场景。摄像机移动使用世界坐标系。 |
| `Scene Origin` | - 将视点设置在场景原点。 - 在自由摄像机模式下查看场景。摄像机移动使用世界坐标系。 |

下表列出了模型包含车辆模块、actor 模块或自定义视点时的其他选项。

| 选项 | 描述 |
| --- | --- |
| 车辆名称 | - 将虚拟摄像机附加到模型中所选车辆模块。 - 只能更改摄像机围绕车辆的位置。 |
| `sim3d` actor 名称 | - 将虚拟摄像机附加到模型中所选 Simulation 3D Actor 模块。 - 此选项启用以下参数，以设置摄像机相对于 actor 原点的位置。  - **Viewer relative translation [X, Y, Z] (m)**   - **Viewer relative rotation [Roll, Pitch, Yaw] (deg)** |
| 视点名称 | - 将视点设置为所选视点名称。此选项还启用以下参数。  - **Name**   - **Translation**   - **Rotation** - 点击 **Save Viewpoint** 更新视点。 - 点击 **Delete Viewpoint** 将其移除。 - 在自由摄像机模式下查看场景。摄像机移动使用世界坐标系。 |

**场景控制**

当 **Scene view** 设置为 `Scene Origin` 或 `Custom` 时，您可以在仿真期间使用键盘和鼠标控制来更改摄像机的位置以在场景中导航。仿真暂停时也可以更改摄像机位置。

要在 3D 环境中导航，请使用以下键盘快捷键。

| 键盘快捷键 | 摄像机控制 |
| --- | --- |
| **W** | 向前移动。 |
| **Shift+W** | 沿向前方向更快移动。 |
| **S** | 向后移动。 |
| **Shift+S** | 沿反向更快移动。 |
| **A** | 向左移动。 |
| **Shift+A** | 向左更快移动。 |
| **D** | 向右移动。 |
| **Shift+D** | 向右更快移动。 |
| **E** | 向上移动。 |
| **Shift+E** | 沿向上方向更快移动。 |
| **Q** | 向下移动。 |
| **Shift+Q** | 沿向下方向更快移动。 |
| 鼠标滚轮 | 控制摄像机到光标点的距离。 |
| **Shift**+鼠标滚轮 | 摄像机移动更快。 |
| 鼠标右键单击并拖动 | 围绕光标点旋转。 |
| **O** | 将摄像机附加到光标点下的 actor，包括车辆、行人或骑行者。 |
| 鼠标左键单击并拖动 | 摄像机附加到 actor 后，围绕该 actor 旋转。 |
| **P** | 从 actor 分离摄像机。 |
| **L** | 记录当前视点，并在场景上显示 `Location saved`。 |
| **1 到 9** | 访问存储的视点（如果可用）。 |
| **Tab** | 在场景中的所有车辆与仿真开始时的视点之间向前循环切换视图。 |
| **Shift+Tab** | 在场景中的所有车辆与仿真开始时的视点之间向后循环切换视图。 |
| **I** | 在屏幕上切换键盘快捷键的显示。按一次显示，再按一次隐藏。 |

**车辆视图**

当 **Scene view** 设置为车辆名称时，在仿真期间，可以更改摄像机围绕车辆的位置。还可以在仿真期间按 **Tab** 将视图设置为车辆。

要平滑更改摄像机视图，请使用以下键盘快捷键。

| 键盘快捷键 | 摄像机视图 | |
| --- | --- | --- |
| **1** | 左后 | 示意图显示了与摄像机视图对应的数字键命令   查看动画 GIF  摄像机视图的动画 gif |
| **2** | 后 |
| **3** | 右后 |
| **4** | 左 |
| **5** | 内部 |
| **6** | 右 |
| **7** | 左前 |
| **8** | 前 |
| **9** | 右前 |
| **0** | 顶置 |

有关其他摄像机控制，请使用以下键盘快捷键。

| 键盘快捷键 | 摄像机控制 |
| --- | --- |
| **Tab** | 在场景中的所有车辆之间循环切换视图。  查看动画 GIF  在场景中所有车辆之间循环切换视图的动画 gif |
| 鼠标滚轮 | 控制摄像机到车辆的距离。  查看动画 GIF  摄像机距离控制的动画 gif |
| **L** | 打开或关闭摄像机滞后效果。启用滞后效果后，摄像机视图包括：  - 位置滞后，基于车辆平移加速度 - 旋转滞后，基于车辆旋转速度  此滞后可改善整体车辆加速度和旋转的可视化。  查看动画 GIF  摄像机滞后效果的动画 gif |
| **F** | 打开或关闭自由摄像机模式。启用自由摄像机模式后，可以使用鼠标更改摄像机的俯仰角和偏航角。此模式允许您围绕车辆旋转摄像机。  查看动画 GIF  自由摄像机模式的动画 gif |

### **Name** — 自定义视点的名称 `custom` (默认) | 字符数组 | 字符串标量

*自 R2025a 起*

将自定义视点的名称指定为字符数组或字符串标量。

**示例：** `View1`

#### 依赖关系

要启用此参数，请将 **Scene view** 设置为 `Custom`。

**数据类型：** `char` | `string`

### **Translation** — 视点平移 `[0 0 0]` (默认) | 实数 1×3 向量

*自 R2025a 起*

将视点平移 (*x*,*y*,*z*) 指定为实数 1×3 向量，以 m 为单位。

#### 依赖关系

要启用此参数，请将 **Scene view** 设置为 `Custom`。

**数据类型：** `double`

### **Rotation** — 视点旋转 `[0 0 0]` (默认) | 实数 1×3 向量

*自 R2025a 起*

将视点旋转 (*roll*, *pitch*, *yaw*) 指定为实数 1×3 向量，以 deg 为单位。

#### 依赖关系

要启用此参数，请将 **Scene view** 设置为 `Custom`。

**数据类型：** `double`

### **Viewer relative translation [X, Y, Z] (m)** — 视点相对于 actor 的平移 `[0 0 0]` (默认) | 实数 1×3 向量

*自 R2025a 起*

将视点平移 (*x*,*y*,*z*) 相对于 `sim3d` actor 原点指定为实数 1×3 向量，以 m 为单位。

#### 依赖关系

要启用此参数，请将 **Scene view** 设置为 `sim3d` actor 名称。

**数据类型：** `double`

### **Viewer relative rotation [Roll, Pitch, Yaw] (deg)** — 视点相对于 actor 的旋转 `[0 0 0]` (默认) | 实数 1×3 向量

*自 R2025a 起*

将视点旋转 (*roll*, *pitch*, *yaw*) 相对于 `sim3d` actor 原点指定为实数 1×3 向量，以 deg 为单位。

#### 依赖关系

要启用此参数，请将 **Scene view** 设置为 `sim3d` actor 名称。

**数据类型：** `double`

### **Sample time** — 可视化引擎的采样时间 `1/60` (默认) | 实数正标量

可视化引擎的采样时间 *Ts*，指定为实数正标量。单位为秒。

可视化引擎的图形帧速率是采样时间的倒数。例如，如果 **Sample time** 为 `1/60`，则可视化引擎求解器会尝试达到每秒 60 帧的帧速率。但是，实时图形帧速率通常较低，原因包括显卡性能和模型复杂度等因素。

默认情况下，从可视化引擎接收数据的模块继承此采样率。

### **Display 3D simulation window** — Unreal Engine 可视化 `on` (默认) | `off`

选择是否在 3D 可视化环境中运行仿真而不可视化结果，即以 *无头模式* 运行。

在以下情况下，考虑以无头模式运行：

- 希望并行运行多个 3D 仿真，以在不同 Unreal Engine 场景中测试模型。
- 希望捕获传感器数据以在 MATLAB 中分析，但不需要观看可视化。

#### 依赖关系

要启用此参数，请将 **Scene source** 设置为 `Default Scenes` 或 `Unreal Executable`。

### 天气

### **Override scene weather** — 用于控制场景天气和太阳位置的选项 `off` (默认) | `on`

选择是否在仿真期间控制场景天气和太阳位置。使用启用的参数更改太阳位置、云、雾、雨和雪。

下表总结了特定一天中时间的太阳位置设置。

| 一天中时间 | 设置 | Unreal Editor 环境 |
| --- | --- | --- |
| 午夜 | **Sun altitude**: -90  **Sun azimuth**: 180 | 午夜的道路 |
| 北部日出 | **Sun altitude**: 0  **Sun azimuth**: 180 | 日出时的道路 |
| 正午 | **Sun altitude**: 90  **Sun azimuth**: 180 | 正午的道路 |

下表总结了特定云条件的设置。

| 云条件 | 设置 | Unreal Editor 环境 |
| --- | --- | --- |
| 晴朗 | **Cloud opacity**: 0 | 晴朗天空的道路 |
| 厚重 | **Cloud opacity**: 85 | 多云的天空的道路 |
| 厚重 | **Enable Volumetric clouds**: 选中  **Cloud Coverage**: 50  **Cloud layer altitude**: 6 | 带有体积云的道路 |

下表总结了特定雾条件的设置。

| 雾条件 | 设置 | Unreal Editor 环境 |
| --- | --- | --- |
| 无 | **Fog density**: 0 | 无雾的道路 |
| 浓雾 | **Fog density**: 100 | 浓雾的道路 |

下表总结了特定雨条件的设置。

| 雨条件 | 设置 | Unreal Editor 环境 |
| --- | --- | --- |
| 小雨 | **Cloud opacity**: 10  **Rain density**: 25 | 小雨的城市场景 |
| 大雨 | **Cloud opacity**: 10  **Rain density**: 80 | 大雨的城市场景 |

下表总结了特定雪条件的设置。

| 雪条件 | 设置 | Unreal Editor 环境 |
| --- | --- | --- |
| 大雪 | **Snow density**: 50 | 大雪的道路场景 |

#### 太阳

### **Sun azimuth** — 从南到太阳光线水平投影的方位角 `90` (默认) | `0` 到 `360` 之间的任意值

在水平面中从南到太阳光线水平投影测量的方位角，以 deg 为单位。

太阳高度角（垂直箭头）和太阳方位角（水平箭头）示意图

使用 **Sun altitude** 和 **Sun azimuth** 参数控制场景中的一天中时间。例如，要指定北部日出，请将 **Sun altitude** 设置为 0 deg，将 **Sun azimuth** 设置为 180 deg。

#### 依赖关系

要启用此参数，请选择 **Override scene weather**。

### **Sun altitude** — 太阳与地平线之间的高度角 `40` (默认) | `-90` 到 `90` 之间的任意值

在垂直面中太阳光线与光线水平投影之间的高度角，以 deg 为单位。

太阳高度角（垂直箭头）和太阳方位角（水平箭头）示意图

使用 **Sun altitude** 和 **Sun azimuth** 参数控制场景中的一天中时间。例如，要指定北部日出，请将 **Sun altitude** 设置为 0 deg，将 **Sun azimuth** 设置为 180 deg。

#### 依赖关系

要启用此参数，请选择 **Override scene weather**。

### **Enable geospatial sun** — 启用地理空间太阳的选项 `off` (默认) | `on`

选中此复选框以启用地理空间太阳。启用地理空间太阳有助于仿真极点附近或昼夜长度不成比例的位置的条件。

#### 依赖关系

要启用此参数，请选择 **Override scene weather**。

### **Latitude** — 地球上地理位置的纬度 `0` (默认) | 标量

地球上地理位置的纬度，指定为标量，以 deg 为单位。

#### 依赖关系

要启用此参数，请选择 **Override scene weather** 和 **Enable geospatial sun**。

### **Longitude** — 地球上地理位置的经度 0 (默认) | 标量

地球上地理位置的经度，指定为标量，以 deg 为单位。

#### 依赖关系

要启用此参数，请选择 **Override scene weather** 和 **Enable geospatial sun**。

### **Date (YYYY-MM-DD)** — 日期 2023-01-01 (默认) | 整数

日期，指定为格式为 `YYYY-MM-DD` 的整数。

#### 依赖关系

要启用此参数，请选择 **Override scene weather** 和 **Enable geospatial sun**。

### **Time (HH:MM:SS)** — 时间 `10:30:00` (默认) | 整数

时间，指定为格式为 `HH:MM:SS` 的整数。

#### 依赖关系

要启用此参数，请选择 **Override scene weather** 和 **Enable geospatial sun**。

### **Time zone** — 时区 `-5.0` (默认) | `-12.0` 到 `12.0` 之间的任意值

时区指定与协调世界时 (UTC) 或格林尼治标准时间 (GMT) 的小时偏移量。

#### 依赖关系

要启用此参数，请选择 **Override scene weather** 和 **Enable geospatial sun**。

### **Daylight saving time** — 启用夏令时的选项 `off` (默认) | `on`

选中此复选框以启用夏令时。

#### 依赖关系

要启用此参数，请选择 **Override scene weather** 和 **Enable geospatial sun**。

#### 云

### **Cloud speed** — Unreal Editor Cloud Speed 全局 actor 目标值 `1` (默认) | `-100` 到 `100` 之间的任意值

对应于 Unreal Editor **Cloud Speed** 全局 actor 目标值的参数。对于正值，云从西向东移动；对于负值，云从东向西移动。

Unreal Editor 中的 Cloud Opacity 和 Cloud Speed 设置

使用 **Cloud opacity** 和 **Cloud speed** 参数控制场景中的云。

#### 依赖关系

要启用此参数，请选择 **Override scene weather**。

### **Cloud opacity** — Unreal Editor Cloud Opacity 全局 actor 目标值 `10` (默认) | `0` 到 `100` 之间的任意值

对应于 Unreal Editor **Cloud Opacity** 全局 actor 目标值的参数，以百分比为单位。零表示无云场景。

Unreal Editor 中的 Cloud Opacity 和 Cloud Speed 设置

使用 **Cloud opacity** 和 **Cloud speed** 参数控制场景中的云。

#### 依赖关系

要启用此参数，请选择 **Override scene weather**。

### **Enable volumetric clouds** — 启用体积云的选项 `off` (默认) | `on`

选中此复选框以启用体积云。

#### 依赖关系

要启用此参数，请选择 **Override scene weather**。

### **Cloud coverage** — Unreal Editor Cloud Density 全局目标值 `1.0` (默认) | `0` 到 `100` 之间的任意值

对应于 Unreal Editor **Cloud Density** 全局 actor 目标值的参数，以百分比为单位。

Unreal Editor 中的云覆盖率设置

使用 **Cloud coverage** 参数控制场景中的云。

#### 依赖关系

要启用此参数，请选择 **Override scene weather** 和 **Enable volumetric clouds**。

### **Cloud layer altitude** — Unreal Editor Layer Bottom Altitude 全局 actor 目标值 `6` (默认) | `5` 到 `20` 之间的任意值

对应于 Unreal Editor **Layer Bottom Altitude** 全局 actor 目标值的参数，以 km 为单位。

Unreal Editor 中的云高度设置

#### 依赖关系

要启用此参数，请选择 **Override scene weather** 和 **Enable volumetric clouds**。

#### 雾

### **Fog density** — Unreal Editor Set Fog Density 和 Set Start Distance 目标值 `0` (默认) | `0` 到 `100` 之间的任意值

对应于 Unreal Editor **Set Fog Density** 和 **Set Start Distance** 目标值的参数，以百分比为单位。

Unreal Editor 中的 Set Fog Density 设置

#### 依赖关系

要启用此参数，请选择 **Override scene weather**。

#### 雨

### **Rain density** — 控制雨密度、湿度、雨坑和涟漪的 Unreal Editor 本地 actor `0` (默认) | `0` 到 `100` 之间的任意值

对应于控制雨密度、湿度、雨坑和涟漪的 Unreal Editor 本地 actor 的参数，以百分比为单位。

用于控制雨密度的 Unreal Editor 设置。左侧的 Get Components by Class 激活或停用雨密度设置。右侧的雨效果控制湿度、雨坑和涟漪等设置。

使用 **Cloud opacity** 和 **Rain density** 参数控制场景中的雨。

#### 依赖关系

要启用此参数，请选择 **Override scene weather**。

### **Enable raindrops on camera lens** — 启用摄像机镜头上的雨滴的选项 `off` (默认) | `on`

选中此复选框以启用摄像机镜头上的雨滴。

Unreal Editor 中的云高度设置

#### 依赖关系

要启用此参数，请选择 **Override scene weather**。

#### 雪

### **Snow density** — 控制雪密度的 Unreal Editor 全局 actor `0` (默认) | `0` 到 `100` 之间的任意值

此参数对应于控制雪密度的 Unreal Editor 全局 actor，以百分比为单位。

Unreal Editor 中的云高度设置

#### 依赖关系

要启用此参数，请选择 **Override scene weather**。

## 所属库

Offroad Autonomy Library / Simulation 3D Aerospace Blockset / Animation / Simulation 3D Automated Driving Toolbox / Simulation 3D Robotics System Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Environment UAV Toolbox / Simulation 3D Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Core

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

### R2025a: 将 USD 和 RoadRunner 场景或 scenario 文件导入 Unreal Engine 仿真环境

可以导入以下 RoadRunner 场景文件：

- Universal Scene Description (`.usd`、`.usdc` 和 `.usda`) 文件
- RoadRunner 场景或 scenario (`.rrscene` 或 `.rrscenario`) 文件

要指定场景来源，请将 **Scene source** 参数设置为 `RoadRunner`。然后，在 **Project** 参数中，指定相应的 RoadRunner 场景文件。

### R2025a: 创建 3D 环境的多个视图

可以使用 **Scene view** 参数中的 `Custom` 选项创建自定义视点。此选项启用以下参数。

- **Name**
- **Translation**
- **Rotation**

可以保存视点，以视点名称填充 **Scene view** 参数列表。选择该视点以设置场景的视图。还可以编辑或删除视点。

### R2025a: 设置相对于 `sim3d` actor 的场景视图

可以将 **Scene view** 参数设置为模型中包含的 Simulation 3D Actor 模块的 **Name** 参数。此选项启用以下参数，以设置摄像机相对于 actor 原点的位置。

- **Viewer relative translation [X, Y, Z] (m)**
- **Viewer relative rotation [Roll, Pitch, Yaw] (deg)**

### R2025a: 安装其他场景

除了默认场景之外，还可以下载并安装 Unreal Engine 环境中可用于 3D 仿真的任何预构建 3D 场景。

要选择和下载场景，请点击 **Install**。安装场景后，MATLAB 将重新启动。现在可以从 **Scene view** 参数列表中选择已安装的场景。

### R2024a: 需要 Simulink 3D Animation

使用 Simulation 3D Scene Configuration 模块仿真模型需要 Simulink 3D Animation。

### R2024a: 新增参数可用于仿真其他天气条件

使用新的天气参数来仿真其他天气条件。

| 天气 | 参数 |
| --- | --- |
| **Sun** | - **Enable geospatial sun** - **Latitude** - **Longitude** - **Date** - **Time** - **Daylight saving time** |
| **Cloud** | - **Enable volumetric clouds** - **Cloud coverage** - **Cloud layer altitude** |
| **Rain** | - **Enable raindrops on camera lens** |
| **Snow** | - **Snow density** |

### R2023b: 将 RoadRunner 场景导入 Unreal Engine 仿真环境

使用 Simulation 3D Scene Configuration 模块导入 RoadRunner 场景并在该场景中进行仿真。要指定场景来源，请将 **Scene source** 参数选择为 `RoadRunner`。然后，在 **Project** 参数中，指定对应于 RoadRunner 场景的 Filmbox `(.fbx)` 文件。有关示例，请参阅 Import RoadRunner Scene into Unreal Engine Using Simulink (Simulink 3D Animation)。

### R2023b: 摄像机视图改进以查看虚拟世界

使用 Simulation 3D Scene Configuration 模块从位于自定义视点的摄像机查看虚拟世界。要设置自定义视点，请将 **Scene view** 选择为 `Custom`，并设置 **Initial viewer translation** 和 **Initial viewer rotation** 值。还可以使用键盘快捷键和鼠标控件在虚拟世界场景中导航。

## 描述

3D 仿真环境的场景配置

**注意**

使用 Simulation 3D Scene Configuration 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Scene Configuration 模块实现了一个 3D 仿真环境，该环境使用 Epic Games® 的 Unreal Engine® 渲染。Automated Driving Toolbox™ 将 3D 仿真环境与 Simulink 集成，以便您可以查询车辆周围的世界，并虚拟测试感知、控制和规划算法。使用此模块，还可以控制场景的太阳位置和天气条件。有关更多详细信息，请参阅 Sun Position and Weather。

可以从一组预构建场景或您自己的自定义场景进行仿真。场景自定义需要 Automated Driving Toolbox Interface for Unreal Engine Projects 支持包。有关更多详细信息，请参阅 Customize Unreal Engine Scenes for Automated Driving。

还可以仿真在 RoadRunner 中设计和构建的自定义场景。为此，必须首先从 RoadRunner 导出场景，并在 Simulation 3D Scene Configuration 模块的 **Project** 参数中指定导出场景工件的路径。

**提示**

Simulation 3D Scene Configuration 模块必须在向 3D 环境发送数据的模块之后执行，并在从 3D 环境接收数据的模块之前执行。要验证此类模块的执行顺序，请右键点击模块并选择 **Properties**。然后，在 **General** 选项卡上，确认以下 **Priority** 设置：

- 对于向 3D 环境发送数据的模块，例如 Simulation 3D Vehicle with Ground Following 模块，**Priority** 必须设置为 `-1`，以便这些模块可以在 3D 环境接收数据之前准备数据。
- 对于模型中的 Simulation 3D Scene Configuration 模块，**Priority** 必须设置为 `0`。
- 对于从 3D 环境接收数据的模块，例如 Simulation 3D Camera 模块，**Priority** 必须设置为 `1`，以便 3D 环境可以在这些模块接收数据之前准备数据。

有关执行顺序的详细信息，请参阅 How Unreal Engine Simulation for Automated Driving Works。
