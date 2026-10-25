# FG-TIDA Working Group Charter Template

*Version 1.0 — 21 October 2026. Draft for discussion with the FG-TIDA management.*

See the template live:
📄 [Web page](https://fg-tida.github.io/wg-charter-template/)
· 📑 [PDF](https://fg-tida.github.io/wg-charter-template/wg-charter.pdf)

The pages you see there are produced by this repository — they double as the
template's documentation, explaining and demonstrating how to write a wg charter.

> **Starting a new charter?** Follow
> **[WG-ONBOARDING.md](WG-ONBOARDING.md)**. Once your repo is created, replace
> the text of this README with a short description of *your* specification
> (what it is, its status, and a link to its published site).

---

A specification for the FG-TIDA working groups, authored with the shared TIDA wg charter
template: one source that builds a modern web page and a print-ready PDF, with
support for diagrams and auto-generated API references.

## Quick start

1. Click **Use this template → Create a new repository** (owner `FG-TIDA`, name
   `FG-TIDA WG<n>: <Full name of the working group> (<ACRONYM>)`).
2. In the new repo: **Settings → Pages → Source: GitHub Actions**.
3. Edit the content under `src/doc/` — replace the `<placeholders>` and the
   example text. Full instructions are in **[WG-ONBOARDING.md](WG-ONBOARDING.md)**.
4. Push to `main`. The site and PDF publish automatically to
   `https://fg-tida.github.io/<repo-name>/`.

## In this repository

- `src/doc/index.rst` — the document details.
- `HOWTO.md` — how to build and preview locally, and how to customise.
- `WG-ONBOARDING.md` — the full step-by-step guide for authors to create charters.


This repository is the official template for drafting and publishing FG-TIDA Working Group Charters.

This template is for the charters of the FG-TIDA working groups. It is modelled on the charters of approved IETF working groups, adapted to an ITU-T Focus Group.

## How to use this template

- Keep the charter short: one to two pages, about 600–1,200 words. Like the IETF, the charter is a contract on scope and deliverables, not a tutorial or a position paper.
- Every section marked **[Mandatory]** must be present, even if it is short. Sections marked **[Optional]** are added only when they carry real content.
- Delete all the *guidance* text in italics before circulating a charter.
- Write in the future tense and in the third person ("The working group will develop …"). Avoid "we", marketing language, product names and company names in the body.
- One charter per working group. When the scope changes, revise the charter with a new version number rather than stretching the existing text.

### What the IETF charters were used as models

These approved IETF charters were reviewed on the IETF Datatracker to derive the structure:

| Charter | Why it is a useful model |
|---|---|
| [WIMSE](https://datatracker.ietf.org/doc/charter-ietf-wimse/) (workload identity) | Clear list of what it will **not** define; each deliverable tagged with its intended output type ([PS], [I], [BCP]); explicit liaisons (CNCF/SPIFFE, OpenID Foundation). |
| [RATS](https://datatracker.ietf.org/doc/charter-ietf-rats/) (remote attestation) | Short introduction defining the roles; goals stated with explicit out-of-scope sentence; numbered programme of work. |
| [SCITT](https://datatracker.ietf.org/doc/charter-ietf-scitt/) (supply-chain transparency) | Numbered problem statement; separate **Non-Goals** section; programme of work grouped by work area. |
| [OAuth](https://datatracker.ietf.org/doc/charter-ietf-oauth/) (delegation, incl. automated agents) | Compact "Work Program" and "Coordination" sections; shows how to frame agentic delegation in a charter. |

The general rule for charter content comes from [RFC 2418 (BCP 25), section 2.2](https://www.rfc-editor.org/rfc/rfc2418#section-2.2): name, chairs, mailing list, a description of the group and its objectives, and goals and milestones.

### IETF practice adapted to FG-TIDA

| IETF element | FG-TIDA equivalent |
|---|---|
| Responsible Area Director | FG-TIDA co-chairs (and, through them, the parent Study Group, ITU-T SG17) |
| [PS] / [I] / [BCP] tags on deliverables | Output type of the Focus Group deliverable, e.g. [TR] technical report, [TS] technical specification, [UC] use-case document, [GL] guideline, [IN] input to SG17 |
| Internet-Draft adopted by the WG | Draft deliverable in the FG-TIDA repository (GitHub) |
| Milestones on the Datatracker | Milestones aligned with the FG-TIDA meeting calendar and its terms of reference |
| IESG charter approval | Approval by the FG-TIDA plenary, within the terms of reference agreed by SG17 |

---

## Charter template

```markdown
# FG-TIDA WG<n>: <Full name of the working group> (<ACRONYM>)

Charter version: <v0.x> — <date> — <status: draft / under review / approved by FG-TIDA on <date>>
```

### 1. Group information [Mandatory]

| Field | Content |
|---|---|
| Working group name and acronym | |
| Theme(s) of the FG-TIDA terms of reference covered | |
| Chair(s) / co-chairs | |
| Editor(s) of the main deliverables (if known) | |
| Mailing list | |
| Repository (GitHub) and issue tracker | |
| Charter status and version | |

*Guidance — write:* names and affiliations only here, nowhere else in the charter; the exact link to the repository.
*Do not write:* biographies, titles of honour, or people who have not agreed to serve.

### 2. Background and problem statement [Mandatory]

*Guidance — write:* two to four short paragraphs, or a numbered list of problems (as in SCITT). State the problem, who has it (people, organisations, agents), and why existing work does not solve it. Define the key terms in one sentence each when they are needed to read the rest of the charter (as RATS does for Attester, Verifier and Relying Party).
*Do not write:* the history of the topic, a literature review, a proposed solution, or claims about any one vendor's product. Do not use undefined buzzwords ("trust layer", "AI-native") without saying what they mean here.

### 3. Goals [Mandatory]

*Guidance — write:* what the working group will produce and to what end, in three to six sentences or bullets. Say whether the work is to describe (use cases, terminology, gap analysis), to specify (formats, interfaces, protocols) or to recommend (guidelines, best practices). Say that the group builds on existing work where it can (as WIMSE does with OAuth, JWT and SPIFFE).
*Do not write:* open-ended goals ("and any other related topics"), or goals that only the parent Study Group can achieve (for example, approving ITU-T Recommendations).

### 4. Scope and non-goals [Mandatory]

- **In scope**
- <item>**Out of scope (non-goals)**
- <item>*Guidance — write:* an explicit list of what the group will **not** do. This is the section the IETF charters rely on most to prevent scope creep (WIMSE lists four things it "will not define"; SCITT has a separate "Non-Goals" section). Name the neighbouring topics that belong to other FG-TIDA working groups, to SG17 Questions, or to other organisations.
*Do not write:* a non-goal that is in fact a goal of a sister FG-TIDA working group without saying which one; or a scope so wide that two working groups could both claim the same deliverable.

### 5. Programme of work and deliverables [Mandatory]

| # | Deliverable | Output type | Short description | Input documents (if any) |
|---|---|---|---|---|
| 1 | | [UC] / [TR] / [TS] / [GL] / [IN] | | |

*Guidance — write:* a numbered list of concrete documents, each with its output type (the FG-TIDA equivalent of the IETF [PS]/[I]/[BCP] tags) and one to three sentences on what it contains. If a candidate draft already exists, name it as an input (as WIMSE names its use-case draft) — an input, not an adopted text.
*Do not write:* deliverables with no clear end ("ongoing analysis"); more deliverables than the group has editors for; or text that commits the group to adopt a specific contribution.

### 6. Milestones [Mandatory]

| Target date | Milestone |
|---|---|
| <meeting / month> | First draft of deliverable 1 in the repository |
| <meeting / month> | Deliverable 1 agreed by the working group |
| <meeting / month> | Deliverable 1 submitted to the FG-TIDA plenary |

*Guidance — write:* dated, checkable steps tied to the FG-TIDA meeting calendar (first draft, working-group agreement, submission to the plenary). Keep them realistic; they can be updated without rechartering.
*Do not write:* milestones beyond the life of the Focus Group, or dates that depend on another body's decision without saying so.

### 7. Coordination, dependencies and liaisons [Mandatory]

*Guidance — write:* the other FG-TIDA working groups, the SG17 Questions concerned, and the external bodies the group expects to work with, each with one line saying on what. The IETF models are WIMSE (OAuth, SCITT, RATS, CNCF/SPIFFE, OpenID Foundation) and OAuth (WIMSE, SPICE, the EU Digital Identity Wallet).
*Do not write:* a long list of every organisation in the field. Name only the ones with a real dependency, and do not imply an agreement that does not exist.

### 8. Terminology [Optional]

*Guidance — write:* a pointer to the FG-TIDA terminology work, plus the three to five terms specific to this group.
*Do not write:* a full glossary in the charter.

### 9. Working methods [Optional]

*Guidance — write:* only what differs from the FG-TIDA general working methods, e.g. how the repository and issues are used, how drafts are adopted, interim calls.
*Do not write:* a repeat of the ITU-T or FG-TIDA rules.

### 10. Security and privacy considerations [Optional — recommended]

*Guidance — write:* one short paragraph on the security and privacy aspects the group's deliverables must address (for example, the risk of linkability or surveillance when identifying people and agents).
*Do not write:* a generic disclaimer.

### 11. Success criteria and conclusion [Optional]

*Guidance — write:* how the group will know it has finished (for example, all deliverables submitted to the FG-TIDA plenary), and what happens next (input to SG17, transfer to a Question, closure).
*Do not write:* outcomes that depend on later approval by SG17 as if they were guaranteed.

### 12. Revision history [Mandatory]

| Version | Date | Change |
|---|---|---|
| 0.1 | | First draft |

---

## Quick checklist before submitting a charter

- Is it no longer than about two pages?
- Does every deliverable have an output type and at least one milestone?
- Is there an explicit list of non-goals?
- Are overlaps with the other FG-TIDA working groups and with SG17 Questions named?
- Are people's names only in section 1?
- Has all the guidance text been removed?
