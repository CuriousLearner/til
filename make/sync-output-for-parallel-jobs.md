# Improve `make` Output Readability with `--output-sync` for Parallel Jobs

When using parallel builds (`make -j`), the output from multiple jobs can get mixed, making logs difficult to follow. The `--output-sync` flag helps organize output for better readability.

## 🔥 Available `--output-sync` Options

```bash
make -j$(nproc) --output-sync=[MODE]
```

📌 Modes:

- `none` (default) – No synchronization, output may be interleaved.
- `line` – Ensures each line of output is completed before switching jobs.
- `target` – Groups output per target (useful for debugging).
- `recurse` – Like target, but also applies to recursive make calls.

## 🚀 Example: Using `--output-sync=target`

```bash
make -j$(nproc) --output-sync=target
```

This keeps output of each target together & avoids mixing logs from multiple jobs. It makes errors easier to trace and improves readability in CI/CD pipelines.

## 🔥 Example Makefile

```bash
NPROC := $(shell if command -v nproc >/dev/null; then nproc; else sysctl -n hw.ncpu; fi)

all:
	@echo "Building with $(NPROC) jobs..."
	make -j$(NPROC) --output-sync=target build

build:
	@echo "Building target..."
	sleep 1
	@echo "Done!"
```
