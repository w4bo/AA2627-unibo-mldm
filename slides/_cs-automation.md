# Case Study: Data Science and Automation

:::: {.columns}

::: {.column width="70%"}

Consider the following task.

> Given a query result, return insights describe the query result.
>
> This task requires to:
>
> - extract interesting patterns/insights,
> - rank them by their interest,
> - select the most interesting insights given a limited word/time budget.
>
> Everything should be automatic, and without the human in the loop

How would you do that?

What insights would you return to describe the query result?
:::
::: {.column width="30%"}

<div style="font-size:15px!important">

| productDepartment   | gender | quantity |
|---------------------|--------|----------|
| Produce             | M      | 19076    |
| Produce             | F      | 18711    |
| Alcoholic Beverages | F      | 16939    |
| Snack Foods         | M      | 16859    |
| Snack Foods         | F      | 16186    |
| Alcoholic Beverages | M      | 15399    |
| Household           | M      | 13757    |
| Frozen Foods        | M      | 13644    |
| Household           | F      | 13278    |
| Frozen Foods        | F      | 13011    |
| Baking Goods        | M      | 10404    |
| Baking Goods        | F      | 9841     |
| ...                 | ...    | ...      |
| Dairy               | M      | 8571     |
| Dairy               | F      | 8500     |
| Beverages           | M      | 6811     |
| Beverages           | F      | 6775     |
| Seafood             | F      | 947      |
| Seafood             | M      | 817      |
| Carousel            | M      | 473      |
| Carousel            | F      | 368      |

</div>

:::
::::

# Our solution: VOOL {visibility="hidden"}


:::: {.columns}
::: {.column width="60%"}

For instance, this has been done in VOOL [@DBLP:conf/adbis/FranciaGGR22] by:

1. applying existing ML techniques (modules) in a bag-of-task fashion,
2. let each module compute its own insight (in a range that is shared by all modules)
3. Compute a knapsack of the patterns extracted on time.


> Grouped by product department and sex the average quantity is 6699.
> All genders have similar quantity values.
> Facts can be grouped into 3 clusters, the largest has 22 facts and 1803 as average quantity, the second has 12 facts and 8187 as average quantity, the third has 10 facts and 15686 as average quantity.
> The 2 anomalous facts are (Produce, M) with 19076, and (Produce, F) with 18711.


The reviewer #2 found it "good old fashioned AI", and asked us to compare against LLMs and LLM-based applications.

:::
::: {.column width="40%"}

