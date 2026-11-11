> Imported from Google Drive on 2026-11-09. Source: [AI_and_Cognitive_Decline_Research.md](https://docs.google.com/document/d/1wDgT_biJNjmCG2NXi6LOWjXmZ6Gh3R6zHbL3NRCsupQ/edit).
> Literature synthesis supporting the 'hollowed mind' and cognitive sovereignty concerns in technical training.
>
> **Supporting file for [R012](R012-spatial-memory-and-session-design.md), not a numbered record.** Sections 1, 2, and 4 were checked against the sources named in those sections (2026-11-11). Studies 1, 3 and 4 appear in the verified source list archived in learning-narrative-kit ([`sources.md`](https://github.com/cwarloe/learning-narrative-kit/blob/main/research/memory-palace-spatial-learning/sources.md), #55, #53, #56). Studies 2 and 5 are not on that list. Study 5 was not re-checked here and should be checked before it is quoted. Nothing here measures NADF learners, and none of it supports a claim that any learner has reached a level.

# AI and Cognitive Decline: Research Synthesis & Key Takeaways
A summary of current research on how artificial intelligence impacts learning, skill retention, brain connectivity, and workplace verification.

# 1. High School Math Experiment in Turkey (PNAS, June 2025)
* **Study Overview**: 839 students (9th–11th grade) across four 90-minute class sessions split into three learning environments:  
  1. **Control Group**: Textbook and notes only.  
  2. **Basic GPT-4 Assistant**: Answered student prompts directly.  
  3. **AI Tutor Group**: GPT-4 restricted to giving hints, loaded with correct solutions and common student mistakes.  
* **Key Findings**:  
  * **Practice Phase**: Basic GPT-4 students scored 48% higher during practice relative to control.  
  * **Unassisted Exam**: On closed-book exams without AI, the Basic GPT-4 group scored 17% lower than control (a 5.4 percentage point deficit against a 32.1% control average).  
  * **Root cause**: 67% of first interactions across problems in the first session, in the GPT Base arm, either repeated the question text or asked for the answer. Students often used GPT Base as a crutch by asking for and copying solutions, and they did not perceive any reduction in their learning (the paper's phrasing; "illusion of competence" is a gloss, not a quoted term).  
  * **The Tutor Effect**: Students using the AI Tutor performed 127% better during practice and showed no significant exam deficit when tested unassisted (the archived source list summarizes this as removing most of the harm).

# 2. Python Developer Skill Study (Anthropic, January 2026)
* **Study Overview**: 52 software engineers (the authors describe them as mostly junior; eligibility was weekly Python use for over a year, some familiarity with AI coding assistants, and no prior Trio use; 29 of 52 are reported to have had 7+ years of coding experience generally) given 35 minutes to complete coding tasks in an unfamiliar Python library (Trio).
  * Half used a GPT-4o assistant capable of generating full code.
  * Half worked without AI support.
  * All then took an unaided quiz covering debugging, code reading, and conceptual items (14 questions, for a total of 27 points). The authors discussed code writing as a fourth skill in the evaluation design but excluded code-writing questions from the quiz.
* **Key Findings**:
  * **Quiz scores**: The AI group averaged **50%** vs. **67%** for the hand-coding group (a statistically significant 17-point gap; the authors also describe this as 17% lower, Cohen's *d* = 0.738, *p* = 0.01).
  * **Usage behavior**: Participants whose AI use included conceptual or follow-up questions scored higher (the authors' high-scoring patterns averaged 65% or above) than those who used the assistant mainly to generate and paste code.

This study is not on the archived LNK source list. The figures above were checked against the public Anthropic write-up and the arXiv preprint (2601.20245v2), not a peer-reviewed PDF. The 50% and 67% means are from the public write-up; the preprint reports a 4.15-point difference on the 27-point quiz, described as a 17% score difference, with the same Cohen's *d* and *p*. The 14-question count, 35-minute cap, and 29-of-52 experience figure are from the preprint (section 4 and Table 1).

# 3. "Your Brain on ChatGPT" EEG Study (MIT, June 2025 Preprint)
* **Study Overview**: 54 participants (ages 18–39) wrote SAT-style essays while EEG caps measured brain connectivity across three groups: ChatGPT-only, Search Engine-only, and No-Tools.  
* **Key Findings**:  
  * **Brain Connectivity**: The ChatGPT group exhibited up to **55% lower brain connectivity** during writing compared to the no-tools group.  
  * **Information Retention**: 83% of the ChatGPT group could not quote a single sentence from their essay immediately after writing (vs. 11% in other groups).  
  * **Session 4 Swap Experiment**:  
    * **Struggle First**: Participants who wrote on their own first before gaining access to ChatGPT showed high brain connectivity and retained memory of their work (7/9 quoted correctly).  
    * **AI First**: Participants who relied on ChatGPT first and then lost access showed poor recall (1/9 quoted correctly).

# 4. AI Trust and Critical Thinking in the Workplace (Lee et al., CHI 2025; LNK #56)
* **Study Overview**: Survey of 319 knowledge workers who use generative AI weekly, reporting 936 real-world work tasks.
* **Key Findings**:
  * Participants self-reported enacting some form of critical thinking on 555 of 936 tasks (59%). That is a self-report of critical-thinking enaction, including goal setting, prompt refinement, and assessing output, not a measured rate of checking or scrutinizing AI output.
  * Higher confidence in GenAI was associated with less reported critical thinking; higher self-confidence in the task was associated with more. Overall trust was reported as not significantly related to whether critical thinking was enacted.

Do not quote a 50% drop in verification per 1-point trust increase, or +30% / +36% odds on verification drivers, unless those figures are located in the paper. The Lee et al. PDF could not be retrieved in this pass, so the overall-trust clause was not re-checked against the paper, and the 50% / +30% / +36% figures remain unverified.

# 5. Digital Technology & Long-Term Cognition Meta-Analysis (Nature Human Behaviour, April 2025)
* **Study Overview**: 57 studies following 411,430 adults (age 50+) over 1–18 years.  
* **Key Findings**:  
  * General digital technology use was associated with **58% lower odds of cognitive impairment** and a **26% slower rate of cognitive decline**. These are associations in older adults using digital technology in general, not AI, and do not show cause.

# Strategic Recommendations & Best Practices
1. **Struggle First**: Engage with a problem independently before requesting AI assistance to ensure active cognitive processing.  
2. **Use AI as a Tutor or Challenger**: Prompt AI models to provide hints, challenge assumptions, or play devil's advocate rather than writing final solutions.  
3. **Mandate Verification Workflows**: Build review and verification steps into task pipelines, particularly for junior staff or unfamiliar topics.
