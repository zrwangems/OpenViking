---
type: simulink-block
title: 'Simulation 3D Scene Configuration'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Simulation 3D'
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

### **场景源** — 场景的来源 `Default Scenes`（默认）| `RoadRunner` | `Unreal Executable` | `Unreal Editor`

用于仿真的场景来源，指定为表中的选项之一。

| 选项 | 描述 |
| --- | --- |
| `Default Scenes` | 在 **场景名称** 参数中指定的默认预构建场景之一中进行仿真。 |
| `RoadRunner` | 在 RoadRunner 场景中进行仿真。要导入 RoadRunner 场景，请在 **工程** 参数中指定相应的文件。可以使用以下文件格式。 - Filmbox（`.fbx`）文件。 - Universal Scene Description（`.usd`、`.usdc` 和 `.usda`）文件。 - RoadRunner 场景或场景剧本（`.rrscene` 或 `.rrscenario`）文件。 |
| `Unreal Executable` | 在属于 Unreal Engine 可执行文件一部分的场景中进行仿真。在 **工程名称** 参数中指定可执行文件。在 **场景** 参数中指定场景。选择此选项可在已打包为可执行文件的自定义场景中进行仿真，以实现更快的仿真速度。 |
| `Unreal Editor` | 在属于 Unreal Engine 工程（`.uproject`）文件一部分且已在 Unreal® Editor 中打开的场景中进行仿真。在 **工程** 参数中指定工程文件。在开发自定义场景时选择此选项。通过点击 **打开 Unreal Editor**，您可以在 Simulink 和 Unreal Editor 中进行协同仿真，并根据仿真结果修改场景。 |

### **场景名称** — 预构建 3D 场景的名称 `US city block` | `Suburban scene`

用于仿真的预构建 3D 场景的名称，指定为以下选项之一。有关场景的详细信息，请参阅其列出的相应参考页。

- `US city block` – US City Block
- `Suburban scene` – Suburban scene

#### 依赖关系

要启用此参数，请将 **场景源** 设置为 `Default Scenes`。

### **工程名称** — Unreal Engine 可执行文件的名称 `VehicleSimulation.exe`（默认）| 有效的可执行文件名

Unreal Engine 可执行文件的名称，指定为有效的可执行工程文件名。您可以浏览该文件，或使用反斜杠指定工程文件的完整路径。要指定此文件中用于仿真的场景，请使用 **场景** 参数。

默认情况下，**工程名称** 设置为 `VehicleSimulation.exe`，该文件位于 MATLAB® 搜索路径中。

**注意**

如果您选择使用与当前 MATLAB 版本不兼容的 Unreal Engine 版本构建的自定义 Unreal 可执行文件，您将收到以下错误消息之一：

- `"Incompatible version of 3D Simulation engine: Undefined"`：对于为 R2023b 之前的 MATLAB 版本构建的 Unreal 可执行文件
- `"Incompatible version of 3D Simulation engine: 23.2.0"`：对于为 MATLAB R2023b 或更高版本构建的 Unreal 可执行文件

要解决这些错误，您必须迁移 Unreal 工程，并使用已安装的最新支持包重新构建可执行文件。有关详细信息，请参阅 Migrate Projects Developed Using Prior Support Packages。

**示例：** `C:\Local\WindowsNoEditor\AutoVrtlEnv.exe`

#### 依赖关系

要启用此参数，请将 **场景源** 设置为 `Unreal Executable`。

### **Project** — Unreal Engine 项目文件或 RoadRunner 文件的名称，有效的项目文件名

Unreal Engine 项目文件或 RoadRunner 文件的名称，指定为有效的项目文件名。您可以浏览文件，或使用反斜杠指定文件的完整路径。文件名不得包含空格。

要在 Unreal Editor 中模拟 Unreal Engine 项目文件的场景，请点击 **Open Unreal Editor**。如果您已经打开了 Unreal Editor 会话，则此按钮将被禁用。

要运行仿真，请在 Simulink 中点击 **Run**。在 Unreal Editor 中点击 **Play** 之前，请等待 Diagnostic Viewer 窗口显示以下确认消息：

```
In the Simulation 3D Scene Configuration block, you set the scene source to 'Unreal Editor'.
In Unreal Editor, select 'Play' to view the scene.
```

此消息确认 Simulink 已在 Unreal Engine 3D 环境中实例化场景 actor，包括车辆和相机。如果您在 Diagnostic Viewer 窗口显示此确认消息之前点击 **Play**，Simulink 可能不会在 Unreal Editor 中实例化 actor。

要模拟 RoadRunner 场景，您可以导入 Filmbox（`.fbx`）、Universal Scene Description（USD）、RoadRunner 场景（`.rrscene`）或 RoadRunner 场景（`.rrscenario`）格式的文件。

