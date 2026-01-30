---
layout: default
title: Home
nav_order: 1
permalink: /
---

# OCSAS - OpenClaw Security Assurance Standard

**OCSAS** is a security checklist and hardening guide for [OpenClaw](https://openclaw.ai) users. It helps you deploy OpenClaw safely by telling you exactly what settings to configure and how to verify your setup is secure.

---

## What Is This?

Think of OCSAS like a **car safety checklist**:

```
You buy a car (OpenClaw)
       |
The car has seatbelts, airbags, ABS (security features)
       |
OCSAS is the checklist that says:
  - "Make sure seatbelt is fastened"
  - "Check airbags are enabled"
  - "Verify ABS light is off"
       |
You follow the checklist - You're safer
```

**OCSAS doesn't change OpenClaw.** It just documents:
- What security features OpenClaw already has
- How to turn them on
- How to verify they're working

---

## Quick Start

### Step 1: Run the Security Check

OpenClaw has a built-in security auditor:

```bash
openclaw security audit --deep
```

### Step 2: Auto-Fix Common Issues

```bash
openclaw security audit --fix
```

### Step 3: Verify It Worked

```bash
openclaw health
openclaw status --all
```

---

## Security Levels

| Level | You Are... | Time to Setup |
|-------|-----------|---------------|
| **L1** | Solo user, running locally | 5 minutes |
| **L2** | Team user, sharing over network | 15 minutes |
| **L3** | Enterprise, needs compliance proof | 30 minutes |

---

## Quick Reference

### What OCSAS Maps

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

---

## Documentation

- [Introduction](docs/introduction.md) - Overview and getting started
- [OpenClaw Profile](docs/profiles/openclaw.md) - Complete control mappings and verification procedures

---

## Resources

- [OpenClaw Security Docs](https://docs.openclaw.ai/gateway/security) - Official OpenClaw security documentation
- [OpenClaw Sandboxing](https://docs.openclaw.ai/gateway/sandboxing) - Docker-based tool sandboxing guide
- [OSSASAI Framework](https://github.com/gensecaihq/ossasai) - Parent security standard specification

---

## License

[Apache License 2.0](LICENSE)

---

**OCSAS v0.1.0** - January 2026
