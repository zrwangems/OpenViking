---
type: simulink-block
title: 'Bushing Joint'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Joints'
documentation_page: 'bushingjoint'
documentation_source_path: 'ref/bushingjoint.html'
language: zh-CN
chinese_source: worker-translation
---

# Bushing Joint

## 端口

### 坐标系

### **B** — 基础坐标系 frame

关节模块的基础坐标系。

### **F** — 从动坐标系 frame

关节模块的从动坐标系。
### 输入

#### X 移动副基元 (Px)

### **fx** — 驱动力物理信号

物理信号输入端口，接受关节基元的驱动力。模块沿基础坐标系的 *x* 轴将力等大反向地施加到关节的基础坐标系和从动坐标系。

#### 依赖项

要启用此端口，请在 **X 移动副基元 (Px)** > **驱动** 下，将 **力** 设为 `Provided by Input`。

### **px** — 运动轮廓物理信号

物理信号输入端口，接受关节基元的运动轮廓。模块使用此信号确定从动坐标系相对于基础坐标系沿基础坐标系 *x* 轴的位移。该信号还必须包含位移的一阶和二阶导数。

#### 依赖项

要启用此端口，请在 **X 移动副基元 (Px)** > **驱动** 下，将 **运动** 设为 `Provided by Input`。

#### Y 移动副基元 (Py)

### **fy** — 驱动力物理信号

物理信号输入端口，接受关节基元的驱动力。模块沿基础坐标系的 *y* 轴将力等大反向地施加到关节的基础坐标系和从动坐标系。

#### 依赖项

要启用此端口，请在 **Y 移动副基元 (Py)** > **驱动** 下，将 **力** 设为 `Provided by Input`。

### **py** — 运动轮廓物理信号

物理信号输入端口，接受关节基元的运动轮廓。模块使用此信号确定从动坐标系相对于基础坐标系沿基础坐标系 *y* 轴的位移。该信号还必须包含位移的一阶和二阶导数。

#### 依赖项

要启用此端口，请在 **Y 移动副基元 (Py)** > **驱动** 下，将 **运动** 设为 `Provided by Input`。

#### Z 移动副基元 (Pz)

### **fz** — 驱动力物理信号

物理信号输入端口，接受关节基元的驱动力。模块沿基础坐标系的 *z* 轴将力等大反向地施加到关节的基础坐标系和从动坐标系。

#### 依赖项

要启用此端口，请在 **Z 移动副基元 (Pz)** > **驱动** 下，将 **力** 设为 `Provided by Input`。

### **pz** — 运动轮廓物理信号

物理信号输入端口，接受关节基元的运动轮廓。模块使用此信号确定从动坐标系相对于基础坐标系沿基础坐标系 *z* 轴的位移。该信号还必须包含位移的一阶和二阶导数。

#### 依赖项

要启用此端口，请在 **Z 移动副基元 (Pz)** > **驱动** 下，将 **运动** 设为 `Provided by Input`。

#### X 转动副基元 (Rx)

### **tx** — 驱动力矩物理信号

物理信号输入端口，接受关节基元的驱动力矩。模块将力矩等大反向地施加到关节基元的基础坐标系和从动坐标系两者。该力矩围绕基础坐标系的 *x* 轴。在仿真期间，从动坐标系和基础坐标系的 *x* 轴相互对齐。

#### 依赖项

要启用此端口，请在 **X 转动副基元 (Rx)** > **驱动** 下，将 **力矩** 设为 `Provided by Input`。

### **qx** — 运动轮廓物理信号

物理信号输入端口，接受关节基元的运动轮廓。模块使用此信号确定从动坐标系相对于基础坐标系围绕基础坐标系 *x* 轴的旋转。该信号还必须包含旋转的一阶和二阶导数。

#### 依赖项

要启用此端口，请在 **X 转动副基元 (Rx)** > **驱动** 下，将 **运动** 设为 `Provided by Input`。

#### Y 转动副基元 (Ry)

### **ty** — 驱动力矩物理信号

物理信号输入端口，接受关节基元的驱动力矩。模块将力矩等大反向地施加到关节基元的基础坐标系和从动坐标系两者。该力矩围绕基础坐标系的 *y* 轴。在仿真期间，从动坐标系和基础坐标系的 *y* 轴相互对齐。

#### 依赖项

要启用此端口，请在 **Y 转动副基元 (Ry)** > **驱动** 下，将 **力矩** 设为 `Provided by Input`。

### **qy** — 运动轮廓物理信号

物理信号输入端口，接受关节基元的运动轮廓。模块使用此信号确定从动坐标系相对于基础坐标系围绕基础坐标系 *y* 轴的旋转。该信号还必须包含旋转的一阶和二阶导数。

#### 依赖项

要启用此端口，请在 **Y 转动副基元 (Ry)** > **驱动** 下，将 **运动** 设为 `Provided by Input`。

#### Z 转动副基元 (Rz)

### **tz** — 驱动力矩物理信号

物理信号输入端口，接受关节基元的驱动力矩。模块将力矩等大反向地施加到关节基元的基础坐标系和从动坐标系两者。该力矩围绕基础坐标系的 *z* 轴。在仿真期间，从动坐标系和基础坐标系的 *z* 轴相互对齐。

#### 依赖项

要启用此端口，请在 **Z 转动副基元 (Rz)** > **驱动** 下，将 **力矩** 设为 `Provided by Input`。

### **qz** — 运动轮廓物理信号

物理信号输入端口，接受关节基元的运动轮廓。模块使用此信号确定从动坐标系相对于基础坐标系围绕基础坐标系 *z* 轴的旋转。该信号还必须包含旋转的一阶和二阶导数。

#### 依赖项

要启用此端口，请在 **Z 转动副基元 (Rz)** > **驱动** 下，将 **运动** 设为 `Provided by Input`。

#### 模式配置

### **mode** — 关节模式控制物理信号

控制关节模式的输入端口。该信号必须是无单位标量。当输入信号为 `0` 时，关节模式为 normal；当输入信号为 `-1` 时，为 disengaged；当输入信号为 `1` 时，为 locked。您可以在仿真期间的任何时间更改模式。

下表显示了关节在模式转换期间位置和速度的变化方式。