- 要模拟 Filmbox（`.fbx`）格式的场景，请浏览包含导出的 RoadRunner 场景文件的文件夹，并指定 `.fbx` 文件。您可以使用 Export Using CARLA Filmbox (RoadRunner) 中的 **CARLA** **Filmbox** 选项导出 RoadRunner 场景。此选项将以下三个文件导出到一个文件夹：

  - Filmbox（`.fbx`）文件
  - ASAM OpenDrive（`.xodr`）文件
  - XML（`.rrdata.xml`）文件
- 要模拟 Universal Scene Description（USD）格式的场景，请浏览包含导出的 RoadRunner 场景文件的文件夹，并选择 `.usd`、`.usdc` 或 `.usda` 文件。从 USD 文件导入的 actor 与碰撞检测不兼容。要以 USD 格式导出 RoadRunner 场景，请参阅 Export to USD (RoadRunner)。
- 要模拟 RoadRunner 场景或场景（`.rrscene` 或 `.rrscenario`）格式的场景，请浏览包含 RoadRunner 文件的文件夹，并选择相应的文件。在仿真之前，您必须使用 `roadrunnerSetup` (RoadRunner) 函数配置 RoadRunner 与 MATLAB 的集成。

  - 在 MATLAB 命令窗口中输入 `roadrunnerSetup` 函数。
  - RoadRunner Setup 对话框打开。
  - 指定 **RoadRunner Project Folder** 和 **RoadRunner Installation Folder** 位置。

有关导出和模拟 RoadRunner 场景的更多信息，请参阅 Simulate in RoadRunner Scene。

**注意**

Linux® 上不支持 USD 和 RoadRunner 场景或场景（`.rrscene` 或 `.rrscenario`）文件导入。

#### 依赖关系

要启用此参数，请将 **Scene source** 设置为 `Unreal Editor` 或 `RoadRunner`。

#### 场景参数

### **Scene view** — 用于显示场景的虚拟相机放置 `Scene Origin`（默认）| `Custom` | 车辆名称 | `sim3d` actor 名称 | 视点名称

配置虚拟相机的放置，以设置在仿真期间显示场景的视点。**Scene view** 参数列表会填充模型中车辆和 actor 模块的所有 **Name** 参数值，以及您创建的任何其他自定义视点。如果向模型中添加 Simulation 3D Scene Configuration 模块，虚拟相机将保持在场景原点位置。要将相机重新定位到自定义视点或跟随车辆或 actor，请更新此参数。

如果您的模型不包含车辆模块、actor 模块或自定义视点，下表列出了 **Scene view** 参数选项。

| 选项 | 描述 |
| --- | --- |
| `Custom` | - 创建自定义视点。此选项会启用以下参数。  - **Name**   - **Translation**   - **Rotation** - 点击 **Save Viewpoint** 以创建视点。 - 在自由相机模式下查看场景。相机移动使用世界坐标系。 |
| `Scene Origin` | - 将视点设置在场景原点。 - 在自由相机模式下查看场景。相机移动使用世界坐标系。 |

如果您的模型包含车辆模块、actor 模块或自定义视点，下表列出了其他选项。

| 选项 | 描述 |
| --- | --- |
| 车辆名称 | - 将虚拟相机附加到模型中选定的车辆模块。 - 您只能更改相机围绕车辆的位置。 |
| `sim3d` actor 名称 | - 将虚拟相机附加到模型中选定的 Simulation 3D Actor 模块。 - 此选项会启用以下参数，以设置相机相对于 actor 原点的位置。  - **Viewer relative translation [X, Y, Z]     (m)**   - **Viewer relative rotation [Roll, Pitch, Yaw]     (deg)** |
| 视点名称 | - 将视点设置为选定的视点名称。此选项还会启用以下参数。  - **Name**   - **Translation**   - **Rotation** - 点击 **Save Viewpoint** 以更新视点。 - 点击 **Delete Viewpoint** 以移除它。 - 在自由相机模式下查看场景。相机移动使用世界坐标系。 |

**Scene Controls**

当 **Scene view** 设置为 `Scene Origin` 或 `Custom` 时，您可以在仿真期间使用键盘和鼠标控制来更改相机位置以在场景中导航。您也可以在仿真暂停时更改相机位置。

要在 3D 环境中导航，请使用以下键盘快捷键。

