# OCSAS - OpenClaw Security Assurance Standard

[![OSSASAI Profile](https://img.shields.io/badge/OSSASAI-v0.1-blue)](https://github.com/gensecaihq/ossasai)
[![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-0.1.0-orange)](CHANGELOG.md)

**OCSAS** is the official [OSSASAI](https://github.com/gensecaihq/ossasai) implementation profile for [OpenClaw](https://openclaw.ai) — a multi-platform AI agent gateway for WhatsApp, Telegram, Discord, iMessage, and Slack with shell, filesystem, and browser access.

## How This Framework Works

> **Important:** OpenClaw is not maintained by us. OCSAS is an **external compliance framework** that documents OpenClaw's existing security features — it does not require any changes to OpenClaw itself.

### The Relationship

```
┌─────────────────────────────────────────────────────────────────────┐
│                      OpenClaw (Third-Party Product)                  │
│                                                                      │
│  Already has: openclaw security audit, dmPolicy, sandbox,           │
│               gateway.auth, and all security features we document    │
│                                                                      │
│  Does NOT know about OCSAS/OSSASAI — and doesn't need to            │
└─────────────────────────────────────────────────────────────────────┘
                              ▲
                              │ We observe & document
                              │
┌─────────────────────────────────────────────────────────────────────┐
│                    OCSAS (This Repository)                           │
│                                                                      │
│  • Maps OpenClaw's existing features to OSSASAI security controls   │
│  • Provides compliance checklists for auditors                       │
│  • Gives users structured deployment guidance                        │
│  • Uses OpenClaw's own CLI for verification                          │
└─────────────────────────────────────────────────────────────────────┘
```

### Analogy: Industry Standards

| Standard | Target Software | Does Software Know About It? |
|----------|----------------|------------------------------|
| CIS Ubuntu Benchmark | Ubuntu Linux | No - CIS documents existing settings |
| OWASP ASVS | Any web app | No - ASVS verifies existing features |
| PCI-DSS | Payment systems | No - auditors check existing configs |
| **OCSAS** | **OpenClaw** | **No - we document existing features** |

### What OCSAS Does

1. **Documentation Layer** - Maps OpenClaw features to security controls
2. **Verification** - Uses OpenClaw's own CLI (`openclaw security audit`)
3. **Compliance Evidence** - Structured output for auditors
4. **Deployment Guidance** - L1/L2/L3 conformance recipes

### Who Uses OCSAS?

| User | How They Use OCSAS |
|------|-------------------|
| **OpenClaw users** | Deployment checklists, hardening guides |
| **Security auditors** | Compliance verification framework |
| **Enterprises** | Risk assessment, vendor due diligence |
| **Regulators** | Structured security evaluation criteria |

---

## Overview

OCSAS maps OSSASAI's 24 security controls to OpenClaw's built-in security features, providing structured verification for secure AI agent deployments.

```
OSSASAI (Framework)          OCSAS (This Profile)           OpenClaw (Platform)
─────────────────────        ────────────────────           ───────────────────
24 Security Controls    →    Control Mappings          →    CLI & Config
L1/L2/L3 Levels         →    Conformance Recipes       →    Security Audit
Trust Boundaries        →    Verification Steps        →    Built-in Features
```

## Quick Start

### Step 1: Install OpenClaw (if not already installed)

```bash
curl -fsSL https://openclaw.bot/install.sh | bash
openclaw onboard --install-daemon
```

### Step 2: Verify Security Baseline

```bash
# Health check
openclaw health

# Security audit (uses OpenClaw's built-in auditor)
openclaw security audit --deep

# Auto-fix common issues
openclaw security audit --fix

# Check sandbox configuration
openclaw sandbox explain
```

### Step 3: Choose Your Assurance Level

| Level | Name | When to Use | Key Config |
|-------|------|-------------|------------|
| **L1** | Local-First | Single-user, development | Loopback + auth + pairing |
| **L2** | Network-Aware | Teams, LAN/Tailnet | L1 + sandboxing + isolation |
| **L3** | High-Assurance | Production, regulated | L2 + all sandboxed + mDNS off |

### Step 4: Apply Configuration

**L1 Baseline:**
```json5
{
  gateway: { bind: "loopback", auth: { mode: "token", token: "your-token" } },
  channels: { whatsapp: { dmPolicy: "pairing" } }
}
```

**L2 Additions:**
```json5
{
  session: { dmScope: "per-channel-peer" },
  agents: { defaults: { sandbox: { mode: "non-main" } } },
  channels: { whatsapp: { groups: { "*": { requireMention: true } } } }
}
```

**L3 Additions:**
```json5
{
  agents: { defaults: { sandbox: { mode: "all", workspaceAccess: "none" } } },
  discovery: { mdns: { mode: "off" } }
}
```

### Step 5: Verify Continuously

```bash
openclaw security audit --deep  # Run regularly after config changes
```

---

## Control Mappings

| OSSASAI Control | OpenClaw Implementation |
|-----------------|-------------------------|
| **CP-01** Default-Deny Exposure | `gateway.bind: "loopback"` |
| **CP-02** Strong Authentication | `gateway.auth.mode: "token"` |
| **ID-01** Peer Verification | `dmPolicy: "pairing"` |
| **ID-02** Session Isolation | `session.dmScope: "per-channel-peer"` |
| **TB-01** Least Privilege Tools | `agents.list[].tools.allow/deny` |
| **TB-03** Sandboxing | `agents.defaults.sandbox.mode: "non-main"` |
| **LS-01** Secrets at Rest | `~/.openclaw/` permissions (700/600) |
| **LS-02** Log Redaction | `logging.redactSensitive: "tools"` |
| **NS-04** mDNS Security | `discovery.mdns.mode: "minimal"` |

[View complete mappings →](profiles/openclaw.mdx)

---

## Assurance Level Checklists

### L1 Checklist (Local-First)

```bash
openclaw security audit --deep
```

- [ ] Gateway bound to loopback (`gateway.bind: "loopback"`)
- [ ] Gateway auth configured (token or password)
- [ ] DM policy set to `pairing` or `allowlist`
- [ ] File permissions correct (`~/.openclaw/` = 700, config = 600)
- [ ] Log redaction enabled (`logging.redactSensitive: "tools"`)

### L2 Checklist (includes L1)

- [ ] Session isolation configured (`session.dmScope`)
- [ ] Mention gating enabled for groups (`requireMention: true`)
- [ ] Sandboxing enabled for non-main sessions
- [ ] Elevated exec restricted (`tools.elevated.allowFrom`)
- [ ] Trusted proxies configured (if using reverse proxy)

### L3 Checklist (includes L2)

- [ ] Strictest session isolation (`per-account-channel-peer`)
- [ ] All sessions sandboxed (`sandbox.mode: "all"`)
- [ ] No workspace access from sandbox (`workspaceAccess: "none"`)
- [ ] mDNS discovery disabled (`mdns.mode: "off"`)

---

## Evidence Generation

Generate compliance evidence for auditors using OpenClaw's own tools:

```bash
mkdir -p evidence

# Security audit report
openclaw security audit --deep 2>&1 | tee evidence/audit-report.txt

# System status (secrets redacted)
openclaw status --all > evidence/status-redacted.txt

# Sandbox configuration
openclaw sandbox explain > evidence/sandbox-config.txt

# File permissions
ls -la ~/.openclaw/ > evidence/permissions.txt
stat -c "%a %n" ~/.openclaw/* >> evidence/permissions.txt
```

---

## Documentation

| Document | Description |
|----------|-------------|
| [profiles/openclaw.mdx](profiles/openclaw.mdx) | Complete control mappings and conformance recipes |
| [CHANGELOG.md](CHANGELOG.md) | Version history |
| [SECURITY.md](SECURITY.md) | Security policy |

## Related Projects

| Project | Description |
|---------|-------------|
| [OSSASAI](https://github.com/gensecaihq/ossasai) | Parent security framework (vendor-neutral) |
| [OpenClaw](https://openclaw.ai) | AI agent gateway platform (third-party) |
| [OpenClaw Security Docs](https://docs.openclaw.ai/gateway/security) | Official security documentation |

## Contributing

Contributions welcome. Please ensure:

1. Changes align with OSSASAI framework structure
2. All claims are verified against actual OpenClaw documentation
3. No placeholder, fictional, or assumed information
4. Use OpenClaw's existing CLI commands for verification steps

## License

[Apache License 2.0](LICENSE)

---

**OCSAS v0.1.0** | [OSSASAI](https://github.com/gensecaihq/ossasai) Profile | [OpenClaw](https://openclaw.ai)
