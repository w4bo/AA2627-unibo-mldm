---
subtitle: Business understanding
---

#

<img src="./img/crispdm_bu.svg" class="center-img">

# Business Understanding

(*Perhaps the most important/hard phase of any data mining project* [@shearer2000crisp])

The **business understanding** phase focuses on

1. Determining the *business objectives*
2. Assessing the *context of the analysis*
3. Determining and *translating objectives into data mining goals*
4. Producing the *project plan*

It is essential to understand which data should later be analyzed and how

# <img src="./img/cs.svg" class="title-icon" /> Business Understanding: Brown Spot {background-color="#121011"}

{{< include _cs-brownspot.md >}}

# End of the case study {background-color="#121011"}

Back to CRISP-DM: Business understanding

# Determine the Business Objectives

**Understanding a client's true goal** is critical to uncovering the important factors involved in the project

- Data analysts must uncover the primary business objective as well as the related questions the business would like to address
- Ensure that the project *does not produce the right answers to the wrong questions*
- Beware of *setting unattainable goals*
- Make sure that each *success criterion relates to at least one of the specified business objectives*

> The business goal could be to retain current customers by predicting when they are prone to move to a competitor
>
> - "How does the primary channel (e.g., ATM, branch visit, Internet) of a bank customer affect whether they stay or go?"
> - "Will lower ATM fees significantly reduce the number of high-value customers who leave?"

# Assess the Situation

**Outline the available resources** to accomplish the data mining project, from personnel to software

- *Discover what data is available* to meet the primary business goal
  - Do you have data that's relevant to the question?
    - Do you have measures of the target and features that are related to the target?
    - Do you have an accurate measure of your model target and the features of interest?
  - An existing system might not have the data it needs to address a problem and achieve a project goal
    - Find external data sources or update your systems to collect new data

> To address the business question, a minimum number of customers over age 50 is necessary

- List the *project risks and potential solutions* to those risks
- List the *assumptions* made in the project
- Create a *glossary of business and data mining terms*
  - This is essential in interdisciplinary teams!
- Construct a *cost-benefit analysis* for the project

#

Things are more complex in a company (*this is the added value of DTM!*)

*Determine the Organizational Structure*

1. Identify key individuals in the organization (also to provide domain expertise)
1. Identify business units that will be affected by the data mining project

*Describe Problem Area*

1. Identify the problem area, such as marketing, customer care, or business development.
1. Describe the problem in general terms
1. Clarify the prerequisites of the project
    - What are the motivations behind the project?
    - Does the business already use data mining?
1. Check on the status of the data mining project within the business group
    - Has the effort been approved, or does data mining need to be "advertised" as a key technology for the business group?
1. If necessary, prepare informational presentations on data mining for your organization

*Describe Current Solution*

1. Describe any solutions currently used to address the business problem
1. Describe the advantages and disadvantages of the current solution

# Determine the Data Mining Goals

Formulate **project objectives in business terms**

Ask and refine sharp questions that are relevant, specific, and unambiguous.

- Data science is a process that *uses numbers to answer such questions*
- You typically use data science or machine learning to answer *five types of questions*
    1. How much or how many? (regression)
    1. Which category? (classification)
    1. Which group? (clustering)
    1. Is this unusual? (anomaly detection)
    1. Which option should be taken? (recommendation)

#

:::: {.columns}
::: {.column width="50%"}

The metrics must be **SMART**:

- *S*pecific
- *M*easurable
- *A*chievable
- *R*elevant
- *T*ime-bound

:::
::: {.column width="50%"}

![SMART metrics](./img/businessunderstanding/smart.png)

:::
::::

If the business goal cannot be effectively translated into a data mining goal, *it may be wise to consider redefining the problem*

> Success may be measured by reducing lost customers by 10% or by achieving a better understanding of the customer base
>
> Success should also be defined in these terms, such as achieving a certain level of predictive accuracy

# Produce a Project Plan

**Describe the intended plan for achieving the goals**, including:

- outlining specific steps and a proposed timeline
- an assessment of potential risks
- and an initial assessment of the tools and techniques needed to support the project

Generally accepted industry timeline standards are [@shearer2000crisp]:

- 50 to 70 percent of the time and effort in a data mining project involves the *Data Preparation Phase*;
- 20 to 30 percent involves the *Data Understanding Phase*;
- only 10 to 20 percent is spent in each of the *Modeling, Evaluation, and Business Understanding Phases*;
- and 5 to 10 percent is spent in the *Deployment Planning Phase*.

# Special Mention: Interdisciplinarity

Identifying and delving into the problem to solve

- Is an **interdisciplinary** phase
- Even if you have good knowledge in the fields of computer and data science...
- ... maybe you still miss domain knowledge that is fundamental to understanding and modeling the problem

# <img src="./img/cs.svg" class="title-icon" /> Business Understanding: Personal Gazetteer {background-color="#121011"}

{{< include _cs-trajectory.md >}}

# Case Study: Stocks {background-color="#121011"}

The [Standard and Poor's 500](https://en.wikipedia.org/wiki/S%26P_500) index tracks the stock performance of [500 of the largest companies](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies) in the United States.

![Top 25 company from the S&P 500 index](./img/datapreprocessing/market_cap_topn.svg)

- Companies issue stocks that are bought by investors; the number of stocks is called *shares outstanding*
    - *Shares outstanding* are shares of a corporation that have been purchased by investors and are held by them
- Stocks are traded daily in the stock market
    - *Volume* is the number of shares that are traded daily
    - *Close* and *Open* are closing/opening prices of daily trades

How would you define the *weight* of a company in the index?

# Case Study: Stocks

As a semplification, given a company $C$ and a generic index $I$

:::: {.columns}
::: {.column width="49%"}

*Market cap weight* (e.g., [S&P 500](https://en.wikipedia.org/wiki/S%26P_500))

- $\text{MarketCap(C)} = \text{SharesOut(C)} \times \text{StockPrice(C)}$
- $\text{MarketCapWeight(C)} = \frac{\text{MarketCap(C)}}{\sum_{C' \in I} \text{MarketCap(C')}}$

*Price weight index* (e.g., [Dow Jones Industrial Average](https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average))

- $\text{PriceWeight(C)} = \frac{\text{StockPrice(C)}}{\sum_{C' \in I} \text{StockPrice(C')}}$

:::
::: {.column width="50%"}

> Given a few companies such as
>
> | Ticker   |   Close |      Shares |   PWI (%) |   Market Cap (%) |
> |:---------|--------:|------------:|----------:|-----------------:|
> | AMZN     |  222.13 | 1.0515e+10  |  3.20253  |         4.53745  |
> | AAPL     |  242.7  | 1.51158e+10 |  3.4991   |         7.12683  |
> | GS       |  580.02 | 3.1391e+08  |  8.36237  |         0.353707 |
> | MSFT     |  424.56 | 7.43488e+09 |  6.12105  |         6.13209  |
> | NVDA     |  140.11 | 2.449e+10   |  2.02002  |         6.66582  |
>
> What is their impact on DJIA and S&P?

:::
::::

# Case Study: Stocks

![Price vs market cap weighted](./img/datapreprocessing/price_weight_distribution.svg)

# <img src="./img/cs.svg" class="title-icon" /> Business Understanding: Sport KPIs {background-color="#121011"}

{{< include _cs-kpisport.md >}}

# End of the case study {background-color="#121011"}

Back to CRISP-DM: Business understanding

# References