| 键盘快捷键 | 相机控制 |
| --- | --- |
| **W** | 向前移动。 |
| **Shift+W** | 沿向前方向更快移动。 |
| **S** | 向后移动。 |
| **Shift+S** | 沿反向方向更快移动。 |
| **A** | 向左移动。 |
| **Shift+A** | 向左更快移动。 |
| **D** | 向右移动。 |
| **Shift+D** | 向右更快移动。 |
| **E** | 向上移动。 |
| **Shift+E** | 沿向上方向更快移动。 |
| **Q** | 向下移动。 |
| **Shift+Q** | 沿向下方向更快移动。 |
| 鼠标滚轮 | 控制相机与光标点之间的距离。 |
| **Shift**+鼠标滚轮 | 相机移动更快。 |
| 鼠标右键单击并拖动 | 围绕光标点旋转。 |
| **O** | 将相机附加到光标点下的 actor。 |
| 鼠标左键单击并拖动 | 相机附加到 actor 后，围绕该 actor 旋转。 |
| **P** | 将相机从 actor 分离。 |
| **L** | 记录当前视点并在场景上显示 `Location saved`。 |
| **1 到 9** | 访问已存储的视点（如果可用）。 |
| **Tab** | 在场景中所有车辆与仿真开始时的视点之间正向循环切换视图。 |
| **Shift+Tab** | 在场景中所有车辆与仿真开始时的视点之间反向循环切换视图。 |
| **I** | 切换屏幕上键盘快捷键的显示。按一次显示，再按一次隐藏。 |

**车辆视图**

当 **Scene view** 设置为某个车辆名称时，在仿真期间，
您可以更改相机围绕该车辆的位置。您还可以在仿真期间按 **Tab** 将视图设置为某个车辆。

要平滑地更改相机视图，请使用以下键盘
快捷键。

| 键盘快捷键 | 相机视图 | |
| --- | --- | --- |
| **1** | 左后方 | 一张图显示了与相机视图对应的数字键命令     查看动画 GIF  相机视图的动画 gif |
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
| **Tab** | 在场景中所有车辆之间循环切换视图。  查看动画 GIF  在场景中所有车辆之间循环切换视图的动画 gif |
| 鼠标滚轮 | 控制相机与车辆之间的距离。  查看动画 GIF  相机距离控制的动画 gif |
| **L** | 打开或关闭相机滞后效果。启用滞后效果后，相机视图包括：  - 位置滞后，基于车辆平移   加速度 - 旋转滞后，基于车辆旋转   速度  此滞后可改善整体车辆加速度和旋转的可视化效果。  查看动画 GIF  相机滞后效果的动画 gif |
| **F** | 打开或关闭自由相机模式。启用自由相机模式后，您可以使用鼠标更改相机的俯仰角和偏航角。此模式允许您围绕车辆旋转相机。  查看动画 GIF  自由相机模式的动画 gif |

### **Name** — 自定义视点的名称 `custom`（默认）| 字符数组 | 字符串标量

*自 R2025a 起*

将自定义视点的名称指定为字符数组或字符串
标量。

**示例：** `View1`

#### 依赖关系

要启用此参数，请将 **Scene view** 设置为
`Custom`。

**数据类型：** `char` | `string`

### **Translation** — 视点平移 `[0 0 0]`（默认）| 实数 1×3 向量

*自 R2025a 起*

将视点平移
(*x*,*y*,*z*) 指定为实数 1×3
向量，单位为 m。

#### 依赖关系

要启用此参数，请将 **Scene view** 设置为
`Custom`。

**数据类型：** `double`

### **Rotation** — 视点旋转 `[0 0 0]`（默认）| 实数 1×3 向量

*自 R2025a 起*

将视点旋转（*roll*、*pitch*、
*yaw*）指定为实数 1×3 向量，单位为 deg。

#### 依赖关系

要启用此参数，请将 **Scene view** 设置为
`Custom`。

**数据类型：** `double`

### **Viewer relative translation [X, Y, Z] (m)** — 相对于 actor 的视点平移 `[0 0 0]`（默认）| 实数 1×3 向量

*自 R2025a 起*

将相对于 `sim3d` actor 原点的视点平移
(*x*,*y*,*z*) 指定为实数 1×3 向量，单位为 m。

#### 依赖关系

要启用此参数，请将 **Scene view** 设置为
`sim3d` actor 名称。

**数据类型：** `double`

### **Viewer relative rotation [Roll, Pitch, Yaw] (deg)** — 相对于 actor 的视点旋转 `[0 0 0]`（默认）| 实数 1×3 向量

*自 R2025a 起*

将相对于 `sim3d` actor 原点的视点旋转（*roll*、*pitch*、
*yaw*）指定为实数 1×3 向量，单位为 deg。

#### 依赖关系

要启用此参数，请将 **Scene view** 设置为
`sim3d` actor 名称。

**数据类型：** `double`

### **Sample time** — 可视化引擎的采样时间 `1/60`（默认）| 实数正标量

