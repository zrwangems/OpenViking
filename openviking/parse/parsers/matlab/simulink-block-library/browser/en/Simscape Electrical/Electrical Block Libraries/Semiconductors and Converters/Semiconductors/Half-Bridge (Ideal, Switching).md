---
type: simulink-block
title: 'Half-Bridge (Ideal, Switching)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Semiconductors and Converters / Semiconductors'
documentation_page: 'halfbridgeidealswitching'
documentation_source_path: 'ref/halfbridgeidealswitching.html'
language: en
---

# Half-Bridge (Ideal, Switching)

## Ports

### Input

### **G** — Gate terminals vector physical signal

Physical signal conserving port associated with the gate terminals of the two switching
devices, specified as a vector of two physical signals.

The first element of the vector controls the upper side switch. The
second element of the vector controls the lower side switch. If, in the
**Diode** settings, you set the **Integral
protection diode** parameter to
`Yes`, the first and second element of the
vector also controls the lower and upper diode, respectively.

#### Dependencies

To enable this port, set **Gate-control port** to
`PS`.
### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the positive terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the negative terminal.

### **O** — Output node electrical

Electrical conserving port associated with the output node.

### **G1** — Gate terminal 1 electrical

Electrical conserving port associated with the gate terminal for the first switching
device.

#### Dependencies

To enable this port, set **Gate-control port** to
`Electrical`.

### **G2** — Gate terminal 2 electrical

Electrical conserving port associated with the gate terminal for the second switching
device.

#### Dependencies

To enable this port, set **Gate-control port** to
`Electrical`.

### **H** — Thermal port thermal

Thermal conserving port.

#### Dependencies

To enable this port, clear the **Separate thermal ports
for upper and lower devices** and **Separate
thermal ports for integral diodes** parameters.

### **H1Switch** — Thermal port for upper switching device thermal

*Since R2024a*

Thermal conserving port associated with the upper switching
device.

#### Dependencies

To enable this port, select the **Separate thermal ports
for upper and lower devices** parameter.

### **H2Switch** — Thermal port for lower switching device thermal

*Since R2024a*

Thermal conserving port associated with the lower switching
device.

#### Dependencies

To enable this port, select the **Separate thermal ports
for upper and lower devices** parameter.

### **H1Diode** — Thermal port for upper diode thermal

*Since R2024a*

Thermal conserving port associated with the upper diode.

#### Dependencies

To enable this port, select the **Separate thermal ports
for upper and lower devices** and **Separate
thermal ports for integral diodes** parameters.

### **H2Diode** — Thermal port for lower diode thermal

*Since R2024a*

Thermal conserving port associated with the lower diode.

#### Dependencies

To enable this port, select the **Separate thermal ports
for upper and lower devices** and **Separate
thermal ports for integral diodes** parameters.

## Parameters

### Main

The visibility of the **Main** parameters depends on the
**Switching device** and **On-state behavior and
losses** parameters. To learn how to read this table, see Parameter Dependencies.

**Main Parameter Dependencies**

| Parameters and Options | | | | | |
| --- | --- | --- | --- | --- | --- |
| Gate-control port | | | | | |
| **Switching Device** | | | | | |
| *`MOSFET`* | | *`IGBT`* | | *`GTO`* | |
| Threshold voltage, Vth | | Threshold voltage, Vth | | Gate trigger voltage, Vgt | |
| Gate turn-off voltage, Vgt\_off | |
| Holding current | |
| **On-state behavior and losses** | | **On-state behavior and losses** | | **On-state behavior and losses** | |
| *`Specify constant values`* | *`Tabulate`* | *`Specify constant values`* | *`Tabulate`* | *`Specify constant values`* | *`Tabulate`* |
| Drain-source on resistance, R\_DS(on) | On-state voltage, Vds(Tj,Ids) | Forward voltage, Vf | On-state voltage, Vds(Tj,Ice) | Forward voltage, Vf | On-state voltage, Vak(Tj,Iak) |
| Temperature vector, Tj | On-state resistance | Temperature vector, Tj | On-state resistance | Temperature vector, Tj |
| Drain-source current vector, Ids | Collector-emitter current vector, Ice | Anode-cathode current vector, Iak |
| Off-state conductance | | | | | |

### **Gate-control port** — Gate-control port `PS` (default) | `Electrical`

Option to use the physical signal input port **G** or
the electrical conserving ports **G1** and
**G2** as the gate control ports.

### **Switching device** — Switching device option `MOSFET` (default) | `IGBT` | `GTO`

Switching device for the half-bridge.

### **Threshold voltage, Vth** — Threshold voltage `2` `V` | `6` `V` | positive scalar

Threshold voltage at which the device turns on. The default value depends on the
**Switching device** setting.

#### Dependencies

See the Main Parameter Dependencies
table.

### **Gate trigger voltage, Vgt** — Gate trigger voltage `6` `V` (default) | positive scalar

Gate-cathode voltage threshold. The device turns on when the
gate-cathode voltage is above this value.

#### Dependencies

See the Main Parameter Dependencies
table.

### **Gate turn-off voltage, Vgt\_off** — Gate turn-off voltage `-1` `V` (default) | scalar

Gate-cathode voltage threshold. The device turns off when the
gate-cathode voltage is below this value.

#### Dependencies

See the Main Parameter Dependencies
table.

### **Holding current** — Current threshold `1` `A` (default) | positive scalar

Current threshold. The device stays on when the current is above this
value, even when the gate-cathode voltage falls below the gate trigger
voltage.

#### Dependencies

See the Main Parameter Dependencies
table.

### **On-state behavior and losses** — On-state behavior and losses `Specify constant values` (default) | `Tabulate`

Parameterization method for on-state behavior and switching losses,
specified as one of these values:

- `Specify constant values` — Use
  scalar values to specify the output current, switch-on loss,
  and switch-off loss data. The block assumes that the energy
  dissipated during a single switch-on or switch-off event
  scales linearly with the off-state voltage and on-state
  current. The block also assumes that the losses are
  independent of temperature.
- `Tabulate` — Use vectors to
  specify the output current and temperature data. Use arrays
  to specify the switch-on loss and switch-off loss
  data.

#### Dependencies

See the Main Parameter Dependencies
table.

### **Drain-source on resistance, R\_DS(on)** — Drain-source on resistance `0.01` `Ohm` (default) | positive scalar

Drain-source resistance when the device is on.

#### Dependencies

See the Main Parameter Dependencies
table.

### **On-state voltage, Vds(Tj,Ids)** — On-state voltage `[0, 1.1, 1.3, 1.45, 1.75, 2.25, 2.7; 0, 1, 1.15, 1.35, 1.7, 2.35, 3]` `V` (default) | matrix of nonnegative scalars

Voltage drop across the device in a triggered conductive state. This parameter is a
function of temperature and final on-state output current.

#### Dependencies

See the Main Parameter Dependencies
table.

### **Drain-source current vector, Ids** — Drain-source current vector `[0 10 50 100 200 400 600]` `A` (default) | vector of positive scalars

