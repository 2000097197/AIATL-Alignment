# AIATL-Alignment
Project made for AIATL's "AI Alignment: Evaluating LLMs" track.
Google Doc (Report): https://docs.google.com/document/d/1dyzEjGUQhtF19D2mYHxHzO6szpA8VTixdFi8uLbVsbs/edit?usp=sharing
Title: 

# Evaluating LLM’s for AI Safety

# Abstract: 
The security of large language models (LLMs) has greatly improved over time, addressing many obvious issues. In most modern, popular models, simple prompt injection attacks are less likely to produce harmful outcomes. This paper explores a new method to evaluate LLMs and develop a testing approach that produces realistic results. By using insights from developer blogs, AI articles, and research papers, this paper aims to inspire developers with new ideas to better identify and address security risks in LLMs.

# Introduction: 
As LLMs are increasingly used in various applications, ensuring their safety and alignment with intended functions is essential. Despite significant advancements in LLM security, vulnerabilities like prompt injection attacks remain a concern. This paper investigates innovative ways to evaluate and enhance the safety of LLMs, focusing on aligning outputs with designers' intentions. By drawing on insights from developer blogs, AI articles, and research papers, we aim to equip developers with new strategies to spot and reduce security risks in LLMs.

# Methodology: 
Our approach to testing AI alignment involves verifying that the LLM's output matches the designer's intended functionality. For instance, if a model is designed to create stories based on user input, it should not produce outputs discussing politics or sensitive topics. To achieve this, we propose using a separate LLM that users cannot access. This secondary LLM is configured by engineers to respond with either "PASS" or "FAIL" based on the initial LLM's output, ensuring it doesn't contain malicious content. 

The key advantage of this method is its resistance to prompt injection attacks since users cannot directly interact with the verification LLM. Its sole purpose is to confirm that outputs are safe and align with the designer’s intent. During testing, we refined instructions for the verification LLM to ensure it focused on compliance rather than generating responses. We also developed a comprehensive list of potential prompt leaks for the LLM to monitor. Enhancements could include integrating a Retrieval-Augmented Generation (RAG) database into the verification LLM, allowing it to reference extensive research papers and documentation on malicious user prompts.

# Results: 
We tested this method against various existing and hypothetical LLM attacks. Initially, it took several attempts to clearly instruct the verification LLM not to "answer" outputs but instead verify compliance. We also had to identify different types of prompt leaks for the LLM to monitor. This process could be enhanced by integrating a Retrieval-Augmented Generation (RAG) database into the verification LLM, allowing it to reference numerous research papers and documentation on malicious user prompts.

# Implications: 
A potential implication of this approach is its resource intensity, as it requires two LLMs per user, effectively doubling the computational workload. Along with that, implementing a dual-LLM system adds complexity to the architecture, requiring more sophisticated management and maintenance. Running two models per user could significantly increase operational costs, impacting budget allocations for AI projects. There is also the chance that the verification LLM might incorrectly flag safe outputs as unsafe or vice versa, leading to false positives or negatives.

# References: 
https://www.tigera.io/learn/guides/llm-security/prompt-injection/<br/>
https://aclanthology.org/2024.acl-long.830.pdf<br/>
https://ir.elastic.co/news/news-details/2024/Elastic-Security-Labs-Releases-Guidance-to-Avoid-LLM-Risks-and-Abuses/default.aspx<br/>
