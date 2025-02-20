# Control `make` Behavior with `MAKEFLAGS`

`MAKEFLAGS` is an environment variable that lets you set default options for `make`, avoiding the need to specify them every time.

## 🔥 Usage

Instead of running:

```bash
make -j$(nproc) --output-sync=target
```

You can set `MAKEFLAGS` once:

```bash
export MAKEFLAGS="-j$(nproc) --output-sync=target"
make
```

## 📌 Common MAKEFLAGS Options
* `-jN` → Run N parallel jobs (-j$(nproc) uses all CPU cores).
* `--output-sync=target` → Keeps target outputs grouped.
* `-s` → Silent mode (no command output).
* `-k` → Keep going even if some targets fail.
* `--warn-undefined-variables` → Debug undefined variables.

## 🚀 Example Makefile

```make
MAKEFLAGS += --warn-undefined-variables --environment-overrides --output-sync=target

all:
	@echo "Building with $(MAKEFLAGS)..."
	make build

build:
	@echo "Compiling..."
	sleep 1
	@echo "Done!"
```

would run as:

```sh
make
```

and output

```bash
Building with  --warn-undefined-variables -e...
make build
Compiling...
sleep 1
Done!
```

`MAKEFLAGS` helps streamline make commands for faster and cleaner builds! 🚀🔥
