---
type: simulink-block
title: 'Simulation 3D Message Set'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Simulation 3D'
documentation_page: 'simulation3dmessageset'
documentation_source_path: 'simulation3dmessageset.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Message Set

## 端口

### 输入

### **WriteMsg** — 发送到场景的数据 `scalar` | `array`

发送到 3D 可视化环境场景的数据。在 Unreal Engine 环境中，您可以配置 `Sim3DGet` 类以从 Simulink 模型接收数据。

## 参数

### **Signal name, SigName** — 消息信号名称 `mySignal` (default)

指定 3D 可视化环境中的信号名称。在 Unreal Engine 环境中，请使用位于 'Details' 窗格中的 `Sim3Get` actor 类 'Tags' 属性。

例如，您可以将数据发送到 double lane change 场景，以将交通信号灯颜色更改为红色、黄色或绿色。要将数据发送到交通信号灯，请将此参数设置为 `TrafficLight1`。在 double lane change 场景中，`Sim3dGetInteger` actor 类的 'Tags' 属性值设置为 TrafficLight1。

### **Sample time** — 采样时间 `0.02` (default) | `-1` | `scalar`

采样时间，以 s 为单位。图形帧速率是采样时间的倒数。如果将采样时间设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。

## 所属库

Vehicle Dynamics Blockset / Vehicle Scenarios / Sim3D / Sim3D Core Aerospace Blockset / Animation / Simulation 3D Simulink 3D Animation / Simulation 3D / Utilities

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2021b 中引入**

### R2024a: 需要 Simulink 3D Animation

使用 Simulation 3D Message Set 模块仿真模型需要 Simulink 3D Animation。

## 描述

将数据发送到 Unreal Engine 可视化环境

**注意**

使用 Simulation 3D Message Set 模块仿真模型需要 Simulink® 3D Animation™。

Simulation 3D Message Set 模块将数据发送到 Unreal Engine® 3D 可视化环境。在模型中，确保 Simulation 3D Scene Configuration 模块与 Simulation 3D Message Set 模块处于同一层级。

**提示**

验证 Simulation 3D Message Set 模块在 Simulation 3D Scene Configuration 模块之前执行。这样，Simulation 3D Message Set 会在 Unreal Engine 3D 可视化环境接收信号数据之前准备好信号数据。要检查模块执行顺序，请右键点击这些模块并选择 **Properties**。在 **General** 选项卡上，确认以下 **Priority** 设置：

- Simulation 3D Scene Configuration — `0`
- Simulation 3D Message Set — `-1`

有关执行顺序的更多信息，请参阅控制和显示执行顺序。

### 配置场景以接收数据

要使用该模块，必须配置 Unreal Engine 环境中的场景，以从 Simulink 模型接收数据：

1. 安装用于航空航天仿真的自定义 3D 场景。
2. 在 Unreal® Editor 中，遵循以下常规工作流从 Simulink 接收数据。

   | Unreal Engine 用户 | 工作流 |
   | --- | --- |
   | Blueprint | 1. 实例化与您要从 Simulink 模型接收的数据类型对应的 `Sim3DGet` actor。此示例显示 Unreal Editor `Sim3DGet` 数据类型。Unreal Engine 选项的图像<br>2. 指定与 Simulation 3D Message Set 模块 **Signal name** 参数匹配的 actor tag 名称。<br>3. 导航到 Level Blueprint。<br>4. 根据您要从 Simulink 模型接收的数据类型和大小，找到 `Sim3DGet` actor 类的 blueprint 方法。<br>例如，在 Unreal Editor 中，此图显示 `Read Scalar Integer` 是 `Sim3DGetInteger` actor 类用于接收大小为 scalar 的 `int32` 数据类型的方法。<br>Unreal Engine blueprint 连接的图像<br>5. 编译并保存场景。<br>**注意**<br>默认情况下，Double Lane Change 场景有一个 tag 名称为 `TrafficLight1` 的 `Sim3DGetInteger` actor。 |
   | C++ 类 | 1. 为希望 Simulink 模型与之交互的 mesh 或 asset 创建新的 actor 类。从 `ASim3dActor` 派生该类。<br>2. 在新的 actor 类中：<br>&nbsp;&nbsp;- 将指向信号名称的指针声明为类字段。<br>&nbsp;&nbsp;- 获取类 tag。<br>&nbsp;&nbsp;- 创建信号读取器，并在方法 `Sim3dSetup` 中分配该指针。<br>&nbsp;&nbsp;- 在方法 `Sim3dStep` 中，调用 `ReadSimulation3DMessage` 函数以从 Simulink 模型读取数据。<br>&nbsp;&nbsp;- 在 actor 的方法 `Sim3dRelease` 中删除信号读取器。 |

有关 Unreal Editor 的更多信息，请参阅 Unreal Engine 文档。
