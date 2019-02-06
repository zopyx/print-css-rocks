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

Using the print-css.rocks repository
------------------------------------

Setting up your own environment
-------------------------------

You need a decent Python 3 installation (Python 3.6 or 3.7) for installing the print-css.rocks setup
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

