---
type: simulink-block
title: 'Simulation 3D Message Get'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Simulation 3D'
documentation_page: 'simulation3dmessageget'
documentation_source_path: 'simulation3dmessageget.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Message Get

## 端口

### 输出

### **ReadMsg** — 从场景中检索的数据 `scalar` | `array`

从 3D 可视化环境场景数据中检索的数据。在 Unreal Engine 环境中，您可以使用 `Sim3DSet` 类来配置场景 actor 以将数据发送到 Simulink 模型。

## 参数

### **Signal name, SigName** — 消息信号名称 `mySignal`（默认）

指定 3D 可视化环境中的信号名称。在 Unreal Engine 环境中，使用位于“Details”窗格中的 `Sim3DSet` actor 类“Tags”属性。

例如，您可以从双车道变换场景中检索数据，该数据指示在双车道变换操作期间是否撞到锥桶。要从双车道变换场景中检索锥桶碰撞数据，请将此参数设置为 `NumOfConesHit`。在双车道变换场景中，`Sim3DSet` actor 类“Tags”属性设置为 `NumOfConesHit`。

### **Data type, DataType** — 消息数据类型 `double`\* | `single` | `int8`\* | `uint8`\* | `int16`\* | `uint16`\* | `int32` | `uint32`\* | `boolean`

3D 可视化环境信号数据类型。支持的数据类型取决于 Unreal Engine 工作流。

| 工作流 | 支持的数据类型 |
| --- | --- |
| Blueprint | `single`  `int32`  `Boolean` |
| \*C++ class | `double`  `single`  `int8`  `uint8`  `int16`  `uint16`  `int32`  `uint32`  `Boolean` |

在 Unreal Engine 环境中，为您想要发送到 Simulink 模型的数据类型实例化 `Sim3DSet` actor 类。例如，您可以从双车道变换场景中检索数据，该数据指示在双车道变换操作期间是否撞到锥桶。要从双车道变换场景中检索锥桶碰撞数据，请将此参数设置为 `boolean`。在双车道变换场景中，实例化 `Sim3DSetBoolean` actor 类以发送锥桶碰撞或未碰撞的布尔数据。

### **Message size, MsgSize** — 消息维度 `[1 1]`（默认）| `scalar` | `array`

3D 可视化环境信号维度。在 Unreal Engine 环境蓝图中，将 `Sim3DSet` actor 类节点的输入设置为指定您想要发送到 Simulink 模型的数据维度。

例如，您可以从双车道变换场景中检索数据，该数据指示在双车道变换操作期间是否撞到锥桶。要从双车道变换场景中检索锥桶碰撞数据，请将此参数设置为 `[2 15]`。在双车道变换场景中，`Sim3DSetBoolean` actor 类的蓝图节点输入设置为 30，即场景中锥桶的数量。

### **Sample time** — 采样时间 `0.02`（默认）| `-1` | `scalar`

采样时间，以 s 为单位。图形帧率是采样时间的倒数。如果将采样时间设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。

## 所属库

Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Core Aerospace Blockset / Animation / Simulation 3D Simulink 3D Animation / Simulation 3D / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

### R2024a: 需要 Simulink 3D Animation

使用 Simulation 3D Message Get 模块仿真模型需要 Simulink 3D Animation。

## 描述

从 Unreal Engine 可视化环境检索数据

**注意**

使用 Simulation 3D Message Get 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Message Get 模块从 Unreal Engine® 3D 可视化环境中检索数据。在您的模型中，确保 Simulation 3D Scene Configuration 模块与 Simulation 3D Message Get 模块处于同一层级。

**提示**

验证 Simulation 3D Scene Configuration 模块在 Simulation 3D Message Get 模块之前执行。这样，Unreal Engine 3D 可视化环境会在 Simulation 3D Message Get 模块接收数据之前准备好数据。要检查模块执行顺序，请右键单击模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Message Get — `1`

有关执行顺序的详细信息，请参阅 Control and Display Execution Order。

### 配置场景以发送数据

要使用该模块，您必须在 Unreal Engine 环境中配置场景以将数据发送到 Simulink 模型：

1. 安装用于航空航天仿真的自定义 3D 场景。
2. 在 Unreal® Editor 中，按照以下通用工作流将数据发送到 Simulink。

   | Unreal Engine 用户 | 工作流 |
   | --- | --- |
   | Blueprint | 1. 实例化与您想要发送到 Simulink 模型的数据类型相对应的 `Sim3DSet` actor。此示例显示了 Unreal Editor `Sim3DSet` 数据类型。Unreal Engine 选项的图像 2. 指定与 Simulation 3D Message Get 模块 **Signal name** 参数匹配的 actor 标签名称。3. 导航到 Level Blueprint。4. 根据 Simulation 3D Message Get 模块 **Data type** 和 **Message size** 参数指定的数据类型和大小，找到 `Sim3DSet` actor 类的蓝图方法。例如，在 Unreal Editor 中，此图显示 `Write Array Boolean` 是 `Sim3DSetBoolean` actor 类的方法，用于发送数组大小为 30 的 Boolean 数据类型。Unreal Engine 蓝图连接的图像 5. 编译并保存场景。**注意** 默认情况下，Double Lane Change 场景具有一个标签名称为 `NumOfConesHit` 的 `Sim3DSetBoolean` actor。 |
   | C++ class | 1. 为您希望 Simulink 模型交互的网格或资产创建新的 actor 类。从 `ASim3dActor` 派生它。2. 在新的 actor 类中：- 将信号名称的指针声明为类字段。- 获取类标签。- 创建信号写入器并在方法 `Sim3dSetup` 中分配指针。- 在方法 `Sim3dStep` 中，调用 `WriteSimulation3DMessage` 函数将数据写入 Simulink 模型。- 在 actor 的方法 `Sim3dRelease` 中删除信号写入器。 |

   有关 Unreal Editor 的详细信息，请参阅 Unreal Engine Documentation。
