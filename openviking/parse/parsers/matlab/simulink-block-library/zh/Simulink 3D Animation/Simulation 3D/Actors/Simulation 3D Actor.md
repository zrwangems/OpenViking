---
type: simulink-block
title: 'Simulation 3D Actor'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Simulation 3D / Actors'
documentation_page: 'simulation3dactor'
documentation_source_path: 'simulation3dactor.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Actor

## 端口

### 输入

### **Instance** — 角色的实例编号，实数整数

角色的实例编号，指定为实数整数。

- 对于正值，如果尚未创建角色，则创建一个新角色。如果该角色存在于世界中，引用模块将引用此角色。
- 对于负值，如果角色实例存在，则将其删除。例如，如果在给定时间步长内此端口的值是 `-1`，则实例 1 被删除。

#### 依赖

当模块的运行模式设置为 `Create at step` 或 `Reference by instance number` 时，此输入可见。

### 输出

### **Valid** — 指定角色的有效性 `false`（默认）| `true`

指定角色的有效性，如果无法在世界中找到指定的角色，则返回 `false`；如果找到该角色，则返回 `true`。

## 参数

### 主要

### **Actor Name** — 角色的名称 `Sim3dActor1`（默认）| 字符串

当前 Simulation 3D Actor 模块的根角色名称。

### **Parent Name** — 角色的父级 `Scene Origin`（默认）| 字符串

角色的父级名称，指定为字符串。

### **Operation** — 模块的运行模式 `Create at setup`（默认）| `Create at step` | `Reference by name` | `Reference by instance number`

决定模块行为的运行模式，指定为以下选项之一。

- `Create at setup` – 使用此选项在场景中创建角色。角色在游戏设置期间、仿真运行之前创建。您还可以使用 **Input**、**Output** 和 **Event** 端口控制这些角色的仿真。
- `Create at step` – 使用此选项在仿真运行时动态创建和删除角色。此模式下会创建一个类型为 `int` 的 **Instance** 输入端口，角色根据输入到模块的值动态生成。如果 **Instance** 的值大于零，则创建一个名称为 `'Actor name + Instance value'` 的角色。角色名称派生自模块掩码中的 `'Actor Name'`。实例值是端口的当前值。当 **Instance** 的值为负时，则删除该角色。与 `Create at setup` 选项不同，您无法在模块掩码中控制使用此选项创建的角色。
- `Reference by name` – 使用此选项通过 `Actor Name` 引用场景中的角色，并使用模块的输入控制此角色的仿真。使用输出或事件获取角色的数据。这还提供了一个 **Valid** 输出端口。

  如果指定名称的角色不存在，**Valid** 端口返回 `false` 或 `0`。在这种情况下，其余输出端口（如果有）将传递默认值作为输出。使用 `Valid` 端口验证生成的其他输出当前是否有效。

  **注意**

  **Path to source file** 和 **Initialization script** 参数在 `Reference by name` 运行模式下不可用。
- `Reference by instance number` – 使用此选项引用通过不同角色模块创建的实例。与 `Create at step` 运行模式类似，此选项在模块中创建一个 **Instance** 输入，并使用有效角色名称 `'Actor name + Instance value'` 来引用角色。

  如果生成的名称对应的角色不存在，**Valid** 端口返回 `false` 或 `0`。在这种情况下，其余输出端口（如果有）将传递默认值作为输出。使用 **Valid** 端口验证生成的其他输出当前是否有效。

  **注意**

  **Path to source file** 和 **Initialization script** 参数在 `Reference by instance number` 运行模式下不可用。

#### 依赖

如果将 **Operation** 设置为 `Create at setup` 或 `Create at step`，则 **Transform** 选项卡可用。

### **Path to source file** — 获取 actor 的源文件 字符串

获取 actor 的源文件，指定为字符串。

此选项加载 3D 文件或导入 `sim3d.Actor` 对象，包括子 actor 对象。
`Simulation 3D Actor` 模块支持这些作为源。

**文件格式**

- MAT（来自 MATLAB® 的 MAT 文件）
- STL（立体光刻）
- FBX（Autodesk®
  Filmbox 格式）
- URDF（统一机器人描述文件）
- X3D（可扩展 3D）
- WRL（虚拟现实建模语言）
- DAE（Collada 数字资产交换）
- USD、USDA、USDC（通用场景描述）

您还可以使用
`.m` 文件实例化 actor。

或者，**Select** 按钮也可用于
从 Windows® 文件浏览器中选择文件。

**注意**

Linux® 上不支持 USD 文件导入。USD 文件不支持碰撞检测。

### **Initialization script** — 用于初始化 actor 的 MATLAB 脚本代码

用于初始化由该模块创建的 actor 的代码，指定为 MATLAB 脚本。您还可以使用此脚本创建其他 actor
对象、设置其属性，并使用 `add` 函数将它们作为子 actor 添加到 3D 环境中。您必须使用 `add`
函数中的 `parent` 设置父 actor。

此 MATLAB 脚本在 3D 环境初始化由该模块创建的 actor 时运行。actor 创建的顺序为：