| 转换 | 位置 | 速度 |
| --- | --- | --- |
| Normal 到 Locked | 关节位置保留当前值，并在转换后保持恒定。 | 关节速度变为零，并在转换后保持恒定。 |
| Normal 到 Disengaged | 关节位置保留当前值，但转换后可在任意方向上变化。 | 关节速度保留当前值，但转换后可在任意方向上变化。 |
| Locked 到 Normal | 关节位置保留当前值，但转换后可沿与关节自由度 (DOFs) 对齐的方向变化。 | 关节速度保持为零，但转换后可沿与关节 DOFs 对齐的方向变化。 |
| Locked 到 Disengaged | 关节位置保留当前值，但转换后可在任意方向上变化。 | 关节速度保持为零，但转换后可在任意方向上变化。 |
| Disengaged 到 Normal | 对于与关节 DOFs 对齐的方向，关节位置最初取通过牛顿法计算的值，此后可以变化。在受约束方向上，关节位置变为零，并在转换后保持恒定。 | 对于与关节 DOFs 对齐的方向，关节速度最初取通过牛顿法计算的值，此后可以变化。在受约束方向上，关节速度变为零，并在转换后保持恒定。 |
| Disengaged 到 Locked | 对于与关节 DOFs 对齐的方向，关节位置最初取通过牛顿法计算的值，并在转换后保持恒定。在受约束方向上，关节位置变为零，并在转换后保持恒定。 | 关节速度变为零，并在转换后保持恒定。 |

#### 依赖项

要启用此端口，请在 **模式配置** 下，将 **模式** 设为 `Provided by Input`。
### 输出

#### X 移动副基元 (Px)

### **px** — 基元位置物理信号

输出关节基元位置的物理信号端口。该值是从动坐标系相对于基础坐标系沿基础坐标系 *x* 方向的位移。

#### 依赖项

要启用此端口，请在 **X 移动副基元 (Px)** > **感测** 下，选择 **位置**。

### **vx** — 基元速度物理信号

输出关节基元速度的物理信号端口。该值是来自端口 **px** 的信号的一阶导数。

#### 依赖项

要启用此端口，请在 **X 移动副基元 (Px)** > **感测** 下，选择 **速度**。

### **ax** — 基元加速度物理信号

输出关节基元加速度的物理信号端口。该值是来自端口 **px** 的信号的二阶导数。

#### 依赖项

要启用此端口，请在 **X 移动副基元 (Px)** > **感测** 下，选择 **加速度**。

### **fx** — 作用在关节基元上的执行器力物理信号

输出作用在关节基元上的执行器力的物理信号端口。

#### 依赖项

要启用此端口，请在 **X 移动副基元 (Px)** > **感测** 下，选择 **执行器力**。

### **fllx** — 下限力物理信号

输出下限力的物理信号端口。当关节基元位置小于自由区域的下界时，模块施加此力。模块将此力施加到关节基元的基础坐标系和从动坐标系两者，以使相对位置加速回到自由区域。

#### 依赖项

要启用此端口，请在 **X 移动副基元 (Px)** > **感测** 下，选择 **下限力**。

### **fulx** — 上限力物理信号

输出上限力的物理信号端口。当关节基元位置超过自由区域的上界时，模块施加此力。模块将此力施加到关节基元的基础坐标系和从动坐标系两者，以使相对位置加速回到自由区域。

#### 依赖项

要启用此端口，请在 **X 移动副基元 (Px)** > **感测** 下，选择 **上限力**。

#### Y 移动副基元 (Py)

### **py** — 基元位置物理信号

输出关节基元位置的物理信号端口。该值是从动坐标系相对于基础坐标系沿基础坐标系 *y* 方向的位移。

#### 依赖项

要启用此端口，请在 **Y 移动副基元 (Py)** > **感测** 下，选择 **位置**。

### **vy** — 基元速度物理信号

输出关节基元速度的物理信号端口。该值是来自端口 **py** 的信号的一阶导数。

#### 依赖项

要启用此端口，请在 **Y 移动副基元 (Py)** > **感测** 下，选择 **速度**。

### **ay** — 基元加速度物理信号

输出关节基元加速度的物理信号端口。该值是来自端口 **py** 的信号的二阶导数。

#### 依赖项

要启用此端口，请在 **Y 移动副基元 (Py)** > **感测** 下，选择 **加速度**。

### **fy** — 作用在关节基元上的执行器力物理信号

输出作用在关节基元上的执行器力的物理信号端口。

#### 依赖项

要启用此端口，请在 **Y 移动副基元 (Py)** > **感测** 下，选择 **执行器力**。

### **flly** — 下限力物理信号

输出下限力的物理信号端口。当关节基元位置小于自由区域的下界时，模块施加此力。模块将此力施加到关节基元的基础坐标系和从动坐标系两者，以使相对位置加速回到自由区域。

#### 依赖项

要启用此端口，请在 **Y 移动副基元 (Py)** > **感测** 下，选择 **下限力**。

### **fuly** — 上限力物理信号

输出上限力的物理信号端口。当关节基元位置超过自由区域的上界时，模块施加此力。模块将此力施加到关节基元的基础坐标系和从动坐标系两者，以使相对位置加速回到自由区域。

#### 依赖项

要启用此端口，请在 **Y 移动副基元 (Py)** > **感测** 下，选择 **上限力**。

#### Z 移动副基元 (Pz)

### **pz** — 关节基元位置物理信号

输出关节基元位置的物理信号端口。该值是从动坐标系相对于基础坐标系沿基础坐标系的 *z* 轴的位移。

#### 依赖项

要启用此端口，请在 **Z 移动副基元 (Pz)** > **感测** 下，选择 **位置**。

### **vz** — 关节基元速度物理信号

输出关节基元速度的物理信号端口。该值是来自端口 **pz** 的信号的一阶导数。

#### 依赖项

要启用此端口，请在 **Z 移动副基元 (Pz)** > **感测** 下，选择 **速度**。

### **az** — 关节基元加速度物理信号

输出关节基元加速度的物理信号端口。该值是来自端口 **pz** 的信号的二阶导数。

#### 依赖项

要启用此端口，请在 **Z 移动副基元 (Pz)** > **感测** 下，选择 **加速度**。

### **fz** — 作用在关节基元上的执行器力物理信号

输出作用在关节基元上的执行器力的物理信号端口。

#### 依赖项

要启用此端口，请在 **Z 移动副基元 (Pz)** > **感测** 下，选择 **执行器力**。

### **fllz** — 作用在关节基元上的下限力物理信号

输出下限力的物理信号端口。当关节基元位置小于自由区域的下界时，模块施加此力。模块将此力施加到关节基元的基础坐标系和从动坐标系两者，以使相对位置加速回到自由区域。

#### 依赖项

要启用此端口，请在 **Z 移动副基元 (Pz)** > **感测** 下，选择 **下限力**。

### **fulz** — 作用在关节基元上的上限力物理信号

输出上限力的物理信号端口。当关节基元位置超过自由区域的上界时，模块施加此力。模块将此力施加到关节基元的基础坐标系和从动坐标系两者，以使相对位置加速回到自由区域。

