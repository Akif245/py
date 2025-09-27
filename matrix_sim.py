# # fake_hack.py
# import time
# import random
# import sys
# import os

# loading = ["|", "/", "-", "\\"]
# spinner_len = len(loading)

# def progress_scan(total=100, step=1, delay=0.05):
#     """Show a nicer percent progress bar with spinner."""
#     for i in range(0, total + 1, step):
#         spinner = loading[(i // step) % spinner_len]
#         bar_len = 30
#         filled = int(bar_len * i / total)
#         bar = "[" + "#" * filled + "-" * (bar_len - filled) + "]"
#         sys.stdout.write(f"\r🔎 Scanning {bar} {i:3d}% {spinner}")
#         sys.stdout.flush()
#         time.sleep(delay)
#     print()  # newline

# def print_slow(lines, delay=0.8):
#     for line in lines:
#         print(line)
#         time.sleep(delay)

# def make_fake_report(target, items):
#     fname = f"fake_report_{target.replace(' ', '_')}.txt"
#     with open(fname, "w", encoding="utf-8") as f:
#         f.write(f"Report for target: {target}\n")
#         f.write(f"Generated: {time.ctime()}\n\n")
#         for it in items:
#             f.write(f"- {it}\n")
#     return fname

# def main():
#     target = input("Enter target name (for simulation only): ").strip() or "unknown_device"
#     print(f"\n🔌 Connecting to {target}...")
#     time.sleep(1.2)

#     # Simulated scanning
#     progress_scan(total=100, step=2, delay=0.03)

#     print("\n🔁 Establishing secure channel...")
#     for _ in range(6):
#         sys.stdout.write(random.choice(loading))
#         sys.stdout.flush()
#         time.sleep(0.18)
#     print("\n")

#     # Fake retrieved data
#     data = [
#         "📞 Call Logs Accessed",
#         "💬 Messages Retrieved",
#         "🖼️ Gallery Synced",
#         "🌐 Browsing History Loaded",
#         "🔑 Saved Passwords Extracted"
#     ]

#     print_slow([f"✔ {d}..." for d in data], delay=0.9)

#     print("\n✅ Access Granted to Target Mobile (SIMULATED)")
#     report_file = make_fake_report(target, data)
#     print(f"🗂️  Fake report saved as: {os.path.abspath(report_file)}")

# if __name__ == "__main__":
#     main()


# matrix_sim.py
import sys
import time
import random
import os
import shutil

# Attempt to enable ANSI escape codes on Windows consoles
def enable_ansi_on_windows():
    if os.name != "nt":
        return
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE = -11
        mode = ctypes.c_uint32()
        if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            ENABLE_VT_PROCESSING = 0x0004
            new_mode = mode.value | ENABLE_VT_PROCESSING
            kernel32.SetConsoleMode(handle, new_mode)
    except Exception:
        pass

# Basic progress bar + spinner
loading = ["|", "/", "-", "\\"]

