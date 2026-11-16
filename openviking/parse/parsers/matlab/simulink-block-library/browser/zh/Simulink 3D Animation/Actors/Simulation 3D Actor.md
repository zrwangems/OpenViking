---
type: simulink-block
title: 'Simulation 3D Actor'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Actors'
documentation_page: 'simulation3dactor'
documentation_source_path: 'simulation3dactor.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Actor

## 端口

### 输入

### **Instance** — 角色的实例编号 real integer

角色的实例编号，指定为 real integer。

- 对于正值，如果尚未创建新角色，则会创建一个新角色。如果该角色存在于世界中，则引用模块会引用此角色。
- 对于负值，如果角色实例存在，则会删除它们。例如，如果在给定时步此端口的值是 `-1`，则实例 1 会被删除。

#### 依赖关系

当模块的运行模式设置为 `Create at step` 或 `Reference by instance number` 时，此输入可见。

### 输出

### **Valid** — 指定角色的有效性 `false` (default) | `true`

指定角色的有效性，如果无法在世界中找到指定角色，则返回 `false`；如果找到该角色，则返回 `true`。

## 参数

### 主要

### **Actor Name** — 角色名称 `Sim3dActor1` (default) | string

当前 Simulation 3D Actor 模块的根角色名称。

### **Parent Name** — 角色的父级 `Scene Origin` (default) | string

角色的父角色名称，指定为 string。

### **Operation** — 模块的运行模式 `Create at setup` (default) | `Create at step` | `Reference by name` | `Reference by instance number`

确定模块行为的运行模式，指定为下列选项之一。

- `Create at setup` – 使用此选项在场景中创建角色。这些角色在游戏设置期间、仿真运行之前创建。你还可以使用 **Input**、**Output** 和 **Event** 端口控制这些角色的仿真。
- `Create at step` – 使用此选项在仿真运行时动态创建和删除角色。在此模式下会创建一个类型为 `int` 的 **Instance** 输入端口，并且会根据输入到模块的值动态生成角色。如果 **Instance** 的值大于零，则会创建一个名为 `'Actor name + Instance value'` 的角色。角色名称派生自模块掩码中的 `'Actor Name'`。实例值是端口的当前值。当 **Instance** 的值为负时，则删除该角色。与 `Create at setup` 选项不同，你无法在模块掩码中控制使用此选项创建的角色。
- `Reference by name` – 使用此选项通过 `Actor Name` 引用场景中的角色，并使用模块的输入控制此角色的仿真。使用输出或事件获取角色的数据。这还会提供一个 **Valid** 输出端口。

  如果不存在具有指定名称的角色，则 **Valid** 端口会返回 `false` 或 `0`。在这种情况下，对于其余输出端口（如果有），将传递默认值作为输出。使用 `Valid` 端口验证生成的其他输出当前是否有效。

  **注意**

  在 `Reference by name` 运行模式下，**Path to source file** 和 **Initialization script** 参数不可用。
- `Reference by instance number` – 使用此选项引用通过其他角色模块创建的实例。与 `Create at step` 运行模式类似，此选项会在模块中创建一个 **Instance** 输入，并使用有效角色名称 `'Actor name + Instance value'` 来引用该角色。

  如果不存在具有生成名称的角色，则 **Valid** 端口会返回 `false` 或 `0`。在这种情况下，对于其余输出端口（如果有），将传递默认值作为输出。使用 **Valid** 端口验证生成的其他输出当前是否有效。

  **注意**

  在 `Reference by instance number` 运行模式下，**Path to source file** 和 **Initialization script** 参数不可用。

#### 依赖关系

如果将 **Operation** 设置为 `Create at setup` 或 `Create at step`，则 **变换** 选项卡可用。

### **Path to source file** — 角色来源文件 string

角色来源文件，指定为 string。

此选项加载 3D 文件或导入 `sim3d.Actor` 对象，包括子角色对象。`Simulation 3D Actor` 模块支持这些作为来源。

**文件格式**

- MAT（来自 MATLAB® 的 MAT 文件）
- STL（Stereolithography）
- FBX（Autodesk® Filmbox 格式）
- URDF（Unified Robot Description File）
- X3D（Extensible 3D）
- WRL（Virtual Reality Modeling Language）
- DAE（Collada digital asset exchange）
- USD、USDA、USDC（Universal Scene Description）

你也可以使用 `.m` 文件实例化角色。

或者，还可以使用 **Select** 按钮从 Windows® 文件浏览器中选择文件。

**注意**

Linux® 上不支持 USD 文件导入。USD 文件不支持碰撞检测。

### **Initialization script** — 用于初始化角色的代码 MATLAB script

用于初始化模块所创建角色的代码，指定为 MATLAB script。你也可以使用此脚本创建其他角色对象、设置其属性，并使用 `add` 函数将它们作为子角色添加到 3D 环境。必须使用 `add` 函数中的 `parent` 设置父角色。