可视化引擎的采样时间 *Ts*，指定为实数正标量。单位为秒。

可视化引擎的图形帧率是采样时间的倒数。例如，如果 **Sample time** 为
`1/60`，则可视化引擎求解器尝试达到每秒 60 帧的帧率。但是，由于显卡性能和模型
复杂度等因素，实时图形帧率通常较低。

默认情况下，从可视化引擎接收数据的模块继承此采样率。

### **Display 3D simulation window** — Unreal Engine 可视化 `on`（默认）| `off`

选择是否在 3D 可视化环境中运行仿真而不可视化结果，即以*无头模式*运行。

在以下情况下，请考虑以无头模式运行：

- 您希望并行运行多个 3D 仿真，以在不同 Unreal Engine 场景中测试模型。

#### 依赖关系

要启用此参数，请将 **Scene source** 设置为
`Default Scenes` 或 `Unreal
Executable`。

### 天气

### **Override scene weather** — 用于控制场景天气和太阳位置的选项 `off`（默认）| `on`

选择是否在仿真期间控制场景天气和太阳位置。
使用已启用的参数更改太阳位置、云、雾、雨和
雪。

此表总结了特定一天中时间的太阳位置设置。

| 一天中时间 | 设置 | Unreal Editor 环境 |
| --- | --- | --- |
| 午夜 | **Sun altitude**：-90  **Sun azimuth**：180 | 午夜道路 |
| 北方日出 | **Sun altitude**：0  **Sun azimuth**：180 | 日出道路 |
| 正午 | **Sun altitude**：90  **Sun azimuth**：180 | 正午道路 |

此表总结了特定云条件的设置。

| 云条件 | 设置 | Unreal Editor 环境 |
| --- | --- | --- |
| 晴朗 | **Cloud opacity**：0 | 晴朗天空道路 |
| 厚重 | **Cloud opacity**：85 | 多云天空道路 |
| 厚重 | **Enable Volumetric clouds**：已选择  **Cloud Coverage**：50  **Cloud layer altitude**：6 | 体积云道路 |

此表总结了特定雾条件的设置。

| 雾条件 | 设置 | Unreal Editor 环境 |
| --- | --- | --- |
| 无 | **Fog density**：0 | 无雾道路 |
| 浓重 | **Fog density**：100 | 浓雾道路 |

此表总结了特定雨条件的设置。

| 雨条件 | 设置 | Unreal Editor 环境 |
| --- | --- | --- |
| 小雨 | **Cloud opacity**：10  **Rain density**：25 | 小雨城市场景 |
| 大雨 | **Cloud opacity**：10  **Rain density**：80 | 大雨城市场景 |

此表总结了特定雪条件的设置。

| 雪条件 | 设置 | Unreal Editor 环境 |
| --- | --- | --- |
| 大雪 | **Snow density**：50 | 大雪道路场景 |

#### 太阳

### **Sun azimuth** — 从南到太阳光线水平投影的方位角 `90`（默认）| `0` 到 `360` 之间的任意值

水平面内从南到太阳光线水平投影的方位角，单位为度。

太阳高度角（垂直箭头）和太阳方位角（水平箭头）示意图

使用 **Sun altitude** 和 **Sun azimuth** 参数控制场景中的时间。例如，要将日出指定在北方，请将 **Sun altitude** 设置为 0 度，将 **Sun azimuth** 设置为 180 度。

#### 依赖关系

要启用此参数，请选择 **Override scene weather**。

### **Sun altitude** — 太阳与地平线之间的高度角 `40`（默认）| `-90` 到 `90` 之间的任意值

垂直平面内太阳光线与光线水平投影之间的高度角，单位为度。

太阳高度角（垂直箭头）和太阳方位角（水平箭头）示意图

使用 **Sun altitude** 和 **Sun azimuth** 参数控制场景中的时间。例如，要将日出指定在北方，请将 **Sun altitude** 设置为 0 度，将 **Sun azimuth** 设置为 180 度。

#### 依赖关系

要启用此参数，请选择 **Override scene weather**。

### **Enable geospatial sun** — 启用地理空间太阳的选项 `off`（默认）| `on`

选中此复选框以启用地理空间太阳。启用地理空间太阳可用于模拟极点附近或昼夜长度不成比例的位置的条件。

#### 依赖关系

要启用此参数，请选择 **Override scene weather**。

### **Latitude** — 地球上地理位置的纬度 `0`（默认）| 标量

地球上地理位置的纬度，指定为标量，单位为度。

#### 依赖关系

要启用此参数，请选择 **Override scene weather** 和 **Enable geospatial sun**。

### **Longitude** — 地球上地理位置的经度 0（默认）| 标量

地球上地理位置的经度，指定为标量，单位为度。

