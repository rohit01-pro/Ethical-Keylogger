# Ethical-Keylogger

A research and educational project implemented in Python that demonstrates how keystroke-capture techniques work for the purpose of defensive security research, detection, and education.

Important: This repository is intended strictly for lawful, ethical, and authorized uses only — for example, security research on systems you own or manage, defensive tooling development, or classroom/learning environments where all participants have given informed consent. Do not use this project to capture keystrokes from devices or users without explicit permission. Misuse may be illegal and unethical.

## Table of Contents

- Project overview
- Intended use cases
- Key features (high level)
- Safety, legal & ethical notice
- Requirements
- Safe testing & sandboxing
- How to use (installation & usage)
- Development & contribution
- Responsible disclosure & reporting
- License
- Acknowledgments

## Project overview

Ethical-Keylogger is a compact Python project built to help security practitioners, students, and educators explore the concepts behind keystroke capture and monitoring, with the goal of improving defenses, detection rules, and user awareness. It is not meant to be used as a covert surveillance tool.

This repository contains code, examples, and documentation to:

- Demonstrate keystroke capture concepts in a controlled environment
- Provide artifacts (log formats, detection samples) useful for creating IDS/AV rules
- Support safe experiments and detection exercises for defensive teams and instructors

## Intended use cases

- Security research and analysis on systems you own or that you are explicitly authorized to test
- Demonstrations for classroom or training scenarios with full consent of participants
- Generating sample logs and artifacts for developing detection rules and telemetry ingestion pipelines
- Building defensive tooling that recognizes and mitigates keystroke-capture behavior

## Key features (high level)

- Python-based implementation (single-language codebase)
- Configurable logging and output formats for analysis and detection
- Demo/test mode for safe demonstrations in isolated environments
- Lightweight and easy to inspect so it can be used in teaching and code-review settings

## Safety, legal & ethical notice

By using this repository you agree to follow all applicable laws and respect the privacy and consent of others. Before running any code that captures input events:

- Obtain explicit, informed consent from any person whose inputs will be captured.
- Use isolated test systems or virtual machines that are not connected to production networks.
- Do not deploy this code to systems you do not own or administer.
- Follow your organization’s policies and local laws governing security testing and privacy.

The maintainers of this repository are not responsible for misuse. If you are unsure whether a particular use is allowed, consult legal counsel or your organization’s security/privacy team.

## Requirements

- Python 3.8+ (or as specified in the repository)
- Any dependencies are listed in requirements.txt (if present)

Note: Install and run dependencies only in a controlled environment. Prefer using virtual environments (venv, conda) for isolation.

## Safe testing & sandboxing

Always run experiments in a safe environment:

- Use an isolated virtual machine or container specifically provisioned for testing.
- Use demo or test modes included in this project that limit scope and simplify cleanup.
- Keep test data and logs local to the sandbox and securely wipe them after experiments.
- Do not connect the sandbox to production networks or shared directories containing sensitive data.

If you want help creating an isolated testing environment (VM configuration, snapshots, recommended tooling), open an issue and include details about your platform/requirements.

## How to use (installation & usage)

The following usage guide assumes the repository contains a simple Python script or package for demonstration. Adjust filenames and options to match the actual scripts in this repository.

1) Clone the repository (or download a snapshot)

```bash
git clone https://github.com/rohit01-pro/Ethical-Keylogger.git
cd Ethical-Keylogger
```

2) Create and activate an isolated virtual environment
- Linux / macOS:
```bash
python3 -m venv .env
source .env/bin/activate
```
- Windows (PowerShell):
```powershell
python -m venv .env
.\.env\Scripts\Activate.ps1
```

3) Install dependencies (if requirements.txt is present)
```bash
pip install -r requirements.txt
```
If there is no requirements.txt, inspect the repository to see required packages (for example, pynput or keyboard) and install them manually in the venv:
```bash
pip install pynput
```

4) Quick start / demo mode (recommended)
This repository includes a demo/test mode intended for safe, local experimentation. The demo mode restricts runtime behavior and only records synthetic or local test inputs. Replace `keylogger.py` below with the actual script name used in this repo.

```bash
# Example: run the keylogger in demo/test mode, write output to ./logs/demo.log
python keylogger.py --demo --output ./logs/demo.log --duration 60
```

Common options you may find (or add) in the script:
- --demo: enable demo/test mode (limits/filters captured data, no persistent installation)
- --output <path>: write captured events to a log file
- --format <plain|json|csv>: choose output format for easier ingestion
- --duration <seconds>: run for a fixed amount of time then exit (useful for tests)
- --verbose: enable console logging for debugging

If the repository uses a different interface (a package entry-point or a GUI), consult the script headers or README fragments in the repo to find exact option names.

5) Example: run for a short test and stop manually
```bash
# Start a short test (30 seconds), then press Ctrl+C to stop early
python keylogger.py --demo --output ./logs/test1.json --format json --duration 30
```

6) Inspecting logs
- JSON: parse with jq or Python for ingestion into detection tools
```bash
jq . ./logs/test1.json
```
- Plain text: open with a text editor or tail for live viewing
```bash
tail -f ./logs/test1.txt
```

7) Stopping and cleanup
- Most scripts can be stopped with Ctrl+C (SIGINT). The demo/test mode and scripts should flush logs on exit.
- After experiments, securely remove logs if they contain sensitive test data:
```bash
shred -u ./logs/test1.json    # Linux: overwrite then delete
```
Or simply delete in the VM/sandbox and revert the snapshot.

8) Running on different OSes
- Linux: may require running with appropriate permissions to access input devices or using a userspace library such as pynput/keyboard. Prefer demo mode and VMs.
- macOS: additional accessibility permissions may be required for input monitoring. Use a sandbox VM when possible.
- Windows: scripts that use low-level hooks may require administrator privileges; avoid running on production machines.

9) Extending or customizing for defensive testing
- Add configurable filters to limit which keys or windows are recorded
- Use synthetic input generators (in a sandbox) for predictable tests
- Produce structured logs and include context metadata (timestamp, test-id, host-id) to aid detection development
- Keep all enhancements focused on defensive or educational purposes

10) Example minimal Python snippet (safe demo-only pattern)
If you add helper/demo scripts, ensure they document limitations and consent reminders at the top of the file. For teaching, prefer simulated input or recorded sample logs rather than capturing real users.

## Development & contribution

Contributions that improve documentation, detection artifacts, safety features, or defensive use cases are welcome.

Suggested contribution process:
- Fork the repository and create a topic branch for your changes.
- Keep changes focused and include tests/documentation where appropriate.
- Open a pull request that explains the purpose and safety considerations for the change.

Please do not submit changes that facilitate covert deployment, persistence across systems, or obfuscation aimed at evading detection.

## Responsible disclosure & reporting

If you discover a security vulnerability in this project or associated tooling, please follow responsible disclosure practices:

- Create a private security advisory, or
- Open an issue marked as a security/bug report (if public disclosure is appropriate), or
- Contact the maintainer(s) via the email listed in the repository profile

Provide enough detail to reproduce and remediate the issue. Do not post exploit details publicly until a fix is available and coordinated disclosure is completed.

## License

See the LICENSE file in the repository for licensing information. If there is no LICENSE file, please contact the repository owner to clarify permitted uses.

## Acknowledgments

Thanks to all contributors who help keep this project focused on safe, ethical, and educational use. This project is intended to foster better defensive tools and understanding — if you have ideas for improving its educational value or safety controls, please contribute.
