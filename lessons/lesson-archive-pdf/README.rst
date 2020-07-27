Support for "archive PDF" aka PDF/A profile is available for Prince, Antennahouse and 
PDFreactor.

Check the *Makefile* in the Github repository (link above) for investigating
the related commandline parameters for PDF/A. Note that Antennahouse requires a
dedicated *config.xml* file with a reference to an existing ICC profile file
(here *default_rgb.icc*).

We used the *VeraPDF Checker* (https://verapdf.org) for checking PDF/A compliance.
