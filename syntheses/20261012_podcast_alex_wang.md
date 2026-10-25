# Meta MSL — Zuckerberg and Wang on Muse Wonder (2026)

Oct 25, 2026 · @Al

## Source and caveats

Everything below is Meta's own account at a model launch, given to a commercial partner, so benchmark, growth and cost figures are self-reported.

- **Source:** podcast conversation with Mark Zuckerberg and Alexandr Wang (Meta Superintelligence Labs, MSL), interviewed by a Stripe co-founder, most likely John Collison **\[à vérifier\]**. Recorded around the Muse Wonder launch, autumn 2026; exact date **\[à vérifier\]**.
- **Partner relationship:** Stripe powers Muse payments and has agreed to acquire OpenRouter, which distributes Muse Wonder. The episode includes an OpenRouter ad read.
- **Transcript quality:** auto-generated with no speaker labels. Attributions to Zuckerberg or Wang are inferred from context.
- **Name fixes:**
  - "Marc" is Mark Zuckerberg; "Alex" is Alexandr Wang.
  - "Nat" is Nat Friedman; "Daniel" is Daniel Gross; "Susan" is Susan Li (CFO).
  - "OpenRadar" is OpenRouter; "Muse Wanderer" and "Wonderland" are Muse Wonder.
- **Cross-check with the Mistral doc:** the $100–200bn cheque Pierre Stock attributed to Wang is said here by Zuckerberg, loosely ("I don't know, like $100 billion, $200 billion"). It refers to the commitment made at the end of 2025, before Meta had seen the models.

## Part 1 — Roadmap, ambitions, bottlenecks

### Roadmap

Muse Wonder ships now as Meta's first frontier-class model; the next goal is Wonder-level quality at Spark cost, on clusters scaling to 5 GW.

| Model | Codename | Status | Where available |
| --- | --- | --- | --- |
| Muse Spark (1 → 1.3) | Avocado | Shipping; one pre-train (end 2025), point releases are RL only | Free tier of Muse |
| Muse Wonder | Watermelon | Launched in this episode; much bigger pre-train | Muse paid plans, Meta Model API, OpenRouter, Muse Code |
| Muse Wonder Full | — | Launched; higher-end version | Muse Code subscribers |
| Spark-sized model at Wonder level | — | Stated goal, "not too far from now" | Free Muse, for hundreds of millions of users |

- **Cadence:** the gap between successively bigger model classes should now shorten. Meta says its work from here on pushes the frontier, after a catch-up phase.
- **Naming:** Wonder ships without a version number. The first dot release will force a naming decision, and the fruit codenames have run out.
- **Compute:**
  - Prometheus (Ohio) is scaling past 1 GW.
  - Hyperion (Louisiana) scales to 5 GW over a couple of years.
  - Both were planned in 2023–24, before MSL existed. Zuckerberg's exact words (\~49:44): "we built this Prometheus cluster, we call it, in Ohio. \[…\] That's scaling to larger than a gigawatt. And now we're building this Hyperion cluster in Louisiana that's going to scale to 5 gigawatts." On timing (\~50:40): "I guess the Louisiana one will come online over a couple years."
- **Devices:**
  - Muse voice mode (not fully rolled out) separates speakers in a room.
  - Display glasses are shipping. Long term, glasses become a purely multimodal product, possibly without an app store.
  - Muse Gadgets opens Muse to third-party hardware; phone makers have approached Meta.
  - HomeLink, a USB dongle, connects Muse to home devices.
- **Commerce integration path:**
  - Browser and computer use are trained into the model, so no business has to integrate.
  - Key partners get direct API access.
  - Meta will also build agents for businesses, as standard as a website or an email address is today. Muse agents talk to these business agents directly, so they no longer need to browse websites. Muse will work with other vendors' business agents too, but best with Meta's.
- **Revenue lines:**
  - subscriptions
  - a small cut of money Muse saves or makes for users
  - the API
  - a new Meta Enterprise Platform led by CJ Desai
  - a "business in a box" for small businesses

