---
title: "Checkpoint 2 - Team UFO"
author: "Cory Maclauchlan, John Myers, Arivirku Thirugnanam"
date: "6/24/2022"
output:
  pdf_document:
    latex_engine: xelatex
  word_document: default
  html_document:
    df_print: paged
subtitle: An Analysis of Declassified Government Documents
header-includes:
 \usepackage{booktabs}
 \usepackage{longtable}
 \usepackage{array}
 \usepackage{multirow}
 \usepackage{wrapfig}
 \usepackage{float}
 \floatplacement{figure}{H}
---

# Introduction

There has been a recent uptick in the conversations surrounding the notion of "Unidentified Flying Objects," or UFOs, in the media due to Congressional inquiries on the topic. The United States Government Freedom of Information Act (FOIA) preserves individual citizens' rights to ask for and receive previously unreleased documents possessed by the Government upon request. When these documents are released according to the law, "Internet detectives" pour through the documents to find that hidden nugget of information. In the case of this project, we want to see if there are any hidden patterns surrounding the origin of these so-called UFOs that the Government hasn't disclosed before. We will apply our developed system to a series of documents released by the Central Intelligence Agency (CIA) through a FOIA request to better understand the nature of the data.

# Source Data Collection

Our goal is to use 713 Government-released documents that have been on made available through the website "The Black Vault." This site provides two sets of digital artifacts. The first is a zip of PDFs have been made searchable from the original release by the authors of the website. The original source for these documents is also available in TIFF image form. An explanation of the artifacts and processing of each is further explained.

# Data Conditioning and Processing

The backend data subsystem will be responsible for opening all PDF files within the specified directory, cleaning them as appropriate, and building the interim data products for the data processing pipeline.

1.  Documents are opened, tokenized, and imported into memory.
2.  All tokenized words will be compared to a Wordnet, and only words with semantics will be indexed.
3.  Only documents that ultimately have more than two actual words will be indexed.

The team initially discovered upon using the processed PDFs made available by the above website that they inserted advertisements into the PDFs. These ads were causing false keywords to be inserted into the document and causing our statistics not to be valid. As a result, we returned to the source original TIFF images released by the CIA and reran Optical Character Recognition (OCR) on those documents. This OCR was run in batch mode through Adobe Acrobat Pro and was quite time-consuming; however, because of this work, all of our initial observations are much more accurate to the reality of parsing through Government released documents. These OCR-processed documents are available upon request.

Using the criteria listed, we are forced to eliminate 95 documents with no valuable content.

# Initial Observations

After parsing through the data using the documents produced and filtered as detailed above, we were able to establish a dictionary of 8,205 unique words within all of the documents available. As seen in Figure \ref{WordCountHist}, we first looked at the overall distribution of word counts within the 618 documents that had useful content within them. There is a large concentration on the lower end, so there isn't a normal distribution. In addition, there are some extreme outliers on the upper end. The team doesn't feel that this distribution will negatively affect the research to be conducted in this case as we did a fair amount of prepping of the dataset to get to this point.

![Histogram of Word Count\label{WordCountHist}](./images/WordCountHist.png)

After observing this distribution, we continued by computing the overall page word count summary statistics. The summary is seen in Table \ref{SummStats} and shows that, on average over the 618 documents, we see \~238 words per document. While this mean is skewed by the single outlier document of 5392 words, a look at the offending document, `C05517512.pdf`, shows a relatively cleanly scanned document of the same relative type as the rest. Because of this, we don't feel even the median of 82 words causes this dataset to be invalid for our research.

| count | mean   | std    | min | 25%   | 50% | 75%    | max  |
|-------|--------|--------|-----|-------|-----|--------|------|
| 618   | 238.34 | 492.13 | 3   | 31.25 | 82  | 184.50 | 5392 |

: Summary Statistics of Word Count\label{SummStats}

\newpage

After the analysis of the word counts per document, we next wanted to look at some simple statistics related to frequent words seen within all of the documents. We can see in Figure \ref{FrequentWordsBar} that some not surprising words emerge at the top of this list. We see that `unclassified` appears the most number of times within the documents, at 2768 times, followed by `soviet` and `russian` at 2218 and 1345, respectively. This gives us reasonable assurance that our techniques and processes are in order, as these are obviously critical keywords to the domain we are in.

![Top 25 Frequent Words\label{FrequentWordsBar}](./images/FrequentWordsBar.png)

Now that we know we have a reasonable data processing pipeline for the backend, we began to look at refining our software development approach and converge on what information retrieval and text mining operations can be applied for our entire application.

# Software Development Approach Refinement

We began looking at a high level of what we can learn.

![Plot of 2-20 Clusters\label{ElbowMethodOptimalK}](./images/ElbowMethodOptimalK.png)

# Document Sets

-   Raw TIFF images from Government: <https://documents2.theblackvault.com/documents/cia/CIAUFOCD-FULL-UNTOUCHED.zip>
-   Processed "Searchable" PDFs with Advertisement: <https://documents2.theblackvault.com/documents/cia/CIAUFOCD-FULL-CONVERTED.zip>