#### 依赖项

要启用此端口，请在 **Z 移动副基元 (Pz)** > **感测** 下，选择 **上限力**。

#### X 转动副基元 (Rx)

### **qx** — 关节基元位置物理信号

输出关节基元位置的物理信号端口。该值是从动坐标系相对于基础坐标系围绕基础坐标系 *x* 轴的旋转角度。

#### 依赖项

要启用此端口，请在 **X 转动副基元 (Rx)** > **感测** 下，选择 **位置**。

### **wx** — 关节基元的角速度物理信号

输出关节基元角速度的物理信号端口。该值是来自端口 **qx** 的信号的一阶导数。

#### 依赖项

要启用此端口，请在 **X 旋转基元 (Rx)** > **感测** 下，选择 **Velocity**。

### **bx** — 关节基元的角加速度物理信号

输出关节基元角加速度的物理信号端口。该值是来自端口 **qx** 的信号的二阶导数。

#### 依赖项

要启用此端口，请在 **X 旋转基元 (Rx)** > **感测** 下，选择 **Acceleration**。

### **tx** — 作用在关节基元上的执行器力矩物理信号

输出作用在关节基元上的执行器力矩的物理信号端口。

#### 依赖项

要启用此端口，请在 **X 旋转基元 (Rx)** > **感测** 下，选择 **Actuator Torque**。

### **tllx** — 作用在关节基元上的下限力矩物理信号

输出下限力矩的物理信号端口。当关节基元位置小于自由区域的下界时，该模块施加此力矩。该模块将此外力矩施加到关节基元的基座坐标系和从动坐标系两者，以加速相对位置返回到自由区域。

#### 依赖项

要启用此端口，请在 **X 旋转基元 (Rx)** > **感测** 下，选择 **Lower-Limit Torque**。

### **tulx** — 作用在关节基元上的上限力矩物理信号

输出上限力矩的物理信号端口。当关节基元位置超过自由区域的上界时，该模块施加此力矩。该模块将此外力矩施加到关节基元的基座坐标系和从动坐标系两者，以加速相对位置返回到自由区域。

#### 依赖项

要启用此端口，请在 **X 旋转基元 (Rx)** > **感测** 下，选择 **Upper-Limit Torque**。

#### Y 旋转基元 (Ry)

### **qy** — 关节基元位置物理信号

输出关节基元位置的物理信号端口。该值是从动坐标系相对于基座坐标系绕基座坐标系 *y* 轴的旋转角度。

#### 依赖项

要启用此端口，请在 **Y 旋转基元 (Ry)** > **感测** 下，选择 **Position**。

### **wy** — 关节基元的角速度物理信号

输出关节基元角速度的物理信号端口。该值是来自端口 **qy** 的信号的一阶导数。

#### 依赖项

要启用此端口，请在 **Y 旋转基元 (Ry)** > **感测** 下，选择 **Velocity**。

### **by** — 关节基元的角加速度物理信号

输出关节基元角加速度的物理信号端口。该值是来自端口 **qy** 的信号的二阶导数。

#### 依赖项

要启用此端口，请在 **Y 旋转基元 (Ry)** > **感测** 下，选择 **Acceleration**。

### **ty** — 作用在关节基元上的执行器力矩物理信号

输出作用在关节基元上的执行器力矩的物理信号端口。

#### 依赖项

要启用此端口，请在 **Y 旋转基元 (Ry)** > **感测** 下，选择 **Actuator Torque**。

### **tlly** — 作用在关节基元上的下限力矩物理信号

输出下限力矩的物理信号端口。当关节基元位置小于自由区域的下界时，该模块施加此力矩。该模块将此外力矩施加到关节基元的基座坐标系和从动坐标系两者，以加速相对位置返回到自由区域。

#### 依赖项

要启用此端口，请在 **Y 旋转基元 (Ry)** > **感测** 下，选择 **Lower-Limit Torque**。

### **tuly** — 作用在关节基元上的上限力矩物理信号

输出上限力矩的物理信号端口。当关节基元位置超过自由区域的上界时，该模块施加此力矩。该模块将此外力矩施加到关节基元的基座坐标系和从动坐标系两者，以加速相对位置返回到自由区域。

#### 依赖项

要启用此端口，请在 **Y 旋转基元 (Ry)** > **感测** 下，选择 **Upper-Limit Torque**。

#### Z 旋转基元 (Rz)

### **qz** — 关节基元位置物理信号

输出关节基元位置的物理信号端口。该值是从动坐标系相对于基座坐标系绕基座坐标系 *z* 轴的旋转角度。

#### 依赖项

要启用此端口，请在 **Z 旋转基元 (Rz)** > **感测** 下，选择 **Position**。

### **wz** — 关节基元的角速度物理信号

输出关节基元角速度的物理信号端口。该值是来自端口 **qz** 的信号的一阶导数。

#### 依赖项

要启用此端口，请在 **Z 旋转基元 (Rz)** > **感测** 下，选择 **Velocity**。

### **bz** — 关节基元的角加速度物理信号

输出关节基元角加速度的物理信号端口。该值是来自端口 **qz** 的信号的二阶导数。

#### 依赖项

要启用此端口，请在 **Z 旋转基元 (Rz)** > **感测** 下，选择 **Acceleration**。

### **tz** — 作用在关节基元上的执行器力矩物理信号

输出作用在关节基元上的执行器力矩的物理信号端口。

#### 依赖项

要启用此端口，请在 **Z 旋转基元 (Rz)** > **感测** 下，选择 **Actuator Torque**。

### **tllz** — 作用在关节基元上的下限力矩物理信号

输出下限力矩的物理信号端口。当关节基元位置小于自由区域的下界时，该模块施加此力矩。该模块将此外力矩施加到关节基元的基座坐标系和从动坐标系两者，以加速相对位置返回到自由区域。

#### 依赖项

要启用此端口，请在 **Z 旋转基元 (Rz)** > **感测** 下，选择 **Lower-Limit Torque**。

### **tulz** — 作用在关节基元上的上限力矩物理信号

输出上限力矩的物理信号端口。当关节基元位置超过自由区域的上界时，该模块施加此力矩。该模块将此外力矩施加到关节基元的基座坐标系和从动坐标系两者，以加速相对位置返回到自由区域。

#### 依赖项

要启用此端口，请在 **Z 旋转基元 (Rz)** > **感测** 下，选择 **Upper-Limit Torque**。

#### 复合力/力矩感测

### **fc** — 约束力，N 物理信号

输出作用在关节上的约束力的物理信号端口。这些力维持关节的平移约束。输出采用 3-by-1 向量格式，表示沿解析坐标系 `x`、`y` 和 `z` 轴的分力。有关详细信息，请参阅力和力矩感测。

