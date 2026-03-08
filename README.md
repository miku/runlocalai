# RUN LOCAL AI

Quick update on how to run your own LLM/VLM and other AI applications:
opportunities and challenges.

> 2026-04-21 13:15-14:45 [90m],
> [BMN](https://www.ub.uni-leipzig.de/standorte/medizinnaturwissenschaften),
> Leipzig University Library, [Martin
> Czygan](https://www.linkedin.com/in/martin-czygan-58348842/)

## Today

* [ ] landscape of open LLM [10]
* [ ] landscape of applications for local use, for macOS, Windows or Linux [10]
* [ ] install and try [25]

In a second part, we try to assess, what kind of work a local LLM can or cannot do:

* [ ] grammar checks, text work, summarization (system prompt)
* [ ] literature review (analyzing documents)
* [ ] coding help (agent)
* [ ] sandboxed claws (generic tasks)

## Reminder

You will be using AI tools best, when you have developed an expertise in a
subject. You may call it
[KI-Fachkompetenzschwelle](https://barbarageyer.substack.com/p/ki-fachkompetenzschwelle).

## Background

A recording of one my first sessions with a local model (2023-04-18, 20w):

![](static/578575.gif)

An a longer journey:
[#35](https://golangleipzig.space/posts/meetup-35-wrapup/),
[#38](https://github.com/miku/localmodels),
[#51](https://github.com/miku/nightjet/blob/main/notes/2025-05-27-lgo-51-short-talk.md),
[WD](https://raw.githubusercontent.com/miku/ubl-wd-2024-pe/main/UBL-WD-2024-PE-MC.pdf),
[PE](https://github.com/miku/prompteng),
[E1](https://github.com/miku/aiexp-25-1),
[E2](https://github.com/miku/aiexp-25-2),
[E3](https://github.com/miku/aiexp-25-3),
[E5](https://github.com/miku/aiexp-25-5),
[E6](https://github.com/miku/aiexp-25-6),
[OI](https://github.com/miku/ollamaintro),
[KT](https://github.com/miku/localai-kith-2025),
[AG](https://github.com/miku/unplugged)

Some software I wrote with AI: [repoctx](github.com/miku/repoctx),
[minimalwave](https://github.com/miku/minimalwave),
[apodwall](https://github.com/miku/apodwall), [and more
...](https://github.com/miku/nightjet?tab=readme-ov-file#done)

## Why

* ownership vs renting
* a level of autonomy, control, privacy and freedom

[The Latent Role of Open Models in the AI
Economy](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5767103) (2025),
"Closed models dominate, with on average 80% of monthly LLM tokens using closed
models despite much higher prices — on average 6x the price of open models —
and only modest performance advantages"

> This systematic underutilization
is **economically significant**: reallocating demand from observably dominated
closed models to superior open models would reduce average prices by over 70%
and, when extrapolated to the total market, generate an **estimated $24.8
billion in additional consumer savings across 2025**.

## Why not

* usually less capable models (fewer parameters, quantized)
* you will need hardware, or access to hardware
* if you start from scratch, a useful setup may cost between EUR 1-8K (and
  since EOY25 we additionally have a full on [RAM crisis](https://en.wikipedia.org/wiki/2024%E2%80%93present_global_memory_supply_shortage))
* more initial setup, heterogeneous model landscape

Some consumer market machines in 2026:

* [AMD Strix Halo APU](https://strixhalo.wiki/Guides/Buyer's_Guide) based
  systems, [Mac mini](https://www.apple.com/de/mac-mini/), [Mac
  Studio](https://www.apple.com/de/mac-studio/), anything with an [Nvidia
  GPU](https://en.wikipedia.org/wiki/List_of_Nvidia_graphics_processing_units)

Many models will run even on single board computers (e.g. raspberry pi, N150
based boards, ...), but just slowly.

An example of performance regression caused by lower parameters counts
([source](https://old.reddit.com/r/LocalLLaMA/comments/1ro7xve/qwen35_family_comparison_on_shared_benchmarks/)):

![](static/krs0xrebcung1.png)

The Strix Halo (128GB) box runs 122B-A10B (88GB) with PE/PP of 68/21 t/s.

### Special Case: Software development

* [SWE-rebench: A Continuously Evolving and Decontaminated Benchmark for Software Engineering LLMs](https://swe-rebench.com/?insight=oct_2025)

![SWE-rebench: 01/2026](static/leaderboard_with_logos.png)

While not at the top, Kimi K2 Thinking at **#12**, GLM-5 at **#14**, GLM-4.7 at **#15** and Qwen3-Coder-Next at **#16**.

Note: except for the BF16 version, a 128GB VRAM machine could run all versions of Qwen3-Coder-Next.

![](static/screenshot-2026-03-08-234643-hf-qwen3-coder-next-128gb.png)

## Hardware requirements

Devices that you can use to run LLMs at home:

> TODO: montage of zimaboard, framework, gen8 x1, gen13 x1, p3 ultra, ...

