---
type: simulink-block
title: 'C2803x LIN Receive'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2803x'
documentation_page: 'c2803xlinreceive'
documentation_source_path: 'ref/c2803xlinreceive.html'
language: en
---

# C2803x LIN Receive

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters: []
```

**Data type**
:   Select the data type the LIN block outputs to the model. Available options are
    `single`, `int8`,
    `uint8`, `int16`,
    `uint16`, `int32`, or
    `uint32`. To interpret the data, the data type and data
    length must match those of the data input to transmitting LIN node.

    The default value is `int16`.

**Data length**
:   Set the length of the data the LIN block outputs to the model. This value is
    measured in multiples of the **Data type**. For example, if
    **Data type** is `int16` and
    **Data length** is `int16`, the LIN block
    outputs the data to the model in lengths of

    1 x int16

    If you set the **Data length** to a value greater than 1,
    the block outputs the data as vectors.

    To interpret the data, the data type and data length must match those of the data
    input to transmitting LIN node.

    The default value is 1.

    **Note**

    In a loopback configuration, the maximum data length cannot exceed 8 bytes. If
    the sum of the incoming and the outgoing data exceeds the hardware buffer length of
    the LIN module, the module discards incoming bytes of data.

**Initial output**
:   Set the initial value the DATA port outputs to the model before the LIN node has
    received data.

    The default value is `0`.

**Action taken when connection times out**
:   Specify what the LIN block outputs on the DATA port in response to a connection
    time-out. The choices are:

    - `Output the last received value` — the DATA
      port outputs the last data value the LIN node received.
    - `Output custom value` — the DATA port outputs
      the value defined by **Output value when connection times
      out**.

    The default value is `Output the last received
    value`.

    If the LIN node has not received data, and you set this parameter to
    `Output the last received value`, the DATA port outputs the
    **Initial output** value.

**Output value when connection times out**
:   Specify the custom value the DATA port outputs when **Action taken when
    connection times out** is set to `Output custom
    value` and a connection timeout occurs.

**Enable blocking mode**
:   If you enable (select) this checkbox, the target application stops and waits for
    the LIN node to receive data before continuing. If you disable this option, the
    application continues running and does not wait for data to arrive.

    The default value is disabled (deselected).

**Verify checksum**
:   If you enable (select) this option, the LIN node verifies the checksum it
    receives.

    The default value is disabled (deselected).

**Output receiving status**
:   Enabling (selecting) this checkbox adds a `status` output to the
    LIN Receive block, as shown in the following figure.

    The `status` output reports the following values for each message
    the LIN node receives:

    - `0`: No error.
    - `-1`: A time-out occurred while the block was waiting to
      receive data.
    - `-2`: Unable to receive.
    - Other status values represent the highest 8 bits of the SCI Flags Register.
      Convert these values from decimal to binary. Then determine the meaning of these
      values by referring to Table 14. SCI Flags Register (SCIFLR) Field Descriptions
      in *TMS320F2803x Piccolo Local Interconnect Network (LIN)
      Module*, Literature Number SPRUGE2, available at the Texas Instruments® Web site.

**Receive buffer interrupt**
:   If you enable this option, the SCI node generates an interrupt after it receives a
    complete frame. The default value is `Disabled`.

**Checksum error interrupt**
:   If you enable this option, the LIN block generates an interrupt when the incoming
    message contains an invalid checksum.

    The default value is `Disabled`.

    The TXRX Error Detector Checksum Calculator verifies checksums for incoming
    messages. With the classic LIN implementation, the checksum only covers the data
    fields. For LIN 2.0–compliant messages, the checksum includes both the ID field and
    the data fields. If you enable this option, the Checksum Calculator generates
    interrupts when it detects checksum errors, such as those caused by LIN message
    collisions.

**Framing error interrupt**
:   If you enable this option, the LIN module generates interrupts when framing errors
    occur.

    The default value is `Disabled`.

**Overrun error interrupt**
:   If you enable this option, the LIN module generates interrupt when overrun errors
    occur.

    The default value is `Disabled`.

**ID parity error interrupt**
:   If you enable this option, the LIN module generates an ID-Parity interrupt when it
    receives an invalid ID.

    The default value is `Disabled`.

    If you enable this option, also enable **Parity mode** in
    Hardware Implementation -> Target Hardware Resources.

**ID match interrupt**
:   If you enable this option, the LIN module generates an interrupt when the LIN node
    validates the ID in messages it receives.

    The default value is `Disabled`.

**Sample time**
:   Set the block's input sample time,
    `Ts`.

    The default value is `0.1` seconds.

**Data type**
:   Select the data type the LIN block outputs to the model. Available options are
    `single`, `int8`,
    `uint8`, `int16`,
    `uint16`, `int32`, or
    `uint32`. To interpret the data, the data type and data
    length must match those of the data input to transmitting LIN node.

    The default value is `int16`.

**Data length**
:   Set the length of the data the LIN block outputs to the model. This value is
    measured in multiples of the **Data type**. For example, if
    **Data type** is `int16` and
    **Data length** is `int16`, the LIN block
    outputs the data to the model in lengths of

    1 x int16

    If you set the **Data length** to a value greater than 1,
    the block outputs the data as vectors.

    To interpret the data, the data type and data length must match those of the data
    input to transmitting LIN node.

    The default value is 1.

    **Note**

    In a loopback configuration, the maximum data length cannot exceed 8 bytes. If
    the sum of the incoming and the outgoing data exceeds the hardware buffer length of
    the LIN module, the module discards incoming bytes of data.

**Initial output**
:   Set the initial value the DATA port outputs to the model before the LIN node has
    received data.

    The default value is `0`.

**Action taken when connection times out**
:   Specify what the LIN block outputs on the DATA port in response to a connection
    time-out. The choices are:

    - `Output the last received value` — the DATA
      port outputs the last data value the LIN node received.
    - `Output custom value` — the DATA port outputs
      the value defined by **Output value when connection times
      out**.

    The default value is `Output the last received
    value`.

    If the LIN node has not received data, and you set this parameter to
    `Output the last received value`, the DATA port outputs the
    **Initial output** value.

**Output value when connection times out**
:   Specify the custom value the DATA port outputs when **Action taken when
    connection times out** is set to `Output custom
    value` and a connection timeout occurs.

**Enable blocking mode**
:   If you enable (select) this checkbox, the target application stops and waits for
    the LIN node to receive data before continuing. If you disable this option, the
    application continues running and does not wait for data to arrive.

    The default value is disabled (deselected).

**Verify checksum**
:   If you enable (select) this option, the LIN node verifies the checksum it
    receives.

    The default value is disabled (deselected).

**Output receiving status**
:   Enabling (selecting) this checkbox adds a `status` output to the
    LIN Receive block, as shown in the following figure.

    The `status` output reports the following values for each message
    the LIN node receives:

    - `0`: No error.
    - `-1`: A time-out occurred while the block was waiting to
      receive data.
    - `-2`: Unable to receive.
    - Other status values represent the highest 8 bits of the SCI Flags Register.
      Convert these values from decimal to binary. Then determine the meaning of these
      values by referring to Table 14. SCI Flags Register (SCIFLR) Field Descriptions
      in *TMS320F2803x Piccolo Local Interconnect Network (LIN)
      Module*, Literature Number SPRUGE2, available at the Texas Instruments® Web site.

**Receive buffer interrupt**
:   If you enable this option, the SCI node generates an interrupt after it receives a
    complete frame. The default value is `Disabled`.

**Checksum error interrupt**
:   If you enable this option, the LIN block generates an interrupt when the incoming
    message contains an invalid checksum.

    The default value is `Disabled`.

    The TXRX Error Detector Checksum Calculator verifies checksums for incoming
    messages. With the classic LIN implementation, the checksum only covers the data
    fields. For LIN 2.0–compliant messages, the checksum includes both the ID field and
    the data fields. If you enable this option, the Checksum Calculator generates
    interrupts when it detects checksum errors, such as those caused by LIN message
    collisions.

**Framing error interrupt**
:   If you enable this option, the LIN module generates interrupts when framing errors
    occur.

    The default value is `Disabled`.

**Overrun error interrupt**
:   If you enable this option, the LIN module generates interrupt when overrun errors
    occur.

    The default value is `Disabled`.

**ID parity error interrupt**
:   If you enable this option, the LIN module generates an ID-Parity interrupt when it
    receives an invalid ID.

    The default value is `Disabled`.

    If you enable this option, also enable **Parity mode** in
    Hardware Implementation -> Target Hardware Resources.

**ID match interrupt**
:   If you enable this option, the LIN module generates an interrupt when the LIN node
    validates the ID in messages it receives.

    The default value is `Disabled`.

**Sample time**
:   Set the block's input sample time,
    `Ts`.

    The default value is `0.1` seconds.
## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Receive data via local interconnect network (LIN) module on target

# C2803x LIN Receive

Receive data via local interconnect network (LIN) module on target

The Local Interconnect Network (LIN) bus implements a serial communications protocol for
distributed automotive and industrial applications. In particular, LIN serves low cost
applications that do not require the bandwidth or robustness provided by the CAN
protocol.

The LIN Receive block configures the target to receive scalar or vector data from the
LINRX or LINTX pins.

Each C2803x target has one LIN module. Your model can only contain one LIN Transmit and
one LIN Receive block per module.

The C2803x LIN Transmit block takes three inputs:

- **ID**: Set the value of the LIN ID for the LIN transmit
  node.
- **TX ID Mask**: Set the value of the LIN ID mask for the LIN
  transmit node.
- **Data**: Connect this input to the data source.

For more information and examples, see:

- Configuring LIN Communications
- LIN-Based Control of PWM Duty Cycle

**Note**

Many LIN-specific settings are located under **Peripherals** >
**LIN** in Hardware Implementation -> Target Hardware Resources for
your model. Verify that these settings meet the requirements of your application.

- C2803x LIN Receive block
