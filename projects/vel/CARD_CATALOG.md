# VEL Card Catalog 0.1

This catalog defines the initial visual vocabulary. Color and icon are presentation hints; stable IDs and typed fields carry meaning.

## Entity cards

| Card family | Suggested kind | Meaning |
|---|---|---|
| SYSTEM | system | Whole system or bounded context |
| SUBSYSTEM | subsystem | A bounded part of a system |
| MODULE | module | Logical or physical module |
| COMPONENT | component | Replaceable constituent |
| SERVICE | service | Software service |
| DEVICE | device | Physical device |
| ACTOR | actor | Human or external actor |
| API | interface | Software interface |
| DATA STORE | datastore | Persistent or transient storage |
| RESOURCE | resource | Compute, energy, material, or capacity |
| PROCESS | process | Defined operation |
| EVENT | event | Occurrence or notification |
| RULE | rule | Constraint or policy |
| TEST | test | Verification activity |
| EVIDENCE | evidence | Artifact supporting a claim |
| RISK | risk | Uncertainty or potential loss |
| DECISION | decision | Explicit choice and rationale |

## Connector cards

| Connector | Semantic meaning | Typical use |
|---|---|---|
| DATA | Payload transfer | Request, result, record |
| CONTROL | Command or control signal | Start, stop, configure |
| EVENT | Event notification | Publish/subscribe |
| POWER | Electrical or energy supply | Power rail |
| SIGNAL | Measured or analog/digital signal | Sensor/actuator |
| MECHANICAL | Physical attachment or force path | Mount, shaft, linkage |
| NETWORK | Network communication | TCP/IP, fieldbus |
| DEPENDENCY | Required capability or prerequisite | Package/service dependency |
| MATERIAL | Material transfer | Manufacturing |
| FLUID | Fluid transfer | Pneumatics/hydraulics |
| THERMAL | Heat transfer | Cooling/thermal path |

## State tokens

| Token | Meaning |
|---|---|
| ? | Unknown / requires clarification |
| ! | Risk or attention required |
| X | Explicitly forbidden or disconnected |
| + | Add |
| ~ | Provisional / assumption |
| = | Approved decision |
| * | Priority marker |
| @ | Owner / responsible actor |
| # | Stable identifier |
| [] | Set or selected scope |
| {} | Group or bounded collection |

## Card design rules

1. Label, stable ID, kind, and status MUST be visually distinguishable.
2. Ports MUST have visible direction and channel labels.
3. A color MUST never be the only carrier of meaning.
4. Card size SHOULD scale with information density, not importance.
5. Printed cards SHOULD reserve a QR/short-code area for stable identity.
6. Physical and digital versions MUST share the same ID and field semantics.
7. Unknown or unverified fields MUST remain visibly distinct from confirmed fields.

## Print-kit proposal

The first printable kit should use A6 entity cards, narrow connector strips, small state tokens, and transparent boundary overlays. This is a design proposal, not a manufacturing specification. Dimensions and accessibility must be tested before release.
