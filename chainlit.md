# Wittgenbot 🗿

<span style="font-size: 18px;">
    <img src="/public/readme_image.png" alt="Sample Image" style="float: right; margin-right: 10px; width: 50%">
    Welcome to <b>Wittgenbot</b>, your chatbot companion for exploring Ludwig Wittgenstein's <i>Philosophical Investigations</i>.<br><br>
    Simply select a model to chat with, ask away, and let your philosophical confusions dissolve 💭.
</span>
<br><br>


## Retrieval Augmented Generation 🔄

<span style="font-size: 18px;">


Our chatbot is based on **Retrieval Augmented Generation (RAG)**. Academic secondary texts were partitioned into chunks of size <span style="font-size: 16px;">`chunk_size`</span>. The chunks were then embedded into vectors using the [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) embedding model and stored in a vector database. The chatbot uses this database as a context reference before answering the question through an LLM, [Mistral-7B-Instruct-v0.2](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF), which was manually chosen with the help of a philosophy expert.<br>
The question-answer procedure is outlined below:
1. The user asks a question.
2. The question is embedded into a vector and *mathematically* compared to other vectors in the database, where the 25 most similar vectors are collected. Equivalently, 25 excerpts (chunks) relevant to the question are collected.
3. The 25 relevant excerpts, along with the question, are fed into a reranking model by Cohere, which *semantically* ranks them in terms of relevance to the question, and the top 3 are selected.
4. The question and 3 most semantically relevant excerpts are fed into an LLM, **Mistral-7B-Instruct-v0.2**, which generates an answer using the excerpts as context.

</span>
<br>


## Models 🧠

<span style="font-size: 18px;">

We offer the following models:

- **WITT-0.5K**: Utilizes a RAG chain with
  - `chunk_size` of _512_ and `chunk_overlap` of _50_.
  - Model **Mistral-7B-Instruct-v0.2**.
  - Shorter inference time but higher risk of inaccurate answers.<br><br>

- **WITT-1.5K**: Utilizes a RAG chain with
  - `chunk_size` of _1500_ and `chunk_overlap` of _300_.
  - Model **Mistral-7B-Instruct-v0.2**.
  - Longer inference time but lower risk of inaccurate answers.<br><br>

- **Command**: Cohere's pre-trained model capabale of answering philosophical questions.<br><br>

- **Foo Bar**: Foo bar foo bar.

</span>
<br>

## Dataset 📚

<span style="font-size: 18px;">

Academic secondary sources about **Ludwig Wittgenstein's _Philosophical Investigations_ (1953)** were collected in bulk via [CORE API](https://core.ac.uk/services/api). This work was chosen alone to facilitate manual and automated testing due to limited resources. However, the benefits of RAG allow us to expand the chatbot's knowledge-base to include other works and philosophers by simply collecting more relevant secondary sources through CORE and storing them in our vector database.

</span>
<br>

## Final Year Project 🗂️

<span style="font-size: 18px;">

This project was done by **Ali Jaafar**, **Nadim Akkaoui**, **Shoushy Kojayan** as their Final Year Project.

</span>
<br>

## GitHub Repository 🔮

<span style="font-size: 18px;">

The code of the entire project is available on [this GitHub organization](https://github.com/orgs/philosophy-question-answerer/repositories).

</span>