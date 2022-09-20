#!/usr/bin/env bash

set -e

pdflatex affidavit && \
pdflatex -halt-on-error -interaction errorstopmode -output-format pdf affidavit