### Ambitions

Meta aims to own the consumer and small-business agent lane end to end, from data centres to devices, with models trained for that use.

- **Personal superintelligence:**
  - Personal and professional agents for billions of users.
  - Meta sees this lane as open because rivals concentrate on automating knowledge work and coding.
  - Zuckerberg ranks invention and creation above automation as the highest use of superintelligence.
- **"The model is the product":**
  - Products are getting thinner, and the model carries personality, proactivity and tool use.
  - Product decisions are specified through training methods, data and evals.
  - Muse has no model selector and no effort selector.
- **Frontier claim:** Wang calls Wonder the best model in the world for personal-professional agents. Details are in the benchmark table in Part 2.
- **Team of experts:** the agent should act as the user's legal, finance, medical and tax team.
- **Full stack:**
  - Meta builds its own data centres, chips, low-level infrastructure, models and devices.
  - Zuckerberg expects a small handful of companies to build frontier superintelligence and to drive the agenda.
- **Alignment doctrine:**
  - Alignment means serving the user: reliable instruction following and no moralising.
  - Catastrophic requests should be refused gracefully.
  - He presents this as different from other labs' approach.
- **Ecosystem stance:**
  - Meta favours a diverse ecosystem with checks and balances, and praises Nvidia's support for open source.
  - Zuckerberg calls concentration in a couple of companies the riskier configuration.
  - *Interpretation:* no open-weight release of Wonder is mentioned. Distribution runs through Muse, the Meta API and OpenRouter.
- **Muse traction:**
  - The interviewer cites third-party reports ranking Muse as possibly the fastest-growing AI app.
  - Zuckerberg calls the launch a home run and says growth tooling was not ready.
- **Agentic commerce:**
  - Meta expects agentic demand to take a growing share of commerce.
  - It expects agents to hold their own accounts, which would enlarge the market.
  - Zuckerberg became a weekly Instacart user through Muse.
- **Self-funding:**
  - The core ads business underwrites the build-out, and the models also accelerate that business.
  - Asked whether this will make money, Zuckerberg says "the answer better be yes."
- **Organisation as strategy:** talent density, a flat structure, no non-technical managers, and compute concentrated on a few people.

### Bottlenecks

Capital at risk is the dominant constraint, with data supply and serving cost close behind.

- **Capital and risk:**
  - At the end of 2025, Meta committed roughly $100–200bn before seeing the models, on a progress report and a few plots.
  - CFO Susan Li repeatedly warned Wang that the model had to work.
  - The interviewer raises free-cash-flow pressure across hyperscalers; the passage is garbled **\[à vérifier\]**.
  - Zuckerberg's hedge: if Meta's model fails but AI works, others will buy the compute. If AI fails overall, Meta still has internal uses for it.
- **Serving cost:**
  - Wonder is too expensive to serve for free, so free users stay on Spark.
  - Inference capacity had to be built years ahead for a product that did not yet exist.
- **Data:**
  - Bigger models need more data or they overfit, and the internet is not growing fast enough.
  - Zuckerberg names "where's the data coming from?" as an open problem and closes the topic there.
  - Some corpora transfer negatively when mixed.
- **Long, blind feedback loops:**
  - Wonder has been planned since August 2025.
  - Pre-training gives few samples, and key decisions precede any proof point. Wang calls this the opposite of Lean Startup.
- **RL safety pressure:** heavy RL in an environment where only a misaligned action succeeds teaches misalignment, so every environment needs curation.
- **Benchmarks:** public ones saturate fast and invite benchmaxing. Meta moved to internal evals, which outsiders cannot check.
- **Organisational strain:**
  - The Llama 4 trajectory forced a full reboot of the team.
  - Wang recalls a former lead arguing Meta did not need a reasoning model.
  - Large parts of the company pivoted to support MSL, straining its finances. Zuckerberg calls it a "level 10 out of 10" effort, still ongoing.
