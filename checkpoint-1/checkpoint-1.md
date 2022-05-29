---
title: "Checkpoint 1 - Team UFO"
subtitle: "An Analysis of Declassified Government Documents"
author: "Cory Maclauchlin, John Myers, Arivirku Thirugnanam"
date: "6/3/2022"
output: 
  pdf_document:
    latex_engine: xelatex
---

# Introduction
There has been a recent uptick in the conversations surrounding the notion of "Unidentified Flying Objects," or UFOs, in the media due to Congressional inquiries on the topic.  Freedom of Information Act (FOIA) request.

# Problem Description


# Software Development

## Requirements

This tool will designed generically to accomdate any type of cache of FOIA-released documents from the government in PDF form.

## Design

The overall architecture will be designed around three subsystems and pipelines, the Backend Data Subsystem (in Blue), the Data Processing Pipeline (in Orange), and the Visualization Subsystem (in Green):

![](architecture.png)

### Backend Data Subsystem
The backed data subsystem will be responsible for opening all of the OCR'd PDF files within the specified directory, cleaning them as appropriate, and building the interim data format for the data processing pipeline. 

1. Documents will be parsed and imported
1. All words will be compared to a english dictionary and only actual words will be indexed
1. Only documents that ultimately have more than 2 words will be indexed

Finally, as a stretch goal, we will have an accessor available so that a user can choose a specific document from a cluster displayed on the rendered visualizations and see the contents of the original (source) document that was used.

### Data Processing Pipeline

1. K-Means Flat Clustering

### Visualization Subsystem

We will create user interfaces that will allow for both the administering of the data processing pipeline parameters and also the visualization of the results of the analysis.  

Several of the parameters that will modifiable in the User Interface will be:
 * Cluster Size
 * Initialization Method
 * Iterations
 * Feature Extraction Method

Once parameters have been changed and processing is complete, the following displays will be displayed to the user as a result:
 * Optimal Cluster Graph
 * K-Means Clusters
 * Word Cloud
 * Linkage to Source

## Implementation

* Apache PDFBox

# Test & Demonstration

* We will use the ### PDFs that have been published here: https://documents2.theblackvault.com/documents/cia/CIAUFOCD-FULL-CONVERTED.zip.  These documents have been made searchable from the original release by the CIA under a FOIA request.

# References