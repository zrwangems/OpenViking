---
type: simulink-block
title: 'Simulation 3D Message Set'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Scenarios / 3D Environment Configuration (requires Simulink 3D Animation)'
documentation_page: 'simulation3dmessageset'
documentation_source_path: 'ref/simulation3dmessageset.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Message Set

## 端口

### 输入

### **WriteMsg** — 发送到场景的数据 `scalar` | `array`

发送到 3D 可视化环境场景的数据。在 Unreal Engine 环境中，您可以配置 `Sim3DGet` 类以从 Simulink 模型接收数据。

例如，在 Unreal Editor 中，Double Lane Change 场景有一个标签名称为 `TrafficLight1` 的 `Sim3DGetInteger` 整数 actor。该整数 actor 从 Simulink 模型读取 `int32` 数据类型。您可以使用它来控制交通信号灯颜色。

下表提供了 Double Lane Change 场景中与 `WriteMsg` 值对应的场景交通信号灯颜色。

| Simulation 3D Message Set 模块 `WriteMsg` 值 | `TrafficLight1` 颜色 |
| --- | --- |
| `0` | `Red` |
| `1` | `Yellow` |
| `2` | `Green` |

## 参数

### **Signal name, SigName** — 消息信号名称 `mySignal`（默认）

指定 3D 可视化环境中的信号名称。在 Unreal Engine 环境中，使用位于 'Details' 窗格中的 `Sim3Get` actor 类 'Tags' 属性。

例如，您可以向 double lane change 场景发送数据，以将交通信号灯颜色更改为 red、yellow 或 green。要向交通信号灯发送数据，请将此参数设置为 `TrafficLight1`。在 double lane change 场景中，`Sim3dGetInteger` actor 类的 'Tags' 属性值设置为 TrafficLight1。

### **Sample time** — 采样时间 `0.02`（默认） | `-1` | `scalar`

采样时间，单位为 s。图形帧率是采样时间的倒数。如果将采样时间设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。

## 所属库

Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Core Aerospace Blockset / Animation / Simulation 3D Simulink 3D Animation / Simulation 3D / Utilities

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

### R2024a: 需要 Simulink 3D Animation

使用 Simulation 3D Message Set 模块仿真模型需要 Simulink 3D Animation。

## 描述

将数据发送到 Unreal Engine 可视化环境

**注意**

使用 Simulation 3D Message Set 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Message Set 模块将数据发送到 Unreal Engine® 3D 可视化环境。在您的模型中，确保 Simulation 3D Scene Configuration 模块与 Simulation 3D Message Set 模块处于同一层级。

**提示**

验证 Simulation 3D Message Set 模块在 Simulation 3D Scene Configuration 模块之前执行。这样，Simulation 3D Message Set 会在 Unreal Engine 3D 可视化环境接收信号数据之前准备好信号数据。要检查模块执行顺序，请右键单击这些模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Message Set — `-1`

有关执行顺序的详细信息，请参阅 Control and Display Execution Order。

### 配置场景以接收数据

要使用该模块，您必须配置 Unreal Engine 环境中的场景以从 Simulink 模型接收数据：

1. 安装 Customize 3D Scenes for Vehicle Dynamics Simulations。
2. 在 Unreal® Editor 中，遵循以下常规工作流从 Simulink 接收数据。有关详细信息，请参阅 Get Started Communicating with the Unreal Engine Visualization Environment。

   | Unreal Engine 用户 | 工作流 |
   | --- | --- |
   | Blueprint | 1. 实例化与您要从 Simulink 模型接收的数据类型对应的 `Sim3DGet` actor。此示例显示了 Unreal Editor `Sim3DGet` 数据类型。 Unreal Engine 选项的图像 2. 指定与 Simulation 3D Message Set 模块 **Signal name** 参数匹配的 actor 标签名称。 3. 导航到 Level Blueprint。 4. 根据您要从 Simulink 模型接收的数据类型和大小，找到 `Sim3DGet` actor 类的蓝图方法。 例如，在 Unreal Editor 中，此图显示 `Read    Scalar Integer` 是 `Sim3DGetInteger` actor 类用于接收大小为 scalar 的 `int32` 数据类型的方法。 Unreal Engine 蓝图连接的图像 5. 编译并保存场景。 **注意** 默认情况下，Double Lane Change 场景有一个标签名称为 `TrafficLight1` 的 `Sim3DGetInteger` actor。 |
   | C++ class | 1. 为您希望 Simulink 模型交互的 mesh 或 asset 创建新的 actor 类。从 `ASim3dActor` 派生。 2. 在新的 actor 类中：    - 将信号名称的指针声明为类字段。    - 获取类标签。    - 创建信号读取器，并在方法 `Sim3dSetup` 中分配该指针。    - 在方法 `Sim3dStep` 中，调用 `ReadSimulation3DMessage` 函数以从 Simulink 模型读取数据。    - 在 actor 的方法 `Sim3dRelease` 中删除信号读取器。 |

   有关 Unreal Editor 的详细信息，请参阅 Unreal Engine Documentation。
