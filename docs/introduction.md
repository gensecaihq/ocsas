---
layout: default
title: Introduction
nav_order: 2
parent: Home
---

# OCSAS - OpenClaw Security Assurance Standard

OSSASAI implementation profile for the OpenClaw AI agent gateway

## Overview

**OCSAS** (OpenClaw Security Assurance Standard) is the official [OSSASAI](https://github.com/gensecaihq/ossasai) implementation profile for [OpenClaw](https://openclaw.ai) — a WhatsApp, Telegram, Discord, iMessage, and Slack gateway for AI agents with shell, filesystem, and browser access.

This profile maps OSSASAI's 24 security controls to OpenClaw's built-in security features, providing a structured verification framework for secure deployments.

> **Parent Framework:** OCSAS implements [OSSASAI](https://github.com/gensecaihq/ossasai) (Open Security Standard for Agentic Systems) — a vendor-neutral security framework for AI agent systems.

## Quick Start

```bash
# Run security audit
openclaw security audit

# Deep audit with Gateway probe
openclaw security audit --deep

# Auto-fix common issues
openclaw security audit --fix
```

## What OCSAS Maps

| OSSASAI Control | OpenClaw Feature |
|-----------------|------------------|
| CP-01: Default-Deny Exposure | `gateway.bind: "loopback"` |
| CP-02: Strong Auth | `gateway.auth.mode: "token"` |
| ID-01: Peer Verification | `dmPolicy: "pairing"` |
| ID-02: Session Isolation | `session.dmScope` |
| TB-01: Least Privilege | `agents.list[].tools.allow/deny` |
| TB-03: Sandboxing | `agents.defaults.sandbox.mode` |
| LS-01: Secrets Protection | `~/.openclaw/` permissions |
| LS-02: Log Redaction | `logging.redactSensitive` |
| NS-04: mDNS Security | `discovery.mdns.mode` |

## Assurance Levels

| Level | Name | OpenClaw Configuration |
|-------|------|------------------------|
| **L1** | Local-First | Loopback binding, basic auth, pairing |
| **L2** | Network-Aware | Tailscale/SSH, sandboxing, mention gating |
| **L3** | High-Assurance | Full sandboxing, strict isolation |

## Resources

- **[OpenClaw Profile](profiles/openclaw.md)** - Complete control mappings and verification procedures
- **[OSSASAI Framework](https://github.com/gensecaihq/ossasai)** - Parent security standard specification
- **[OpenClaw Security Docs](https://docs.openclaw.ai/gateway/security)** - Official OpenClaw security documentation
- **[OpenClaw Sandboxing](https://docs.openclaw.ai/gateway/sandboxing)** - Docker-based tool sandboxing guide

## Version

**OCSAS v0.1.0** — January 2026