#### 依赖关系

要启用此参数，请选择 **Override scene weather** 和 **Enable geospatial sun**。

### **Date (YYYY-MM-DD)** — 日期 2023-01-01（默认）| 整数

日期，指定为 `YYYY-MM-DD` 格式的整数。

#### 依赖关系

要启用此参数，请选择 **Override scene weather** 和 **Enable geospatial sun**。

### **Time (HH:MM:SS)** — 时间 `10:30:00`（默认）| 整数

时间，指定为 `HH:MM:SS` 格式的整数。

#### 依赖关系

要启用此参数，请选择 **Override scene weather** 和 **Enable geospatial sun**。

### **Time zone** — 时区 `-5.0`（默认）| `-12.0` 到 `12.0` 之间的任意值

时区指定与协调世界时（UTC）或格林尼治标准时间（GMT）偏移的小时数。

#### 依赖关系

要启用此参数，请选择 **Override scene weather** 和 **Enable geospatial sun**。

### **Daylight saving time** — 启用夏令时的选项 `off`（默认）| `on`

选中此复选框以启用夏令时。

#### 依赖关系

要启用此参数，请选择 **Override scene weather** 和 **Enable geospatial sun**。

#### Cloud

### **Cloud speed** — Unreal Editor Cloud Speed 全局 actor 目标值 `1`（默认）| `-100` 到 `100` 之间的任意值

对应于 Unreal Editor **Cloud Speed** 全局 actor 目标值的参数。对于正值，云从西向东移动；对于负值，云从东向西移动。

Unreal Editor 中的 Cloud Opacity 和 Cloud Speed 设置

使用 **Cloud opacity** 和 **Cloud speed** 参数控制场景中的云。

#### 依赖关系

要启用此参数，请选择 **Override scene weather**。

### **Cloud opacity** — Unreal Editor 云不透明度全局 actor 目标值 `10`（默认）| `0` 到 `100` 之间的任意值

对应于 Unreal Editor **Cloud Opacity** 全局 actor 目标值的参数，以百分比表示。零表示无云场景。

Unreal Editor 中的 Cloud Opacity 和 Cloud Speed 设置

使用 **Cloud opacity** 和 **Cloud speed** 参数来控制场景中的云。

#### 依赖关系

要启用此参数，请选择 **Override scene weather**。

### **Enable volumetric clouds** — 启用体积云的选项 `off`（默认）| `on`

选中此复选框以启用体积云。

#### 依赖关系

要启用此参数，请选择 **Override scene weather**。

### **Cloud coverage** — Unreal Editor Cloud Density 全局目标值 `1.0`（默认）| `0` 到 `100` 之间的任意值

对应于 Unreal Editor **Cloud Density** 全局 actor 目标值的参数，以百分比表示。

Unreal Editor 中的云覆盖率设置

使用 **Cloud coverage** 参数来控制场景中的云。

#### 依赖关系

要启用此参数，请选择 **Override scene weather** 和 **Enable volumetric clouds**。

### **Cloud layer altitude** — Unreal Editor Layer Bottom Altitude 全局 actor 目标值 `6`（默认）| `5` 到 `20` 之间的任意值

对应于 Unreal Editor **Layer Bottom Altitude** 全局 actor 目标值的参数，以 km 为单位。

Unreal Editor 中的云高度设置

#### 依赖关系

要启用此参数，请选择 **Override scene weather** 和 **Enable volumetric clouds**。

#### 雾

### **Fog density** — Unreal Editor Set Fog Density 和 Set Start Distance 目标值 `0`（默认）| `0` 到 `100` 之间的任意值

对应于 Unreal Editor **Set Fog Density** 和 **Set Start Distance** 目标值的参数，以百分比表示。

Unreal Editor 中的 Set Fog Density 设置

#### 依赖关系

要启用此参数，请选择 **Override scene weather**。

#### 雨

### **Rain density** — Unreal Editor 控制雨密度、湿度、雨坑和涟漪的局部 actor `0`（默认）| `0` 到 `100` 之间的任意值

对应于 Unreal Editor 控制雨密度、湿度、雨坑和涟漪的局部 actor 的参数，以百分比表示。

用于控制雨密度的 Unreal Editor 设置。左侧的 Get Components by Class 激活或停用雨密度设置。右侧的雨效果控制湿度、雨坑和涟漪等设置。

使用 **Cloud opacity** 和 **Rain density** 参数来控制场景中的雨。

#### 依赖关系

要启用此参数，请选择 **Override scene weather**。

### **Enable raindrops on camera lens** — 在相机镜头上启用雨滴的选项 `off`（默认）| `on`

选中此复选框以在相机镜头上启用雨滴。

