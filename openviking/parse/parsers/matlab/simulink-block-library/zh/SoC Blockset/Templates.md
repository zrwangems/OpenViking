---
type: simulink-block
title: 'Use Template to Create SoC Model'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: ''
documentation_page: 'use-templates-to-create-soc-model'
documentation_source_path: 'ug/use-templates-to-create-soc-model.html'
language: zh-CN
chinese_source: official
---

# Use Template to Create SoC Model

SoC Blockset™ model templates provide design patterns and best practices for models intended for simulation, HDL code generation, or SoC deployment. Models created from any one of SoC Blockset model templates have their configuration parameters set up for simulation and code generation.

SoC Blockset™ model templates provide design patterns and best practices for models intended
for simulation, HDL code generation, or SoC deployment. Models created from any one of
SoC Blockset model templates have their configuration parameters set up for simulation and
code generation.

### Create SoC Model Using SoC Blockset Template

To efficiently model hardware for SoC design, create a project by using an SoC Blockset template.

1. In the MATLAB® Home tab, select the **Simulink** button.
   Alternatively, at the command line,
   enter:

   ```
   simulink
   ```
2. On the Simulink® Start Page, scroll down to the **SoC
   Blockset** section, which contains links to SoC templates for
   common workflows. Select a template and save the project. A project folder
   opens in your workspace containing:

   - A model with the name `soc_*_top.slx` – The
     top-level model for the SoC project.
   - `referencedmodels` – A folder containing the
     models referenced from the top model. Some templates include an
     FPGA model and a processor model. Other templates only include
     one referenced model: an FPGA model or a processor model.
   - `utilities` – A folder containing utility
     functions or testbench data used by the model.

   To open the top-level model in Simulink, on the **Project Shortcuts** tab, click
   **Open Top model**.
3. In each template, navigate to the blocks marked **FPGA
   Algorithm** in the FPGA model, or **Processor
   Algorithm** in the processor model. These blocks are
   highlighted for easy detection. Replace the template blocks with your own
   algorithm model.

   **Tip**

   To easily find the algorithm blocks, follow the annotations throughout
   the model hierarchy.
4. To open the **SoC Blockset** Block Library, select the
   Library Browser button, then select **SoC Blockset** in the
   left pane. Alternatively, at the command line,
   enter:

   ```
   soclib
   ```

   This
   library includes blocks for creating SoC models and testbenches.

### Template Structure

The top model in an SoC Blockset template includes an FPGA subsystem, which represents the logic intended
to program the FPGA. The FPGA subsystem includes two Simulink model variants:

- Frame-based FPGA model – For enhanced simulation performance (not
  available in the RFSoC template)
- Sample-based FPGA model – For cycle accuracy and code generation

The top model also includes a processor subsystem, which represents the
software program intended to run on the SoC processor. Both the FPGA and the top
subsystems contain blocks marked as FPGA Algorithm or Processor Algorithm. Replace these
algorithms with your own logic. The top model of the template also includes a memory
system, with a memory controller and memory channels. These blocks represent the
physical memory system on the board. The model often includes a register channel (to
enable communication between the processor and FPGA), testbench, or I/O blocks.

### Modify Project

#### Modify the FPGA Model

From the top model, open the FPGA model by clicking the arrow at the bottom left
of the FPGA block:

The FPGA model contains two model variants: a frame-based variant and a
sample-based variant. Double-click the model variant you want to modify. The FPGA
model typically includes two main subsystems for you to modify:

- FPGA Algorithm Wrapper – Double-click to open the model. The algorithm
  wrapper contains a green-highlighted subsystem named FPGA
  Algorithm. This block has two inputs and one output and is
  implemented as a multiplier. Replace this block with your own FPGA
  algorithm. Add inputs and outputs as required.
- Test Source Wrapper – This block includes a test source and is intended to
  generate stimulus as an input to the FPGA algorithm. Modify the test source
  to your needs, or replace it with an alternative source block. If the input
  to your FPGA algorithm is routed from an I/O block, such as HDMI or SDR,
  consider using a specific application template.

  **Note**

  Not all templates include a Test Source block in the FPGA
  model.

#### Modify the Processor Model

The processor model includes a Task Manager block and a processor
wrapper. The template implements the processor algorithm as a "pass through" wire.
Open the processor algorithm wrapper, and replace the Processor
Algorithm block (highlighted in blue) with your desired
algorithm.

#### Modify the Register Channel

The top model of a template also includes a register channel to communicate
between the processor and the FPGA model. Use the register channel to configure the
FPGA mode,l or to read and check status registers. The Register
Channel block in the template includes one register. To add additional
registers you must modify the register channel block parameters, the FPGA algorithm,
and the processor algorithm:

1. Add registers to the register channel – Double-click the
   Register Channel block to open the block mask and add
   additional registers as needed. Adding registers creates additional
   ports on the Register Channel block. For additional
   information, see Register Channel.
2. Add ports to the processor model – Navigate to the Processor
   Algorithm Wrapper model. To navigate to the processor model,
   click **Open Processor model** on the
   **Project Shortcuts** tab. Double-click
   Processor Algorithm Wrapper to modify it.

   For write registers, add an output port to the module and add logic to
   drive a value to the added output port. For read registers, add an input
   port and logic to process the information returned from a read register.
   From the top model, wire the port to the Register Channel
   block.
3. Add ports to the FPGA model – Navigate to the FPGA Algorithm
   Wrapper model. To navigate to the FPGA/Frame based
   processing model, click **Open FPGA sample model** on
   the **Project Shortcuts** tab. Double-click FPGA
   Algorithm Wrapper to modify it.

   For write registers, add an input port to the module and logic to
   process the information returned from a read register. For read
   registers, add an output port and logic to drive a value to the added
   output port.

   For equivalent behavior when using a Simulink sample-based variant, repeat this step for the
   sample-based processing model in the FPGA wrapper.
4. From the top model, wire the new port to the Register
   Channel block.

## See Also

Task Manager | Register
Channel | Memory
Controller | Memory Channel

### Topics

- Stream from FPGA to Processor Template
- Stream from Processor to FPGA Template
- SDR Template
- HDMI Template
- Frame Buffer with HDMI Template
- RFSoC Template
- SoC Software Architecture Template

## MATLAB Command

You clicked a link that corresponds to this MATLAB command:

Run the command by entering it in the MATLAB Command Window.
Web browsers do not support MATLAB commands.

Close

MathWorks
MathWorks

选择网站

选择网站以获取翻译的可用内容，以及查看当地活动和优惠。根据您的位置，我们建议您选择：。

- (English)
- (Deutsch)
- (Français)

- （简体中文）
- (English)

您也可以从以下列表中选择网站：

**如何获得最佳网站性能**

选择中国网站（中文或英文）以获得最佳网站性能。其他 MathWorks 国家/地区网站并未针对您所在位置的访问进行优化。

美洲

- América Latina (Español)
- Canada (English)
- United States (English)

欧洲

- Belgium (English)
- Denmark (English)
- Deutschland (Deutsch)
- España (Español)
- Finland (English)
- France (Français)
- Ireland (English)
- Italia (Italiano)
- Luxembourg (English)

- Netherlands (English)
- Norway (English)
- Österreich (Deutsch)
- Portugal (English)
- Sweden (English)
- Switzerland
  - Deutsch
  - English
  - Français
- United Kingdom (English)

亚太

- Australia (English)
- India (English)
- New Zealand (English)
- 中国
  - 简体中文
  - English
- 日本 (日本語)
- 한국 (한국어)

联系您当地的办事处
