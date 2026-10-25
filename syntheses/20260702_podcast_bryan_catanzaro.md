# Nvidia Nemotron — Bryan Catanzaro on the MAD Podcast (July 2026)

Oct 25, 2026 · @Al

## Source and caveats

Everything below is Nvidia's own account, recorded about four months ago, so the model landscape has moved since.

- **Source:** MAD Podcast (Matt Turck), interview with Bryan Catanzaro, who leads Nemotron, Nvidia's family of open foundation models. Published 2 July 2026 ([episode listing](https://podwise.ai/podcasts/17886)).
- **Timing:**
  - Recorded around June 2026, a couple of weeks after the Nemotron 3 Ultra release.
  - That was three months after the Nemotron coalition launched in March.
  - It predates the Nemotron 3.5 release Pierre Stock mentions in the Mistral doc.
- **Transcript quality:** auto-generated, with clear host and guest turns. In several places the word "MoE" dropped out ("so fast because of \[MoE\]").
- **Name fixes:**
  - "Brian Kentaro" is Bryan Catanzaro; "Neimotron" and "Neotron" are Nemotron.
  - "BYU" is Baidu; "Andrew Ing" is Andrew Ng; "Daario Amadei" is Dario Amodei; "Jensen Wong" is Jensen Huang.
  - "QDNN" is cuDNN; "member" is Mamba; "QN" is Qwen; "Kimmy" is Kimi; "multi-teer distillation" is multi-teacher distillation.
