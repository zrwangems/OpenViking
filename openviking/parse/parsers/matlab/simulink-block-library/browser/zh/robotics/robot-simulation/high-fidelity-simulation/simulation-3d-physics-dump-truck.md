---
type: simulink-block
title: 'Simulation 3D Physics Dump Truck'
family: 'robotics'
product_id: 'robotics'
product_name: 'Robotics System Toolbox'
documentation_release: R2025b
official_category: 'Robot Simulation / High-Fidelity Simulation'
documentation_page: 'simulation3dphysicsdumptruck'
documentation_source_path: 'ref/simulation3dphysicsdumptruck.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Physics Dump Truck

## 端口

### 输入

### **Velocity** — 使用速度输入移动车辆 `0`（默认）| 标量

用于移动自卸车车辆的速度输入，指定为范围 `[-5 , 5]` 内的正或负标量值。**Velocity** 输入为正值时使车辆向前移动，而为负值时使其向后移动。速度输入的单位是 meters per second (m/s)。

为使输入的卡车速度保持稳定，系统使用 P 控制器，并利用当前卡车速度的反馈来内部估计所需加速度。

**数据类型：** `double`

### **Throttle** — 用于驱动自卸车的归一化输入 `0`（默认）| 标量

用于驱动自卸车的归一化输入，指定为范围 `[-1 , 1]` 内的正或负标量值。**Throttle** 输入为正值时使车辆向前移动，而为负值时使其向后移动。

确切响应由车辆动力总成决定。支持的最大扭矩为 200 Newton-meters (Nm)，支持的最大 RPM 为 6000。

#### 依赖关系

要启用此端口，请选择 **Enable throttle (disable velocity) input signal** 参数。它会将 **Velocity** 输入端口替换为 **Throttle** 输入端口。

**数据类型：** `double`

### **SteeringAngle** — 车辆方向输入 `0`（默认）| 标量

用于为自卸车车辆提供方向的转向角输入，指定为范围 `[-0.7854 , 0.7854]` 内的正或负标量值。使用的单位是 radian。

由于 *z* 轴垂直向上，正输入值执行逆时针运动。

**数据类型：** `double`

### **FootBrake** — 归一化减速度扭矩输入 `0`（默认）| 标量

用于降低车辆加速度的归一化减速度扭矩输入，指定为范围 `[0 , 1]` 内的非负标量值。支持的最大强度为 200 Newton-meters (Nm)。

#### 依赖关系

要启用此端口，请选择 **Enable foot brake input signal** 参数。

**数据类型：** `double`

### **TruckBedAngle** — 使用角度输入上下移动卡车货厢 `0`（默认）| 标量

用于升高和降低卡车货厢的货厢角度输入，指定为范围 `[0 , 0.7854]` 内的非负标量值。使用的单位是 radian。

#### 依赖关系

要启用此端口，请选择 **Enable lift angle input signal** 参数。

**数据类型：** `double`

### 输出

### **DumpTruckTranslation** — 自卸车的当前真值世界平移 向量

自卸车的当前真值世界平移，指定为三元素行向量，形式为 [*x*, *y* , *z*]。*x*、*y* 和 *z* 分别是沿 *x*、*y* 和 *z* 轴的平移。单位为 meters。

#### 依赖关系

要启用此端口，请在 **Dump Truck Outputs** 下选择 **Enable ground truth world tranlsation output signal** 参数。

**数据类型：** `double`

### **DumpTruckRotation** — 自卸车的当前真值世界旋转 向量

自卸车的当前真值世界旋转，指定为三元素行向量，形式为 [*yaw*, *pitch*, *roll*]。*yaw*、*pitch* 和 *roll* 分别是绕 *z*、*y* 和 *x* 轴的旋转。单位为 radians。

#### 依赖关系

要启用此端口，请在 **Dump Truck Outputs** 下选择 **Enable ground truth world rotation output signal** 参数。

**数据类型：** `double`

### **DumpTruckVelocity** — 当前自卸车速度 标量