1. 创建具有指定名称的根 actor。
2. 将 **Path to source file** 加载
   到根 actor 中。
3. 运行 **Initialization script**。

在修改模块的根 actor 时，请使用名称 `Actor`。`Actor` 是初始化脚本中的保留句柄。否则，请使用 `findBy` 函数获取不同名称的 actor 句柄，例如其中一个子 actor。然后使用获取的 actor
句柄初始化该特定 actor。例如，要将一个 actor 添加为根 actor 的子级，请在 `add` 函数中将 `Actor` 设置为父
actor。

对于 3D 环境中的 actor，请使用名称 `World`。`World` 是由
Simulation 3D Scene Configuration 模块创建的 3D 环境的初始化脚本中的保留句柄。

您可以创建并添加以下 `sim3d` actor 对象。

- `sim3d.Light`
- `sim3d.graphics.Arrow`
- `sim3d.graphics.Text`
- `sim3d.graphics.PathMarker`

**Initialization script** 不使用基础
工作区变量。

### **Sample time** — 采样时间 `-1`（默认）| `scalar`

采样时间，*Ts*。图形帧率是采样时间的倒数。

如果将采样时间设置为 `-1`，则该模块使用 Simulation 3D Scene Configuration
模块中指定的采样时间。

为获得最佳性能，请检查此值不小于 Simulation 3D Scene Configuration 模块中指定的 **Sample
time** 值。

### Transform

当您将 **Operation** 设置为 `Create at
setup` 或 `Create at step` 时，**Transform** 选项卡可用于设置初始变换属性。否则，在 **Initialization script** 中设置的变换属性将用于 **Transform** 选项卡，并覆盖其中设置的任何值。

### **Translation** — 相对平移 `[0,0,0]`（默认）| 实数 1×3 向量

actor 对象相对于其父 actor 的平移
(*x*,*y*,*z*)，指定为实数
1×3 向量，单位为米。

#### 依赖关系

在 **Initialization script** 中设置的 Translation 属性会覆盖此
参数值。

### **Rotation** — 相对旋转 `[0,0,0]`（默认）| 实数 1×3 向量

actor 对象相对于其父 actor 的旋转（roll、pitch、yaw），指定为实数 1×3 向量，单位为弧度。

#### 依赖关系

在 **Initialization script** 中设置的 Rotation 属性会覆盖此
参数值。

### **Scale** — 相对缩放 `[1,1,1]`（默认）| 实数 1×3 向量

在 *x*、*y* 和
*z* 坐标中的相对缩放，指定为实数 1×3
向量。

#### 依赖关系

在**初始化脚本**中设置的 Scale 属性会覆盖此参数值。

**注意**

在**初始化脚本**中设置初始变换属性会覆盖 **Transform** 选项卡中的值。

### 输入

### **输入端口** — 用户选择的输入端口列表 文本区域

此文本区域列出模块的用户选择输入端口，并提供一个按钮用于打开端口选择器应用，您可以使用该应用修改输入端口。文本区域中的每一行代表一个模块端口。

您可以使用文本区域手动修改端口，但建议使用端口选择器应用来选择端口。

### 输出

### **输出端口** — 用户选择的输出端口列表 文本区域

此文本区域列出模块的用户选择输出端口，并提供一个按钮用于打开端口选择器应用，您可以使用该应用修改输出端口。文本区域中的每一行代表一个模块端口。

您可以使用文本区域手动修改端口，但建议使用端口选择器应用来选择端口。

## 所属库

Simulink 3D Animation / Simulation 3D / Actors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

### R2024b：创建光源和标注 Actor

使用 Simulation 3D Actor 模块的**初始化脚本**，通过可调模块参数在 3D 环境中初始化并添加以下 actor。

- 使用 `sim3d.Light` 对象创建光源
- 使用 `sim3d.graphics.Arrow` 对象创建箭头
- 使用 `sim3d.graphics.Text` 对象创建文本

### R2023b：可调的平移、旋转和缩放参数

以下 Simulation 3D Actor 模块参数是可调的，允许您使用 For Each Subsystem (Simulink) 模块在虚拟世界中创建同一 actor 类型的多个实例。

- **Translation**
- **Rotation**
- **Scale**

有关示例，请参阅 Create Multiple Instances of Actors。

### R2023a：通信 Unreal Engine 事件

使用 Simulation 3D Actor 模块的事件端口在 Unreal Engine 仿真 3D 环境中通信事件，包括以下情况：

- 您点击某个 actor。
- 某个 actor 与另一个 actor 发生碰撞或重叠。

## 描述

在 3D 环境中创建 actor

Simulation 3D Actor 模块在 Unreal Engine® 环境中实现一个 actor。您可以使用此模块指定 actor 名称和源文件，设置 actor 在仿真期间的创建方式和行为，并初始化该 actor。该模块创建一个可移动的 actor。此外，您还可以创建其他 `sim3d` actor 对象并将其作为此 actor 的子级添加到 3D 环境中。
