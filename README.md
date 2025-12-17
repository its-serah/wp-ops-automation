# wp-ops-automation

WordPress automation toolkit boilerplate.

## Overview

This project is set up as a Python-based automation toolkit for WordPress. It is designed to support:

- Browser automation for the WordPress admin (e.g. login, publishing posts).
- API automation via the WordPress REST API.
- Reusable tasks that you can orchestrate from a CLI.

## Getting started

1. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy the example environment file and fill in your WordPress settings:

```bash
cp .env.example .env
```

4. Run the CLI help to see available commands:

```bash
python -m wp_ops_automation.cli --help
```

## Next steps

- Add concrete tasks in `wp_ops_automation/tasks/` (e.g. publish_post, bulk_update_meta).
- Extend `wp_ops_automation/browser.py` and `wp_ops_automation/api.py` with real automation logic.
- Wire up more CLI commands in `wp_ops_automation/cli.py`.