![Good old fashioned AI](https://github.com/user-attachments/assets/719bb7a2-488b-4fbc-9f22-0d7e5e3d2538)

:::
::::

# Large Language Models (LLMs)

Generative AI and LLMs have recently witnessed a huge hype even in the data science community [@DBLP:conf/nips/BrownMRSKDNSSAA20] [@openai2023gpt4]

- LLMs are autoregressive machine learning models that act as statistical next-word predictors [@bowman2023things] after being trained on huge datasets [@DBLP:conf/fat/BenderGMS21]
- Applications leveraging LLMs, such as ChatGPT, are usually oriented to general-purpose information retrieval

LLMs are powerful tools for broad natural language applications, are they a good choice for data-intensive tasks as well?

# LLM-based applications

:::: {.columns}
::: {.column width="70%"}

Several LLM-based applications have been deployed to overcome these limitations.

- There are applications for data analysis that generate and interpret code (mainly Python) to analyze datasets and support data scientists in doing analyses.
    - Applications can be deployed by LLM providers (e.g., Data Analyst [@dataanalyst])
    - or by third-party users (e.g., Data Scientist [@datascientist]).
- Intuitively, these applications allow the underlying LLM to invoke functions from external libraries when appropriate (e.g., Python's pandas, scikit-learn, and scipy) and to generate and execute external code.

:::
::: {.column width="30%"}

![Data Scientist](https://github.com/user-attachments/assets/42d12755-4833-4836-983d-e8442f80372f)

:::
::::

# Applying LLMs to query results

:::: {.columns}
::: {.column width="30%"}

<div style="font-size:15px!important">

| productDepartment   | gender | quantity |
|---------------------|--------|----------|
| Produce             | M      | 19076    |
| Produce             | F      | 18711    |
| Alcoholic Beverages | F      | 16939    |
| Snack Foods         | M      | 16859    |
| Snack Foods         | F      | 16186    |
| Alcoholic Beverages | M      | 15399    |
| Household           | M      | 13757    |
| Frozen Foods        | M      | 13644    |
| Household           | F      | 13278    |
| Frozen Foods        | F      | 13011    |
| Baking Goods        | M      | 10404    |
| Baking Goods        | F      | 9841     |
| ...                 | ...    | ...      |
| Dairy               | M      | 8571     |
| Dairy               | F      | 8500     |
| Beverages           | M      | 6811     |
| Beverages           | F      | 6775     |
| Seafood             | F      | 947      |
| Seafood             | M      | 817      |
| Carousel            | M      | 473      |
| Carousel            | F      | 368      |

</div>

:::
::: {.column width="70%"}

Imagining a session of query results, here follow the prompts of an initial query:

> You are a data scientist describing the highlights of query results.
> Given the following query result in CSV format, return the most interesting quantitative insights describing it.
> You can use any algorithm to compute the insights (e.g., the ones from scikit-learn).
> The highlights must be 100 words at most.
>
> [Query result is added here]

and the one of a subsequent query obtained by drilling down the previous one (to verify how sales are characterized by gender)

> The following is the result of a drill-down of the previous data. Given the result in CSV format, return the most interesting quantitative insights describing it also in relationship with the previous result. You can use any algorithm to compute the insights (e.g., the ones from scikit-learn). The highlights must be 100 words at most.
>
> [Query result is added here]
:::
::::

# Comparing the results (done in 2024)

:::: {.columns}
::: {.column width="30%"}

<div style="font-size:15px!important">

| productDepartment   | gender | quantity |
|---------------------|--------|----------|
| Produce             | M      | 19076    |
| Produce             | F      | 18711    |
| Alcoholic Beverages | F      | 16939    |
| Snack Foods         | M      | 16859    |
| Snack Foods         | F      | 16186    |
| Alcoholic Beverages | M      | 15399    |
| Household           | M      | 13757    |
| Frozen Foods        | M      | 13644    |
| Household           | F      | 13278    |
| Frozen Foods        | F      | 13011    |
| Baking Goods        | M      | 10404    |
| Baking Goods        | F      | 9841     |
| ...                 | ...    | ...      |
| Dairy               | M      | 8571     |
| Dairy               | F      | 8500     |
| Beverages           | M      | 6811     |
| Beverages           | F      | 6775     |
| Seafood             | F      | 947      |
| Seafood             | M      | 817      |
| Carousel            | M      | 473      |
| Carousel            | F      | 368      |

</div>

:::
::: {.column width="70%"}

<img src="https://github.com/user-attachments/assets/9ec3dbd8-a7ef-49f9-8d78-df8cf96c238b" style="height: 600px !important; max-height: 1000px !important" />

:::
::::

#

![Data Error](https://imgs.xkcd.com/comics/data_error.png)

# Running algorithms

Algorithmic tasks such as SQL querying and data mining are better handled by DBMSs and query engines since

- they are optimized for these types of operations (e.g., using R-trees to speed up clustering in Euclidean spaces);
- their answers are correct, consistent, and reproducible;
- they do not have hallucinations.

At the moment (2024), while (plain) LLMs have many strengths, they are not typically suitable for data-intensive tasks.

# Data volume and cost

- Since business data are sensitive, they are stored in private repositories (such as data warehouses) unknown to LLMs
- To feed data to an LLM, the main possibility is to use the prompt.
    - Depending on the LLM, prompts [have limits in the \#tokens (as of 2024-06)](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them) composing input and answer
    - The [OpenAI price calculator in Microsoft Azure (as of 2024-06)](https://azure.microsoft.com/en-us/pricing/calculator/?service=openai-service) estimates that using GPT-4-32K costs around \$0.06 per $10^3$ input tokens and \$0.12 per $10^3$ output tokens, where 1000 tokens correspond to almost 750 words.
      - Prompting a table with $10^5$ tuples (if feasible) costs several dollars per execution.
- LLMs now allow users to attach files to the prompt, and some LLM-based applications can even extract succinct summaries from these files and use them in place of the whole file content.
    - This can overcome the limits and cost of tokens.
    - However, if the summary process is incorrect, it will add errors and bias to the final answer.

# Additional Issues

**Interpretability**

The process that leads to the computation of the insights and their interest remains hidden and not interpretable to the end-user

- Has the model added some distortion to the data?

**Domain-specific data**

The insights returned by LLM-based applications strongly depend on the context since LLMs also leverage domain knowledge for their "reasoning"

- It is usually recommended to use semantic-rich column names to enhance data analyses.
- This domain knowledge can introduce bias and inconsistencies with the data at hand.
- For very specific domains and data types, a lack of knowledge can cause issues in the interpretation of the result.
    - For instance, in precision agriculture, having low temperatures could be bad for the production rates, but good in terms of pest control and water management.

**Domain-specific modules**

Should additional modules be necessary to produce domain-specific insights, such modules should be embedded into the LLM through prompting or calls to (external) third-party libraries.

# Additional Issues

**Libraries**

- LLMs produce good results with well-known libraries such as Python's scikit-learn and pandas.
- When less-known libraries are required, LLMs can fail to produce the necessary code.

**Development**

- Many LLM-based applications are commercial (or handcrafted) and not associated with research papers.
- Hence, following their development and deeply understanding their capabilities is often hard, also due to a lack of documentation.
    - On the one hand, this makes non-empirical comparisons between LLMs unfeasible.
    - On the other, exactly reproducing the results of empirical tests may be impossible.

# References