- **Context on the Fable episode:** in the safety discussion, Catanzaro refers to the Fable release and the US government's response.
  - On 12 June 2026, Anthropic suspended access to Claude Fable 5 and Mythos 5 to comply with US Department of Commerce export controls.
  - The controls were lifted on 30 June, and access was restored on 1 July ([Anthropic statement](https://www.anthropic.com/news/fable-mythos-access)).

## Part 1 — Roadmap, ambitions, bottlenecks

### Roadmap

Nemotron 3 has just shipped in three sizes, Nemotron 4 is in development, and Nvidia has substantially increased the compute behind the programme.

- **Nemotron 3 family (shipping):**
  - Nano, Super and Ultra, all mixture-of-experts; specs are in Part 2.
  - The host calls Ultra the number one US open-weight model at release.
- **Nemotron 4 (in development):** the name clashes with the 2024 Nemotron-4 340B. Catanzaro jokes that this is a marketing problem he didn't create.
- **Compute:** Nvidia has "recently increased our investment substantially" because it sees Nemotron as key to the company's future. More teams across the company now contribute.
- **Nemotron coalition (launched March 2026):**
  - Partners help shape models before they are built, contributing evaluations, RL environments, benchmarks and other technology.
  - Membership is non-exclusive; partners stay free to work with anyone.
- **Open data:** Nvidia keeps releasing training data, including purchased data where it has redistribution rights, plus large synthetic datasets.
- **Next for RL:** much more diverse and sophisticated training environments over the next few years. Catanzaro calls today's environments "fairly simple."
- **Inference speed:** ongoing work to raise the acceptance rate of multi-token prediction, which directly sets inference speed.
- **Graphics spin-off:** DLSS 5, a fully generative version of Nvidia's AI rendering, has been announced.

### Ambitions

Nvidia builds frontier open models to design better hardware and to keep the open AI ecosystem, its customer base, thriving.

- **Nemotron's two jobs:**
  1. Teach Nvidia how AI really works, so it can co-design chips, networking and software. With Moore's law dead, acceleration comes from specialisation, and specialisation needs that understanding.
  2. Support the ecosystem, so companies of every size can build and deploy their own AI. Whatever grows AI grows Nvidia's business, so Nvidia welcomes other open models too.
- **Long-term commitment:** Catanzaro compares Nemotron to CUDA, which Nvidia backed for more than ten years. His message: Nvidia follows through.
- **Efficiency thesis:**
  - Every organisation will run at its limit, whether money, power or gigawatts, because intelligence is so valuable.
  - At the limit, more intelligence can only come from using resources more efficiently. Nemotron is therefore "speed first."
- **Agents as the target:** agentic workflows are the use case Nvidia cares about most.
- **Openness:**
  - Nvidia is maximally open with data and welcomes other models trained on it.
  - Catanzaro praises Chinese labs' openness, OpenAI's GPT-OSS and Google's Gemma. He wants the rest of the world to catch up with China on open development.
- **Why customers choose open models:**
  - Every company is built around a secret: its data, platform and customer knowledge.
  - Open models let a company keep that secret in-house, meet regulatory constraints, and customise guardrails and integration.
  - *Interpretation:* this is the same sovereignty argument Mistral makes, framed as customisation.
- **Safety stance:**
  - Catanzaro calls his view unorthodox: open technology is safer because more people can inspect it.
  - He argues diversity of ideas is safer than a monoculture, and compares this to freedom of speech and conscience.
- **No singularity:**
  - Intelligence is multifaceted and depends on context. He likens raw intelligence to an engine with no wheels.
  - He frames AI as an "external brain," by analogy with the kitchen as an external stomach.
  - He is optimistic overall but worried about how society manages the transition.

### Bottlenecks

Compute is scarce even inside Nvidia, and Catanzaro treats physical and economic limits as the binding constraint on progress.

- **Compute at the limit:**
  - The research effort does not get all the GPUs it wants. Allocation is reviewed every two weeks, and many projects go unfunded.
  - His number one wish is more GPUs.
- **End of Moore's law:**
  - Transistors still shrink, but more slowly and at a higher cost.
  - Shrinking an existing design no longer brings economic gains, so every gain has to come from co-designing the whole stack.
- **Organisation:**
  - About ten teams across Nvidia build Nemotron, and Catanzaro mentions 500 people as an example scale.
  - Without the right method, teams pull the model in competing directions. He calls humans naturally tribal.
- **Data:**
  - Purchased data can be released only where Nvidia holds redistribution rights.
  - Synthetic data is "garbage in, garbage out": it has to add real value and help the model generalise.
- **Verifiable rewards beyond code:** coding is special because it produced huge amounts of training text and has tools to check results. Other domains depend on RL environments that are still simple.
- **Training risk:** 4-bit pre-training can diverge, which required real algorithmic invention to avoid.
- **Mixture-of-experts costs:**
  - MoE models need a lot more memory, and with little memory a dense model is smarter.
  - They work best for single-user local runs or very large data centres, and are trickier in between.
- **Long context costs:** reasoning over very long inputs gets expensive, which is why context windows have limits.
- **Distillation question:**
  - The host asks whether closed labs discouraging distillation could slow open models.
  - Catanzaro dismisses the risk: no small group has a monopoly on good ideas.
- **Public acceptance:** he takes the AI backlash seriously. Societies that want technological change get more of it, and acceptance grows with everyday use.

## Part 2 — Technical insights

### Model family

Nemotron 3 comes in three mixture-of-experts sizes, each activating about a tenth of its parameters per token.

| Model | Total parameters | Active parameters | Positioning |
| --- | --- | --- | --- |
| Nemotron 3 Ultra | 550B | 55B | Most capable; pre-trained in 4-bit |
| Nemotron 3 Super | 120B | 12B | Most popular; best cost/intelligence balance; pre-trained in 4-bit |
| Nemotron 3 Nano | 30B | 3B | Tasks needing less knowledge or reasoning |

### Architecture

- **Hybrid Mamba-Transformer:**
  - A 2024 Nvidia paper swept the mix and found the best model is mostly state-space layers (Mamba) with a little full attention.
  - The hybrid is smarter than either alone, independent of speed.
  - State-space layers compress the whole sequence into a fixed-size state, which helps global, "impressionistic" understanding.
  - Attention retrieves specific details exactly, with no lossy compression.
  - Speed bonus: state-space memory stays constant as the sequence grows, so larger batches fit on the GPU.
  - Others have adopted the approach, such as Qwen's hybrid models and Kimi's linear attention.
- **Mixture of experts:**
  - A learned router in each layer sends each token to a subset of experts.
  - His analogy is a library: you read only the books you need.
  - He calls MoE the default for frontier AI "for a long time."
- **LatentMoE (new in Nemotron 3):**
  - Each token's vector is compressed before it travels over NVLink to its experts, and expanded at the other end.
  - This saves network bandwidth and gives 4× more experts at the same inference cost.
- **1M-token context:**
  - Long context lets users attach codebases, instructions or a whole mailbox to a query.
  - Context compaction (summarising old context) works well in agent loops, but native long context is more useful.

### NVFP4 pre-training

- **The feat:** Nemotron 3 Super and Ultra were pre-trained entirely in 4-bit arithmetic (NVFP4).
- **What 4-bit means:**
  - Each number has only 16 possible values.
  - Groups of numbers share an 8-bit scaling factor ("block-scaled" formats).
- **Why:**
  - Much higher throughput on Blackwell Ultra GPUs.
  - Less memory, and less energy to move numbers on and off the chip.
- **The hard part:**
  - 4-bit inference is now routine; 4-bit pre-training is not.
  - The optimiser is sensitive to coarse numbers, so a run can diverge. Avoiding that required new algorithms.
- **How it was decided:** leadership chose to invest in FP4 hardware and flagged the opportunity. The technical solution came from researchers who volunteered for it.

### Multi-token prediction

- **The insight:**
  - At low batch sizes, such as fast interactive use or one local user, generation is limited by reading weights from memory, and the arithmetic units sit partly idle.
  - Pushing five tokens through the same weights costs about the same time as pushing one.
- **How it works:**
  - The model drafts several tokens at once.
  - The next pass checks them: correct ones are kept and wrong ones discarded.
  - Accuracy never drops, because every draft is verified.
- **Payoff:**
  - If all drafts are accepted, generation runs about 4× faster.
  - Real speed-up depends on the acceptance rate, so a more accurate model is also faster and cheaper to run.

### Hardware co-design

- **NVL72 was built for mixture of experts:** 72 Blackwell GPUs can read and write each other's memory at high speed and low latency.
- **Why it matters:**
  - Experts are split across GPUs, and tokens are routed between GPUs dynamically at every layer.
  - Where each token goes cannot be predicted in advance.
- **Proof of the "first job":** Catanzaro says Nvidia could not have designed Blackwell properly without the understanding it gained from building models.

### Multi-domain on-policy distillation (MOPD)

- **Specialist teachers:** for Nemotron 3 Ultra, about 10–15 teacher models were each pushed as far as possible in one domain. Domains include science, math theorem proving, coding and agent-harness interaction.
- **One student:**
  - A single student model learns from all the teachers through reinforcement learning.
  - Each teacher supervises every token, so the reward signal is dense and the student learns fast.
  - The student ends up almost as good as each teacher in its domain.
- **Many labs use the technique.**
- **Organisational benefit:**
  - Each team improves its own teacher, so teams no longer fight over a single model.
  - Catanzaro calls this one of the challenges of building AI in 2026.

### Data

- **Purchased data:** bought from dataset vendors and released openly wherever Nvidia holds the rights.
- **Synthetic data:**
  - Generated at scale by running language models on Nvidia's own systems, and much of it is released.
  - It only helps if it adds real value and improves generalisation.

### Reinforcement learning

- **Coding is special:**
  - It is an intellectual task that created a lot of economic value.
  - That left a large body of training text and tools to check whether code works.
- **Next frontier:** much richer and more diverse environments, from which models learn both the problem and the consequences of their actions.

### Lineage

Nemotron grew out of Megatron, a 2017 systems project. Catanzaro himself is unsure of some dates.

| Date | Release | Note |
| --- | --- | --- |
| 2026 (in development) | Nemotron 4 (new) | Name clashes with the 2024 model |
| \~June 2026 | Nemotron 3 Ultra | 550B / 55B; pre-trained in 4-bit; host calls it the top US open-weight model at release |
| Shortly after Nemotron 2 | Nemotron 3 (Nano, Super) | Switched to MoE |
| 2025 | Nemotron 2 | No MoE, which left it uncompetitive against the much faster GPT-OSS 20B |
| 2024 or 2025 | Llama-Nemotron | First reasoning model built on Llama |
| 2024 | Nemotron-4 340B | Earlier model, source of today's naming clash |
| 2021 | Megatron-Turing NLG 530B | Trained jointly with Microsoft, GPT-3 era; retroactively "Nemotron 1" |
| 2017 | Megatron project starts | Systems work to train the largest transformers on Nvidia hardware, against claims only TPUs could |

**Name:** "Nemotron" combines the NeMo software team with the Megatron systems team.

### Catanzaro's path

- **2008:** joined Nvidia as a graduate student. Presented an early paper on training models on GPUs at ICML, where attendees questioned why it was there.
- **Early Nvidia work:** Copperhead, a Python-embedded GPU language that foreshadowed TensorFlow and PyTorch, then cuDNN, Nvidia's first deep-learning product.
- **Baidu:** helped build the Silicon Valley AI Lab with Andrew Ng, where Dario Amodei also worked. He praises Amodei's "strength of conviction" and says he himself was more cautious about AI.
- **2016:** returned at Jensen Huang's request to build an applied research lab.
- **DLSS:**
  - His first project back became DLSS, Nvidia's real-time AI rendering for games.
  - It is about 10× more efficient, and 23 of every 24 pixels are generated by AI.

### Research organisation

Nemotron is a cross-company effort run by mission rather than by org chart.

- **Where it sits:**
  - Catanzaro's team is part of the organisation that builds the GPU, separate from Nvidia Research.
  - About ten teams contribute, spanning enterprise software, AI software and GPU design.
- **"The mission is the boss":** people from around the company volunteer to help build Nvidia's AI.
- **Idea pipeline:**
  - Staff post ideas on an internal website.
  - Each idea goes to one of 25 area leads, who develop it or defer it to the next model.
  - The goal is that everyone feels their ideas are fairly heard.
- **Culture:**
  - Jensen Huang calls Nvidia "a company of volunteers."
  - Many senior leaders have been there for three decades, and "no one fails alone."
  - Accelerated computing is the composition of thousands of technologies: if any one fails, the whole value is lost.

### Compute allocation

- **Process:**
  - Nemotron has its own compute budget, split into programmes and then projects.
  - Requests are reviewed every two weeks, with hierarchical decisions.
- **Goal:** people should at least understand why other projects won, even if they disagree.
- **Research has to be bootstrapped:**
  - Start small, get a signal, ask for a bit more, and repeat.
  - Good results attract both resources and people.
- **Top-down versus bottom-up:**
  - Early research is mostly bottom-up.
  - Strategic bets such as 4-bit pre-training are set from the top, with the technical solution left to researchers.
