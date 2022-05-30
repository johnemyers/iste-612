
---
title: "Checkpoint 1 - Team UFO"
author: "Cory Maclauchlin, John Myers, Arivirku Thirugnanam"
date: "6/3/2022"
output:
  pdf_document:
    latex_engine: xelatex
  html_document:
    df_print: paged
subtitle: An Analysis of Declassified Government Documents
---

\vspace{-15truemm}

# Introduction
There has been a recent uptick in the conversations surrounding the notion of "Unidentified Flying Objects," or UFOs, in the media due to Congressional inquiries on the topic. The United States Government Freedom of Information Act (FOIA) allows individual citizens the right to ask for and receive previously unreleased documents possessed by the Government upon request. When these documents are released according to the law, "Internet detectives"" must pour through the documents to find that hidden nugget of information. In the case of this project, we want to see any hidden patterns surrounding the origin of these so-called UFOs that Government hasn't disclosed before. We will apply our developed system to a series of documents released by the Central Intelligence Agency (CIA) through a so-called FOIA request to better understand the nature of the data.

# Problem Description
Some of the technical challenges of this project include:

* **Large Troves of Documents.**When released, a trove of documents is published all at once. These can include hundreds of PDFs with thousands of pages. For this particular release of documents from the CIA, there are ### documents composed of ### pages.
* **Data That is Dirty.** The Government releases documents that are scans of printed materials, with redactions made. This is the ensure that nothing is accidentally revealed that isn't supposed to be, so a physical step is required in Government release procedures.  As such, any useful digital representation is obliterated.
* **Unusual Lexicon.** A standard dictionary methodology may not be appropriate for certain documents types, especially this dataset.  The unusual lexicon surrounding both alien and terrestrial technology will require an unsupervised approach to performing processing.
* **No Categorization or Labeling.** Documents are released without any labeling or categorization of any kind. This leaves it as an exercise to the recipient to pour through the mounds of information to find the needle in the haystack they are looking for.

# Software Development

Our development methodology will leverage on the tools of the trade for.  We have performed an initial survey of the requirements of the system, along with a design and implementation approach, which will now be discussed in more detail.

## Requirements

This tool will be designed generically to accommodate any type of cache of FOIA-released documents from the government in PDF form.

There will be two primary user classes for the developed software.  The first user class is the *data scientist* who will set up the backend for data processing, including administering the parameters for the model generation steps.  The second user class is a *citizen data consumer* interested in understanding the document set, especially for finding the hidden patterns within the data.  In addition, this user class will leverage the clusters that have been exposed 

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
The data processing pipeline will be responsible for TODO...

1. K-Means Flat Clustering

### Visualization Subsystem
The visualization subsystem will be responsible for displaying user interfaces that will allow for both the administering of the data processing pipeline parameters and also the visualization of the results of the analysis.  

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
We intend to heavily leverage existing libraries to supplement our implementation of this project. Some initial libraries that we've identified include:

* Apache PDFBox - Open and proces text data within an OCR'd PDF document.

# Test & Demonstration

We will use the ### PDFs that have been published here: https://documents2.theblackvault.com/documents/cia/CIAUFOCD-FULL-CONVERTED.zip.  These documents have been made searchable from the original release by the CIA under a FOIA request.

# Appendix


