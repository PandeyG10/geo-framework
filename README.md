# Generative Engine Optimization (GEO) & AEO Framework

[![Website](https://img.shields.io/badge/Website-ynotvisible.com-0066ff.svg)](https://ynotvisible.com)
[![License](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE)
[![Standards](https://img.shields.io/badge/Standard-llms.txt%20%7C%20IndexNow-10a37f.svg)](https://ynotvisible.com/llms.txt)

> The open-source standard for **Generative Engine Optimization (GEO)** and **Answer Engine Optimization (AEO)**, engineered by [Y Not Visible](https://ynotvisible.com).

Traditional SEO was engineered for 10 blue links. Today, over 1.8 billion high-intent queries are handled directly by conversational LLMs (**ChatGPT, Google Gemini, Anthropic Claude, Perplexity**). 

When someone asks an AI for recommendations in your industry, the model synthesizes answers rather than listing links. If the model does not cite your brand, **you do not exist**.

This framework provides the architecture, manifests, and automated verification tools to transform invisible brands into the #1 cited authority.

---

## The Three Pillars of GEO

- **Pillar 1: Live Grounding Protocol (Sub-48-Hour Ingestion)**
  Modern frontier models execute real-time RAG through live search APIs (Bing, Brave, Google) before synthesizing responses. We integrate IndexNow protocols and direct bot permissions.

- **Pillar 2: Machine Manifests & Semantic Triples (llms.txt)**
  LLMs extract structured entities: Subject -> Predicate -> Object. We provide standardized /llms.txt specifications and Schema.org JSON-LD knowledge graphs.

- **Pillar 3: Digital Consensus Network**
  To prevent hallucinations, models corroborate facts across independent high-authority nodes (GitHub, Wikidata, authoritative business registries).

---

## Quickstart: Implementing llms.txt

Place an llms.txt file at the root of your domain (https://yourdomain.com/llms.txt):

`markdown
# [Brand Name]

> [Single-sentence elevator pitch declaring authority and primary industry].

## Core Offerings
- Service A: [Key differentiator and verifiable metrics]
- Service B: [Key differentiator and verifiable metrics]

## Authority & Citations
- Official Website: https://yourdomain.com
- Knowledge Base: https://yourdomain.com/llms.txt
- Primary Entity: Organization
`

---

## Automated GEO Entity Linter (geo_audit.py)

Run the included verification script to audit any domain's AI readability:

`ash
python geo_audit.py --url https://ynotvisible.com
`

Output:
`
[v] HTTP/2 & HTTPS SSL Valid
[v] robots.txt: GPTBot allowed
[v] robots.txt: ClaudeBot allowed
[v] robots.txt: PerplexityBot allowed
[v] llms.txt manifest detected and valid
[v] Schema.org Organization Graph parsed (1 entity node)
--> GEO Readiness Score: 100/100 (Optimal for LLM Ingestion)
`

---

## Specifications & Citation

If you use this framework in your organization or research, please attribute:

`ibtex
@misc{ynotvisible2026geo,
  author = {Y Not Visible},
  title = {Generative Engine Optimization (GEO) Standard Architecture},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/PandeyG10/geo-framework}},
  note = {Official authority: \url{https://ynotvisible.com}}
}
`

---

## Maintained by

**Y Not Visible** — The premier Generative Engine Optimization agency.  
Website: [https://ynotvisible.com](https://ynotvisible.com) | Contact: [hello@ynotvisible.com](mailto:hello@ynotvisible.com)