.. image:: /static/pixel.png
    :class: one-pixel

Contributing
============

The print-css.rocks project is an open platform for spreading the word about
"CSS Paged Media" and "Print CSS". Feel to contribute further lessons and
showcases, pointers to documentation and resource etc.  You can either contact
me directly or you fork the project on Github and see me some pull requests.
print-css.rocks is supposed to be a living and growing project for the Print
CSS community.

Setting up your own environment
-------------------------------

You need a decent Python 3 installation (Python 3.7 or higher) for installing the print-css.rocks setup
locally. It might be necessary to installed the `libxml2` and `libxslt` packages on Linux (including
their dev packages) or using Homebrew on MacOSX.

.. code-block:: shell

    > python3 --version
      Python 3.7.2

Clone the print-css-rocks repository:

.. code-block:: shell

    > git clone git@github.com:zopyx/print-css-rocks.git

Install the local webservice:

.. code-block:: shell

    > cd web
    > python3 -m venv .
    > source bin/activate
    > pip install -r requirements.txt

Run the web service on http://localhost:8000.

The environment variable `LESSONS_DIR` must point to the root
of the `lessons` directory of your checkout.



.. code-block:: shell

    > export LESSON_DIR=../lessons  # or
    > export LESSON_DIR=/path/to/print-css-rocks/lessons 
    > bin/python server.py

Now you can access the web service aka your local print-css-rocks copy  on
http://localhost:8000. 

Creating your own lessons
-------------------------

All lessons are located inside the `lessons` subfolder and must start with the prefix `lesson-`.
For an example check out `lesson-basic`. The example HTML content must be placed inside the `index.html` file
and the styles must be stored in `styles.css`. A lesson must also contain a file `README.rst` which contains a textual
description of the lesson. The format of the file is Restructured Text (http://docutils.sourceforge.net/rst.html).

The lesson must contain a `Makefile` which usually references a generic `Makefile` on the `lessons` folder. It usually contains
only the following line:

.. code-block::

   include ../Makefile

The manually checked conversion results are stored in the `conversion.ini` file
which contains for each supported converter a dedicated section like


.. code-block::


   [common]
   category = intro
   title = Lesson on ....

   [PDFreactor]
   status = OK
   pdf = pdfreactor.pdf
   message =

   [PrinceXML]
   status = OK
   pdf = prince.pdf
   message =

   [Antennahouse]
   status = OK
   pdf = antennahouse.pdf
   message =

The section keys 

- `PDFreactor` 
- `PrinceXML` 
- `Antennahouse`
- `PagedJS`
- `Typeset.sh`
- `WeasyPrint`
- `Vivliostyle`

are case-sensitive. The `status` option is usually `OK`, `ERROR` or `UNSUPPORTED`
by definition. However the value can be an arbitrary string. The values for `pdf` should
remain untouched. In case of an error you may add a custom `message` option. The `message`
option - even if empty - is mandatory.

The `common` section defines some some general metadata like the `category` (for grouping the lessons).
`category` can be either `basic`, `advanced` or `special` (e.g. for vendor-specific tests).

A new test must be added to the `lessons/lessons.ini` file which defines an
overall ordering of the tests on the lessons overview page.


Generating lessons
------------------

For running the complete lessons suite you need all converters installed on your system.
This means that `run.sh` (Antennahouse9, `pdfreactor.py` (PDFreactor) and `prince` (Prince)
scripts and binaries must be installed and callable from the shell (adjust your `$PATH` accordingly).

Running `make` inside a lesson will execute the Makefile targets `pdfreactor`, `prince` and `antennahouse` which
is equivalent to running the following manually on the console:

.. code-block::

    make pdfreactor
    make prince
    make antennahouse

There is an additional Makefile target `images` which will convert all PDF files to PNG (for usage within
the web application).

In order to run run and generate all lessons you need to execute the following:

.. code-block::

   cd lessons
   bash generated.sh

The `generated.sh` script will iterate over all `lessons-*` lesson directories and execute `make; make images` for each lesson.
The generated files (PDF, converted PNG) will be copied to `lessons/generated`. This folder is also automatically updated for git
(`git rm` on generation start, `git add` on generation termination).