当 3D 环境初始化模块创建的角色时，会运行此 MATLAB script。角色创建顺序为：

1. 创建具有指定名称的根角色。
2. 将 **Path to source file** 加载到根角色中。
3. 运行 **Initialization script**。

修改模块的根角色时，请使用名称 `Actor`。`Actor` 是初始化脚本中的保留句柄。否则，请使用 `findBy` 函数获取不同名称（例如某个子角色）的角色句柄。然后使用检索到的角色句柄初始化该特定角色。例如，要将一个角色添加为根角色的子级，请在 `add` 函数中将 `Actor` 设置为父角色。

对于 3D 环境中的角色，请使用名称 `World`。`World` 是由 Simulation 3D Scene Configuration 模块创建的 3D 环境的初始化脚本中的保留句柄。

你可以创建并添加以下 `sim3d` 角色对象。

- `sim3d.Light`
- `sim3d.graphics.Arrow`
- `sim3d.graphics.Text`
- `sim3d.graphics.PathMarker`

**Initialization script** 不使用基础工作区变量。

### **Sample time** — 采样时间 `-1` (default) | `scalar`

采样时间，*Ts*。图形帧率是采样时间的倒数。

如果将采样时间设置为 `-1`，则模块使用 Simulation 3D Scene Configuration 模块中指定的采样时间。

为获得最佳性能，请检查此值不小于 Simulation 3D Scene Configuration 模块中指定的 **Sample time** 值。

### 变换

当将 **Operation** 设置为 `Create at setup` 或 `Create at step` 时，**变换** 选项卡可用于设置初始变换属性。否则，**Initialization script** 中设置的变换属性会用于 **变换** 选项卡并覆盖那里设置的任何值。

### **Translation** — 相对平移 `[0,0,0]` (default) | real 1-by-3 vector

角色对象相对于其父角色的平移 (*x*,*y*,*z*)，指定为 real 1-by-3 vector，以 meters 为单位。

#### 依赖关系

**Initialization script** 中设置的 Translation 属性会覆盖此参数值。

### **Rotation** — 相对旋转 `[0,0,0]` (default) | real 1-by-3 vector

角色对象相对于其父角色的旋转（roll、pitch、yaw），指定为 real 1-by-3 vector，以 radians 为单位。

#### 依赖关系

**Initialization script** 中设置的 Rotation 属性会覆盖此参数值。

### **Scale** — 相对缩放 `[1,1,1]` (default) | real 1-by-3 vector

在 *x*、*y* 和 *z* 坐标中的相对缩放，指定为 real 1-by-3 vector。

#### 依赖关系

**Initialization script** 中设置的 Scale 属性会覆盖此参数值。

**注意**

在 **Initialization script** 中设置初始变换属性会覆盖 **变换** 选项卡中的值。

### 输入

### **Input ports** — 用户选择的输入端口列表 text area

此文本区域列出用户选择的模块输入端口，并提供一个按钮，用于打开端口选择器应用，你可以使用该应用修改输入端口。文本区域中的每一行表示一个模块端口。

你可以使用文本区域手动修改端口，但建议使用端口选择器应用来选择端口。

### 输出

### **Output ports** — 用户选择的输出端口列表 text area

此文本区域列出用户选择的模块输出端口，并提供一个按钮，用于打开端口选择器应用，你可以使用该应用修改输出端口。文本区域中的每一行表示一个模块端口。

你可以使用文本区域手动修改端口，但建议使用端口选择器应用来选择端口。

## 所属库

Simulink 3D Animation / Simulation 3D / Actors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

### R2024b: 创建 Light 和 Annotation 角色

使用 Simulation 3D Actor 模块的 **Initialization script**，通过可调模块参数在 3D 环境中初始化并添加这些角色。

- 使用 `sim3d.Light` 对象的 Light
- 使用 `sim3d.graphics.Arrow` 对象的 Arrow
- 使用 `sim3d.graphics.Text` 对象的 Text

### R2023b: 可调的 Translation、Rotation 和 Scale 参数

这些 Simulation 3D Actor 模块参数是可调的，允许你使用 For Each Subsystem (Simulink) 模块在虚拟世界中创建同一角色类型的多个实例。

- **Translation**
- **Rotation**
- **Scale**

有关示例，请参阅 Create Multiple Instances of Actors。

### R2023a: 传递 Unreal Engine 事件

使用 Simulation 3D Actor 模块事件端口在 Unreal Engine 仿真 3D 环境中传递事件，包括以下情况：

- 你点击某个角色。
- 一个角色与另一个角色发生碰撞或重叠。

## 描述

在 3D 环境中创建角色

Simulation 3D Actor 模块在 Unreal Engine® 环境中实现一个角色。你可以使用此模块指定角色名称和源文件，设置角色在仿真期间的创建方式和行为，并初始化角色。该模块会创建一个可移动角色。此外，你还可以创建其他 `sim3d` 角色对象，并将它们作为此角色的子级添加到 3D 环境。
