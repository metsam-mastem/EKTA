---
id: EKTA-CON-000006
canonical_name: Controller
status: PROPOSED
revision: 0.1.0
created: 2026-11-23
updated: 2026-11-23
domains: [software-engineering, control-automation, embedded-firmware, systems-engineering]
layers: [application-agent, workflow-orchestration, firmware-control, physical-implementation]
knowledge_types: [concept, component]
aliases: [control unit, control component]
confidence: medium
sources: []
---

# Controller

## Definition
A controller is a component that determines or coordinates actions to move a system toward a target condition, enforce a policy, or manage a controlled process.

## Scope and disambiguation
In control engineering, a controller computes control actions from setpoints, measurements, and a control law. In software architecture, a controller may route requests or coordinate application behavior. In workflow systems, it may reconcile desired and observed process state. These meanings share a coordination/control family but are not interchangeable.

## Purpose
Translate goals, events, or measured state into actions.

## Mechanism
Observe inputs/state, evaluate rules or a control law, select actions, issue commands, and optionally use feedback to adjust subsequent actions.

## Inputs and outputs
Inputs: desired state, observed state, events, policy, constraints. Outputs: commands, routing decisions, control signals, state transitions.

## Relationships
- CONTROLS: managed component or process
- OBSERVES: state or measurement
- USES: policy, control law, feedback
- PART_OF: control loop or application architecture

## Techniques
Feedback control, feedforward control, PID, state reconciliation, event routing, policy evaluation.

## Trade-offs
Centralization can simplify coordination but create bottlenecks or single points of failure. Feedback delay, sensor quality, model mismatch, and unstable policies can cause oscillation or poor control.

## Verification
Test response, stability where applicable, overshoot, settling time, policy correctness, failure modes, and safe behavior under missing or noisy inputs.