#### 依赖项

要启用此端口，请在 **复合力/力矩感测** 下，选择 **Constraint Force**。

### **tc** — 约束力矩，N\*m 物理信号

输出作用在关节上的约束力矩的物理信号端口。这些力矩维持关节的旋转约束。输出采用 3-by-1 向量格式，表示绕解析坐标系 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅力和力矩感测。

#### 依赖项

要启用此端口，请在 **复合力/力矩感测** 下，选择 **Constraint Torque**。

### **ft** — 总力，N 物理信号

输出作用在关节上的总力的物理信号端口。总力是通过关节在相连坐标系之间传递的所有力之和。输出采用 3-by-1 向量格式，表示沿解析坐标系 `x`、`y` 和 `z` 轴的分力。

为了演示作用在关节上的总力，该图显示了一个使用 Prismatic Joint 模块的模型。

总力示意图

总力包括执行器力（*F*A）、内部力（*F*I）和约束力（*F*C）。有关详细信息，请参阅力和力矩感测。

#### 依赖项

要启用此端口，请在 **复合力/力矩感测** 下，选择 **Total Force**。

### **tt** — 总力矩，N\*m 物理信号

输出作用在关节上的总力矩的物理信号端口。总力矩是通过关节在相连坐标系之间传递的所有力矩之和。该力矩包括驱动、内部、限制和约束力矩。输出采用 3-by-1 向量格式，表示绕解析坐标系 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅力和力矩感测。

#### 依赖项

要启用此端口，请在 **复合力/力矩感测** 下，选择 **Total Torque**。

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink Toolstrip 中，**Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### X 平移基元 (Px)

#### 状态目标

### **Specify Position Target** — 是否指定位置目标 `off`（默认） | `on`

选择此参数以指定 *x* 平移基元的位置目标。

### **Priority** — 位置目标的优先级级别 `High (desired)`（默认） | `Low (approximate)`

位置目标的优先级级别，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖项

要启用此参数，请选择 **Specify Position Target**。

### **Value** — 位置目标 0 `m`（默认） | scalar

*x* 平移基元的位置目标，指定为长度单位的 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Position Target**。

### **Specify Velocity Target** — 是否指定线速度目标 `off`（默认） | `on`

选择此参数以指定 *x* 平移基元的线速度目标。

### **Priority** — 线速度目标的优先级级别 `High (desired)`（默认） | `Low (approximate)`

线速度目标的优先级级别，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖项

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 速度目标 0 `m/s`（默认） | scalar

*x* 平移基元的线速度目标，指定为线速度单位的 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Velocity Target**。

#### 内部力学

### **Equilibrium Position** — 内部力为零的位置 0 `m`（默认） | scalar

弹簧力为零的位置，指定为长度单位的 scalar。

### **Spring Stiffness** — 力定律的刚度 0 `N/m`（默认） | scalar

关节基元的内部弹簧-阻尼力定律的刚度，指定为线性刚度单位的 scalar。

### **Damping Coefficient** — 力定律的阻尼系数 0 `N(m/s)`（默认） | scalar

关节基元的内部弹簧-阻尼力定律的阻尼系数，指定为线性阻尼系数单位的 scalar。

#### 限制

### **Specify Lower Limit** — 是否指定下限位置 `off`（默认） | `on`

选择此参数以指定 *x* 平移基元的下限。

### **Bound** — 自由区域下界 -1 `m`（默认） | scalar

*x* 平移基元的自由区域下界，指定为长度单位的 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Spring Stiffness** — 下界处的弹簧刚度 1e6 `N/m`（默认） | scalar

下界处的弹簧刚度，指定为线性刚度单位的 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Damping Coefficient** — 下界处的阻尼系数 1e3 `N/(m/s)`（默认） | scalar

下界处的阻尼系数，指定为线性阻尼系数单位的 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Transition Region Width** — 用于平滑弹簧力和阻尼力的区域 1e-4 `m`（默认） | scalar

用于平滑弹簧力和阻尼力的区域，指定为长度单位的 scalar。

当穿透达到过渡区域宽度时，该模块施加完整的下限力值。区域越小，力的出现越陡峭，求解器所需的时间步长越小。在仿真精度和仿真速度之间的权衡中，减小过渡区域可提高精度，扩大过渡区域可提高速度。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定上限位置 `off`（默认） | `on`

选择此参数以指定 *x* 平移基元的上限。

### **Bound** — 自由区域上界 1 `m`（默认） | scalar

关节基元自由区域的上界，指定为长度单位的 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上界处的弹簧刚度 1e6 `N/m`（默认） | scalar

上界处的弹簧刚度，指定为线性刚度单位的 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上界处的阻尼系数 1e3 `N/(m/s)`（默认） | scalar

上界处的阻尼系数，指定为线性阻尼系数单位的 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧力和阻尼力的区域 1e-4 `m`（默认） | scalar

用于平滑弹簧力和阻尼力的区域，指定为长度单位的 scalar。

当穿透达到过渡区域宽度时，该模块施加完整的上限力值。区域越小，力的出现越陡峭，求解器所需的时间步长越小。在仿真精度和仿真速度之间的权衡中，减小过渡区域可提高精度，扩大过渡区域可提高速度。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Force** — 提供执行器力的选项 `None`（默认） | `Provided by Input` | `Automatically Computed`

为关节基元提供执行器力的选项，指定为以下值之一：

| 力设置 | 描述 |
| --- | --- |
| `None` | 无执行器力。 |
| `Provided by Input` | 输入端口 **fx** 为 *x* 平移基元指定执行器力。 |
| `Automatically Computed` | 该模块自动计算满足机构运动输入所需的力。如果将此参数设置为 `Automatically Computed`，则无需为同一关节基元将 **Motion** 设置为 `Provided by Input`。自动计算的力可以满足机构其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

提供关节原语运动的选项，指定为以下值之一：

| 运动设置 | 描述 |
| --- | --- |
| `Automatically Computed` | 模块根据模型动力学计算并应用关节原语运动。 |
| `Provided by Input` | 输入端口 **px** 指定关节原语的运动。 |

### Y Prismatic Primitive (Py)

#### 状态目标

### **Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选择此参数以指定 *y* 移动副原语的位置目标。

### **Priority** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖项

要启用此参数，请选择 **Specify Position Target**。

### **Value** — 位置目标 0 `m`（默认）| scalar

*y* 移动副原语的位置目标，以长度为单位指定为 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Position Target**。

### **Specify Velocity Target** — 是否指定线速度目标 `off`（默认）| `on`

