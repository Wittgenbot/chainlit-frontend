# Wittgenbot 🗿

<span style="font-size: 18px;">
    <img src="/public/readme_image.png" alt="Sample Image" style="float: right; margin-right: 10px; width: 50%">
    Welcome to <b>Wittgenbot</b>, your chatbot companion for exploring Ludwig Wittgenstein's philosophy.
</span>
<br>

## Instructions 📋

<span style="font-size: 18px;">

Simply select a model to chat with, ask away, and let your philosophical confusions dissolve. 💭

Below are some sample questions related to Wittgenstein's work that you could ask <strong>Wittgenbot</strong>:
<ul style="list-style-type: square;">
  <li><em>What determines the meaning of a word?</em></li>
  <li><em>When can something be classified as a game?</em></li>
  <li><em>Is the existence of a private language possible?</em></li>
  <li><em>How do philosophical problems arise from misunderstandings of language?</em></li>
</ul>
</span>

## Models 🧠

<span style="font-size: 18px;">

We offer the following models:

- **WITT-0.5K**: Utilizes a RAG chain with
  - Context length (<span style="font-size: 16px;">`chunk_size`</span>) of *512* tokens and overlap (<span style="font-size: 16px;">`chunk_overlap`</span>) of *50* tokens.
  - Model **Mistral-7B-Instruct-v0.2**.
  - Shorter inference time but higher risk of inaccurate answers.<br><br>

- **WITT-1.5K**: Utilizes a RAG chain with
  - Context length (<span style="font-size: 16px;">`chunk_size`</span>) of *1500* tokens and overlap (<span style="font-size: 16px;">`chunk_overlap`</span>) of *300* tokens.
  - Model **Mistral-7B-Instruct-v0.2**.
  - Longer inference time but lower risk of inaccurate answers.<br><br>
  
- **Command**: [Cohere](https://cohere.com/)'s pre-trained model capabale of answering philosophical questions.<br><br>

- **Foo Bar**: Foo bar foo bar.

## Retrieval Augmented Generation (RAG) 🔄

<span style="font-size: 18px;">


Our chatbot is based on **Retrieval Augmented Generation (RAG)** with a collection of academic secondary texts as its knowledge base. The texts were partitioned into chunks of size <span style="font-size: 16px;">`chunk_size`</span> tokens with consecutive chunks overlapping by <span style="font-size: 16px;">`chunk_overlap`</span> tokens. The chunks were then embedded into vectors of dimensionality 384 using the [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) embedding model and stored in a vector database. The chatbot uses this database as a context reference before answering the question through an LLM, [Mistral&#8209;7B&#8209;Instruct&#8209;v0.2](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF), which was manually chosen with the help of a philosophy expert.<br>
The question-answer procedure is outlined below:
1. The user asks a question.
2. The question is embedded into a vector and *mathematically* compared to other vectors in the database, where the 25 most similar vectors (chunks) are collected. Equivalently, 25 excerpts relevant to the question are collected.
3. The 25 relevant excerpts, along with the question, are fed into a reranking model by [Cohere](https://cohere.com/), which *semantically* reranks them in terms of relevance to the question, and the top 3 are selected.
4. The question and 3 most relevant excerpts, each of size <span style="font-size: 16px;">`chunk_size`</span> tokens, are fed into an LLM, **Mistral-7B-Instruct-v0.2**, which generates an answer using the excerpts as context.

</span>

## Dataset 📚

<span style="font-size: 18px;">

Academic secondary sources about Ludwig Wittgenstein's **_Tractatus Logico-Philosophicus_ (1921)** and **_Philosophical Investigations_ (1953)** were collected in bulk via [CORE API](https://core.ac.uk/services/api). This work was chosen alone to facilitate manual and automated testing due to limited resources. However, the benefits of RAG allow us to expand the chatbot's knowledge-base to include other philosophers by simply collecting more relevant secondary sources through CORE and storing them in our vector database.

</span>

## Final Year Project 🗂️

<span style="font-size: 18px;">

This project was done by **Ali Jaafar**, **Nadim Akkaoui** and **Shoushy Kojayan** as their Final Year Project.

</span>

## GitHub Repository 🔮

<span style="font-size: 18px;">

The code of the entire project is available on [this GitHub organization](https://github.com/Wittgenbot).

</span>