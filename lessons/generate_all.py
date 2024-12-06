#!python3

import os
import shutil
import traceback
import datetime
from configparser import ConfigParser
from multiprocessing import Pool, set_start_method
from pathlib import Path
from typing import List

import typer
from easyprocess import EasyProcess
from loguru import logger as LOG

POOL_SIZE = os.cpu_count()

now = datetime.datetime.now().isoformat()
LOG.add(f"conversion-{now}.log")


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


def execute(cmd, log_fn, verbose=False):

    try:
        return _execute(cmd, log_fn, verbose)
    except Exception as e:
        traceback.print_exc()
        return dict(error=str(e))


def _execute(cmd, log_fn, verbose=False):

    if verbose:
        LOG.info(cmd)

    p = EasyProcess(cmd).call()
    stdout = p.stdout
    stderr = p.stderr
    if p.return_code != 0:
        LOG.info("Error in: " + cmd)
        if verbose:
            LOG.error(stdout)
            LOG.error(stderr)

    with open(log_fn, "a") as f:
        f.write("CMD:" + cmd + "\n")
        f.write("Status: " + str(p.return_code) + "\n")
        f.write("Output:\n")
        f.write(stdout + "\n")
        f.write(stderr + "\n")
        f.write("\n")


def process_target(lesson_dir, make_target, verbose=False):

    os.chdir(lesson_dir)

    LOG.info(f"Processing {lesson_dir}:{make_target}")

    log_fn = lesson_dir / f"{make_target}.log"
    if log_fn.exists():
        log_fn.unlink()

    cmd = f"make {make_target}"
    execute(cmd, log_fn, verbose)

    pdf_fn = lesson_dir / PDF_FILES[make_target]
    if not pdf_fn.exists():
        msg = f"PDF file {pdf_fn} not found"
        LOG.info(msg)
        return dict(error=msg, make_target=make_target, lesson_dir=lesson_dir)

    images_dir = lesson_dir / "images" / make_target
    if images_dir.exists():
        shutil.rmtree(images_dir)
    images_dir.mkdir(parents=True)

    # PDF to PNG
    cmd = f'mutool convert -F png -O resolution=150 -o "{images_dir}/{make_target}.png" "{pdf_fn}"'
    execute(cmd, log_fn, verbose)

    # PDF to thumbnail PNG
    cmd = f'mutool convert -F png -O resolution=150 -O width=100 -O height=100 -o "{images_dir}/thumb-{make_target}.png" "{pdf_fn}"'
    execute(cmd, log_fn, verbose)
    return dict(error=None, make_target=make_target, lesson_dir=lesson_dir)


def main(
    lessons: list[Path] = [],
    verbose: bool = False,
):

    cwd = Path(".").resolve()

    # Remove generated directory
    generated_dir = cwd / "generated"
    if generated_dir.exists():
        EasyProcess(f"git rm -fr {generated_dir}").call()
        if generated_dir.exists():
            shutil.rmtree(generated_dir)
    generated_dir.mkdir(parents=True, exist_ok=True)

    if not lessons:
        lessons = list(cwd.glob("lesson-*"))

    for i, lesson_dir in enumerate(lessons):

        LOG.info(f"{i+1}/{len(lessons)} {lesson_dir}")

        conversion_ini = lesson_dir / "conversion.ini"
        if not conversion_ini.exists():
            LOG.info(f"No {conversion_ini} found")
            continue

        # target directory
        generated_lesson_dir = generated_dir / lesson_dir.name
        if generated_lesson_dir.exists():
            shutil.rmtree(generated_lesson_dir)
        generated_lesson_dir.mkdir(parents=True)

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
                jobs.append((lesson_directory, make_target, verbose))

            result = pool.starmap(process_target, jobs)
            for r in result:
                if r["error"]:
                    LOG.info(f'  ERROR: {r["error"]}')

                # Add generated directory

        # copy PDF
        for target in TARGETS:
            if not target in sections:
                continue
            make_target = TARGETS[target]
            pdf_fn = lesson_dir / PDF_FILES[make_target]
            if pdf_fn.exists():
                shutil.copy(pdf_fn, generated_lesson_dir)

        # copy images
        images_dir = lesson_dir / "images"
        if images_dir.exists():
            shutil.copytree(images_dir, generated_lesson_dir / "images")

    EasyProcess(f"git add {generated_dir}").call()


if __name__ == "__main__":
    typer.run(main)