Unreal Editor 中的云高度设置

#### 依赖关系

要启用此参数，请选择 **Override scene weather**。

#### 雪

### **Snow density** — Unreal Editor 控制雪密度的全局 actor `0`（默认）| `0` 到 `100` 之间的任意值

此参数对应于 Unreal Editor 控制雪密度的全局 actor，以百分比表示。

Unreal Editor 中的云高度设置

#### 依赖关系

要启用此参数，请选择 **Override scene weather**。

### 地理空间

### **Enable geospatial configuration** — 启用地理空间参数和变体子系统的选项 `off`（默认）| `on`

选中此复选框以启用地理空间参数和变体子系统。

### **Access token ID** — 存储的令牌 ID 字符串，表示存储的令牌 ID

存储的令牌 ID，指定为字符串。要创建此令牌，请创建 Cesium Ion® 账户，然后通过此账户生成令牌。Authentication Manager 存储来自 Cesium Ion 的令牌。有关详细信息，请参阅 Visualize with Cesium (Aerospace Blockset) 和 https://ion.cesium.com/。

#### 依赖关系

要启用此参数，请选中 **Enable geospatial configuration** 复选框。

### **Use Earth center as origin (ECEF)** — 使用地心作为原点 (ECEF) `off`（默认）| on

选中此复选框可将航空航天器相对于地心进行定位。将此选项与 pack 模块中的 ECEF 坐标系选择一起使用。

### **Origin height (m)** — 地球上地理参考点处的高度 实标量

地球上地理参考点处的高度，指定为实标量。此参数表示在 **Origin latitude** 和 **Origin longitude** 中指定的纬度和经度处，地球 1984 年世界大地测量系统 (WGS84) 椭球模型上方的高度。

#### 依赖关系

要启用此参数：

- 选中 **Enable geospatial configuration** 复选框。
- 清除 **Use Earth center as origin (ECEF)** 复选框。

### **Origin latitude** — 纬度 实标量

纬度，以十进制度数指定为实标量。

#### 依赖关系

要启用此参数：

- 选中 **Enable geospatial configuration** 复选框。
- 清除 **Use Earth center as origin (ECEF)** 复选框。

### **Origin longitude** — 经度 实标量

经度，以十进制度数指定为实标量。

#### 依赖关系

要启用此参数：

- 选中 **Enable geospatial configuration** 复选框。
- 清除 **Use Earth center as origin (ECEF)** 复选框。

### **Map style** — 栅格叠加类型 `Aerial`（默认）| `Aerial with labels` | `Road`

栅格叠加类型，指定为 `Aerial`、`Aerial with labels` 或 `Road`。

#### 依赖关系

要启用此参数，请选中 **Enable geospatial configuration** 复选框。

### **Additional asset IDs** — 本地数据集 ID `[]`（默认）| 数组 | 向量

本地数据集 ID，指定为数组或向量。

#### 依赖关系

要启用此参数，请选中 **Enable geospatial configuration** 复选框。

### **Use advanced Sun sky** — 地理参考的、位置精确的 Sun Sky actor `off`（默认）| on

选中此复选框可在仿真中添加地理参考的、位置精确的 Sun Sky actor。

#### 依赖关系

要启用此参数，请选中 **Enable geospatial configuration** 复选框。

### **Solar time** — 当前太阳时 `11`（默认）| 标量实数

当前太阳时，指定为从午夜起的标量小时数。

#### 依赖关系

要启用此参数：

- 选中 **Enable geospatial configuration** 复选框。
- 选中 **Use advanced Sun sky** 复选框。

### **Time zone** — 时区 `11`（默认）| 标量实数

时区，指定为相对于格林尼治标准时间 (GMT) 的小时偏移量。要指定 GMT 之前的小时数，请使用负号 (`-`)。

#### 依赖关系

要启用此参数：

- 选中 **Enable geospatial configuration** 复选框。
- 选中 **Use advanced Sun sky** 复选框。

### **Day** — 日 `21`（默认）| `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12` | `13` | `14` | `15` | `16` | `17` | `18` | `19` | `20` | `21` | `22` | `23` | `24` | `25` | `26` | `27` | `28` | `29` | `30` | `31`

日，指定为从 `1` 到 `31` 的标量。

#### 依赖关系

要启用此参数：

- 选中 **Enable geospatial configuration** 复选框。
- 选中 **Use advanced Sun sky** 复选框。

### **Month** — 月 `9`（默认）| `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12`

月，指定为从 `1` 到 `12` 的标量。

#### 依赖关系

要启用此参数：

- 选中 **Enable geospatial configuration** 复选框。
- 选中 **Use advanced Sun sky** 复选框。

### **Year** — 年 `2022`（默认）| 标量实数

