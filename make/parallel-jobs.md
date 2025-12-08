# Speed Up Builds with `make -j` and Auto-Detect CPU Cores

Parallelizing `make` builds can significantly reduce compile time. You can dynamically set the number of jobs based on available CPU cores.

## Example Makefile

```make
# Detect number of available CPU cores
NPROC := $(shell if command -v nproc >/dev/null; then nproc; else sysctl -n hw.ncpu; fi)
# Use half the cores to avoid system overload
NPROC_LIMIT := $(shell expr $(NPROC) / 2)

all:
	@echo "Building with $(NPROC_LIMIT) jobs..."
	make -j$(NPROC_LIMIT) target
```

This `Makefile` dynamically sets the number of jobs to half the available CPU cores. You can adjust the `NPROC_LIMIT` variable to suit your system. Now, your builds will run faster by utilizing multiple cores.

The expression:

```bash
$(shell if command -v nproc >/dev/null; then nproc; else sysctl -n hw.ncpu; fi)
```

makes sure the CPU cores are fetched using `nproc` command if available on Linux systems. If not, it falls back to using `sysctl -n hw.ncpu` on macOS.