Drain-source currents at which you quote the on-state voltage. The sign of the
drain-source current must be the same as the sign of the corresponding
drain-source voltage. If the drain-source voltage is zero, the
corresponding drain-source current must also be zero.

#### Dependencies

See the Main Parameter Dependencies
table.

### **Forward voltage, Vf** — Forward voltage `0.8` `V` (default) | positive scalar

Minimum voltage required across the collector and emitter or anode and cathode block
ports for the gradient of the diode I-V characteristic to be
1/*R*on, where
*R*on is the value of the
**On-state resistance** parameter.

#### Dependencies

See the Main Parameter Dependencies
table.

### **On-state resistance** — On-state collector-emitter resistance `0.001` `Ohm` (default) | positive scalar

Collector-emitter resistance when the device is on.

#### Dependencies

See the Main Parameter Dependencies
table.

### **On-state voltage, Vds(Tj,Ice)** — On-state voltage `[0, .1, .6, .8, 1, 1.3, 1.6, 2, 2.4; 0, .1, .7, 1, 1.2, 1.5, 1.9, 2.4, 2.8]` `V` (default) | matrix of nonnegative scalars

Voltage drop across the device in a triggered conductive state. This parameter is a
function of temperature and final on-state output current.

#### Dependencies

See the Main Parameter Dependencies
table.

### **Collector-emitter current vector, Ice** — Collector-emitter current vector `[0, .1, 1, 5, 10, 20, 40, 70, 100]` `A` (default) | vector of positive scalars

Collector-emitter currents at which you quote the on-state voltage. The sign of the
collector-emitter current must be the same as the sign of the
corresponding collector-emitter voltage. If the collector-emitter
voltage is zero, the corresponding collector-emitter current must also
be zero.

#### Dependencies

See the Main Parameter Dependencies
table.

### **On-state voltage, Vak(Tj,Iak)** — On-state voltage `[0, .1, .6, .8, 1, 1.3, 1.6, 2, 2.4; 0, .1, .7, 1, 1.2, 1.5, 1.9, 2.4, 2.8]` `V` (default) | matrix of nonnegative scalars

Voltage drop across the device in a triggered conductive state. This parameter is a
function of temperature and final on-state output current.

#### Dependencies

See the Main Parameter Dependencies
table.

### **Anode-cathode current vector, Iak** — Anode-cathode current vector `[0, .1, 1, 5, 10, 20, 40, 70, 100]` `A` (default) | vector of positive scalars

Anode-cathode currents at which you quote the on-state voltage. The sign of the
anode-cathode current must be the same as the sign of the corresponding
anode-cathode voltage. If the anode-cathode voltage is zero, the
corresponding anode-cathode current must also be zero.

#### Dependencies

See the Main Parameter Dependencies
table.

### **Temperature vector, Tj** — Temperature values `[298.15, 398.15]` `K` (default) | vector

Temperature values at which you quote the on-state voltage.

#### Dependencies

See the Main Parameter Dependencies
table.

### **Off-state conductance** — Off-state collector-emitter conductance `1e-6` `1/Ohm` (default) | positive scalar

Conductance when the device is off. The value must be less than 1/*R*,
where *R* is the value of the **On-state
resistance** parameter.

#### Dependencies

See the Main Parameter Dependencies
table.

### Losses

### **Switch-on loss** — Switch-on loss `22.86e-3` `J` (default) | positive scalar

Energy dissipated during a single switch-on event.

#### Dependencies

To enable this parameter, set **On-state behavior and
losses** to `Specify constant
values`.

### **Switch-off loss** — Switch-off loss `17.14e-3` `J` (default) | positive scalar

Energy dissipated during a single switch-off event.

#### Dependencies

To enable this parameter, set **Switching
device** to `MOSFET` or
`IGBT` and set **On-state
behavior and losses** to `Specify constant
values`.

### **Diode reverse recovery loss** — Loss from diode-reverse recovery `5.70e-3` `J` (default) | positive scalar

Energy dissipated during a diode-reverse recovery event.

#### Dependencies

To enable this parameter, set **On-state behavior and
losses** to `Specify constant
values` and set **Integral protection
diode** to `Yes`.

### **On-state current for loss data** — Output current `600` `A` (default) | positive scalar

Output current at which you quote the switch-on loss, switch-off loss, and on-state
voltage.

#### Dependencies

To enable this parameter, set **On-state behavior and
losses** to `Specify constant
values`.

### **Off-state voltage for loss data** — Off-state voltage `300` `V` (default) | positive scalar

Output voltage when the device is off. This value is the blocking voltage at which you
quote the losses. If you specify switching losses as scalar values or as
a function of the junction temperature and on-state current at a fixed
off-state voltage, the block uses this value to calculate switching
losses. If you set **Integral protection diode** to
`Yes`, the block uses this value to
calculate diode reverse recovery loss.

#### Dependencies

To enable this parameter, choose one of these options:

- Set **Integral protection diode** to
  `Yes`.
- Set **On-state behavior and losses**
  to `Specify constant
  values`.
- Set **Switching device** to
  `MOSFET`, set
  **On-state behavior and losses** to
  `Tabulate`, and clear the
  **Include switching loss tabulation with
  off-state Vds voltage** parameter.
- Set **Switching device** to
  `IGBT`, set
  **On-state behavior and losses** to
  `Tabulate`, and clear the
  **Include switching loss tabulation with
  off-state voltage** parameter.
- Set **Switching device** to
  `GTO`.

### **Apply switching losses to electrical supply** — Option to apply switching losses to electrical supply `Off` (default) | `On`

*Since R2023b*

Option to apply the switching losses to the electrical supply.

Clear this parameter to apply the switching losses to the thermal node
only.

Select this parameter to apply the switching losses to the thermal
node and the electrical supply.

### **Switch-on loss, Eon(Tj,Ids)** — Switch-on loss `[0, .29, 1.43, 2.86, 5.71, 13.14, 22.86; 0, .57, 2.63, 5.14, 10.29, 20.57, 30.29] * 1e-3` `J` (default) | vector of positive scalars

Energy dissipated during a single switch-on event as a function of temperature and final
on-state drain-source current.

#### Dependencies

To enable this parameter:

- Set **Switching device** to
  `MOSFET`.
- Set **On-state behavior and losses**
  to `Tabulate`.
- Clear the **Include switching loss tabulation
  with off-state Vds voltage**
  parameter.

### **Switch-off loss, Eoff(Tj,Ids)** — Switch-off loss `[0, .21, 1.07, 2.14, 4.29, 9.86, 17.14; 0, .43, 1.97, 3.86, 7.71, 15.43, 22.71] * 1e-3` `J` (default) | vector of positive scalars

Energy dissipated during a single switch-off event as a function of temperature and
final on-state drain-source current.

#### Dependencies

To enable this parameter:

- Set **Switching device** to
  `MOSFET`.
- Set **On-state behavior and losses**
  to `Tabulate`.
- Clear the **Include switching loss tabulation
  with off-state Vds voltage**
  parameter.

### **Diode reverse recovery loss, Erec(Tj,Ids)** — Loss from diode-reverse recovery `[0, .0031, .021, .11, .21, .43, .99, 1.71, 3.078; 0, .0041, .043, .2, .39, .77, 1.54, 2.27, 4.08] * 1e-3` `J` (default) | vector of positive scalars

Energy dissipated during a diode-reverse recovery event as a function of temperature and
final on-state drain-source current.

#### Dependencies

To enable this parameter:

- Set **Switching device** to
  `MOSFET`.
- Set **On-state behavior and losses**
  to `Tabulate`.
- Set **Integral protection diode** to
  `Yes`.

### **Temperature vector for losses, Tj** — Temperature for losses `[298.15, 398.15]` `K` (default) | vector

Temperature values at which you quote the losses.

#### Dependencies

To enable this parameter, set **On-state behavior and
losses** to `Tabulate`.

### **Drain-source current vector for losses, Ids** — Drain-source current for switching losses `[0, 10, 50, 100, 200, 400, 600]` `A` (default) | vector of positive scalars

Drain-source currents at which you quote the losses. The sign of the drain-source
current must be the same as the sign of the corresponding drain-source
voltage. If the drain-source voltage is zero, the corresponding
drain-source current must also be zero.

#### Dependencies

To enable this parameter, set **Switching
device** to `MOSFET` and set
**On-state behavior and losses** to
`Tabulate`.

### **Include switching loss tabulation with off-state Vds voltage** — Option to tabulate switching losses with off-state Vds voltage `Off` (default) | `On`

*Since R2023b*

Option to tabulate the switching losses with the off-state
drain-source voltage.

Clear this parameter to tabulate the switch-on loss and switch-off
loss with the on-state drain-source current and temperature. The block
assumes that the losses scale linearly with the off-state drain-source
voltage.

Select this parameter to tabulate the switch-on loss and switch-off
loss with the temperature, on-state drain-source current, and off-state
drain-source voltage.

#### Dependencies

To enable this parameter, set **Switching
device** to `MOSFET` and set
**On-state behavior and losses** to
`Tabulate`.

### **Switch-on loss, Eon(Tj,Ids,Vds)** — Switch-on loss `[zeros(2, 7, 3)]` `J` (default) | 3-D array of nonnegative scalars

*Since R2023b*

Energy dissipated during a single switch-on event as a function of temperature, on-state
drain-source current, and off-state drain-source voltage.

#### Dependencies

To enable this parameter:

- Set **Switching device** to
  `MOSFET`.
- Set **On-state behavior and losses**
  to `Tabulate`.
- Select the **Include switching loss tabulation
  with off-state Vds voltage**
  parameter.

### **Switch-off loss, Eoff(Tj,Ids,Vds)** — Switch-off loss `[zeros(2, 7, 3)]` `J` (default) | 3-D array of nonnegative scalars

*Since R2023b*

Energy dissipated during a single switch-off event as a function of temperature,
on-state drain-source current, and off-state drain-source
voltage.

#### Dependencies

To enable this parameter:

- Set **Switching device** to
  `MOSFET`.
- Set **On-state behavior and losses**
  to `Tabulate`.
- Select the **Include switching loss tabulation
  with off-state Vds voltage**
  parameter.

### **Switch-on loss, Eon(Tj,Ice)** — Switch-on loss `[0, .0024, .024, .12, .2, .48, 1.04, 2.16, 3.24; 0, .003, .03, .15, .25, .6, 1.3, 2.7, 4.05] * 1e-3` `J` (default) | vector of positive scalars

Energy dissipated during a single switch-on event as a function of temperature and final
on-state collector-emitter current.

#### Dependencies

To enable this parameter:

- Set **Switching device** to
  `IGBT`.
- Set **On-state behavior and losses**
  to `Tabulate`.
- Clear the **Include switching loss tabulation
  with off-state voltage** parameter.

### **Switch-off loss, Eoff(Tj,Ice)** — Switch-off loss `[0, .0007, .0066, .033, .066, .17, .33, .83, 1.5; 0, .001, .01, .05, .1, .25, .5, 1.2, 2.2] * 1e-3` `J` (default) | vector of positive scalars

Energy dissipated during a single switch-off event as a function of temperature and
final on-state collector-emitter current.

#### Dependencies

To enable this parameter:

- Set **Switching device** to
  `IGBT`.
- Set **On-state behavior and losses**
  to `Tabulate`.
- Clear the **Include switching loss tabulation
  with off-state voltage** parameter.

### **Diode reverse recovery loss, Erec(Tj,Ice)** — Loss from diode-reverse recovery loss `[0, .0031, .021, .11, .21, .43, .99, 1.71, 3.078; 0, .0041, .043, .2, .39, .77, 1.54, 2.27, 4.08] * 1e-3` `J` (default) | vector of positive scalars

Energy dissipated during a diode-reverse recovery event as a function of temperature and
final on-state collector-emitter current.

#### Dependencies

To enable this parameter:

- Set **Switching device** to
  `IGBT`.
- Set **On-state behavior and losses**
  to `Tabulate`.
- Set **Integral protection diode** to
  `Yes`.

### **Collector-emitter current vector for losses, Ice** — Collector-emitter current for losses `[0, .1, 1, 5, 10, 20, 40, 70, 100]` `A` (default) | vector of positive scalars

Collector-emitter currents at which you quote the losses. The sign of the
collector-emitter current must be the same as the sign of the
corresponding collector-emitter voltage. If the collector-emitter
voltage is zero, the corresponding collector-emitter current must also
be zero.

#### Dependencies

To enable this parameter, set **Switching
device** to `IGBT` and set
**On-state behavior and losses** to
`Tabulate`.

### **Include switching loss tabulation with off-state voltage** — Option to tabulate switching losses with off-state voltage `Off` (default) | `On`

*Since R2023b*

Option to tabulate the switching losses with the off-state voltage.

Clear this parameter to tabulate the switch-on loss and switch-off loss with the
on-state collector-emitter current and temperature. The block assumes
that the losses scale linearly with the off-state voltage.

Select this parameter to tabulate the switch-on loss and switch-off loss with the
temperature, on-state collector-emitter current, and off-state
voltage.

#### Dependencies

To enable this parameter, set **Switching
device** to `IGBT` and set
**On-state behavior and losses** to
`Tabulate`.

### **Switch-on loss, Eon(Tj,Ice,Vce)** — Switch-on loss `[zeros(2, 9, 3)]` `J` (default) | 3-D array of nonnegative scalars

*Since R2023b*

Energy dissipated during a single switch-on event as a function of
temperature, on-state collector-emitter current, and off-state
collector-emitter voltage.

#### Dependencies

- Set **Switching device** to
  `IGBT`.
- Set **On-state behavior and losses** to
  `Tabulate`.
- Select the **Include switching loss tabulation
  with off-state voltage** parameter.

### **Switch-off loss, Eoff(Tj,Ice,Vce)** — Switch-off loss `[zeros(2, 9, 3)]` `J` (default) | 3-D array of nonnegative scalars

*Since R2023b*

Energy dissipated during a single switch-off event as a function of
temperature, on-state collector-emitter current, and off-state
collector-emitter voltage.

#### Dependencies

To enable this parameter:

- Set **Switching device** to
  `IGBT`.
- Set **On-state behavior and losses**
  to `Tabulate`.
- Select the **Include switching loss tabulation
  with off-state voltage** parameter.

### **Off-state voltage vector for switching losses, Vce** — Off-state voltage vector for switching loss data `[0, 150, 300]` `V` (default) | vector

*Since R2023b*

Off-state collector-emitter voltages at which you quote the switch-on
loss and switch-off loss.

#### Dependencies

To enable this parameter:

- Set **Switching device** to
  `IGBT`.
- Set **On-state behavior and losses**
  to `Tabulate`.
- Select the **Include switching loss tabulation
  with off-state voltage** parameter.

### **Forced commutation switch-off loss** — Forced commutation switch-off loss `17.14e-3` `J` (default) | positive scalar

Energy dissipated during a forced commutation switch-off event.

#### Dependencies

To enable this parameter, set **Switching
device** to `GTO` and set
**On-state behavior and losses** to
`Specify constant values`.

### **Natural commutation rectification loss** — Natural commutation rectification loss `10e-3` `J` (default) | positive scalar

Rectification loss that the block applies when the device switches off because the
current falls below the value of the **Holding
current** parameter.

#### Dependencies

To enable this parameter, set **Switching
device** to `GTO`.

### **Switch-on loss, Eon(Tj,Iak)** — Switch-on loss `[0, .0024, .024, .12, .2, .48, 1.04, 2.16, 3.24; 0, .003, .03, .15, .25, .6, 1.3, 2.7, 4.05] * 1e-3` `J` (default) | matrix of nonnegative scalars

Energy dissipated during a single switch-on event as a function of temperature and final
on-state anode-cathode current.

#### Dependencies

To enable this parameter, set **Switching
device** to `GTO` and set
**On-state behavior and losses** to
`Tabulate`.

### **Switch-off loss, Eoff(Tj,Iak)** — Switch-off loss `[0, .0007, .0066, .033, .066, .17, .33, .83, 1.5; 0, .001, .01, .05, .1, .25, .5, 1.2, 2.2] * 1e-3` `J` (default) | vector of positive scalars

Energy dissipated during a single switch-off event as function of temperature and final
on-state anode-cathode current.

#### Dependencies

To enable this parameter, set **Switching
device** to `GTO` and set
**On-state behavior and losses** to
`Tabulate`.

### **Diode reverse recovery loss, Erec(Tj,Iak)** — Loss from diode-reverse recovery loss `[0, .0031, .021, .11, .21, .43, .99, 1.71, 3.078; 0, .0041, .043, .2, .39, .77, 1.54, 2.27, 4.08] * 1e-3` `J` (default) | vector of positive scalars

Energy dissipated during a diode-reverse recovery event as a function of temperature and
final on-state anode-cathode current.

#### Dependencies

To enable this parameter:

- Set **Switching device** to
  `GTO`.
- Set **On-state behavior and losses**
  to `Tabulate`.
- Set **Integral protection diode** to
  `Yes`.

### **Anode-cathode current vector for losses, Iak** — Anode-cathode current for losses `[0, .1, 1, 5, 10, 20, 40, 70, 100]` `A` (default) | vector of positive scalars

Anode-cathode currents at which you quote the losses. The sign of the anode-cathode
current must be the same as the sign of the corresponding anode-cathode
voltage. If the anode-cathode voltage is zero, the corresponding
anode-cathode current must also be zero.

#### Dependencies

To enable this parameter, set **Switching
device** to `GTO` and set
**On-state behavior and losses** to
`Tabulate`.

### **Averaging period for switching losses** — Averaging period for switching losses `1e-3` `s` (default) | positive scalar

*Since R2023b*

Duration over which the block applies the switching losses to the electrical
supply.

#### Dependencies

To enable this parameter, select the **Apply switching
losses to electrical supply** parameter.

### Integral Diode

### **Integral protection diode** — Protection diode `No` (default) | `Yes`

Whether to model the block integral protection diode.

### **Diode model** — Diode model `Piecewise Linear` (default) | `Tabulated I-V curve`

Diode model, specified as either:

- `Piecewise Linear` — Use a
  piecewise linear model for the diode, as described in Piecewise Linear Diode.
- `Tabulated I-V curve` —
  Use tabulated forward bias I-V data and fixed reverse bias
  off conductance.

#### Dependencies

To enable this parameter, set **Integral protection
diode** to `Yes`.

### **Forward voltage** — Forward voltage `0.8` `V` (default) | positive scalar

Minimum voltage required across the `+` and `-` block
ports for the gradient of the diode I-V characteristic to be
1/*R*on, where
*R*on is the value of the
**On resistance** parameter.

#### Dependencies

To enable this parameter, set **Integral protection diode** to
`Yes` and **Diode
model** to `Piecewise linear`.

### **On resistance** — On resistance `0.001` `Ohm` (default) | positive scalar

Rate of change of the voltage versus the current above the value of the
**Forward voltage** parameter.

#### Dependencies

To enable this parameter, set **Integral protection diode** to
`Yes` and **Diode
model** to `Piecewise linear`.

### **Off conductance** — Off conductance `1e-5` `1/Ohm` (default) | positive scalar

Conductance of the reverse-biased diode.

#### Dependencies

To enable this parameter, set **Integral protection diode** to
`Yes` and either:

- **Diode model** to
  `Piecewise linear`.
- **Diode model** to
  `Tabulated I-V curve` and
  **Reverse I-V characteristics
  type** to `Specify off
  conductacne`.

### **Table type** — Tabulated function `Table in If(Tj,Vf) form` (default) | `Table in Vf(Tj,If) form`

Whether to tabulate the current as a function of temperature and
voltage or the voltage as a function of temperature and current.

#### Dependencies

To enable this parameter, set **Integral protection diode** to
`Yes` and **Diode
model** to `Tabulated I-V
curve`.

### **Reverse I-V characteristics type** — Type of reverse I-V characteristics `Specify off conductance` (default) | `Tabulate`

*Since R2024a*

Whether to specify the reverse I-V characteristics by using the diode
off conductance or by tabulating the current as a function of
temperature and voltage or the voltage as a function of temperature and
current.

#### Dependencies

To enable this parameter, set **Integral protection
diode** to `Yes` and
**Diode model** to `Tabulated I-V
curve`.

### **Forward currents, If(Tj,Vf)** — Forward currents `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12]` `A` (default) | nonnegative vector

Forward currents. This parameter must be a vector of at least three nonnegative elements
in ascending order. The zero point is optional
(*If(Tj,Vf)* = 0A).

#### Dependencies

To enable this parameter, set **Integral protection
diode** to `Yes`,
**Diode model** to `Tabulated I-V
curve`, and **Table type** to
`Table in If(Tj,Vf) form`.

### **Junction temperatures, Tj** — Junction temperatures `[25, 125]` `degC` (default) | vector of positive scalars

Vector of junction temperatures. This parameter must be a vector of at
least two elements.

#### Dependencies

To enable this parameter, set **Integral protection
diode** to `Yes`, and
**Diode model** to `Tabulated I-V
curve`.

### **Forward voltages, Vf** — Forward voltages `[.5, .7, .9, 1.3, 1.7, 2.1, 2.5]` `V` (default) | nonnegative vector

Vector of forward voltages. This parameter must be a vector of at least three
nonnegative elements in ascending order. The zero point is optional
(*Vf* = 0V).

#### Dependencies

To enable this parameter, set **Integral protection
diode** to `Yes`,
**Diode model** to `Tabulated I-V
curve`, and **Table type** to
`Table in If(Tj,Vf) form`.

### **Forward voltages, Vf(Tj,If)** — Forward voltages `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7]` `V` (default) | nonnegative vector

Forward voltages. This parameter must be a vector of at least three nonnegative elements
in ascending order. The zero point is optional
(*Vf(Tj,If)* = 0V).

#### Dependencies

To enable this parameter, set **Integral protection
diode** to `Yes`,
**Diode model** to `Tabulated I-V
curve`, and **Table type** to
`Table in Vf(Tj,If) form`.

### **Forward currents, If** — Forward currents `[.1, .2, .5, 1, 2, 4, 7, 10]` `A` (default) | nonnegative vector

Vector of forward currents. This parameter must be a vector of at least three
nonnegative elements in ascending order. The zero point is optional
(*If* = 0A).

#### Dependencies

To enable this parameter, set **Integral protection
diode** to `Yes`,
**Diode model** to `Tabulated I-V
curve`, and **Table type** to
`Table in Vf(Tj,If) form`.

### **Reverse currents, Ir(Tj,Vr)** — Vector of reverse currents `[1e-06, 2e-06, 5e-06, 1e-05, 2.5e-05, 5e-05, .0001; 2e-06, 5e-06, 1e-05, 4e-05, 8e-05, .0002, .0005]` `A` (default) | nonnegative vector

*Since R2024a*

Reverse currents. This parameter must be a vector of at least three nonnegative elements
in ascending order. The zero point is optional
(*Ir(Tj,Vr)* = 0A).

#### Dependencies

To enable this parameter, set:

- **Integral protection diode** to
  `Yes`
- **Diode model** to
  `Tabulated I-V
  curve`
- **Table type** to `Table
  in If(Tj,Vf) form`
- **Reverse I-V characteristics** to
  `Tabulate`

### **Reverse voltages, Vr** — Vector of reverse voltages `[10, 20, 40, 50, 70, 80, 100]` `V` (default) | nonnegative vector

*Since R2024a*

Vector of reverse voltages. This parameter must be a vector of at least three
nonnegative elements in ascending order. The zero point is optional
(*Vr* = 0V).

#### Dependencies

To enable this parameter, set:

- **Integral protection diode** to
  `Yes`
- **Diode model** to
  `Tabulated I-V
  curve`
- **Table type** to `Table
  in If(Tj,Vf) form`
- **Reverse I-V characteristics** to
  `Tabulate`

### **Reverse voltages, Vr(Tj,Ir)** — Vector of reverse voltages `[10, 100, 200, 250, 300, 325, 350; 10, 70, 160, 220, 270, 300, 320]` `V` (default) | nonnegative vector

*Since R2024a*

Reverse voltages. This parameter must be a vector of at least three nonnegative elements
in ascending order. The zero point is optional
(*Vr(Tj,Ir)* = 0V).

#### Dependencies

To enable this parameter, set:

- **Integral protection diode** to
  `Yes`
- **Diode model** to
  `Tabulated I-V
  curve`
- **Table type** to `Table
  in Vf(Tj,If) form`
- **Reverse I-V characteristics** to
  `Tabulate`

### **Reverse currents, Ir** — Vector of reverse currents `[1e-06, 2e-06, 5e-06, 1e-05, 2e-05, 5e-05, .0001]` `A` (default) | nonnegative vector

*Since R2024a*

Vector of reverse currents. This parameter must be a vector of at least three
nonnegative elements in ascending order. The zero point is optional
(*Ir* = 0A).

#### Dependencies

To enable this parameter, set:

- **Integral protection diode** to
  `Yes`
- **Diode model** to
  `Tabulated I-V
  curve`
- **Table type** to `Table
  in Vf(Tj,If) form`
- **Reverse I-V characteristics** to
  `Tabulate`

### Thermal Port

Use the thermal ports to simulate the effects of generated heat and device temperature.
This block implements a single internal thermal model for both transistors and the
two diodes. Any thermal model parameters, such as Cauer model parameters, apply to
the aggregated thermal model.

### **Separate thermal ports for upper and lower devices** — Option to separate thermal ports for upper and lower devices `off` (default) | `on`

*Since R2024a*

Whether to separate the thermal ports for the upper and lower
devices.

### **Separate thermal ports for integral diodes** — Option to separate thermal ports for integral diodes `off` (default) | `on`

*Since R2024a*

Whether to separate the thermal ports for the integral diodes of the
upper and lower devices.

#### Dependencies

To enable this parameter, select the **Separate thermal
ports for upper and lower devices** parameter and, in
the **Integral Diode** section, set
**Integral protection diode** to
`Yes`.

### **Thermal network** — Options for thermal network modeling `External` (default) | `Specify junction and case thermal parameters` | `Cauer model` | `Cauer model parameterized with Foster coefficients`

Options for modeling the thermal network of the block.

### **Thermal mass parameterization** — Option to parameterize thermal mass `By thermal time constants` (default) | `By thermal mass`

Options to parameterize the thermal mass:

- `By thermal time constants` —
  Parameterize the thermal masses in terms of thermal time
  constants.
- `By thermal mass` — Specify the
  thermal mass values directly.

### **Junction case and case-ambient (or case-heatsink) thermal resistances, [R\_JC R\_CA]** — Junction case and case-ambient (or case-heatsink) thermal resistances `[.03, .2]` `K/W` (default) | vector of positive values

Row vector [ *R\_JC*
*R\_CA* ] of two thermal resistance values, represented
by two Conductive Heat Transfer blocks. The first value,
*R\_JC*, is the thermal resistance between the
junction and the case. The second value, *R\_CA*, is the
thermal resistance between port **H** and the device
case.

#### Dependencies

To enable this parameter, set **Thermal network**
to `Specify junction and case thermal
parameters`.

### **Junction and case thermal time constants, [t\_J t\_C]** — Junction and case thermal time constants `[.1, 5]` `s` (default) | vector of positive values

Row vector [ *t\_J*
*t\_C* ] of two thermal time constant values. The first
value, *t\_J*, is the junction time constant. The second
value, *t\_C*, is the case time constant.

#### Dependencies

To enable this parameter, set **Thermal network**
to `Specify junction and case thermal
parameters` and **Thermal mass
parameterization** to `By thermal time
constants`.

### **Junction and case thermal masses, [M\_J M\_C]** — Junction and case thermal masses `[3, 25]` `J/K` (default) | vector of positive values

Row vector [ *M\_J*
*M\_C* ] of two thermal mass values. The first value,
*M\_J*, is the junction thermal mass. The second
value, *M\_C*, is the case thermal mass.

#### Dependencies

To enable this parameter, set **Thermal network**
to `Specify junction and case thermal
parameters` and **Thermal mass
parameterization** to `By thermal
mass`.

### **Junction and case initial temperatures, [T\_J T\_C]** — Junction and case initial temperatures `[25, 25]` `degC` (default) | vector of positive values

Row vector [ *T\_J* *T\_C* ] of two
temperature values. The first value, *T\_J*, is the
junction initial temperature. The second value, *T\_C*,
is the case initial temperature.

#### Dependencies

To enable this parameter, set **Thermal network**
to `Specify junction and case thermal
parameters`.

### **Diode junction case and case-ambient (or case-heatsink) thermal resistances, [R\_JC R\_CA]** — Junction case and case-ambient (or case-heatsink) thermal resistances for integral diode `[.03, .2]` `K/W` (default) | vector of positive values

*Since R2024a*

Row vector [ *R\_JC*
*R\_CA* ] of two thermal resistance values, represented
by two Conductive Heat Transfer blocks, for the integral protection
diode. The first value, *R\_JC*, is the thermal
resistance between the junction and the case. The second value,
*R\_CA*, is the thermal resistance between port
**H** and the diode case.

#### Dependencies

To enable this parameter:

- In the **Integral Diode** section,
  set **Integral protection diode** to
  `Yes`.
- In the **Thermal Port** section:

  - Select the **Separate thermal ports
    for upper and lower devices** parameter.
  - Select the **Separate thermal ports
    for integral diodes** parameter.
  - Set **Thermal network** to
    `Specify junction and case thermal
    parameters`.

### **Thermal time constants of diode junction and case, [t\_J t\_C]** — Junction and case thermal time constants for integral diode `[.1, 5]` `s` (default) | vector of positive values

*Since R2024a*

Row vector [ *t\_J*
*t\_C* ] of two thermal time constant values for the
integral protection diode. The first value, *t\_J*, is
the junction time constant. The second value, *t\_C*, is
the case time constant.

#### Dependencies

To enable this parameter:

- In the **Integral Diode** section,
  set **Integral protection diode** to
  `Yes`.
- In the **Thermal Port** section:

  - Select the **Separate thermal ports
    for upper and lower devices** parameter.
  - Select the **Separate thermal ports
    for integral diodes** parameter.
  - Set **Thermal network** to
    `Specify junction and case thermal
    parameters`.
  - Set **Thermal mass
    parameterization** to `By
    thermal time constants`.

### **Thermal masses of diode junction and case, [M\_J M\_C]** — Thermal masses of diode junction and case `[3, 25]` `J/K` (default) | vector of positive values

*Since R2024a*

Row vector [ *M\_J*
*M\_C* ] of two thermal mass values for the integral
protection diode. The first value, *M\_J*, is the
junction thermal mass. The second value, *M\_C*, is the
case thermal mass.

#### Dependencies

To enable this parameter:

- In the **Integral Diode** section,
  set **Integral protection diode** to
  `Yes`.
- In the **Thermal Port** section:

  - Select the **Separate thermal ports
    for upper and lower devices** parameter.
  - Select the **Separate thermal ports
    for integral diodes** parameter.
  - Set **Thermal network** to
    `Specify junction and case thermal
    parameters`.
  - Set **Thermal mass
    parameterization** to `By
    thermal mass`.

### **Initial temperatures of diode junction and case, [T\_J T\_C]** — Initial temperatures of diode junction and case `[25, 25]` `degC` (default) | vector of positive values

*Since R2024a*

Row vector [ *T\_J* *T\_C* ] of two
temperature values for the integral protection diode. The first value,
*T\_J*, is the junction initial temperature. The
second value, *T\_C*, is the case initial
temperature.

#### Dependencies

To enable this parameter:

- In the **Integral Diode** section,
  set **Integral protection diode** to
  `Yes`.
- In the **Thermal Port** section:

  - Select the **Separate thermal ports
    for upper and lower devices** parameter.
  - Select the **Separate thermal ports
    for integral diodes** parameter.
  - Set **Thermal network** to
    `Specify junction and case thermal
    parameters`.

### **Thermal resistances, [R1 R2 … Rn]** — Thermal resistances `[.03, .1, .2]``K/W` (default) | `[.03, .2]` `K/W` | vector of positive values

Row vector of *n* thermal resistance values,
represented by the Cauer elements used in the thermal network.

If you set **Thermal network** to `Cauer
model`, the default value is `[.03, .1,
.2]`. If you set **Thermal network** to
`Cauer model parameterized with Foster
coefficients`, the default value is `[.03,
.2]`.

#### Dependencies

To enable this parameter, set **Thermal network**
to `Cauer model` or `Cauer
model parameterized with Foster
coefficients`.

### **Thermal time constants, [t1 t2 … tn]** — Thermal time constants `[.1, 1, 5]` `s` (default) | `[1, 10]` `s` | vector of positive values

Row vector of *n* thermal time constant values, where
*n* is the number of Cauer elements used in the
thermal network. The length of this vector must match the length of
**Thermal resistances, [R1 R2 … Rn]**. With this
parameterization, the thermal masses are computed as
`Mi =
ti/Ri`,
where `Mi`,
`ti` and
`Ri` are the thermal
mass, thermal time, and thermal resistance for the
ith Cauer element (if you set
**Thermal network** to `Cauer
model`) or Foster element (if you set **Thermal
network** to `Cauer model parameterized with
Foster coefficients`).

If you set **Thermal network** to `Cauer
model`, the default value is `[.1, 1,
5]`. If you set **Thermal network** to
`Cauer model parameterized with Foster
coefficients`, the default value is `[1,
10]`.

#### Dependencies

To enable this parameter, set **Thermal network**
to `Cauer model` or `Cauer
model parameterized with Foster coefficients`and
**Thermal mass parameterization** to
`By thermal time constants`.

### **Thermal masses, [M1 M2 … Mn]** — Thermal masses `[3, 10, 25]` `J/K` (default) | `[33, 50]` `J/K` | vector of positive values

Row vector of *n* thermal mass values, where n is the
number of Cauer elements used in the thermal network.

If you set **Thermal network** to `Cauer
model`, the default value is `[3, 10,
25]`. If you set **Thermal network** to
`Cauer model parameterized with Foster
coefficients`, the default value is `[33,
50]`.

#### Dependencies

To enable this parameter, set **Thermal network**
to `Cauer model` or `Cauer
model parameterized with Foster coefficients` and
**Thermal mass parameterization** to
`By thermal masses`.

### **Thermal masses initial temperatures, [T1 T2 … Tn]** — Thermal masses initial temperatures `[25, 25, 25]` `degC` (default) | vector of positive values

Row vector of temperature values that corresponds to the temperature
drop across each thermal capacity in the model.

#### Dependencies

To enable this parameter, set **Thermal network**
to `Cauer model`.

### **Diode thermal resistances, [R1 R2 … Rn]** — Thermal resistances for integral diode `[.03, .1, .2]``K/W` (default) | `[.03, .2]` `K/W` | vector of positive values

*Since R2024a*

Row vector of *n* thermal resistance values for the
integral protection diode, represented by the Cauer elements used in the
thermal network.

If you set **Thermal network** to `Cauer
model`, the default value is `[.03, .1,
.2]`. If you set **Thermal network** to
`Cauer model parameterized with Foster
coefficients`, the default value is `[.03,
.2]`.

#### Dependencies

To enable this parameter:

- In the **Integral Diode** section,
  set **Integral protection diode** to
  `Yes`.
- In the **Thermal Port** section:

  - Select the **Separate thermal ports
    for upper and lower devices** parameter.
  - Select the **Separate thermal ports
    for integral diodes** parameter.
  - Set **Thermal network** to
    `Cauer model` or
    `Cauer model parameterized with Foster
    coefficients`.

### **Diode thermal time constants, [t1 t2 … tn]** — Thermal time constants for integral diode `[.1, 1, 5]` `s` (default) | `[1, 10]` `s` | vector of positive values

*Since R2024a*

Row vector of *n* thermal time constant values for the integral
protection diode, where *n* is the number of Cauer
elements used in the thermal network. The length of this vector must
match the length of **Diode thermal resistances, [R1 R2 …
Rn]**. With this parameterization, the thermal masses are
computed as `Mi =
ti/Ri`,
where `Mi`,
`ti` and
`Ri` are the thermal
mass, thermal time, and thermal resistance for the
ith Cauer element (if you set
**Thermal network** to `Cauer
model`) or Foster element (if you set **Thermal
network** to `Cauer model parameterized with
Foster coefficients`).

If you set **Thermal network** to `Cauer
model`, the default value is `[.1, 1,
5]`. If you set **Thermal network** to
`Cauer model parameterized with Foster
coefficients`, the default value is `[1,
10]`.

#### Dependencies

To enable this parameter:

- In the **Integral Diode** section,
  set **Integral protection diode** to
  `Yes`.
- In the **Thermal Port** section:

  - Select the **Separate thermal ports
    for upper and lower devices** parameter.
  - Select the **Separate thermal ports
    for integral diodes** parameter.
  - Set **Thermal network** to
    `Cauer model` or
    `Cauer model parameterized with Foster
    coefficients`.
  - Set **Thermal mass
    parameterization** to `By
    thermal time constants`.

### **Diode thermal masses, [M1 M2 … Mn]** — Thermal masses for integral diode `[3, 10, 25]` `J/K` (default) | `[33, 50]` `J/K` | vector of positive values

*Since R2024a*

Row vector of *n* thermal mass values for the
integral protection diode, where n is the number of Cauer elements used
in the thermal network.

If you set **Thermal network** to `Cauer
model`, the default value is `[3, 10,
25]`. If you set **Thermal network** to
`Cauer model parameterized with Foster
coefficients`, the default value is `[33,
50]`.

#### Dependencies

To enable this parameter:

- In the **Integral Diode** section,
  set **Integral protection diode** to
  `Yes`.
- In the **Thermal Port** section:

  - Select the **Separate thermal ports
    for upper and lower devices** parameter.
  - Select the **Separate thermal ports
    for integral diodes** parameter.
  - Set **Thermal network** to
    `Cauer model` or
    `Cauer model parameterized with Foster
    coefficients`.
  - Set **Thermal mass
    parameterization** to `By
    thermal masses`.

### **Initial temperatures of diode thermal masses, [T1 T2 … Tn]** — Initial temperatures of diode thermal masses `[25, 25, 25]` `degC` (default) | vector of positive values

*Since R2024a*

Row vector of temperature values for the integral protection diode.
This parameter corresponds to the temperature drop across each thermal
capacity in the model.

#### Dependencies

To enable this parameter:

- In the **Integral Diode** section,
  set **Integral protection diode** to
  `Yes`.
- In the **Thermal Port** section:

  - Select the **Separate thermal ports
    for upper and lower devices** parameter.
  - Select the **Separate thermal ports
    for integral diodes** parameter.
  - Set **Thermal network** to
    `Cauer model`.

### **Initial node temperatures, [T1 T2 ... Tn]** — Initial node temperatures `[25, 25, 25, 25]` `degC` (default) | vector of positive values

Row vector of absolute temperature values of each node starting from
the junction.

#### Dependencies

To enable this parameter, set **Thermal network**
to `Cauer model parameterized with Foster
coefficients`.

### **Diode initial node temperatures, [T1 T2 ... Tn]** — Initial node temperatures for integral diode `[25, 25, 25, 25]` `degC` (default) | vector of positive values

*Since R2024a*

Row vector of absolute temperature values of each node starting from
the integral protection diode junction.

#### Dependencies

To enable this parameter:

- In the **Integral Diode** section,
  set **Integral protection diode** to
  `Yes`.
- In the **Thermal Port** section:

  - Select the **Separate thermal ports
    for upper and lower devices** parameter.
  - Select the **Separate thermal ports
    for integral diodes** parameter.
  - Set **Thermal network** to
    `Cauer model parameterized with Foster
    coefficients`.

### **Junction thermal mass** — Thermal mass of junction `0.1` `J/K` (default) | positive scalar

Thermal mass of the junction.

#### Dependencies

To enable this parameter, set **Thermal network**
to `External`.

### **Diode junction thermal mass** — Thermal mass of diode junction `0.1` `J/K` (default) | positive scalar

*Since R2024a*

Thermal mass of the diode junction.

#### Dependencies

To enable this parameter:

- In the **Integral Diode** section,
  set **Integral protection diode** to
  `Yes`.
- In the **Thermal Port** section:

  - Select the **Separate thermal ports
    for upper and lower devices** parameter.
  - Select the **Separate thermal ports
    for integral diodes** parameter.
  - Set **Thermal network** to
    `External`.

For more information about using thermal ports and for the other **Thermal
Port** parameters, see Simulating Thermal Effects in Semiconductors.

## Libraries

Simscape / Electrical / Semiconductors & Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

### R2024a: Separate thermal ports for upper device, lower device, and integral diodes

You can now separate the thermal port **H** into two different thermal
ports associated with the upper and lower switching devices, respectively, by
selecting the **Separate thermal ports for upper and lower
devices** parameter. If you separate the thermal ports for the upper
and lower devices, you can then also separate the thermal ports for the integral
diodes of each switching device by selecting the **Separate thermal ports
for integral diodes** parameter.

The upper and lower switching devices share the same thermal parameters.

### R2024a: Model tabulated reverse I-V characteristics

You can now model the reverse I-V characteristics for the Half-Bridge (Ideal, Switching) block by
tabulating the current as a function of temperature and voltage or the voltage as a
function of temperature and current.

Before R2024a, you can only model the reverse I-V characteristics by specifying
the off conductance of the reverse-biased diode.

### R2023b: Determine switching losses for discontinuous load currents

If you set the **Switching device** parameter to
`MOSFET` or `IGBT`, the
Half-Bridge (Ideal, Switching) block now supports
discontinuous load currents.

The block supports discontinuous load currents by measuring the off-state voltage
and on-state current at all turn-on and turn-off events to compute switching losses.
New models behave this way by default. If you use a fixed-step solver, the shortest
device on or off period is now one step. Before R2023b, the minimum period is three
steps. To report switching losses, the minimum period is still three steps.

Before R2023b, the block measures the off-state voltage before turn-on and
on-state current before turn-off only.

As a result of this change, if you create a model in an earlier release that uses the
Half-Bridge (Ideal, Switching) block with
external diodes that model capacitance or charge, you must update the model. The
best option is to model diodes internally within the Half-Bridge
(Ideal, Switching) block. To model the diodes externally, model
them without capacitance or charge.

### R2023b: Apply switching losses to electrical supply

You can now draw the power due to switching losses from the electrical supply by
selecting the **Apply switching losses to electrical supply**
parameter. Before R2023a, the block applies switching losses to the thermal node
only, stepping the node temperature up by the requisite value.

### R2023b: Tabulate switching losses with temperature, current, and voltage

If you set the **Switching device** parameter to
`MOSFET` or `IGBT`, you can
now tabulate switching losses with temperature, current, and voltage. In earlier
releases, you can tabulate switching losses with temperature and current
only.

## Description

Half-bridge with ideal switches and thermal port

The Half-Bridge (Ideal, Switching) block models a half-bridge
with ideal switches and a thermal port. To choose the ideal switching device, set the
**Switching device** parameter to
`MOSFET`, `IGBT`, or
`GTO`.

You can specify an integral protection diode for each switching device. An integral diode
protects the semiconductor device by providing a conduction path for a reverse current.
An inductive load can produce a high reverse-voltage spike when the semiconductor device
suddenly switches off the voltage supply to the load.

**Note**

The best option is to model diodes internally within the Half-Bridge (Ideal,
Switching) block. To model the diodes externally, model them without capacitance
or charge.

### Switching Losses

For information about how the block models turn-on and turn-off losses, see the
documentation page for the MOSFET (Ideal, Switching) block, IGBT (Ideal, Switching) block, or GTO block, depending on the option you select for the
**Switching Device** parameter. The main difference between how
these blocks and the Half-Bridge (Ideal, Switching)
block model the losses is that, for the `MOSFET` and
`IGBT` options, the Half-Bridge (Ideal,
Switching) block does not use the **Use last on-state
current from previous cycle for turn-on loss** or **Use last
off-state voltage from previous cycle for turn-off loss** parameters.
The reason for this difference is that the Half-Bridge (Ideal,
Switching) block does not model diode capacitance or lead
inductance because the block is designed for fast simulation using ideal switching.
By modeling both switching devices in one block, you avoid the complexities
associated with measuring the on-state current and off-state voltage for diode
reverse recovery, so you do not need a physics-based diode charge model. The block
measures the diode forward current and off-state voltages at the point that you
command the complementary switching device to switch off.

By default, the block applies switching losses to the thermal node only, stepping the node
temperature up by the requisite value. To draw the requisite power due to switching
losses from the electrical supply, select the **Apply switching losses to
electrical supply** parameter.

Instantaneously applying a switching loss to the electrical supply is not mathematically
possible, so the block applies switching losses over a period equal to the value you
specify for the **Averaging period for switching losses**
parameter. Set this value equal to the pulse-width modulation (PWM) period of the
gate driver.

**Note**

For all ideal switching devices, the logged simulation data reports the
thermal losses as `lastTurnOffLoss`,
`lastTurnOnLoss`, and
`lastReverseRecoveryLoss`. These variables include losses
as a pulse with an amplitude equal to the energy loss. If you use a script to
sum the total losses over a defined simulation period, you must sum the pulse
values at each pulse rising edge. Alternatively, you can extract conduction and
switching losses from logged data using the `ee_getPowerLossSummary` and
`ee_getPowerLossTimeSeries` functions.
To learn how to log and plot simulation data, see the Log and Plot Simulation Data example.

You can also access the total accumulated switching losses for each of the two
switching devices from the respective
`accumulatedSwitchingLosses` variables in the logged
simulation data. These variables sum all switching losses to date, including
reverse recovery losses for the diode.

The `power_dissipated` variable in the logged simulation data
does not include switching losses because the block models these losses as
instantaneous events. The `power_dissipated` variable reports
ohmic on-state losses.

If you are using a fixed-step solver, the shortest pulse on or pulse off that
supports capture of the switching losses is three time steps long. If the pulse
is shorter than three steps, the block does not report switching losses.

If you use tabulated data to model the switching losses or reverse recovery
losses, check that the temperature, current, and voltage are in the range you
specify. If you do not define a realistic thermal model, for example, if the
junction mass or the conductance from the junction to the case is too small, the
temperature can exceed the range you specify, causing the block to extrapolate
the losses to nonphysical values.

### Parameterization

The Half-Bridge (Ideal, Switching) block supports multiple
predefined parameterizations.

Use this parameterization data to represent components by specific suppliers. The
parameterizations of these half-bridges match the manufacturer data sheets. To load
a predefined parameterization, double-click the Half-Bridge (Ideal, Switching)
block, click the **<click to select>** hyperlink of
the **Selected part** parameter, and, in the Block Parameterization
Manager window, select the part you want to use from the list of available
components.

**Note**

The predefined parameterizations of Simscape™ components use available data sources for the parameter values. Engineering
judgment and simplifying assumptions are used to fill in for missing data. As a result,
expect deviations between simulated and actual physical behavior. To ensure accuracy,
validate the simulated behavior against experimental data and refine component models as
necessary.

For more information about predefined parameterization and a list of the available
components, see List of Pre-Parameterized Components.

You can also use the `ee_importDeviceParameters` function to extract the device parameters
for the switching device and integral protection diode from XML files and import
them into the block. The XML file must be on the MATLAB® path and must use a parameterization format supported by Hitachi or
Infineon®.

### Thermal Port

Use the thermal port to simulate the effects of generated heat and device
temperature. For more information on using thermal ports and the **Thermal
Port** parameters, see Simulating Thermal Effects in Semiconductors.

You can also separate the thermal port
**H** into two different thermal ports associated with the upper and
lower switching devices, respectively, by selecting the **Separate thermal
ports for upper and lower devices** parameter. If you separate the
thermal ports for the upper and lower devices, you can then also separate the
thermal ports for the integral diodes of each switching device by selecting the
**Separate thermal ports for integral diodes** parameter. The
upper and lower switching devices share the same thermal parameters. *(since R2024a)*

This figure shows the block icon when you expose all the thermal ports:

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Use nominal values to specify the expected magnitude of a variable in a model. Using
system scaling based on nominal values increases the simulation robustness. Nominal values
can come from different sources. One of these sources is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