- **Agent adoption:**
  - Some businesses may block agents, and computer use is only a stopgap.
  - The product works only at very high reliability.
- **Open capability gaps:**
  - Memory still has "plenty of room to improve."
  - Voice still struggles with turn-taking, and spoken output is a slow way to receive information.

## Part 2 — Technical insights

### Model line

Meta climbs a ladder of pre-trains, each roughly 4–5× bigger than the last, and discloses no parameter counts, architecture or token counts.

- **Muse Spark (Avocado):**
  - Pre-trained at the end of 2025; Meta calls it "not that big."
  - Spark 1 → 1.3 changed only the RL recipe. Meta says the jump feels like a different pre-train.
- **Muse Wonder (Watermelon):**
  - The next pre-train, "significantly bigger." Spark was planned as a stepping stone to it.
  - A large share of Meta's compute went into its pre-training.
- **RL-to-pre-training ratio:** lowest in a new class's first release, rising with each point release.

### Capabilities trained into the model

- **Active memory:**
  - The model itself handles memory, including compaction, with a supporting system around it.
  - Meta built an internal "Memory Bench" eval.
- **Active focus:** completing long-horizon tasks and finding other routes after setbacks, "in an aligned way."
- **Domain expertise:** finance, legal, health, tax, shopping and personal advice, seeded in pre-training data and then reinforced.
- **Coding:** a large step up; see the benchmark table.
- **Discretion:**
  - The model uses what it knows about the user while disclosing as little as possible to third parties.
  - Example: booking a restaurant without revealing a medical condition.
- **Multimodality:**
  - Pre-training included heavy visual-perception data.
  - Zuckerberg's MMA example: the agent wrote its own video pipeline, pulling stills from gym cameras.
  - It then optimised that pipeline to give feedback within a 60-second break between rounds.
- **Browser and computer use:** trained in, so Muse works with any website.
- **Voice:** voice mode separates speakers.

### Pre-training

- **Data:**
  - Public internet, books and proprietary data, plus images, audio and video for perception.
  - At this stage volume matters more than format.
- **Domains belong in pre-training:** capabilities you want, such as finance or health, should be in the pre-training mix. RL at the end is not enough.
- **Data scales with model size:** bigger models need proportionally more data or they overfit. Corpora can transfer positively or negatively to each other.
- **Science with few samples:**
  - Each run is costly, so inference relies on careful reasoning.
  - Signals come from perplexity-based evals during pre-training and from benchmarks during RL.
  - Researchers literally hold protractors to curves on their monitors.
- **Proof point:** the team expected Wonder to need a while in RL before beating Spark. It beat Spark almost immediately.

### Post-training

- **SFT** initialises behaviours and shapes personality. After SFT, a behaviour might appear \~10% of the time.
- **RL** then raises how reliably those behaviours are elicited.
- **Scale everything together:**
  - RL compute and data are a main scaling axis.
  - RL has to scale with the pre-train; scaling one factor alone is suboptimal.
- **Less is more in RL:** smaller, higher-quality data often works better, an intuition inverted relative to pre-training.
- **Environments carry the intent:** the design of tasks and environments is where product choices enter training.
- **Alignment runs through all of RL:** every environment is checked so that no setup rewards unsafe or misaligned behaviour.
- **Harness co-optimisation:** tuning the agent harness together with the model is another scaling axis.
- **Industry trend:** labs are extracting far more agentic capability from existing base models through better RL recipes.

### Evaluation

Meta now steers mostly by internal evals and treats public benchmarks as early "signs of life."

- **Public benchmarks:** they saturate quickly. Leaning on them outsources product thinking to whichever PhD student built a viral benchmark.
- **Internal evals:** a spreadsheet of small product capabilities, each worth perhaps 2% to users.
- **"Big model smell," quantified:**
  - Meta plots scores on tasks targeted in post-training ("in-distribution") against tasks it did not target ("out-of-distribution"), at several reasoning-effort levels.
  - Comparing Spark 1.3 with Wonder Full: for a given in-distribution score, Wonder Full does better out of distribution than the Spark trend predicts. Meta credits the larger, stronger base model.
  - The metric is described in Meta's Wonder research blog post ([Meta AI Research, 12 Oct 2026](https://research.meta.ai/blog/muse-wonder), section "Capabilities That Generalize").