年，指定为标量实数。

### **Use daylight saving time (DST)** — 夏令时 `off`（默认）| on

选中此复选框以启用夏令时。

#### 依赖关系

要启用此参数：

- 选中 **Enable geospatial configuration** 复选框。
- 选中 **Use advanced Sun sky** 复选框。

### **DST start day** — 夏令时开始日 `10`（默认）| `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12` | `13` | `14` | `15` | `16` | `17` | `18` | `19` | `20` | `21` | `22` | `23` | `24` | `25` | `26` | `27` | `28` | `29` | `30` | `31`

夏令时开始日，指定为 `1` 到 `31` 的标量。

#### 依赖关系

要启用此参数：

- 选中 **Enable geospatial configuration** 复选框。
- 选中 **Use advanced Sun sky** 复选框。

### **DST start month** — 夏令时开始月份 `3`（默认）| `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12`

夏令时开始月份，指定为 `1` 到 `12` 的标量。

#### 依赖关系

要启用此参数：

- 选中 **Enable geospatial configuration** 复选框。
- 选中 **Use advanced Sun sky** 复选框。

### **DST end day** — 夏令时结束日 `3`（默认）| `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12` | `13` | `14` | `15` | `16` | `17` | `18` | `19` | `20` | `21` | `22` | `23` | `24` | `25` | `26` | `27` | `28` | `29` | `30` | `31`

夏令时结束日，指定为 `1` 到 `31` 的标量。

#### 依赖关系

要启用此参数：

- 选中 **Enable geospatial configuration** 复选框。
- 选中 **Use advanced Sun sky** 复选框。

### **DST end month** — 夏令时结束月份 `11`（默认）| `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12`

夏令时结束月份，指定为 `1` 到 `12` 的标量。

#### 依赖关系

要启用此参数：

- 选中 **Enable geospatial configuration** 复选框。
- 选中 **Use advanced Sun sky** 复选框。

### **DST switch hour** — 夏令时切换小时 `2`（默认）| `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12` | `13` | `14` | `15` | `16` | `17` | `18` | `19` | `20` | `21` | `22` | `23` | `24`

夏令时切换小时，指定为 `1` 到 `24` 的标量。

#### 依赖关系

要启用此参数：

- 选中 **Enable geospatial configuration** 复选框。
- 选中 **Use advanced Sun sky** 复选框。

### **Authentication manager** — 访问令牌管理按钮

点击以管理访问令牌，例如创建、更新和删除令牌。

#### 依赖关系

要启用此参数，请选中 **Enable geospatial configuration** 复选框。

### **TilesetSource** — 瓦片集源 `'Earth Terrain'`（默认）| `'URL'` | `'None'`

瓦片集源，指定为 `'Earth Terrain'`、`'URL'` 或 `'None'` 之一。

#### 依赖关系

要启用此参数，请选中 **Enable geospatial configuration** 复选框。

**数据类型：** `string`

### **TilesetUrl** — 本地存储的 3D 瓦片集数据的文件路径 字符串

本地存储的 3D 瓦片集数据的文件路径，指定为字符串。

#### 依赖关系

要启用此参数，请选中 **Enable geospatial configuration** 复选框，并将 **TilesetSource** 参数设置为 `URL`。

**数据类型：** `string`

## 所属库

Offroad Autonomy Library / Simulation 3D Aerospace Blockset / Animation / Simulation 3D Automated Driving Toolbox / Simulation 3D Robotics System Toolbox / Simulation 3D Simulink 3D Animation / Simulation 3D / Environment UAV Toolbox / Simulation 3D Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Core

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

### R2025a：Simulation 3D Scene Configuration 模块新增两个参数

UAV Toolbox 现在为 Cesium® 中的离线数据集加载提供额外支持，以支持 Air-Gap 用例。Simulation 3D Scene Configuration 模块新增两个参数 `TilesetSource` 和 `Url`。

您可以使用 `TilesetSource` 参数选择 `URL` 参数的值作为源，在其中可以指定离线 tileset 数据的文件路径。

### R2025a：将 USD 和 RoadRunner 场景或情景文件导入 Unreal Engine 仿真环境

您可以导入以下 RoadRunner 场景文件：

- Universal Scene Description（`.usd`、`.usdc` 和 `.usda`）文件
- RoadRunner 场景或情景（`.rrscene` 或 `.rrscenario`）文件

要指定场景的源，请将 **Scene source** 参数设置为 `RoadRunner`。然后，在 **Project** 参数中指定相应的 RoadRunner 场景文件。

### R2025a：创建 3D 环境的多个视图

您可以使用 **Scene view** 参数中的 `Custom` 选项创建自定义视点。此选项启用以下参数。

