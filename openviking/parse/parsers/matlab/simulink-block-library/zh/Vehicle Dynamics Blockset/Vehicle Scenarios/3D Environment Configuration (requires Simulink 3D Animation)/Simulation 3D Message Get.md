---
type: simulink-block
title: 'Simulation 3D Message Get'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / 3D Environment Configuration (requires Simulink 3D Animation)'
documentation_page: 'simulation3dmessageget'
documentation_source_path: 'ref/simulation3dmessageget.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Message Get

## 端口

### 输出

### **ReadMsg** — 从场景检索的数据 `scalar` | `array`

从 3D 可视化环境场景数据检索的数据。在 Unreal Engine 环境中，可以使用 `Sim3DSet` 类配置场景 actor 以将数据发送到 Simulink 模型。

例如，在 Unreal Editor 中，Double Lane Change 场景有一个 `Sim3DSetBoolean` actor，其标签名称为 `NumOfConesHit`。使用它检索车辆在 double-lane change 机动期间撞到的锥桶数量。

下表提供了与 `ReadMsg` 数组元素对应的 Double Lane Change 场景锥桶名称。

| Simulation 3D Message Get 模块 `ReadMsg` 值 | Unreal Editor 锥桶名称 | Simulation 3D Message Get 模块数组元素 | Unreal Editor 锥桶名称 |
| --- | --- | --- | --- |
| `ReadMsg(1,1)` | `SM_Cone5` | `ReadMsg(2,1)` | `SM_Cone10` |
| `ReadMsg(1,2)` | `SM_Cone4` | `ReadMsg(2,2)` | `SM_Cone09` |
| `ReadMsg(1,3)` | `SM_Cone3` | `ReadMsg(2,3)` | `SM_Cone08` |
| `ReadMsg(1,4)` | `SM_Cone2` | `ReadMsg(2,4)` | `SM_Cone07` |
| `ReadMsg(1,5)` | `SM_Cone01` | `ReadMsg(2,5)` | `SM_Cone06` |
| `ReadMsg(1,6)` | `SM_Cone15` | `ReadMsg(2,6)` | `SM_Cone20` |
| `ReadMsg(1,7)` | `SM_Cone14` | `ReadMsg(2,7)` | `SM_Cone19` |
| `ReadMsg(1,8)` | `SM_Cone13` | `ReadMsg(2,8)` | `SM_Cone18` |
| `ReadMsg(1,9)` | `SM_Cone12` | `ReadMsg(2,9)` | `SM_Cone17` |
| `ReadMsg(1,10)` | `SM_Cone11` | `ReadMsg(2,10)` | `SM_Cone16` |
| `ReadMsg(1,11)` | `SM_Cone25` | `ReadMsg(2,11)` | `SM_Cone30` |
| `ReadMsg(1,12)` | `SM_Cone24` | `ReadMsg(2,12)` | `SM_Cone29` |
| `ReadMsg(1,13)` | `SM_Cone23` | `ReadMsg(2,13)` | `SM_Cone28` |
| `ReadMsg(1,14)` | `SM_Cone22` | `ReadMsg(2,14)` | `SM_Cone27` |
| `ReadMsg(1,15)` | `SM_Cone21` | `ReadMsg(2,15)` | `SM_Cone26` |

## 参数

### **Signal name, SigName** — 消息信号名称 `mySignal`（默认）

指定 3D 可视化环境中的信号名称。在 Unreal Engine 环境中，使用位于“Details”窗格中的 `Sim3DSet` actor 类 'Tags' 属性。

例如，可以从 double-lane change 场景检索数据，该数据指示在 double-lane change 机动期间是否撞到锥桶。要从 double-lane change 场景检索锥桶碰撞数据，请将此参数设置为 `NumOfConesHit`。在 double-lane change 场景中，`Sim3DSet` actor 类 'Tags' 属性设置为 `NumOfConesHit`。

### **Data type, DataType** — 消息数据类型 `double`\* | `single` | `int8`\* | `uint8`\* | `int16`\* | `uint16`\* | `int32` | `uint32`\* | `boolean`

3D 可视化环境信号数据类型。支持的数据类型取决于 Unreal Engine 工作流。

| 工作流 | 支持的数据类型 |
| --- | --- |
| Blueprint | `single`  `int32`  `Boolean` |
| \*C++ class | `double`  `single`  `int8`  `uint8`  `int16`  `uint16`  `int32`  `uint32`  `Boolean` |