选择此参数以指定 *y* 移动副原语的线速度目标。

### **Priority** — 线速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

线速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖项

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 速度目标 0 `m/s`（默认）| scalar

*y* 移动副原语的线速度目标，以线速度为单位指定为 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Velocity Target**。

#### 内部力学

### **Equilibrium Position** — 内部力为零时的位置 0 `m`（默认）| scalar

弹簧力为零时的位置，以长度为单位指定为 scalar。

### **Spring Stiffness** — 力定律的刚度 0 `N/m`（默认）| scalar

关节原语的内部弹簧-阻尼力定律的刚度，以线性刚度为单位指定为 scalar。

### **Damping Coefficient** — 力定律的阻尼系数 0 `N(m/s)`（默认）| scalar

关节原语的内部弹簧-阻尼力定律的阻尼系数，以线性阻尼系数为单位指定为 scalar。

#### 限制

### **Specify Lower Limit** — 是否指定位置下限 `off`（默认）| `on`

选择此参数以指定 *y* 移动副原语的下限。

### **Bound** — 自由区域的下界 -1 `m`（默认）| scalar

*y* 移动副原语的自由区域的下界，以长度为单位指定为 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Spring Stiffness** — 下限处弹簧的刚度 1e6 `N/m`（默认）| scalar

下限处弹簧的刚度，以线性刚度为单位指定为 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Damping Coefficient** — 下限处的阻尼系数 1e3 `N/(m/s)`（默认）| scalar

下限处的阻尼系数，以线性阻尼系数为单位指定为 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Transition Region Width** — 用于平滑弹簧力和阻尼力的区域 1e-4 `m`（默认）| scalar

用于平滑弹簧力和阻尼力的区域，以长度为单位指定为 scalar。

当穿透量达到过渡区域的宽度时，模块施加下限力的完整值。该区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，而扩大过渡区域可提高速度。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定位置上限 `off`（默认）| `on`

选择此参数以指定 *y* 移动副原语的上限。

### **Bound** — 自由区域的上界 1 `m`（默认）| scalar

关节原语的自由区域的上界，以长度为单位指定为 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上限处弹簧的刚度 1e6 `N/m`（默认）| scalar

上限处弹簧的刚度，以线性刚度为单位指定为 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上限处的阻尼系数 1e3 `N/(m/s)`（默认）| scalar

上限处的阻尼系数，以线性阻尼系数为单位指定为 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧力和阻尼力的区域 1e-4 `m`（默认）| scalar

用于平滑弹簧力和阻尼力的区域，以长度为单位指定为 scalar。

当穿透量达到过渡区域的宽度时，模块施加上限力的完整值。该区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，而扩大过渡区域可提高速度。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Force** — 提供执行器力的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

提供关节原语执行器力的选项，指定为以下值之一：

| 力设置 | 描述 |
| --- | --- |
| `None` | 无执行器力。 |
| `Provided by Input` | 输入端口 **fy** 指定 *y* 移动副原语的执行器力。 |
| `Automatically Computed` | 模块自动计算满足机构运动输入所需的力的大小。如果将此参数设置为 `Automatically Computed`，则无需为同一关节原语将 **Motion** 设置为 `Provided by Input`。自动计算的力可以满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

提供关节原语运动的选项，指定为以下值之一：

| 运动设置 | 描述 |
| --- | --- |
| `Automatically Computed` | 模块根据模型动力学计算并应用关节原语运动。 |
| `Provided by Input` | 输入端口 **py** 指定关节原语的运动。 |

### Z Prismatic Primitive (Pz)

#### 状态目标

### **Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选择此参数以指定 *z* 移动副原语的位置目标。

### **Priority** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖项

要启用此参数，请选择 **Specify Position Target**。

### **Value** — 位置目标 0 `m`（默认）| scalar

*z* 移动副原语的位置目标，以长度为单位指定为 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Position Target**。

### **Specify Velocity Target** — 是否指定线速度目标 `off`（默认）| `on`

选择此参数以指定 *z* 移动副原语的线速度目标。

### **Priority** — 线速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

线速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖项

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 速度目标 0 `m/s`（默认）| scalar

*z* 移动副原语的线速度目标，以线速度为单位指定为 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Velocity Target**。

#### 内部力学

### **Equilibrium Position** — 内部力为零时的位置 0 `m`（默认）| scalar

弹簧力为零时的位置，以长度为单位指定为 scalar。

### **Spring Stiffness** — 力定律的刚度 0 `N/m`（默认）| scalar

关节原语的内部弹簧-阻尼力定律的刚度，以线性刚度为单位指定为 scalar。

### **Damping Coefficient** — 力定律的阻尼系数 0 `N(m/s)`（默认）| scalar

关节原语的内部弹簧-阻尼力定律的阻尼系数，以线性阻尼系数为单位指定为 scalar。

#### 限制

### **Specify Lower Limit** — 是否指定位置下限 `off`（默认）| `on`

选择此参数以指定 *z* 移动副原语的下限。

### **Bound** — 自由区域的下界 -1 `m`（默认）| scalar

*z* 移动副原语的自由区域的下界，以长度为单位指定为 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Spring Stiffness** — 下限处弹簧的刚度 1e6 `N/m`（默认）| scalar

下限处弹簧的刚度，以线性刚度为单位指定为 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Damping Coefficient** — 下限处的阻尼系数 1e3 `N/(m/s)`（默认）| scalar

下限处的阻尼系数，以线性阻尼系数为单位指定为 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Transition Region Width** — 用于平滑弹簧力和阻尼力的区域 1e-4 `m`（默认）| scalar

用于平滑弹簧力和阻尼力的区域，以长度为单位指定为 scalar。

当穿透量达到过渡区域的宽度时，模块施加下限力的完整值。该区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，而扩大过渡区域可提高速度。

#### 依赖项

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定位置上限 `off`（默认）| `on`

选择此参数以指定 *z* 移动副原语的上限。

### **Bound** — 自由区域的上界 1 `m`（默认）| scalar

关节原语的自由区域的上界，以长度为单位指定为 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上限处弹簧的刚度 1e6 `N/m`（默认）| scalar

上限处弹簧的刚度，以线性刚度为单位指定为 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上限处的阻尼系数 1e3 `N/(m/s)`（默认）| scalar

上限处的阻尼系数，以线性阻尼系数为单位指定为 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧力和阻尼力的区域 1e-4 `m`（默认）| scalar

用于平滑弹簧力和阻尼力的区域，以长度为单位指定为 scalar。

当穿透量达到过渡区域的宽度时，模块施加上限力的完整值。该区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，而扩大过渡区域可提高速度。

#### 依赖项

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Force** — 提供执行器力的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

