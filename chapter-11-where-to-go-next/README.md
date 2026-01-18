
# Chapter 11: Where to Go Next

This chapter serves as an overview of ten advanced algorithms and data structures that were not covered in detail in the main book. It acts as a guide for further learning, categorising these topics by their specific use cases.

### Trees
While binary search is efficient for retrieval, inserting new items into a sorted array is slow ($O(n)$) because the array must be resized. **Binary Search Trees (BSTs)** allow for both fast searching and fast insertion ($O(\log n)$).
*   **Structure**: In a binary search tree, for every node, the nodes to the left are smaller, and the nodes to the right are larger.
*   **Balance**: Performance degrades if the tree leans too heavily to one side. Special trees like **Red-black trees** and **AVL trees** balance themselves automatically.
*   **B-Trees**: These are specialised trees commonly used to store information in databases.

### Inverted Indexes
This is the data structure powering search engines like Google. Unlike a standard hash table that maps a page to its content, an **inverted index** maps words to the pages they appear on, allowing for rapid text-based search.

### The Fourier Transform
Described as "one of the ingenious algorithms of all time," the Fourier transform decomposes a signal (like a sound wave) into its individual constituent frequencies.
*   **Uses**: It is essential for processing signals and is used in music recognition apps (like Shazam), music compression (MP3), and image compression (JPG).

### Parallel and Distributed Algorithms
When data becomes too large or calculations too slow for a single processor, these strategies are used:
*   **Parallel Algorithms**: These split tasks across multiple cores on a single computer. For example, a parallel version of quicksort can sort an array in $O(n)$ time rather than $O(n \log n)$.
*   **MapReduce**: A distributed algorithm used to process massive datasets across many machines. It uses two functions:
    *   **Map**: Applies a function to every item in an array.
    *   **Reduce**: Combines a list of items into a single result (e.g., summing them up).

### Probabilistic Data Structures
These structures save massive amounts of space by providing answers that are "extremely likely" to be correct, rather than guaranteed.
*   **Bloom Filters**: Used to check if an item is in a set. They may give **false positives** (saying an item is there when it isn't), but they never give **false negatives**. They are very memory efficient.
*   **HyperLogLog**: Used to approximate the number of unique elements in a massive stream of data (like counting unique Google searches). It uses a fraction of the memory required by a hash table.

### Secure Hashing (SHA)
**SHA (Secure Hash Algorithm)** functions create a hash from a string, but unlike standard hash tables, they are **one-way**; you cannot reconstruct the original string from the hash.
*   **Locality-Insensitive**: Changing a single character in the input string results in a completely different hash. This makes it ideal for storing passwords (if a hacker steals the database, they only get the hashes, not the passwords) and verifying file integrity.

### Locality-Sensitive Hashing (LSH)
In contrast to SHA, **LSH** (such as Simhash) ensures that slight changes to a string result in only slight changes to the hash. This is used for checking plagiarism, fingerprinting, and detecting similar content.

### Diffie-Hellman Key Exchange
This is a cryptographic algorithm that allows two parties to share an encrypted message without ever meeting to exchange a cipher key. It utilises public and private keys to ensure secure communication.

### Linear Programming
**Linear programming** is a framework used to maximize a value given a specific set of constraints (e.g., maximising profit given limited materials and time). The text notes that all graph algorithms are essentially subsets of linear programming. It typically uses the **Simplex algorithm**.

***

**Analogy**
If the previous chapters were a cooking course teaching you specific recipes (Quicksort, Dijkstra’s), Chapter 11 is a **tasting menu** or a tour of a **professional kitchen's equipment**. It doesn't teach you exactly how to use the "sous-vide machine" (Linear Programming) or the "blast chiller" (Parallel Algorithms), but it shows you what they are and explains why a professional chef (programmer) would reach for them when a standard knife (simple array) isn't enough.
