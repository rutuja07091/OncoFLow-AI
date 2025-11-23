# OncoFlow: AI-Powered Oncology Scheduling & Disruption Management

Built Using IBM watsonx Orchestrate + Multi-Agent Workflows + PubMed Evidence Integration

## 1. Overview

OncoFlow is an intelligent, multi-agent orchestration system designed to solve a real hospital problem: oncology departments struggle with scheduling due to doctor availability constraints, last-minute disruptions, and the critical timing requirements of chemotherapy and radiation therapy.

OncoFlow automates these workflows using:

AI-assisted scheduling

Real-time disruption handling

Calendar integration

Clinical justification via PubMed

LLM-powered patient messaging

All components run inside IBM watsonx Orchestrate, leveraging agents, skill flows, custom tools, and external APIs.

## 2. Problem Statement

Oncology scheduling is operationally complex and clinically fragile:

Doctors avoid specific time windows.

Last-minute sickness or outages disrupt entire patient lists.

Patients have rigid treatment cycles (delays reduce survival).

Communication overload falls on nurses & coordinators.

OncoFlow solves this by orchestrating schedules, reacting to disruptions, and grounding decisions in medical evidence.

## 3. Solution Architecture

OncoFlow uses a three-agent architecture:

### A. Orchestrator Agent

Routes user intent:

Scheduling → Scheduler Agent

Disruptions → Disruption Agent

Clinical justification → PubMed

Tools:

pubmed_search

Delegation to Scheduler/Disruption Agents

### B. Scheduler Agent (Planning)

Optimizes daily/weekly oncology calendars.

Capabilities:

Loads doctor constraints

Retrieves patient appointments

Computes risk scores

Proposes safe schedules

Learns patient preferences

Books on hospital calendar

## Tools:

-mock_data

-get_doctor_schedule

-get_doctor_constraints

-ompute_treatment_risk

-find_available_slots

-propose_schedule_changes
-apply_schedule_changes
-update_patient_preferences
-calendar_block_slot

### C. Disruption Agent (Reactive)

Handles unplanned events (doctor sick, system outage).

Capabilities:

Identifies affected patients

Recomputes treatment risk

Finds safe alternatives

Generates empathetic patient messages

Escalates complex cases

Tools:

-get_appointments_for_window
-compute_treatment_risk
-find_available_slots
-propose_schedule_changes
-generate_patient_message
-send_notification
-update_patient_preferences
-escalate_to_human_scheduler
-calendar_block_slot

## 4. External Integrations
### A. Calendar Adapter

Custom tool that blocks/updates time slots when appointments are booked or moved.

### B. PubMed Integration

Used to justify clinical decisions.

OpenAPI imported from:
openapi/pubmed-openapi.yaml

Tool:
-pubmed_search

Used when:

User asks: “Why is this delay unsafe?”

Or “Provide research evidence.”

## 5. Key Features

Real-time oncology schedule optimization

Intelligent disruption handling

Automated patient messaging

Constraint-aware appointment booking

Clinical justification (PubMed research)

Calendar time-slot blocking

Preference-learning (per patient)

Multi-agent orchestration (Orchestrator → Scheduler/Disruption)

Demo link- 
"https://drive.google.com/drive/folders/1pRDlFKXvFPkdWDwaD2jiuxqfSswvnCp0?usp=sharing "

