## About

This is a test-utility that was used to prototype the calculation of cell area
using the a combination of the cell masks and probibility maps as output by
MoMA. It calculates the 
The concept has since been implemented in MoMA in a more clean way that
also considers partial overlap of the dilated masks of adjacent cells.

## Setup

Owing to its prototype-status this code is not packaged in any way and does
not contains Conda file for setting up the environment. You will have to figure
this out yourself. Check the import statements of the three Python files to
see the dependencies the must be installed.

## Usage

The Python script `run_probability_summing.py` defines the following input files
that are used by this script:

- `mask_path`: path to the label-image as output by MoMA.
- `probability_map_path`: path to the image containing the probability map as
output by MoMA.
- `csv_input_path`: path to the CSV file. This will be read in to get
cell-IDs, which correspond to the label-values in the mask/label-image.
- `csv_output_path`: path to the output CSV file. This file contains the same
information as the input CSV file along with an added column for the new cell
area estimate.
