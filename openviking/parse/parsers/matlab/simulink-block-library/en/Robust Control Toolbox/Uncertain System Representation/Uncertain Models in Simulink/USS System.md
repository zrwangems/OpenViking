---
type: simulink-block
title: 'USS System'
family: 'robust'
product_id: 'robust'
product_name: 'Robust Control Toolbox'
documentation_release: R2025b
official_category: 'Uncertain System Representation / Uncertain Models in Simulink'
documentation_page: 'usssystem'
documentation_source_path: 'ref/usssystem.html'
language: en
---

# USS System

## Ports

Not documented in R2025b.

## Parameters

### USS system variable

The uncertain object (USS, UMAT, `ureal`, or
`ultidyn`) is entered in the USS system
variable.

### Initial states (nominal dynamics)

If the nominal value for the USS system variable has states, then the
initial condition for these states is entered in `Initial
states (nominal dynamics).`

### Uncertainty value

The values for the uncertain elements are controlled by the
`Uncertainty value` menu. If
`Nominal` is selected, then the nominal
value of the uncertain object is used. If you select `User
defined`, then you must enter a MATLAB® structure in the `User-defined uncertainty
(struct)` dialog box. The field names of the
structure should correspond to the names of the uncertain atoms
within the USS system variable, while the values of the fields are
the values used for the uncertain objects (using the command
`usubs`). If some of these values are SS
objects, then these states are referred to as uncertainty
states.

The order of the uncertainty states is determined by the order of
atoms in the Uncertainty property of the USS system variable. The
state dimension is determined by the actual data in the
`User-defined uncertainty` structure. Any
extra fields in the `User-defined uncertainty`structure are ignored.

### User-defined uncertainty (struc)

If `User defined` is selected from the
`Uncertainty value` pop-up menu, then the
structure data entered in `User-defined uncertainty
(struct)` must contain fields corresponding to
every uncertain atom of the USS system variable. Extra fields are
ignored. `usimsamp` generates a random instance
of each atom in a Simulink® model. It returns a structure, suitable for entry in
`User-defined uncertainty (struct)`.

### Initial states (uncertain dynamics)

The initial condition for the uncertainty states is entered in
`Initial states (uncertain
dynamics)`.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2007a**

## Description

(Not recommended) Import uncertain systems into Simulink

The USS System block accepts USS and UMAT containing
`ureal` and `ultidyn`
uncertain objects, as well as `ureal` and
`ultidyn` objects. An instance of the uncertain
system is used in the simulation or linearization. Internally, USS models
are converted to their state space equivalent for evaluation.
