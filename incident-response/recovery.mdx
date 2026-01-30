---
title: 'Recovery Procedures'
description: 'System recovery and restoration after security incidents'
---

## Overview

Recovery procedures ensure systems are restored to a known-good state after security incidents while preventing recurrence.

## Recovery Priorities

1. **Safety** - Ensure no ongoing threat
2. **Integrity** - Restore from trusted sources
3. **Availability** - Minimize service disruption
4. **Evidence** - Preserve forensic data

## Recovery Procedures

### Level 1: Configuration Restore

For incidents involving configuration tampering:

```bash
# 1. Backup current (compromised) config for forensics
cp /etc/ocsas/config.yaml /var/log/incident/config-compromised.yaml

# 2. Restore from known-good backup
cp /var/backups/ocsas/config-verified.yaml /etc/ocsas/config.yaml

# 3. Verify integrity
./ossasai-audit.sh --verify-config

# 4. Restart service
systemctl restart ocsas
```

### Level 2: Session Purge

For session-related incidents:

```bash
# 1. Terminate all active sessions
ocsas-ctl session terminate --all

# 2. Purge session storage
rm -rf /var/lib/ocsas/sessions/*

# 3. Clear caches
rm -rf /var/cache/ocsas/*

# 4. Restart services
systemctl restart ocsas
```

### Level 3: Credential Rotation

For credential exposure:

```bash
# 1. Generate new credentials
ocsas-ctl credentials rotate --all

# 2. Update dependent services
./update-downstream-credentials.sh

# 3. Revoke old credentials
ocsas-ctl credentials revoke --before $(date -d "1 hour ago" +%s)

# 4. Verify new credentials work
ocsas-ctl health check
```

### Level 4: Full Rebuild

For severe compromise:

```bash
# 1. Backup forensic evidence
./forensic-capture.sh /var/log/incident/

# 2. Terminate service
systemctl stop ocsas

# 3. Wipe and reinstall
rm -rf /opt/ocsas
./install-ocsas.sh --from-trusted-source

# 4. Restore configuration from verified backup
cp /var/backups/ocsas/config-verified.yaml /etc/ocsas/

# 5. Generate new credentials
ocsas-ctl credentials generate --all

# 6. Run full audit before enabling
./ossasai-audit.sh --level L2 --verbose

# 7. Enable service
systemctl start ocsas
```

## Verification Checklist

Before returning to production:

- [ ] All security controls verified functional
- [ ] Audit passes at required level
- [ ] No indicators of compromise remain
- [ ] Monitoring enhanced for recurrence
- [ ] Incident fully documented
- [ ] Root cause addressed

## Backup Requirements

| Data | Frequency | Retention | Verification |
|------|-----------|-----------|--------------|
| Configuration | Daily | 30 days | Hash check |
| Credentials | Per rotation | Previous + current | Test access |
| Audit logs | Continuous | 1 year | Integrity chain |
