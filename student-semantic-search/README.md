Semantic Search System using Endee Vector Database Architecture



1\. Project Overview



This project implements a Semantic Search system for student notes using vector embeddings. 

Traditional keyword-based search fails to capture meaning and context. This project demonstrates how vector search enables semantic similarity matching, allowing users to retrieve relevant information based on meaning rather than exact keyword matches.

The system is designed following the Endee Vector Database architecture for storing and querying embeddings.



2\. Problem Statement



Students often store large amounts of notes across subjects. Retrieving specific information using keyword-based search can be inefficient and inaccurate.



This project solves the problem by:

\- Converting text notes into vector embeddings

\- Performing similarity-based retrieval

\- Returning the most semantically relevant note

This simulates how modern AI search engines and RAG systems operate.



3\. System Design and Technical Approach



Architecture



User Query -> Convert to Embedding -> Vector Search (Endee Architecture) -> Retrieve Most Similar Document -> Display Result



Technical Steps:-



I   Load student notes from text file

II  Convert notes into vector embeddings using SentenceTransformers

III Store embeddings in vector space

IV  Convert user query into embedding

V   Compute cosine similarity

VI  Return the most relevant note





4\. How Endee is Used



This project is built inside the forked Endee repository as required.

The architecture follows Endee's vector database design principles:



\- Embeddings represent documents

\- Vector similarity search is core retrieval mechanism

\- Retrieval-first architecture supports future RAG integration



In production deployment:



\- Endee would store embeddings persistently

\- Endee's vector indexing would enable efficient large-scale search

\- Query embeddings would be matched using Endee’s optimized vector search engine



This project demonstrates how Endee can serve as the backbone for AI-powered semantic retrieval systems.



5\. Technologies Used



\- Python

\- SentenceTransformers

\- NumPy

\- Vector Embeddings

\- Endee Vector Database (Architecture Integration)



6\. Setup and Execution Instructions



&nbsp;Step 1: Install Dependencies



pip install -r requirements.txt



&nbsp;Step 2: Run the Application



python main.py



tep 3: Ask Questions



Example:

What is vector database?

What is RAG?



Type 'exit' to stop.



7\. Future Improvements



\- Integrate Endee server for persistent storage

\- Add RAG integration with LLM

\- Scale to large document collections

\- Build API interface for deployment



Conclusion



This project demonstrates a complete AI/ML application using vector search as the core mechanism. It showcases how Endee Vector Database can power semantic retrieval, forming the foundation for advanced AI systems such as RAG and recommendation engines.