当前自卸车速度，指定为正或负标量值。使用的单位是 meters per second (m/s)。

#### 依赖关系

要启用此端口，请在 **Dump Truck Outputs** 下选择 **Enable velocity output signal** 参数。

**数据类型：** `double`

### **DumpTruckAngularVelocity** — 当前自卸车角速度 `[0 0 0]`（默认）

当前自卸车角速度，指定为三元素行向量，形式为 [*wx*, *wy*, *wz*]。使用的单位是 radians per second。

#### 依赖关系

要启用此端口，请在 **Dump Truck Outputs** 下选择 **Enable angular velocity output signal** 参数。

**数据类型：** `double`

### **TruckBedTranslation** — 卡车货厢的当前真值世界平移 向量

卡车货厢的当前真值世界平移，指定为三元素行向量，形式为 [*x*, *y* , *z*]。*x*、*y* 和 *z* 分别是沿 *x*、*y* 和 *z* 轴的平移。单位为 meters。

#### 依赖关系

要启用此端口，请在 **Truck Bed Outputs** 下选择 **Enable ground truth world translation output signal** 参数。

**数据类型：** `double`

### **TruckBedRotation** — 获取当前卡车货厢世界真值位姿 向量

自卸车的当前真值世界旋转，指定为三元素行向量，形式为 [*yaw*, *pitch*, *roll*]。*yaw*、*pitch* 和 *roll* 分别是绕 *z*、*y* 和 *x* 轴的旋转。单位为 radian。

要启用此端口，请在 **Truck Bed Outputs** 下选择 **Enable ground truth world rotation output signal** 参数。

**数据类型：** `double`

### **CurrentTruckBedAngle** — 当前卡车货厢仰角 标量

当前卡车货厢当前仰角，指定为正标量值。使用的单位是 radian。

要启用此端口，请在 **Truck Bed Outputs** 下选择 **Enable current lift angle output signals** 参数。

**数据类型：** `double`

## 参数

要交互式地编辑模块参数，请使用 Property Inspector。在 Simulink Toolstrip 的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### 底盘

### **Type** — 自卸车底盘类型 `Standard Dump Truck`（默认）

自卸车底盘类型，指定为 `Standard Dump Truck`。

### **Color** — 自卸车颜色 `Yellow`（默认）| `Red` | `White`

自卸车车身颜色，指定为以下下拉选项之一：

- `Red`
- `Yellow`
- `White`

### **Name** — 自卸车标识符 字符串标量

自卸车标识符名称，指定为字符串标量。

### 初始值

#### 自卸车初始化

### **Initial translation (m)** — 自卸车车辆的初始平移 `[0 0 0]`（默认）| 三元素行向量

自卸车车辆的初始平移，指定为三元素行向量，形式为 [*x*, *y* , *z*]。*x*、*y* 和 *z* 分别是沿 *x*、*y* 和 *z* 轴的平移，使用右手定则世界坐标系。单位为 meters。

### **Initial rotation (rad)** — 自卸车车辆的初始旋转 `[0 0 0]`（默认）| 三元素行向量

自卸车车辆的初始旋转，指定为三元素行向量，形式为 [*yaw*, *pitch*, *roll*]。*yaw*、*pitch* 和 *roll* 分别是绕 *z*、*y* 和 *x* 轴的旋转，使用右手定则世界坐标系。单位为 radians。

### rigidBodyTree 几何设置

设置此选项卡中的参数，以在 3D 可视化环境中启用刚体树几何的可视化。

#### 碰撞几何可视化

### **Enable collision geometry visualization in 3D scene** — 在 3D 场景中可视化刚体树碰撞几何 `off`（默认）| `on`

选择此参数以在 3D 可视化环境中可视化刚体树碰撞几何。

### **Collision geometry color** — 刚体树碰撞几何的颜色 `[0 1 0]`（默认）| 向量

在 3D 可视化环境中可视化的刚体树碰撞几何的颜色，指定为三元素行向量。

