# PyShell & File Manager

An extensible, object-oriented CLI file management system written from scratch in Python. The system provides an alternative command paradigm for system traversal, file manipulation, privilege delegation, and resilient user input handling.

## Key Features
- **Role-Based Access Control (RBAC):** Configurable privilege modes (`sudo` vs `user`) with brute-force protection (5-attempt lockouts) and per-operation credential verification on sensitive commands (`rm`, `odw`, `ldf`).
- **Custom Traversal & Command Semantics:**
  - `cd <dir>`: Navigate relative or absolute directories.
  - `ed`: Fast exit/escape to the parent directory.
  - `ldf`: Formatted inspection of directory contents and child nodes.
  - `odw`: Application launcher mapping files to preferred editors (VS Code, NetBeans) or system defaults.
  - `rm`: Context-aware deletion with directory state verification and safety warnings.
  - `cls` & `--help`: Display clearing and self-documenting syntax manual.
- **Fuzzy Search & Auto-Correction:** Identifies closest valid directory names upon typo/invalid input and surfaces candidate paths dynamically.
- **Keystroke Handling:** Native escape-key (`Esc`) listeners to undo user input and safely reset terminal state.
- **OOP Architecture:** Built with clean class inheritance hierarchies to isolate command logic, input listeners, and file system primitives.