提供关节原语执行器力的选项，指定为以下值之一：

| 力设置 | 描述 |
| --- | --- |
| `None` | 无执行器力。 |
| `Provided by Input` | 输入端口 **fz** 指定 *z* 移动副原语的执行器力。 |
| `Automatically Computed` | 模块自动计算满足机构运动输入所需的力的大小。如果将此参数设置为 `Automatically Computed`，则无需为同一关节原语将 **Motion** 设置为 `Provided by Input`。自动计算的力可以满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

提供关节原语运动的选项，指定为以下值之一：

| 运动设置 | 描述 |
| --- | --- |
| `Automatically Computed` | 模块根据模型动力学计算并应用关节原语运动。 |
| `Provided by Input` | 输入端口 **pz** 指定关节原语的运动。 |

### X Revolute Primitive (Rx)

#### 状态目标

### **Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选择此参数以指定 *x* 转动副原语的位置目标。

### **Priority** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works.. 的 Guiding Assembly 部分。

#### 依赖项

要启用此参数，请选择 **Specify Position Target**。

### **Value** — 位置目标 0 `deg`（默认）| scalar

*x* 转动副原语的位置目标，以角度为单位指定为 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Position Target**。

### **Specify Velocity Target** — 是否指定角速度目标 `off`（默认）| `on`

选择此参数以指定 *x* 转动副原语的角速度目标。

### **Priority** — 速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

角速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关详细信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖项

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 速度目标 0 `deg/s`（默认）| scalar

*x* 转动副原语的角速度目标，以角速度为单位指定为 scalar。

#### 依赖项

要启用此参数，请选择 **Specify Velocity Target**。

#### 内部力学

### **Equilibrium Position** — 内部力矩为零时的位置 0 `deg`（默认）| scalar

弹簧力矩为零时的位置，以角度为单位指定为 scalar。

### **Spring Stiffness** — 力定律的刚度 0 `N*m/deg`（默认）| scalar

*x* 转动基元的内部弹簧-阻尼力定律的刚度，指定为具有扭转刚度单位的 scalar。

### **Damping Coefficient** — 力定律的阻尼系数 0 `N*m/(deg/s)`（默认）| scalar

*x* 转动基元的内部弹簧-阻尼力定律的阻尼系数，指定为具有阻尼系数单位的 scalar。

#### 限制

### **Specify Lower Limit** — 是否指定位置下限 `off`（默认）| `on`

选择此参数以指定 *x* 转动基元的下限。

### **Bound** — 自由区域的下界 -90 `deg`（默认）| scalar

*x* 转动基元的自由区域的下界，指定为具有角度单位的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Spring Stiffness** — 下界处的弹簧刚度 1e4 `N*m/deg`（默认）| scalar

下界处的弹簧刚度，指定为具有扭转刚度单位的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Damping Coefficient** — 下界处的阻尼系数 10 `N*m/(deg/s)`（默认）| scalar

下界处的阻尼系数，指定为具有阻尼系数单位的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼力矩的区域 0.1 `deg`（默认）| scalar

用于平滑弹簧和阻尼力矩的区域，指定为具有角度单位的 scalar。

当穿透量达到过渡区域宽度时，模块施加下限力矩的完整值。区域越小，力开始作用越急剧，求解器所需的时间步长越小。在仿真精度和仿真速度之间的权衡中，减小过渡区域可提高精度，扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定位置上限 `off`（默认）| `on`

选择此参数以指定 *x* 转动基元的上限。

### **Bound** — 自由区域的上界 90 `deg`（默认）| scalar

*x* 转动基元的自由区域的上界，指定为具有角度单位的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上界处的弹簧刚度 1e4 `N*m/deg`（默认）| scalar

上界处的弹簧刚度，指定为具有扭转刚度单位的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上界处的阻尼系数 10 `N*m/(deg/s)`（默认）| scalar

上界处的阻尼系数，指定为具有阻尼系数单位的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼力矩的区域 0.1 `deg`（默认）| scalar

用于平滑弹簧和阻尼力矩的区域，指定为具有角度单位的 scalar。

当穿透量达到过渡区域宽度时，模块施加上限力矩的完整值。区域越小，力开始作用越急剧，求解器所需的时间步长越小。在仿真精度和仿真速度之间的权衡中，减小过渡区域可提高精度，扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Torque** — 提供执行器力矩的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

提供关节基元执行器力矩的选项，指定为下列值之一：

| 力矩设置 | 描述 |
| --- | --- |
| `None` | 无执行器力矩。 |
| `Provided by Input` | 输入端口 **tx** 指定 *x* 转动基元的执行器力矩。 |
| `Automatically Computed` | 模块自动计算力矩。如果将此参数设置为 `Automatically Computed`，则无需为同一关节基元将 **Motion** 设置为 `Provided by Input`。自动计算的力矩可能会满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

提供关节基元运动的选项，指定为下列值之一：

| 运动设置 | 描述 |
| --- | --- |
| `Automatically computed` | 模块根据模型动力学计算并应用关节基元运动。 |
| `Provided by Input` | 输入端口 **qx** 指定 *x* 转动基元的运动。 |

### Y 转动基元 (Ry)

#### 状态目标

### **Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选择此参数以指定 *y* 转动基元的位置目标。

### **Priority** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关更多信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Value** — 位置目标 0 `deg`（默认）| scalar

*y* 转动基元的位置目标，指定为具有角度单位的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Specify Velocity Target** — 是否指定角速度目标 `off`（默认）| `on`

选择此参数以指定 *y* 转动基元的角速度目标。

### **Priority** — 速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

角速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关更多信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 速度目标 0 `deg/s`（默认）| scalar

*y* 转动基元的角速度目标，指定为具有角速度单位的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

#### 内部力学

### **Equilibrium Position** — 内部力矩为零的位置 0 `deg`（默认）| scalar

弹簧力矩为零的位置，指定为具有角度单位的 scalar。

### **Spring Stiffness** — 力定律的刚度 0 `N*m/deg`（默认）| scalar

*y* 转动基元的内部弹簧-阻尼力定律的刚度，指定为具有扭转刚度单位的 scalar。

### **Damping Coefficient** — 力定律的阻尼系数 0 `N*m/(deg/s)`（默认）| scalar

*y* 转动基元的内部弹簧-阻尼力定律的阻尼系数，指定为具有阻尼系数单位的 scalar。

#### 限制

### **Specify Lower Limit** — 是否指定位置下限 `off`（默认）| `on`

选择此参数以指定 *y* 转动基元的下限。

### **Bound** — 自由区域的下界 -90 `deg`（默认）| scalar

