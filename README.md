# 20440_TARA


## Overview:

This repository is a home for Rashi Jeeda and Victoria Chen's final project for MIT 20.440 Analysis of Biological Networks. The project is titled "Uncovering drivers of ocean microbiome diversity". Our goal is to use metadata and microbial taxonomic classifications generated from Tara Oceans expeditions to understand the principal drivers of microbiome diversity in oceans.

This repository contains data and code for analysis of the Tara Oceans microbiome dataset. Data is drawn from the companion website to "Structure and function of the global ocean microbiome" by Sunagawa, Coelho, Chaffron, et al., Science, 2015. (http://ocean-microbiome.embl.de/companion.html)

## Data:

The data was generated by the Tara Ocean expedition team. Ocean water samples were collected in 68 locations across the globe to create a ocean microbial gene catalog. Metadata was collected for all ocean sampling sites including ocean name, latitude, longitude, date, time, depth, temperature, and more. Metagenomic merged Illumina reads were extracted for all samples and 16S rRNA was sequenced for taxonomic classification of all microbes found in each samples. 16S rRNA reads were mapped to 16S reference sequences from the widely-used SILVA database and clustered into 97% operational taxonomic units (OTUs), which provide a measure of relative abundances of various taxa found in samples. The pre-processed OTU count table was provided.

Citation: "Structure and function of the global ocean microbiome" by Sunagawa, Coelho, Chaffron, et al., Science, 2015. (http://ocean-microbiome.embl.de/companion.html)


## Figure guide:
- ```plots/cyanobacteria_vs_temp.png```
    - Calculate the percent of reads for each sample that are classified to the phylum Cyanobacteria by dividing total Cyanobacteria OTU counts by total counts for each sample. Plot against temperature for each sample and color by sampling location.
    - Generated using: ```plotting_scripts/EDA.ipynb```
    - Necessary data: ```data/clean/companion_table_W1.csv, data/clean/nutrient_temp_table.csv, data/clean/taxonomic_profiles.csv```
    

## Folder structure:

```
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
 ```
 
## Installation:

The following packages should be installed for running both the plotting scripts and processing scripts (also found in requirements.txt):

```
python==3.8.11 

biom_format==2.1.14

bokeh==2.3.3

numpy==1.22.4

pandas==1.3.2
```
