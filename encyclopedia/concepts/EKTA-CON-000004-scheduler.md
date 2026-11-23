---
id: EKTA-CON-000004
canonical_name: Scheduler
status: PROPOSED
revision: 0.1.0
created: 2026-11-23
updated: 2026-11-23
domains: [software-engineering, computer-engineering, operating-systems-platforms, systems-engineering]
layers: [hardware-architecture, operating-system, platform-runtime, workflow-orchestration]
knowledge_types: [concept, component]
aliases: [dispatcher scheduler, task scheduler]
confidence: medium
sources: []
---

# Scheduler

## Definition
A scheduler selects or orders eligible work for execution and assigns it to available execution resources according to policies, constraints, and current system state.

## Scope
Scheduling occurs at multiple levels: instruction, CPU thread/process, real-time task, GPU workload, cluster job, workflow task, and agent task. These are related abstractions but have different timing and resource semantics.

## Purpose and role
Resolve competition for finite resources while balancing objectives such as fairness, throughput, latency, deadlines, priority, locality, energy, and utilization.

## Mechanism
Collect eligible work, inspect constraints and resource state, rank/select candidates using a policy, dispatch selected work, and react to completion, preemption, deadlines, or resource changes.

## Inputs and outputs
Inputs: runnable work, priorities, deadlines, dependencies, resource availability, policy. Outputs: dispatch decisions, queues, preemption decisions, scheduling metrics.

## Relationships
- SCHEDULES: task/process/work item
- USES: queue and resource manager
- OBSERVES: resource availability
- PART_OF: runtime or operating system (context-dependent)

## Techniques
Round-robin, priority scheduling, shortest-job policies, fair scheduling, deadline scheduling, work stealing, affinity, backfilling, admission control.

## Trade-offs
No single policy optimizes all objectives. Fairness can reduce peak throughput; strict priorities can starve low-priority work; preemption has overhead; deadline guarantees depend on workload assumptions.

## Verification
Measure latency, throughput, fairness, starvation, deadline misses, utilization, preemption overhead, and behavior under overload.