*y* 转动基元的自由区域的下界，指定为具有角度单位的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Spring Stiffness** — 下界处的弹簧刚度 1e4 `N*m/deg`（默认）| scalar

下界处的弹簧刚度，指定为具有扭转刚度单位的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Damping Coefficient** — 下界处的阻尼系数 10 `N*m/(deg/s)`（默认）| scalar

下界处的阻尼系数，指定为具有阻尼系数单位的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼力矩的区域 0.1 `deg`（默认）| scalar

用于平滑弹簧和阻尼力矩的区域，指定为具有角度单位的 scalar。

当穿透量达到过渡区域宽度时，模块施加下限力矩的完整值。区域越小，力开始作用越急剧，求解器所需的时间步长越小。在仿真精度和仿真速度之间的权衡中，减小过渡区域可提高精度，扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定位置上限 `off`（默认）| `on`

选择此参数以指定 *y* 转动基元的上限。

### **Bound** — 自由区域的上界 90 `deg`（默认）| scalar

*y* 转动基元的自由区域的上界，指定为具有角度单位的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上界处的弹簧刚度 1e4 `N*m/deg`（默认）| scalar

上界处的弹簧刚度，指定为具有扭转刚度单位的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上界处的阻尼系数 10 `N*m/(deg/s)`（默认）| scalar

上界处的阻尼系数，指定为具有阻尼系数单位的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼力矩的区域 0.1 `deg`（默认）| scalar

用于平滑弹簧和阻尼力矩的区域，指定为具有角度单位的 scalar。

当穿透量达到过渡区域宽度时，模块施加上限力矩的完整值。区域越小，力开始作用越急剧，求解器所需的时间步长越小。在仿真精度和仿真速度之间的权衡中，减小过渡区域可提高精度，扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Torque** — 提供执行器力矩的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

提供关节基元执行器力矩的选项，指定为下列值之一：

| 力矩设置 | 描述 |
| --- | --- |
| `None` | 无执行器力矩。 |
| `Provided by Input` | 输入端口 **ty** 指定 *y* 转动基元的执行器力矩。 |
| `Automatically Computed` | 模块自动计算力矩。如果将此参数设置为 `Automatically Computed`，则无需为同一关节基元将 **Motion** 设置为 `Provided by Input`。自动计算的力矩可能会满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

提供关节基元运动的选项，指定为下列值之一：

| 运动设置 | 描述 |
| --- | --- |
| `Automatically computed` | 模块根据模型动力学计算并应用关节基元运动。 |
| `Provided by Input` | 输入端口 **qy** 指定 *y* 转动基元的运动。 |

### Z 转动基元 (Rz)

#### 状态目标

### **Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选择此参数以指定 *z* 转动基元的位置目标。

### **Priority** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关更多信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Value** — 位置目标 0 `deg`（默认）| scalar

*z* 转动基元的位置目标，指定为具有角度单位的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Position Target**。

### **Specify Velocity Target** — 是否指定角速度目标 `off`（默认）| `on`

选择此参数以指定 *z* 转动基元的角速度目标。

### **Priority** — 速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

角速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。有关更多信息，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

### **Value** — 速度目标 0 `deg/s`（默认）| scalar

*z* 转动基元的角速度目标，指定为具有角速度单位的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Velocity Target**。

#### 内部力学

### **Equilibrium Position** — 内部力矩为零的位置 0 `deg`（默认）| scalar

弹簧力矩为零的位置，指定为具有角度单位的 scalar。

### **Spring Stiffness** — 力定律的刚度 0 `N*m/deg`（默认）| scalar

*z* 转动基元的内部弹簧-阻尼力定律的刚度，指定为具有扭转刚度单位的 scalar。

### **Damping Coefficient** — 力定律的阻尼系数 0 `N*m/(deg/s)`（默认）| scalar

*z* 转动基元的内部弹簧-阻尼力定律的阻尼系数，指定为具有阻尼系数单位的 scalar。

#### 限制

### **Specify Lower Limit** — 是否指定位置下限 `off`（默认）| `on`

选择此参数以指定 *z* 转动基元的下限。

### **Bound** — 自由区域的下界 -90 `deg`（默认）| scalar

*z* 转动基元的自由区域的下界，指定为具有角度单位的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Spring Stiffness** — 下界处的弹簧刚度 1e4 `N*m/deg`（默认）| scalar

下界处的弹簧刚度，指定为具有扭转刚度单位的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Damping Coefficient** — 下界处的阻尼系数 10 `N*m/(deg/s)`（默认）| scalar

下界处的阻尼系数，指定为具有阻尼系数单位的 scalar。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼力矩的区域 0.1 `deg`（默认）| scalar

用于平滑弹簧和阻尼力矩的区域，指定为具有角度单位的 scalar。

当穿透量达到过渡区域宽度时，模块施加下限力矩的完整值。区域越小，力开始作用越急剧，求解器所需的时间步长越小。在仿真精度和仿真速度之间的权衡中，减小过渡区域可提高精度，扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Lower Limit**。

### **Specify Upper Limit** — 是否指定上限位置 `off`（默认）| `on`

选择此参数以指定 *z* 转动基元的上限。

### **Bound** — 自由区域的上限 90 `deg`（默认）| 标量

自由区域的上限（针对 *z* 转动基元），指定为带有角度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Spring Stiffness** — 上限处弹簧的刚度 1e4 `N*m/deg`（默认）| 标量

上限处弹簧的刚度，指定为带有扭转刚度单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Damping Coefficient** — 上限处的阻尼系数 10 `N*m/(deg/s)`（默认）| 标量

上限处的阻尼系数，指定为带有阻尼系数单位的标量。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

### **Transition Region Width** — 用于平滑弹簧和阻尼器扭矩的区域 0.1 `deg`（默认）| 标量

用于平滑弹簧和阻尼器扭矩的区域，指定为带有角度单位的标量。

当穿透量达到过渡区域的宽度时，模块施加完整的上限扭矩值。该区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度与仿真速度之间的权衡中，减小过渡区域可提高精度，增大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请选择 **Specify Upper Limit**。

#### 驱动

### **Torque** — 提供执行器扭矩的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

为关节基元提供执行器扭矩的选项，指定为以下值之一：

| Torque 设置 | 描述 |
| --- | --- |
| `None` | 无执行器扭矩。 |
| `Provided by Input` | 输入端口 **tz** 为 *z* 转动基元指定执行器扭矩。 |
| `Automatically Computed` | 模块自动计算扭矩。如果将此参数设置为 `Automatically Computed`，则对于同一关节基元，无需将 **Motion** 设置为 `Provided by Input`。自动计算的扭矩可能会满足机构中其他位置的运动输入。 |