- **Name**
- **Translation**
- **Rotation**

您可以保存视点，以将视点名称填充到 **Scene view** 参数列表中。选择该视点以设置场景的视图。您还可以编辑或删除该视点。

### R2025a：相对于 `sim3d` actor 设置场景视图

您可以将 **Scene view** 参数设置为模型中包含的 Simulation 3D Actor 模块的 **Name** 参数。此选项启用以下参数，以设置相机相对于 actor 原点的位置。

- **Viewer relative translation [X, Y, Z] (m)**
- **Viewer relative rotation [Roll, Pitch, Yaw] (deg)**

### R2025a：安装附加场景

除了默认场景之外，您还可以下载并安装 Unreal Engine 环境中可用于 3D 仿真的任何预构建 3D 场景。

要选择和下载场景，请点击 **Install**。场景安装完成后，MATLAB 将重新启动。您现在可以从 **Scene view** 参数列表中选择已安装的场景。

### R2024a：需要 Simulink 3D Animation

使用 Simulation 3D Scene Configuration 模块仿真模型需要 Simulink 3D Animation。

### R2024a：新增参数可用于仿真附加天气条件

使用新的天气参数来仿真附加天气条件。

| 天气 | 参数 |
| --- | --- |
| **Sun** | - **Enable geospatial sun** - **Latitude** - **Longitude** - **Date** - **Time** - **Daylight saving time** |
| **Cloud** | - **Enable volumetric clouds** - **Cloud coverage** - **Cloud layer altitude** |
| **Rain** | - **Enable raindrops on camera lens** |
| **Snow** | - **Snow density** |

### R2023b：将 RoadRunner 场景导入 Unreal Engine 仿真环境

使用 Simulation 3D Scene Configuration 模块导入 RoadRunner 场景并在该场景中进行仿真。要指定场景的源，请将 **Scene source** 参数选择为 `RoadRunner`。然后，在 **Project** 参数中指定与 RoadRunner 场景对应的 Filmbox `(.fbx)` 文件。有关示例，请参阅 Import RoadRunner Scene into Unreal Engine Using Simulink (Simulink 3D Animation)。

### R2023b：相机视图改进以查看虚拟世界

使用 Simulation 3D Scene Configuration 模块从位于自定义视点的相机查看虚拟世界。要设置自定义视点，请将 **Scene view** 选择为 `Custom`，并设置 **Initial viewer translation** 和 **Initial viewer rotation** 值。您还可以使用键盘快捷键和鼠标控件在虚拟世界场景中导航。

### R2023a: Cesium 支持指定地理空间坐标

您可以选择 **Enable geospatial configuration** 参数来启用 **Geospatial** 选项卡的参数，例如 **Access token ID** 和 **Georeference parameters**。您可以使用 **Geospatial** 选项卡上的参数，通过 Cesium access token ID 指定地理空间原点坐标。

## 描述

3D 仿真环境场景配置

**注意**

使用 Simulation 3D Scene Configuration 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Scene Configuration 模块实现了一个 3D 仿真环境，该环境使用 Epic Games® 的 Unreal Engine® 进行渲染。UAV Toolbox 将 3D 仿真环境与 Simulink 集成，使您能够查询载具周围的世界，并虚拟测试感知、控制和规划算法。使用此模块，您还可以控制太阳位置和场景的天气条件。有关更多详细信息，请参阅 Sun Position and Weather。

您可以从一组预构建场景或您自己的自定义场景中进行仿真。场景自定义需要 UAV Toolbox Interface for Unreal Engine Projects 支持包。有关更多详细信息，请参阅 Customize Unreal Engine Scenes for UAVs。

您还可以仿真在 RoadRunner 中设计和构建的自定义场景。为此，您必须首先从 RoadRunner 导出场景，并在 Simulation 3D Scene Configuration 模块的 **Project** 参数中指定导出场景工件的路径。

**提示**

Simulation 3D Scene Configuration 模块必须在向 3D 环境发送数据的模块之后执行，并在从 3D 环境接收数据的模块之前执行。要验证此类模块的执行顺序，请右键单击模块并选择 **Properties**。然后，在 **General** 选项卡上，确认以下 **Priority** 设置：

- 对于向 3D 环境发送数据的模块，**Priority** 必须设置为 `-1`，以便这些模块可以在 3D 环境接收数据之前准备好其数据。
- 对于模型中的 Simulation 3D Scene Configuration 模块，**Priority** 必须设置为 `0`。
- 对于从 3D 环境接收数据的模块，**Priority** 必须设置为 `1`，以便 3D 环境可以在这些模块接收数据之前准备好数据。

有关执行顺序的更多信息，请参阅 How Unreal Engine Simulation for UAVs Works。
