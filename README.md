# 20440_TARA


## Overview:

This is a repository containing data and code for analysis of the Tara Oceans microbiome dataset. Data is drawn from the companion website to "Structure and function of the global ocean microbiome" by Sunagawa, Coelho, Chaffron, et al., Science, 2015. (http://ocean-microbiome.embl.de/companion.html)

## Data:

The data was generated by the Tara Ocean expedition team. Ocean water samples were collected in 68 locations across the globe to create a ocean microbial gene catalog. Metadata was collected for all ocean sampling sites including ocean name, latitude, longitude, date, time, depth, temperature, and more. Metagenomic merged Illumina reads were extracted for all samples and 16S rRNA was sequenced for taxonomic classification of all microbes found in each samples. 16S rRNA reads were mapped to 16S reference sequences from the widely-used SILVA database and clustered into 97% operational taxonomic units (OTUS), which provide a measure of relative abundances. The OTU count table was provided.

Citation: "Structure and function of the global ocean microbiome" by Sunagawa, Coelho, Chaffron, et al., Science, 2015. (http://ocean-microbiome.embl.de/companion.html)


## Folder structure:

.
├── data
│   ├── raw
│   │   └── raw datasets as downloaded from the Tara Oceans paper companion website
│   └── clean
│       └── renamed datasets saved in .csv format  
├── plots
│   └── all plots generated from data
├── plotting_scripts
│   └── jupyter notebooks used to explore data and generate plots
└── processing_scripts
    └── all other scripts used to process data
 
## Installation:

The following packages should be installed for running both the plotting scripts and processing scripts (also found in requirements.txt):

python==3.8.11 

biom_format==2.1.14

bokeh==2.3.3

numpy==1.22.4

pandas==1.3.2