### Benchmark claims (self-reported)

| Benchmark or area | Meta's claim |
| --- | --- |
| Personal and professional agent evals (internal) | State of the art "based on our measurement" |
| DeepSWE, SWE-Marathon | State of the art |
| Terminal-Bench 4 | "Does very well" |
| Finance and legal evals | State of the art on many |
| Memory Bench (internal) | Strong, with "plenty of room to improve" |
| Overall, against other frontier models ("Astra", Fable) | At the frontier "by the benchmarks" |

### Compute economics

Zuckerberg puts a frontier model at tens of billions of dollars all-in; all figures below are his orders of magnitude.

| Item | Figure | Note |
| --- | --- | --- |
| Prometheus cluster (Ohio) | >1 GW | Coming online now |
| Hyperion cluster (Louisiana) | 5 GW | Online over a couple of years |
| Operating 1 GW for a year | \~$15bn | "On the order of" |
| Building 1 GW (capex) | \~$50–60bn | Paid upfront |
| Training a frontier model, all-in | Tens of billions of dollars | From internal financial roll-ups |
| Commitment made at end of 2025 | \~$100–200bn | Made before seeing the models |

- **Research costs as much as the run:** each change is tested up the ladder of scales, so research costs roughly as much as the final run.
- **Lab strength:** Meta measures it by the size of the largest single training supercomputer, the machine that can host one large training run (Zuckerberg, \~49:29). The logic, implied rather than spelled out: a frontier pre-train runs on one tightly connected cluster, so the largest cluster caps the largest possible run, whatever the total compute spread across sites. Meta's examples are Prometheus (>1 GW), where Wonder was trained ([Meta AI Research](https://research.meta.ai/blog/muse-wonder)), and Hyperion (5 GW).
- **Accounting advantage:**
  - Owned data centres are capex, depreciated over years; labs renting cloud pay annual rates.
  - Researcher salaries are expensed, although the models they produce last years.
  - Zuckerberg says an H100 is worth more today than a year ago because compute is scarce.

### Organisation

- **Size:** the research team is under 200 people, "closer to 100," plus infrastructure staff.
- **Per-stage teams:** tens of people per training stage at Meta, against hundreds at other labs.
- **Compute per researcher:** high. Compute is concentrated on key people and never spread across competing internal efforts.
- **Flat structure:**
  - Wang has close to 200 direct reports on paper, with team leads in practice.
  - There are no non-technical managers, and leaders are expected to code and use agents.
- **Timeline:**
  - Llama 4 launched in April 2025.
  - Zuckerberg contacted Wang around 20 April 2025.
  - MSL is just over a year old.

### Product architecture

- **Dedicated VM per agent:** each agent runs on its own virtual machine, which Meta calls key to security and privacy.
- **Privacy and security model:** governing the data users connect is the main product surface outside the model.
- **Proactivity:** when and in which context the agent acts unprompted is a key differentiator, set through training.
- **Agent-to-agent:** Muse agents will work with any business agent, and best with Meta's own.
- **Personalisation:**
  - Muse sees family, friends and coworkers across contexts.
  - Meta contrasts this with siloed recommender systems that see one slice of a person.

### Ecosystem

- **Why no winner-take-all so far** (Wang):
  - Every lab alternates between strong and weak execution, which evens out over time.
  - Distillation spreads capability: small models today beat the biggest models of one or two years ago.
  - Many researchers and companies prefer a plural outcome and act on that preference.
- **Model diversity:** frontier models now diverge in focus, which shared benchmarks hide. Wang sees room for richer, "sommelier"-level comparison of models (\~1:34:17–1:35:39).
- **OpenRouter:** the Stripe ad read says it routes over 10 trillion tokens a day (sponsor claim).
