from easyprocess import EasyProcess
from configparser import ConfigParser
from pathlib import Path
import os
import shutil

from multiprocessing import Pool
POOL_SIZE = 4


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

PDF_FILES = {
    "pdfreactor": "pdfreactor.pdf",
    "prince": "prince.pdf",
    "antennahouse": "antennahouse.pdf",
    "weasyprint": "weasyprint.pdf",
    "pagedjs": "pagedjs.pdf",
    "typeset.sh": "typeset.pdf",
    "vivliostyle": "vivliostyle.pdf",
    "bfo": "bfo.pdf",
}


def execute(cmd, log_fn):

    print(cmd)
    p = EasyProcess(cmd).call()
    stdout = p.stdout
    stderr = p.stderr
    if p.return_code != 0:
        print("Error in: " + cmd)
        print(stdout)
        print(stderr)

    with open(log_fn, "a") as f:
        f.write("CMD:" + cmd + "\n")
        f.write("Status: " + str(p.return_code) + "\n")
        f.write("Output:\n")
        f.write(stdout + "\n")
        f.write(stderr + "\n")
        f.write("\n")


def process_target(lesson_dir, make_target):
    print(f"Processing {lesson_dir}:{make_target}")

    os.chdir(lesson_dir)

    log_fn = lesson_dir / f"{make_target}.log"
    if log_fn.exists():
        log_fn.unlink()

    cmd = f'make {make_target}'
    execute(cmd, log_fn)

    pdf_fn = lesson_dir / PDF_FILES[make_target]
    if not pdf_fn.exists():
        print(f"PDF file {pdf_fn} not found")
        return

    images_dir = lesson_dir / "images" / make_target
    if images_dir.exists():
        shutil.rmtree(images_dir)
    images_dir.mkdir(parents=True)

    convert_opts = "-density 150 -quality 85"
    convert_opts2 = "+profile icc"
    thumb_opts = "-thumbnail 100x100 -background white -alpha remove"

    # PDF to PNG
    cmd = f'convert {convert_opts} "{pdf_fn}" {convert_opts2} {images_dir}/{make_target}.png'
    execute(cmd, log_fn)

    # PDF to thumbnail PNG
    cmd = f'convert {thumb_opts} "{pdf_fn}" {convert_opts2} {images_dir}/thumb-{make_target}.png'
    execute(cmd, log_fn)


def main():

    cwd = Path(".").resolve()
    for lesson_dir in cwd.glob("lesson-*"):

#        if lesson_dir.name != "lesson-basic":
#            continue

        conversion_ini = lesson_dir / "conversion.ini"
        if not conversion_ini.exists():
            print(f"No {conversion_ini} found")
            continue

        config = ConfigParser()
        config.read(conversion_ini)
        sections = config.sections()

        with Pool(POOL_SIZE) as pool:

            jobs = []

            for target in TARGETS:
                if not target in sections:
                    continue
                make_target = TARGETS[target]
                lesson_directory = cwd / lesson_dir
                jobs.append((lesson_directory, make_target))

            result = pool.starmap(process_target, jobs)
            print(result)
    


if __name__ == "__main__":
    main()
