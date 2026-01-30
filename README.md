# OCSAS - OpenClaw Security Assurance Standard

[![OSSASAI Profile](https://img.shields.io/badge/OSSASAI-v0.1-blue)](https://github.com/gensecaihq/ossasai)
[![License](https://img.shields.io/badge/License-Apache%202.0-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-0.1.0-orange)](CHANGELOG.md)

**OCSAS** is a security checklist and hardening guide for [OpenClaw](https://openclaw.ai) users. It helps you deploy OpenClaw safely by telling you exactly what settings to configure and how to verify your setup is secure.

---

## What Is This? (Simple Explanation)

Think of OCSAS like a **car safety checklist**:

```
You buy a car (OpenClaw)
       ↓
The car has seatbelts, airbags, ABS (security features)
       ↓
OCSAS is the checklist that says:
  ✓ "Make sure seatbelt is fastened"
  ✓ "Check airbags are enabled"
  ✓ "Verify ABS light is off"
       ↓
You follow the checklist → You're safer
```

**OCSAS doesn't change OpenClaw.** It just documents:
- What security features OpenClaw already has
- How to turn them on
- How to verify they're working

---

## Why Should I Care? (Benefits for Normal Users)

### Without OCSAS

```
Install OpenClaw → Hope default settings are secure → ???
```

### With OCSAS

```
Install OpenClaw → Follow OCSAS checklist → Know exactly what's protected
```

### Real Benefits

| Benefit | What It Means For You |
|---------|----------------------|
| **Don't get hacked** | Checklist prevents common security mistakes |
| **Sleep better** | Know your AI agent can't be abused by strangers |
| **Quick setup** | Copy-paste secure configs instead of guessing |
| **Prove compliance** | Show your boss/auditor your setup is secure |

---

## How To Use This (Step-by-Step)

### Step 1: Install OpenClaw (if you haven't)

```bash
curl -fsSL https://openclaw.bot/install.sh | bash
openclaw onboard --install-daemon
```

### Step 2: Run the Security Check

OpenClaw has a built-in security auditor. Run it:

```bash
openclaw security audit --deep
```

This will show you what's secure and what needs fixing.

### Step 3: Auto-Fix Common Issues

```bash
openclaw security audit --fix
```

This automatically:
- Fixes file permissions
- Enables log redaction
- Tightens group policies

### Step 4: Pick Your Security Level

| Level | You Are... | Time to Setup |
|-------|-----------|---------------|
| **L1** | Solo user, running locally | 5 minutes |
| **L2** | Team user, sharing over network | 15 minutes |
| **L3** | Enterprise, needs compliance proof | 30 minutes |

### Step 5: Apply the Config for Your Level

#### L1: Just Me, On My Computer

Copy this to `~/.openclaw/openclaw.json`:

```json5
{
  // Only allow connections from this computer
  gateway: {
    bind: "loopback",
    auth: { mode: "token", token: "generate-a-random-string-here" }
  },

  // Require approval before responding to new contacts
  channels: {
    whatsapp: { dmPolicy: "pairing" }
  }
}
```

**What this does:**
- `bind: "loopback"` → Only your computer can talk to the bot
- `auth: { mode: "token" }` → Requires password to control the bot
- `dmPolicy: "pairing"` → Strangers can't message your bot without approval

#### L2: My Team, Over Network

Add these to your L1 config:

```json5
{
  // Keep different users' conversations separate
  session: { dmScope: "per-channel-peer" },

  // Only respond when @mentioned in groups
  channels: {
    whatsapp: {
      dmPolicy: "pairing",
      groups: { "*": { requireMention: true } }
    }
  },

  // Run risky commands in a container (safer)
  agents: {
    defaults: {
      sandbox: { mode: "non-main" }
    }
  }
}
```

**What this does:**
- `dmScope: "per-channel-peer"` → User A can't see User B's conversations
- `requireMention: true` → Bot ignores group messages unless @mentioned
- `sandbox: { mode: "non-main" }` → Commands run in isolated container

#### L3: Enterprise / Compliance Required

Add these to your L2 config:

```json5
{
  // Maximum isolation
  session: { dmScope: "per-account-channel-peer" },

  // Sandbox everything
  agents: {
    defaults: {
      sandbox: {
        mode: "all",
        workspaceAccess: "none"
      }
    }
  },

  // Don't broadcast presence on network
  discovery: { mdns: { mode: "off" } }
}
```

### Step 6: Verify It Worked

```bash
# Run the audit again
openclaw security audit --deep

# Check your status
openclaw health
openclaw status --all
```

---

## Quick Reference: Security Checklist

Print this out and check off each item:

### Basic Security (Everyone Should Do This)

- [ ] **Gateway auth enabled** → Run: `grep -q "auth" ~/.openclaw/openclaw.json`
- [ ] **DM pairing on** → Strangers need approval to message bot
- [ ] **File permissions correct** → Run: `ls -la ~/.openclaw/` (should show `drwx------`)
- [ ] **Log redaction on** → Secrets not written to log files

### Team Security (Multiple Users)

- [ ] **Session isolation on** → Users can't see each other's chats
- [ ] **Mention gating on** → Bot only responds when @mentioned in groups
- [ ] **Sandboxing on** → Commands run in containers

### Enterprise Security (Compliance/Audit)

- [ ] **All sessions sandboxed** → Every command is isolated
- [ ] **mDNS discovery off** → Bot doesn't advertise itself on network
- [ ] **Workspace access disabled** → Sandbox can't reach your files

---

## Common Questions

### "I'm not technical. Can I still use this?"

Yes! Just run these three commands:

```bash
openclaw onboard --install-daemon    # Setup wizard
openclaw security audit --fix        # Auto-fix issues
openclaw security audit --deep       # Verify it worked
```

The wizard and auto-fix handle most security settings for you.

### "What if I mess up the config?"

Reset to defaults:

```bash
# Backup current config
cp ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.backup

# Start fresh with the wizard
openclaw onboard
```

### "How do I know if I'm secure?"

Run the audit:

```bash
openclaw security audit --deep
```

If it shows no warnings, you're good. If it shows warnings, either:
- Run `--fix` to auto-fix them
- Follow the warning's instructions to fix manually

### "What does 'pairing' mean?"

When someone new messages your bot:
1. Bot sends them a short code (like `ABC123`)
2. You approve or deny the code
3. Only approved people can use the bot

```bash
# See pending requests
openclaw pairing list whatsapp

# Approve someone
openclaw pairing approve whatsapp ABC123
```

### "What's sandboxing?"

Instead of running commands directly on your computer, they run inside a container (like a virtual computer). If something goes wrong, it can't damage your real files.

---

## How This Framework Works (Technical Details)

<details>
<summary>Click to expand technical explanation</summary>

### Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                      OpenClaw (Third-Party Product)                  │
│                                                                      │
│  Has built-in security: dmPolicy, sandbox, gateway.auth, etc.       │
│  Has built-in auditor: openclaw security audit                       │
│                                                                      │
│  Does NOT know about OCSAS — doesn't need to                        │
└─────────────────────────────────────────────────────────────────────┘
                              ▲
                              │ We document & organize
                              │
┌─────────────────────────────────────────────────────────────────────┐
│                    OCSAS (This Documentation)                        │
│                                                                      │
│  • Maps OpenClaw features to security controls                      │
│  • Provides checklists for different security levels                │
│  • Uses OpenClaw's own CLI for verification                          │
│  • Similar to CIS Benchmarks or OWASP ASVS                          │
└─────────────────────────────────────────────────────────────────────┘
```

### OCSAS is like...

| Standard | What It Documents | Does Target Know About It? |
|----------|-------------------|---------------------------|
| CIS Ubuntu Benchmark | Ubuntu security settings | No |
| OWASP ASVS | Web app security | No |
| **OCSAS** | **OpenClaw security** | **No** |

### Control Mapping

| OCSAS Control | What It Protects | OpenClaw Setting |
|---------------|------------------|------------------|
| CP-01 | Network exposure | `gateway.bind: "loopback"` |
| CP-02 | Admin access | `gateway.auth.mode: "token"` |
| ID-01 | Unknown senders | `dmPolicy: "pairing"` |
| ID-02 | User isolation | `session.dmScope` |
| TB-03 | Command safety | `sandbox.mode` |
| LS-01 | Secret files | File permissions (700/600) |

</details>

---

## Get Help

- **OpenClaw Docs**: https://docs.openclaw.ai/gateway/security
- **OSSASAI Framework**: https://github.com/gensecaihq/ossasai
- **Report Security Issues**: See [SECURITY.md](SECURITY.md)

---

## License

[Apache License 2.0](LICENSE)

---

**OCSAS v0.1.0** | Security checklist for [OpenClaw](https://openclaw.ai) users