在 Unreal Engine 环境中，为要发送到 Simulink 模型的数据类型实例化 `Sim3DSet` actor 类。例如，可以从 double-lane change 场景检索数据，该数据指示在 double-lane change 机动期间是否撞到锥桶。要从 double-lane change 场景检索锥桶碰撞数据，请将此参数设置为 `boolean`。在 double-lane change 场景中，实例化 `Sim3DSetBoolean` actor 类以发送锥桶碰撞或未碰撞的布尔数据。

### **Message size, MsgSize** — 消息维度 `[1 1]`（默认） | `scalar` | `array`

3D 可视化环境信号维度。在 Unreal Engine 环境 Blueprint 中，设置 `Sim3DSet` actor 类节点的输入，以指定要发送到 Simulink 模型的数据维度。

例如，可以从 double-lane change 场景检索数据，该数据指示在 double-lane change 机动期间是否撞到锥桶。要从 double-lane change 场景检索锥桶碰撞数据，请将此参数设置为 `[2 15]`。在 double-lane change 场景中，`Sim3DSetBoolean` actor 类的 Blueprint 节点输入设置为 30，即场景中的锥桶数量。

### **Sample time** — 采样时间 `0.02`（默认） | `-1` | `scalar`

采样时间，单位为 s。图形帧速率是采样时间的倒数。如果将采样时间设置为 `-1`，该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。

## 所属库

Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Core Aerospace Blockset / Animation / Simulation 3D Simulink 3D Animation / Simulation 3D / Utilities

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**R2019b 中引入**

### R2024a: 需要 Simulink 3D Animation

使用 Simulation 3D Message Get 模块模拟模型需要 Simulink 3D Animation。

## 描述

从 Unreal Engine 可视化环境检索数据

**注意**

使用 Simulation 3D Message Get 模块模拟模型需要 Simulink® 3D Animation™。

Simulation 3D Message Get 模块从 Unreal Engine® 3D 可视化环境检索数据。在您的模型中，确保 Simulation 3D Scene Configuration 模块与 Simulation 3D Message Get 模块位于同一层级。

**提示**

验证 Simulation 3D Scene Configuration 模块在 Simulation 3D Message Get 模块之前执行。这样，Unreal Engine 3D 可视化环境会在 Simulation 3D Message Get 模块接收数据之前准备好数据。要检查模块执行顺序，请右键单击这些模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Message Get — `1`

有关执行顺序的详细信息，请参阅 Control and Display Execution Order。

### 配置场景以发送数据

要使用该模块，必须配置 Unreal Engine 环境中的场景以将数据发送到 Simulink 模型：

1. 安装 Customize 3D Scenes for Vehicle Dynamics Simulations。
2. 在 Unreal® Editor 中，按照以下一般工作流将数据发送到 Simulink。有关详细信息，请参阅 Get Started Communicating with the Unreal Engine Visualization Environment。

   | Unreal Engine 用户 | 工作流 |
   | --- | --- |
   | Blueprint | 1. 实例化与要发送到 Simulink 模型的数据类型对应的 `Sim3DSet` actor。此示例显示了 Unreal Editor `Sim3DSet` 数据类型。<br>  Unreal Engine 选项图像<br>  2. 指定与 Simulation 3D Message Get 模块 **Signal name** 参数匹配的 actor 标签名称。<br>  3. 导航到 Level Blueprint。<br>  4. 根据 Simulation 3D Message Get 模块 **Data type** 和 **Message size** 参数指定的数据类型和大小，找到 `Sim3DSet` actor 类的 Blueprint 方法。<br>  例如，在 Unreal Editor 中，此图显示 `Write Array Boolean` 是 `Sim3DSetBoolean` actor 类发送数组大小为 30 的 Boolean 数据类型的方法。<br>  Unreal Engine Blueprint 连接的图像<br>  5. 编译并保存场景。<br>  **注意**<br>  默认情况下，Double Lane Change 场景有一个 `Sim3DSetBoolean` actor，其标签名称为 `NumOfConesHit`。 |
   | C++ class | 1. 为希望 Simulink 模型交互的网格或资产创建新的 actor 类。从 `ASim3dActor` 派生它。<br>  2. 在新 actor 类中：<br>  - 将信号名称的指针声明为类字段。<br>  - 获取类标签。<br>  - 创建信号写入器，并在方法 `Sim3dSetup` 中分配指针。<br>  - 在方法 `Sim3dStep` 中，调用 `WriteSimulation3DMessage` 函数以将数据写入 Simulink 模型。<br>  - 在 actor 的方法 `Sim3dRelease` 中删除信号写入器。 |

   有关 Unreal Editor 的详细信息，请参阅 Unreal Engine Documentation。