### **Collision geometry transparency** — 刚体树碰撞几何的透明度 `0.1`（默认）| 标量

在 3D 可视化环境中可视化的刚体树碰撞几何的透明度，指定为标量。

### 输入

#### 自卸车输入

### **Enable throttle (disable velocity) input signal** — 指定油门以在输入端口移动自卸车 `off`（默认）| `on`

选择此参数以禁用速度并在输入端口指定油门，以移动自卸车。

### **Enable foot brake input signal** — 在输入端口指定脚制动 `off`（默认）| `on`

在输入端口指定脚制动扭矩，以使自卸车车辆减速。

#### 卡车货厢输入

### **Enable lift angle input signal** — 在输入端口指定卡车货厢举升角 `off`（默认）| `on`

指定卡车货厢举升角，以在输入端口启用 **TruckBedAngle** 信号。

### 输出

#### 自卸车输出

### **Enable ground truth world tranlsation output signal** — 输出自卸车的真值世界平移 `off`（默认）| `on`

选择此参数以在 **DumpTruckTranslation** 输出端口输出自卸车的真值世界平移。

### **Enable ground truth world rotation output signal** — 输出自卸车的真值世界旋转 `off`（默认）| `on`

选择此参数以在 **DumpTruckRotation** 输出端口输出自卸车的真值世界旋转。

### **Enable velocity output signal** — 输出当前自卸车速度 `off`（默认）| `on`

选择此参数以在 **DumpTruckVelocity** 输出端口输出自卸车的真值世界旋转。

### **Enable angular velocity output signal** — 输出当前自卸车角速度 `off`（默认）| `on`

选择此参数以在 **DumpTruckAngularVelocity** 输出端口输出自卸车的真值世界旋转。

#### 卡车货厢输出

### **Enable ground truth world translation output signal** — 输出卡车货厢的真值世界平移 `off`（默认）| `on`

选择此参数以在 **TruckBedTranslation** 输出端口输出卡车货厢的真值世界平移。

### **Enable ground truth world rotation output signal** — 输出卡车货厢的真值世界旋转 `off`（默认）| `on`

选择此参数以在 **TruckBedRotation** 输出端口输出卡车货厢的真值世界旋转。

### **Enable current lift angle output signals** — 输出当前卡车货厢仰角 `off`（默认）| `on`

选择此参数以在 **CurrentTruckBedAngle** 输出端口输出当前卡车货厢仰角。

## 所属库

Offroad Autonomy Library / Simulation 3D

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

## 描述

3D 仿真环境中的自卸车物理模型

Simulation 3D Physics Dump Truck 模块提供接口，用于在 Simulink® 3D 世界中实现自卸车车辆。

**注意**

使用 Simulation 3D Physics Dump Truck 模块对模型进行仿真需要 Simulink 3D Animation™ 和 Robotics System Toolbox™ Offroad Autonomy Library 支持包。有关下载支持包的详细信息，请参阅安装 Robotics System Toolbox Offroad Autonomy Library 支持包。

要使用此模块，请确保模型中有 Simulation 3D Scene Configuration 模块。如果将 Simulation 3D Physics Dump Truck 模块的 **Sample time** 参数设置为 `-1`，该模块将继承 Simulation 3D Scene Configuration 模块中指定的采样时间。必须将 Simulation 3D Scene Configuration 模块中的采样时间设置为 0.01 或更小，以防止自卸车在 3D 可视化环境中抖动。

这些图示说明了 `DumpTruck` 资产参数相对于坐标轴的尺寸和位置，遵循 `yaw(z)`、`pitch(y)`、`roll(x)` 顺序。车辆布局遵循 Unreal Engine® 坐标系，该坐标系遵循左手定则世界坐标系。有关详细信息，请参阅 Robotics System Toolbox 中的 Coordinate Systems for Unreal Engine Simulation。

Unreal Engine 自卸车资产尺寸

Unreal Engine 自卸车车轴
