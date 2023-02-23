from pathlib import Path
import os
from configparser import ConfigParser
from easyprocess import EasyProcess


TARGETS = {
    "PDFreactor": "pdfreactor",
    "PrinceXML": "prince",
    "Antennahouse": "antennahouse",
    "Weasyprint": "weasyprint",
    "PagedJS": "pagedjs",
    "Typeset.sh": "typeset.sh",
    "Vivliostyle": "vivliostyle",
    "BFO": "bfo",
}

def process_target(lesson_dir, make_target):
    print(f"Processing {lesson_dir}:{make_target}")

    os.chdir(lesson_dir)
    cmd =f'make {make_target}'
    p = EasyProcess(cmd).call()
    stdout = p.stdout
    stderr = p.stderr
    log_fn = lesson_dir / f"{make_target}.log"
    if p.return_code != 0:
        print("Error in " + cmd)
        print(stdout)
        print(stderr)

    with open(log_fn, "w") as f:
        f.write(cmd + "\n")
        f.write("Status: " + str(p.return_code) + "\n")
        f.write("Output:\n")
        f.write(stdout)
        f.write(stderr)

def main():

    cwd = Path(".").resolve()
    for lesson_dir in cwd.glob("lesson-*"):
        if lesson_dir.name !=  "lesson-basic":
            continue

        conversion_ini = lesson_dir / "conversion.ini"
        if not conversion_ini.exists():
            print(f"No {conversion_ini} found")
            continue

        config = ConfigParser()
        config.read(conversion_ini)
        sections = config.sections()

        for target in TARGETS:
            if not target in sections:
                continue
            make_target = TARGETS[target]
            lesson_directory = cwd / lesson_dir
            process_target(lesson_directory, make_target)


if  __name__ == "__main__":
    main()