### **Motion** — 提供运动的选项 `Automatically Computed`（默认）| `Provided by Input`

为关节基元提供运动的选项，指定为以下值之一：

| Motion 设置 | 描述 |
| --- | --- |
| `Automatically computed` | 模块根据模型动力学计算并施加关节基元运动。 |
| `Provided by Input` | 输入端口 **qz** 为 *z* 转动基元指定运动。 |

### 模式配置

### **Mode** — 关节模式 `Normal`（默认）| `Locked` | `Disengaged` | `Provided by Input`

用于仿真的关节模式，指定为以下值之一：

| Mode | 描述 |
| --- | --- |
| `Locked` | Locked 模式约束关节的所有自由度 (DOFs)。锁定关节在仿真期间以零速度保持其初始装配位置。关节模块可根据 **Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置感测力或扭矩。 |
| `Normal` | Normal 模式启用自由度，并且关节的约束在仿真期间按预期工作。 |
| `Disengaged` | Disengaged 模式在整个仿真过程中释放关节的所有约束。**Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置不影响脱离的关节。所有输出端口输出零。 |
| `Provided by Input` | `Provided by Input` 选项允许你使用输入信号指定关节模式。有关详细信息，请参阅 **Input** 部分中的端口 **mode**。 |

### 复合力/扭矩传感

### **Direction** — 测量方向 `Follower on Base`（默认）| `Base on Follower`

测量方向，指定为以下值之一：

- `Follower on Base` — 模块感测从动坐标系施加在基础坐标系上的力和扭矩。
- `Base on Follower` — 模块感测基础坐标系施加在从动坐标系上的力和扭矩。

此参数仅影响 **Composite Force/Torque Sensing** 部分下的输出信号。反转方向会改变测量值的符号。有关详细信息，请参阅 Force and Torque Measurement Direction。

### **Resolution Frame** — 用于解析测量的坐标系 `Base`（默认）| `Follower`

用于解析测量的坐标系，指定为以下值之一：

- `Base` — 模块在基础坐标系的坐标中解析测量值。
- `Follower` — 模块在从动坐标系的坐标中解析测量值。

此参数仅影响 **Composite Force/Torque Sensing** 部分下的输出信号。

## 所属库

Simscape / Multibody / Joints

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

### R2025a: 模式故障建模

现在可以为所有关节模块对模式故障进行建模。使用这些故障，你可以在仿真期间更改关节模式，而无需更改模型设计。有关详细信息，请参阅描述中的 **故障** 部分。

## 描述

具有三个移动副基元和三个转动副基元的关节

Bushing Joint 模块对具有三个平移和三个旋转自由度的关节进行建模。该关节使从动坐标系能够通过三个正交平移以及随后的三个旋转序列，相对于基础坐标系执行空间变换。该图显示了在给定仿真时间步中关节变换发生的顺序。

变换序列示意图

每次变换得到的坐标系用作下一次变换的基础坐标系。由于三维旋转按序列发生，两个轴可能会对齐，这会导致失去一个旋转自由度。此现象称为万向节锁。

要指定关节基元的初始状态目标，请使用 **State Targets** 下的参数。这些目标在基础坐标系中指定。你还可以为这些目标设置优先级。如果关节无法满足所有状态目标，优先级将确定先满足哪些目标以及满足它们的接近程度。有关示例，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

要针对关节基元对阻尼和弹簧行为进行建模，请使用 **Internal Mechanics** 下的参数。使用 **Damping Coefficient** 参数对能量耗散进行建模，使用 **Spring Stiffness** 参数对能量存储进行建模。关节弹簧试图使关节基元偏离其平衡位置，关节阻尼器用作能量耗散元件。弹簧和阻尼器是严格线性的。

要指定关节基元的限制，请使用 **Limits** 下的参数。下限和上限定义自由区域的宽度。当位置超出边界时，模块施加力以将关节位置加速回自由区域。模块使用平滑的弹簧-阻尼器方法计算力。有关平滑弹簧-阻尼器方法的详细信息，请参阅 Spatial Contact Force 模块的描述部分。

**Actuation** 部分中的 **Force**、**Torque** 和 **Motion** 参数控制仿真期间关节基元的运动。有关详细信息，请参阅 Specifying Joint Actuation Inputs。此外，关节模块具有输出传感数据的端口，例如位置、速度、加速度、力和扭矩，你可以使用这些数据对模型执行分析任务。有关详细信息，请参阅 Sensing 和 Force and Torque Sensing。

要指定关节模式配置，请使用 **Mode** 参数。有关更多详细信息，请参阅 **端口** 和 **参数** 部分中的 **模式配置**。

### 故障

使用模式故障，你可以在仿真期间更改关节模式，而无需修改模型设计。故障注入会覆盖模式设置。例如，如果某个关节的 **Mode** 参数设置为 `Locked`，并且 **Fault behavior** 参数设置为 `Disengaged`，则该关节会脱离。

要向关节模块添加模式故障，请单击该关节模块，在 **Simscape Block** 选项卡和 **Faults** 部分中，单击 **Fault** > `Add Fault`。或者，你可以单击该关节模块，将鼠标悬停在省略号上以打开操作栏，然后单击 Add a fault on the block icon 按钮以添加故障。你可以向一个关节模块添加多个故障，但该关节模块在仿真期间只能有一个活动故障。

添加故障时，请在 Property Inspector 中的 **Fault** 部分下指定故障的行为和触发类型。要定义故障行为，请单击 **Fault Behavior** 旁边的链接。此关节支持 `Locked`、`Normal` 或 `Disengaged` 模式。关节模块支持以下触发类型：`Always on`、`Timed`、`Manual` 和 `Conditional`。有关这些触发类型的更多详细信息，请参阅 Set Fault Triggers。要触发条件故障，你可以使用 Simulink 信号、Simscape 语言模块和 MATLAB 工作区变量。要为模块设置活动故障，请使用 Fault Table。有关更多详细信息，请参阅 Access the Fault Table and Fault Dashboard。

要启用故障仿真，请在 **Simscape Block** 选项卡和 **Faults** 部分中，打开 **Fault Simulation** 按钮。当按钮为绿色且状态为 **on** 时，故障仿真已开启。仿真会记录触发状态数据。要查看数据，请使用 Simulation Data Inspector。此外，你可以在 Fault Dashboard 中查看故障状态和已触发故障的摘要。要打开 Fault Dashboard，请在 **Simscape Block** 选项卡中单击 **Faults** > `Fault Dashboard`。

要创建和修改故障，你还可以使用 Simscape™ 和 Simulink® 故障函数。有关更多详细信息，请参阅 Simulink Fault Controls and Simscape Faults Interface 的函数部分。
