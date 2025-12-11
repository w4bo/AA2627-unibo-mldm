

Machine learning algorithms (e.g., classifiers) make predictions about new data *by training on old data*.

- These predictions may be hiring or not hiring, good or bad credit, and so on.

However, the training data may contain patterns such as a higher rate of good outcomes for members of certain groups.

This is quantified by the "80% rule" of disparate impact, which is a legal measure and definition of bias.

- $\frac{\text{Rate of unprivileged applicants receiving good outcome}}{\text{Rate of privileged applicants receiving good outcome}} < 0.8$

It is ethically and legally undesirable for a classifier to learn these biases from the data.

We propose two methods of modifying data, called Combinatorial and Geometric repair.
We test our repairs on three data sets.
Experiments show that our repairs perform favorably in terms of training classifiers that are both accurate and unbiased.

# Regulations

Regulation without enforcement is meaningless.
We have to go beyond obsession for regulation.

# Racism

Racism and AI: Bias from the past leads to bias in the future.
https://www.ohchr.org/en/stories/2024/07/racism-and-ai-bias-past-leads-bias-future

# Datasets

Can we change our datasets?
Images on the internet are even more sexist than texts.
You go back in time, how would that community be like when taking selfies.

From training to teaching AI

*Training*

- Repetition and optimization
- Reproductive approach

*Teaching*

- Dialogic and social processes
- Reflexive approach
- Data as communicative practices
- Data encodes values, contexts, and cultures
- Goal of diversification

De-biasing datasets

- Should be continuous over time since society is changing.
- Public institutions should push towards open data, but what about the private sector?
    - Burden of the proof should fall on the provider.
    - Privacy was dealt with consent, do not make the same mistake again.

CVs

- Identity & agency: is it descriptive or discriminative?
- Networks of Visibility: de-anonymization based on connections

GeoAI


# Fair division

Distributing resources in a way that each perceives the division as fair

- Some things are indivisible

*Comparison-based*: no one envies anyone else (but I need to know all the assignments)

- Envy free (up to 1 good)

*Threshold-based*

- Proportionality (up to 1 good)

Computational feasibility is NP-complete
What happens if there is no fair solution?

Social impact metric

- Find a fair solution and maximize its social impact (Price of Fairness = best possible solution / best social impact of a fair solution)
- Individual vs group fairness: the goal is also to counter historical disadvantages (this is about pink quotas)
    - You can weigh a group of people more than others when computing fairness
- Sandra Buttock paper

# AI Act

How are we implementing the AI Act?

- A lot of the requirements are not clear about their implementation
- Difficulty in terms of language (law and computer science backgrounds)

Are we also considering that not using AI sometimes is the right solution?

- E.g., do not always increase the size of the gun, but use the simplest working tools

# Privacy

Privacy hinders AI.
Fairness is the only tools to safeguard people's privacy (GDPR).

There is no technological solution to a problem that is political

Companies have created AI governance.
We need a common ground between technicians and humanistic people.
You cannot use the same metric in any scenarios
For a lot of companies AI means buying off the shelf products.

Fairness and transparency about processes goes beyond GDPR (since GDPR is only about personal data).
But if the task is only preparatory, that is not high risk, and many constraints can be dropped.
For most companies, AI is not about developing but buying.

# Social scoring

# LLMs

# Fairness and companies

Is there a chief AI office?
Fairness and explainability.
Fairness is part of the development and whole lifecycle of the project.
It is important to position wrt the AI act.

# Papers

1.
Bias preservation in machine learning: the legality of fairness metrics under EU non-discrimination law.
1.
Why fairness cannot be automated: Bridging the gap between EU non-discrimination law and AI.
1.
Compatibility of Fairness Metrics with EU Non-Discrimination Laws: Demographic Parity & Conditional Demographic Disparity.
1.
Distrust by design.
    - Accountability: how can we deal with whose fault is?
1.
Holigarcs book.

# Other examples

Biases in the definition of the target variable are especially critical, because they are guaranteed to bias the predictions relative to the actual construct we intended to predict, as is the case when we use arrests as a measure of crime, or sales as a measure of job performance

If our target variable is the idea of a "good employee," we might use performance review scores to quantify it.
This means that our data inherit any biases present in managers' evaluations of their reports.
Another example is the use of computer vision to automatically rank people's physical attractiveness [10, 11].
The training data consist of human evaluation of attractiveness, and, unsurprisingly, all these classifiers showed a preference for lighter skin.

In hiring, instead of relying on performance reviews for, say, a sales job, we might rely on the number of sales closed.
But is that an objective measurement or is it subject to the prejudices of the potential customers (who might respond more positively to certain salespeople than to others) and workplace conditions (which might be a hostile environment for some but not others)?

The visual world has an essentially infinite bandwidth compared to what can be captured by cameras, whether film or digital, which means that photography technology involves a series of choices about what is relevant and what isn't, and transforms the captured data based on those choices.
Both film and digital cameras have historically been more adept at photographing lighter-skinned individuals [16].
One reason is the default settings, such as color balance, which were optimized for lighter skin tones.
Another, deeper reason is the limited "dynamic range" of cameras, which makes it hard to capture brighter and darker tones in the same image.
This started changing in the 1970s, in part due to complaints from furniture companies and chocolate companies about the difficulty of photographically capturing the details of furniture and chocolate, respectively! Another impetus came from the increasing diversity of television subjects at this time.

Even if someone else has collected the data, they are almost always too messy for algorithms to handle, hence the dreaded "data cleaning" step.
But the messiness of the real world isn't just an annoyance to be dealt with by cleaning.
It is a manifestation of a diverse world in which people don't fit neatly into categories.
Being inattentive to these nuances can particularly hurt marginalized populations.

# More issues

If subpopulations change differently over time, but the model isn't retrained, that can introduce disparities.
An additional wrinkle: whether or not disparities are objectionable may differ between cultures and may change over time as social norms evolve

# Computational fairness

*Fairness* comes from the law (article 21 of the fundamental rights)

Discrimination, different treatments

- Direct
- Indirect discrimination: something that seems neutral but applies discrimination
- Intersectional? discrimination

*Computational fairness*: algorithms should not perform any discrimination.

- We need to quantify the level of (un)fairness

*Multidisciplinary* approach is a must, at least three perspectives: legal, social, and technical

- Legal: we have a lot of regulations such as AI acts, article 21, national and sectorial regulations
- How do we move this into something quantifiable?
    - Which metrics should we use?
    - Metrics should be legally sound in terms of laws.
    - Metrics conflict with each other
    - Metrics are threshold-based: who defines the thresholds?

Fairness is contextual to the application, an application is FAIR inside some boundaries but not others.

- How do we define the boundaries?
    - Participative design (see: holistic social-legal-technical methodology for AI fairness)
- Boundaries can be based on a context