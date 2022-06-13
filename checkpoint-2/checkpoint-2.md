---
title: "Checkpoint 2 - Team UFO"
author: "Cory Maclauchlin, John Myers, Arivirku Thirugnanam"
date: "6/3/2022"
output:
  html_document:
    df_print: paged
  word_document: default
  pdf_document:
    latex_engine: xelatex
subtitle: An Analysis of Declassified Government Documents
---
\vspace{-18truemm}

# Introduction

There has been a recent uptick in the conversations surrounding the notion of "Unidentified Flying Objects," or UFOs, in the media due to Congressional inquiries on the topic. The United States Government Freedom of Information Act (FOIA) allows individual citizens the right to ask for and receive previously unreleased documents possessed by the Government upon request. When these documents are released according to the law, "Internet detectives" pour through the documents to find that hidden nugget of information. In the case of this project, we want to see if there are any hidden patterns surrounding the origin of these so-called UFOs that the Government hasn't disclosed before. We will apply our developed system to a series of documents released by the Central Intelligence Agency (CIA) through a FOIA request to better understand the nature of the data.

# Source Data Collection

We will use the 712 PDFs that have been published here: https://documents2.theblackvault.com/documents/cia/CIAUFOCD-FULL-CONVERTED.zip. These documents have been made searchable from the original release by the CIA under a FOIA request.

# Data Conditioning and Processing

The backend data subsystem will be responsible for opening all of the OCR'd PDF files within the specified directory, cleaning them as appropriate, and building the interim data format for the data processing pipeline. 

1. Documents are parsed and imported into memory.
1. All words will be compared to a Wordnet, and only words with semantics will be indexed.
1. Only documents that ultimately have more than two actual words will be indexed.

# Initial Observations

# Software Development Approach Refinement

