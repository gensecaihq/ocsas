---
title: 'Continuous Monitoring'
description: 'Ongoing compliance verification and maintenance'
---

## Overview

Continuous monitoring ensures OSSASAI compliance is maintained over time through automated checks, periodic assessments, and drift detection.

## Monitoring Framework

```
┌─────────────────────────────────────────────────────────────────┐
│                 Continuous Monitoring Layers                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Real-time        │ Invariant checks, security events           │
│  ──────────────────────────────────────────────────────────     │
│  Daily            │ Configuration drift, vulnerability scan     │
│  ──────────────────────────────────────────────────────────     │
│  Weekly           │ Full audit, compliance percentage           │
│  ──────────────────────────────────────────────────────────     │
│  Quarterly        │ Penetration test, policy review             │
│  ──────────────────────────────────────────────────────────     │
│  Annual           │ Full assessment, certification renewal      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Monitoring Schedule

| Activity | Frequency | Automation |
|----------|-----------|------------|
| Invariant verification | Real-time | Automatic |
| Security event monitoring | Real-time | Automatic |
| Configuration drift | Daily | Automatic |
| Dependency scan | Daily | Automatic |
| Full compliance audit | Weekly | Automatic |
| Policy review | Monthly | Manual |
| Penetration test | Quarterly | Manual |
| Full assessment | Annual | Manual + Third-party |

## Automated Monitoring

### CI/CD Integration

```yaml
# .github/workflows/continuous-compliance.yml
name: Continuous Compliance

on:
  schedule:
    - cron: '0 0 * * *'  # Daily
  push:
    paths:
      - 'config/**'
      - 'policies/**'

jobs:
  compliance-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run OSSASAI Audit
        run: ./ossasai-audit.sh --level L2 --output json > report.json
      - name: Check Compliance
        run: |
          score=$(jq '.summary.compliance_percentage' report.json)
          if (( $(echo "$score < 100" | bc -l) )); then
            echo "::error::Compliance dropped to ${score}%"
          fi
      - name: Upload to Dashboard
        run: ./upload-metrics.sh report.json
```

### Drift Detection

```yaml
# drift-detection.yaml
drift_detection:
  enabled: true
  baseline: "/var/lib/ocsas/compliance-baseline.json"

  monitored:
    - type: "configuration"
      paths:
        - "/etc/ocsas/*.yaml"
      alert_on_change: true

    - type: "permissions"
      check: "permission_model"
      alert_on_expansion: true

    - type: "dependencies"
      check: "lockfile_hash"
      alert_on_change: true

  alerts:
    channels:
      - type: "slack"
        webhook: "${SLACK_WEBHOOK}"
      - type: "email"
        recipients: ["security@example.com"]
```

## Key Performance Indicators

| KPI | Target | Threshold |
|-----|--------|-----------|
| Compliance Score | 100% | Alert < 95% |
| Critical Findings | 0 | Alert > 0 |
| Mean Time to Remediate | < 24h | Alert > 48h |
| Configuration Drift Events | 0 unauthorized | Alert > 0 |
| Vulnerability SLA | < 30 days | Alert > 30 days |

## Alerting

```yaml
# alerting-config.yaml
alerts:
  compliance_drop:
    condition: "compliance_percentage < 100"
    severity: "high"
    channels: ["pagerduty", "slack"]

  critical_finding:
    condition: "critical_count > 0"
    severity: "critical"
    channels: ["pagerduty", "email"]

  config_drift:
    condition: "unauthorized_config_change"
    severity: "high"
    channels: ["slack", "email"]

  new_vulnerability:
    condition: "new_high_severity_cve"
    severity: "medium"
    channels: ["slack"]
```

## Compliance Dashboard

Track these metrics:

- Current compliance percentage
- Trend over time
- Control status heatmap
- Open findings by severity
- Mean time to remediate
- Upcoming certification expiry
