---
type: simulink-block
title: 'Write Torque & Thrust'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for ArduPilot Autopilots / Algorithm Development'
documentation_page: 'writetorquethrust'
documentation_source_path: 'ardupilot/ref/writetorquethrust.html'
language: zh-CN
chinese_source: worker-translation
---

# Write Torque & Thrust

## 端口

### 输入

### **Roll** — 滚转指令标量

输出车辆的滚转指令。此值指示车辆绕机体坐标系中的纵向 *x-* 轴旋转。正值对应右翼向下（从后方观察时为顺时针）运动，负值对应左翼向下（逆时针）运动。输入范围通常归一化为 `[-1, 1]`，其中该值映射到车辆允许的滚转角范围。

**数据类型：** `single`

### **Pitch** — 俯仰指令标量

输出车辆的俯仰指令。此值指示车辆绕机体坐标系中的横向 *y-* 轴旋转。正值导致机头向上运动，负值导致机头向下运动。输入范围通常归一化为 `[-1, 1]`，其中该值映射到车辆允许的俯仰角范围。

**数据类型：** `single`

### **Yaw** — 偏航指令标量

输出车辆的偏航指令，表示绕机体坐标系 *z-* 轴的期望力矩。指定输入在车辆机体 FRD（Forward-Right-Down）坐标系中归一化到范围 `[-1,1]`。

**数据类型：** `single`

### **Throttle** — 油门指令标量

输出车辆的油门指令。油门指令输出所有电机生成的总推力，直接控制车辆的高度或垂直速度。较高的值会增加总推力并使车辆上升，较低的值会降低推力并使车辆下降。输入范围归一化为 `[0, 1`]，其中 `0` 对应最小推力（电机关闭或怠速），`1` 对应车辆允许的最大推力..

#### 依赖项

要启用此端口，请选择 **Throttle input** 参数。

**数据类型：** `single`

## 参数

### **Throttle input** — 启用 Throttle input `on`（默认） | `off`

选择此参数可启用将油门用作输入参数，以控制传递给所有电机的总功率。启用后，油门输入将直接影响系统生成的升力，从而实现高度控制。此设置对于操作至关重要，因为它调节所有电机的速度。

### **Configure custom mixer matrix** — 启用自定义混控配置 `off`（默认） | `on`

选择此参数可手动为您的机架定义自定义混控矩阵。这允许您为每个电机指定单独的滚转、俯仰、偏航和油门贡献，从而支持自定义多旋翼配置。启用后，您可以输入或修改混控矩阵值，以匹配您的特定机架布局和电机排列。

### **Frame name** — 自定义混控机架名称 `Simulink Quad/Plus`（默认）

为自定义混控机架提供一个名称。

#### 依赖项

要启用此端口，请选择 **Configure custom mixer matrix** 参数。

### **Mixer matrix** — 配置混控矩阵值 `Mixer matrix for a quadcopter`（默认）

Mixer matrix 接口允许您配置每个电机对车辆滚转、俯仰、偏航和油门指令的单独贡献。矩阵中的每一行对应一个电机，各列指定滚转、俯仰、偏航和油门的系数。

您可以通过为每个电机指定滚转、俯仰、偏航和油门系数，为不同机架类型配置自定义混控矩阵。所需的最少电机数为 `4`，最多可添加 `12` 个电机。

下面是一个四旋翼默认值的示例混控矩阵表。

**混控矩阵**

| 电机编号 | 滚转系数 | 俯仰系数 | 偏航系数 | 油门系数 |
| --- | --- | --- | --- | --- |
| 电机 1 | `-1` | `0` | `1` | `1` |
| 电机 2 | `1` | `0` | `1` | `1` |
| 电机 3 | `0` | `1` | `-1` | `1` |
| 电机 4 | `0` | `-1` | `-1` | `1` |

- 添加电机：单击 **Add motor** 向矩阵添加新的电机条目。
- 删除电机：选择一个电机，然后单击 **Delete motor** 将其从矩阵中移除。
- 编辑值：您可以直接修改每个电机的滚转、俯仰、偏航和油门系数，以自定义机架的行为。

#### 依赖项

要启用此端口，请选择 **Configure custom mixer matrix** 参数。

## 所属库

UAV Toolbox Support Package for ArduPilot Autopilots / Controller Interface Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2025b 中引入**

## 描述

将归一化力矩和推力指令写入 ArduPilot mixer

Write Torque & Thrust 模块将归一化力矩（滚转、俯仰、偏航）和推力（油门）指令写入 ArduPilot Mixer。

- 滚转、俯仰和偏航指令应在 [-1,1] 范围内归一化
- 油门指令应在 [0,1] 范围内归一化

您可以在此模块中为自定义机架配置指定自定义混控矩阵。

您可以通过为每个电机指定滚转、俯仰、偏航和油门系数，为不同机架类型配置自定义混控矩阵。所需的最少电机数为 `4`，最多可添加 `12` 个电机。
