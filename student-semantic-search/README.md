AI Study Assistant using Vector-Based Semantic Search (Endee Architecture)



1\. Project Overview



This project implements an AI-powered Study Assistant that enables students to query their study notes using semantic search.Unlike traditional keyword-based search, this system retrieves information based on contextual meaning using vector embeddings.

The system is architected following Endee’s vector database design principles and demonstrates how semantic retrieval systems are built for modern AI applications such as Retrieval-Augmented Generation (RAG).



2\. Problem Statement



Students often accumulate large volumes of study notes. Finding relevant information using keyword search can be inefficient because:

-It does not understand context

-It fails when exact words are not matched

-It cannot retrieve conceptually similar content



This project solves the problem by:



Converting text into vector embeddings

Performing cosine similarity-based retrieval

Returning the most semantically relevant paragraphs

This approach mirrors how production AI search systems operate.



3\. System Design and Technical Approach



Architecture Flow:

Load structured notes from notes.txt

Split content into paragraph-level chunks

Convert each chunk into vector embeddings using SentenceTransformers

Normalize embeddings for cosine similarity

Convert user query into embedding

Compute similarity scores

Retrieve top-k most relevant results



Retrieval Pipeline:



Text Notes

-> Chunking

-> Embedding Model

-> Vector Representation

-> Cosine Similarity

-> Top-K Semantic Retrieval



Key Technical Features:



Paragraph-based chunking

Normalized vector embeddings, Cosine similarity scoring, Top-K retrieval, Interactive Q\&A loop, RAG-ready architecture



4\. How Endee is Used



This project is built inside the forked Endee repository as required and the architecture is designed to be compatible with Endee’s vector database engine.



Currently:



Embeddings are stored in-memory for demonstration

Cosine similarity is computed locally



In production deployment:



Embeddings would be persisted and indexed using Endee’s optimized vector database

Vector search operations would be handled by Endee’s indexing engine

The retrieval layer would scale to large document collections

The current implementation demonstrates the semantic retrieval layer that would plug directly into Endee’s vector storage and search backend.



5\. Practical Use Case



This system acts as a Study Assistant that:

\-Answers exam-related questions from notes

\-Retrieves concept explanations

\-Supports revision preparation

\-Enables semantic concept search



The same architecture can be extended to:



Retrieval-Augmented Generation (RAG)

Recommendation system

Knowledge base search engines

Agentic AI workflows



6\. Technologies Used



Python

SentenceTransformers

NumPy

Vector Embeddings

Endee Vector Database (Architecture Integration)



7\. Setup and Execution Instructions



Step 1: 



Install Dependencies

pip install -r requirements.txt



Step 2: 



Add Study Notes

Place your content inside notes.txt.

Each paragraph represents a searchable chunk.



Step 3: 



Run the Application

python main.py



Step 4: 



Ask Questions



Example queries:



What is Retrieval-Augmented Generation?

Explain overfitting.

Difference between supervised and unsupervised learning.

What is cosine similarity?



Type exit to quit.



Conclusion



This project demonstrates a complete vector-based semantic search system aligned with Endee’s vector database architecture. It showcases how modern AI systems retrieve knowledge using embeddings and similarity search, forming the foundation for scalable AI applications.