def progress_scan(total=100, step=2, delay=0.03):
    spinner_len = len(loading)
    bar_len = 40
    for i in range(0, total + 1, step):
        spinner = loading[(i // step) % spinner_len]
        filled = int(bar_len * i / total)
        bar = "[" + "#" * filled + "-" * (bar_len - filled) + "]"
        sys.stdout.write(f"\rScanning device {bar} {i:3d}% {spinner}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def typing_effect(lines, char_delay=0.02, line_delay=0.6):
    for line in lines:
        for ch in line:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(char_delay)
        print()
        time.sleep(line_delay)

def make_fake_report(target, items):
    fname = f"fake_report_{target.replace(' ', '_')}.txt"
    with open(fname, "w", encoding="utf-8") as f:
        f.write(f"Report for target: {target}\n")
        f.write(f"Generated: {time.ctime()}\n\n")
        for it in items:
            f.write(f"- {it}\n")
    return fname

# Matrix rain animation
def matrix_rain(duration_seconds=12, fps=20):
    # Characters used in rain
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@#$%&*+-=<>"
    term = shutil.get_terminal_size((80, 24))
    cols = term.columns
    rows = term.lines

    # Initialize drop positions for each column (y coordinate of head) and speed
    drops = [random.randint(-rows, 0) for _ in range(cols)]
    speeds = [random.uniform(0.2, 1.0) for _ in range(cols)]  # relative speed
    last_update = [time.time() for _ in range(cols)]
    frame_sleep = 1.0 / fps
    end_time = time.time() + duration_seconds

    GREEN = "\033[32m"
    BRIGHT_GREEN = "\033[92m"
    RESET = "\033[0m"
    CLEAR_SCREEN = "\033[2J"
    CURSOR_HOME = "\033[H"

    try:
        sys.stdout.write(CLEAR_SCREEN)
        while time.time() < end_time:
            buffer_lines = [" " * cols for _ in range(rows)]
            tnow = time.time()

            for c in range(cols):
                # update this column position based on its speed
                if tnow - last_update[c] >= (0.05 * (1.2 - speeds[c])):  # faster speed -> smaller wait
                    drops[c] += 1
                    last_update[c] = tnow

                    # Sometimes reset drop to start above the screen again
                    if drops[c] > rows + random.randint(0, rows // 2):
                        drops[c] = random.randint(-rows, 0)
                        speeds[c] = random.uniform(0.2, 1.0)

                head = drops[c]
                trail_len = int(6 + speeds[c] * 10)  # length of trailing characters

                # For each position in the column, decide if a char appears
                for t in range(trail_len):
                    y = head - t
                    if 0 <= y < rows:
                        # stronger brightness at the head
                        ch = random.choice(chars)
                        line = buffer_lines[y]
                        # replace character at column c
                        buffer_lines[y] = line[:c] + ch + line[c+1:]

            # Render buffer_lines with color: bright head + green trail
            out = [CURSOR_HOME]
            for r, line in enumerate(buffer_lines):
                # To slightly mimic head brightness, we could randomly brighten some chars
                rendered = []
                for c, ch in enumerate(line):
                    if ch == " ":
                        rendered.append(" ")
                    else:
                        # small chance to be bright (the head positions are random so it looks varied)
                        if random.random() < 0.12:
                            rendered.append(BRIGHT_GREEN + ch + RESET)
                        else:
                            rendered.append(GREEN + ch + RESET)
                out.append("".join(rendered))
            sys.stdout.write("\n".join(out))
            sys.stdout.flush()
            time.sleep(frame_sleep)
    except KeyboardInterrupt:
        # Allow user to stop early with Ctrl+C
        pass
    finally:
        # Reset colors and move cursor below animation
        sys.stdout.write(RESET + "\n")
        sys.stdout.flush()

def main():
    enable_ansi_on_windows()

    try:
        target = input("Enter target name (simulation only): ").strip() or "unknown_device"
    except Exception:
        # Non-interactive environment: default target
        target = "unknown_device"

    print(f"\nConnecting to {target}...")
    time.sleep(1.0)

    progress_scan(total=100, step=2, delay=0.02)

    print("\nEstablishing secure channel...")
    for _ in range(20):
        sys.stdout.write(random.choice(["|", "/", "-", "\\"]))
        sys.stdout.flush()
        time.sleep(0.08)
        sys.stdout.write("\b")
    print("\n")

    data = [
        "Call logs accessed...",
        "Messages retrieved...",
        "Gallery synced...",
        "Browsing history loaded...",
        "Saved passwords extracted..."
    ]

    typing_effect(data, char_delay=0.01, line_delay=0.6)

    print("\nAccess granted to target (SIMULATION)\n")
    report = make_fake_report(target, data)
    print(f"Fake report saved as: {os.path.abspath(report)}")
    # print("\nStarting Matrix-style animation. Press Ctrl+C to stop early.\n")
    time.sleep(0.8)

    # Run matrix rain for N seconds
    matrix_rain(duration_seconds=5, fps=25)

    

if __name__ == "__main__":
    main()
