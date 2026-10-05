# -*- coding: utf-8 -*-
"""Front matter + Chapters 1-4 of the restructured report."""
import docxkit as K


def build(d):
    # ======================================================================
    # FRONT MATTER - copied byte-for-byte from the original file
    # (title page, institute logo, certificate page with its full-page image,
    #  declaration, acknowledgement, executive summary)
    # ======================================================================
    d.raw(0, 41)

    # ---- INDEX (placeholder; replaced after the TOC is known) -----------
    d.add('<!--INDEX-->')

    # ---- LIST OF TABLES / LIST OF FIGURES -------------------------------
    d.add('<!--LOT-->')
    d.add('<!--LOF-->')

    # ---- READING AND DATA CONVENTIONS + section break -------------------
    d.raw(43, 48)

    # ======================================================================
    # CHAPTER 1 - INTRODUCTION AND RESEARCH DESIGN
    # ======================================================================
    d.chapter(1, 'Introduction and Research Design',
              'Need, objectives, scope, key concepts, methodology and the limits '
              'of a secondary-data study')

    d.sec('1.1', 'Introduction to the study')
    d.p('A summer internship report in finance is expected to do two things at once. '
        'It must describe the organisation in which the internship was served, and it '
        'must demonstrate that the student can carry out a disciplined piece of applied '
        'financial research. This report does both. The internship was served at Rosy Blue '
        'Securities Pvt. Ltd., a SEBI-registered stock broker, in the dual roles of Dealer '
        'and Analyst. The research exercise applies the Economy–Industry–Company (EIC) '
        'method learned on that desk to a single listed case company, Pine Labs Limited, '
        'using only publicly available documents.',
        'Pine Labs was selected because it is a rare example of a large Indian '
        'commerce-technology platform that listed recently, publishes a detailed '
        'key-performance-indicator (KPI) data book alongside its statutory statements, and '
        'reached its first year of positive reported profit after a multi-year loss record. '
        'That combination makes it an unusually instructive teaching case: the student must '
        'reconcile audited numbers with company-defined measures, must separate transaction '
        'volume from recognised revenue, and must form a view in the absence of a long '
        'public track record.',
        'The report is organised so that the reader moves from context to evidence and only '
        'then to judgement. Chapter 1 sets out the research design. Chapter 2 describes the '
        'host organisation and the job performed. Chapter 3 builds the theoretical and '
        'industry framework. Chapter 4 profiles the case company and its business model. '
        'Chapter 5 presents the analysis and interpretation of financial and operating data. '
        'Chapter 6 states the findings, suggestions and conclusion, and Chapter 7 records the '
        'limitations of the study. References and six annexures follow.')

    d.sec('1.2', 'Need of the study')
    d.o(47, 48)
    d.p('There is a further, narrower need. Most student reports on payment companies stop at '
        'describing transaction growth. Very few test whether that growth is converted into '
        'recognised revenue, contribution, profit and cash. Pine Labs makes this testable '
        'because it publishes both a gross transaction value (GTV) series and a statutory '
        'revenue series. Studying the gap between the two is the analytical core of this '
        'report and is the reason the study was undertaken in this form.')
    d.ip('The need for the study arises from three gaps. First, India’s digital-payment '
         'system has grown faster than the published academic literature on the firms that '
         'operate inside it. Second, a newly listed platform company cannot be judged by the '
         'conventional five-year-track-record method, so a method has to be adapted. Third, '
         'platform companies report a mixture of audited figures and company-defined measures, '
         'and students are rarely taught to separate the two. This report is designed to close '
         'those three gaps on a single, well-documented case.')

    d.sec('1.3', 'Objectives of the study')
    d.o(54)
    d.o(55, 60)
    d.p('Each objective is matched to a specific method and a specific section of this report. '
        'The mapping is given in Table 1.4 so that the reader can verify that every stated '
        'objective is actually discharged somewhere in the document rather than merely '
        'asserted in the introduction.')

    d.cap('Mapping of objectives to methods and report sections')
    d.tbl([
        ['Objective', 'Method applied', 'Where discharged'],
        ['Explain the two-platform operating model and monetisation',
         'Descriptive study of prospectus and segment disclosures',
         'Sections 4.3 to 4.8'],
        ['Assess the Indian payment and fintech context',
         'Industry structure, PESTLE, Porter’s Five Forces, value-chain mapping',
         'Chapter 3'],
        ['Track revenue, profitability, funding and cash flow FY23–FY26',
         'Trend analysis, year-on-year growth, CAGR, common-size reading',
         'Sections 5.2 to 5.11'],
        ['Interpret company KPIs without equating volume with revenue',
         'KPI tabulation and a revenue-to-GTV diagnostic',
         'Sections 5.19 to 5.22'],
        ['Evaluate strategic, regulatory, operational and ESG risks',
         'Qualitative risk register with likelihood/impact rating',
         'Sections 5.31 to 5.33'],
        ['Estimate selected valuation multiples on a stated date',
         'Dated P/E, P/S and P/B snapshot plus sensitivity tables',
         'Sections 5.24 to 5.28'],
        ['Compare the case company with the internship host’s business model',
         'Conceptual business-model contrast',
         'Section 2.9'],
    ], widths=[3100, 3900, 2936])
    d.src('Author’s mapping. Every objective in Section 1.3 is traceable to a method and a '
          'numbered section of this report.')
    d.ip('The mapping is included as a control, not as decoration. A common weakness in student '
         'project work is that the objectives stated in Chapter 1 are never revisited, so the '
         'reader cannot tell whether they were met. Here each of the seven objectives names the '
         'technique used to discharge it and the numbered section in which the result appears, and '
         'Section 6.3 returns to the same list to state which propositions the evidence supported, '
         'refuted or left unresolved.')

    d.sec('1.4', 'Scope of the study')
    d.o(65)
    d.p('The scope is deliberately bounded in four ways. In terms of entity, the study covers '
        'Pine Labs Limited and the subsidiaries consolidated into its reported results; it does '
        'not analyse individual subsidiaries, joint arrangements or overseas legal entities '
        'separately. In terms of period, the annual window is FY23 to FY26 with a single interim '
        'update for Q1 FY27 (quarter ended 30 June 2026). In terms of data, only secondary, '
        'publicly available documents are used. In terms of output, the report produces an '
        'evidence-based research view and explicitly does not produce an investment '
        'recommendation, a price target or a discounted-cash-flow valuation.',
        'The study will be of use to management students learning company analysis, to '
        'readers who wish to understand how merchant-payment economics differ from the '
        'headline transaction numbers quoted in the press, and to the host organisation’s '
        'analyst function as a worked template for covering a newly listed technology company.')

    d.sec('1.5', 'Research questions and propositions')
    d.o(61, 63)
    d.ip('The five propositions are the spine of the report. Each is written so that the '
         'evidence can refute it. Proposition two, in particular, is answered in the negative: '
         'platform GTV grew roughly 3.9 times between FY23 and FY26 while revenue grew about 1.7 '
         'times, so volume growth does not translate one-for-one into revenue. Proposition five '
         'is recorded as not established, because the operating-cash-flow series reverses sign '
         'within the study window. A report that confirmed all five propositions would be a '
         'weaker piece of research than one that reports a mixed result.')

    d.sec('1.6', 'Key concepts and terminology used in this report')
    d.o(50, 52)
    d.p('Two of these definitions deserve emphasis because they are the most frequent source of '
        'error in student work on payment companies. Gross transaction value is the value routed, '
        'processed or serviced across the platform; it is not turnover, it is not revenue, and the '
        'company does not receive it. Contribution margin is a company-defined measure struck after '
        'specified direct costs; it is not gross profit as defined by any accounting standard, and '
        'its definition can be revised by the company.')
    d.ip('The terminology table is the foundation of every number in Chapter 5. Acquiring, issuing '
         'and processing are different activities performed by different entities under different '
         'obligations; digital checkout points and merchants are different counts and must not be '
         'compared with each other; gross transaction value and revenue are different quantities '
         'measured on different bases. Where a report confuses any of these pairs, every ratio '
         'built on them inherits the error.')

    d.sec('1.7', 'Overview of the Indian digital-payments environment')
    d.o(99, 100)
    d.p('For the purposes of the introduction it is enough to record that the system in which '
        'the case company operates is large, is growing quickly in volume terms, and is '
        'characterised by low or zero customer-visible pricing on some of its fastest-growing '
        'rails. That combination — very high volume growth with contested per-transaction '
        'economics — is the central tension examined throughout this report. The detailed '
        'industry treatment is given in Chapter 3.')

    d.sec('1.8', 'Research methodology')
    d.sub('1.8.1 Research design')
    d.p('The research design is descriptive, comparative and analytical, carried out as a single '
        'case study. The descriptive element sets out the structure of the industry, the business '
        'model of the company and the content of its disclosures. The comparative element places '
        'the company alongside qualitatively similar firms and alongside the internship host’s '
        'broking model. The analytical element recomputes growth rates, margins, ratios, a DuPont '
        'decomposition, a revenue-to-GTV diagnostic and a dated set of market multiples from the '
        'reported figures.')
    d.sub('1.8.2 Unit of analysis and period')
    d.o(65)
    d.sub('1.8.3 Data collection')
    d.p('Primary data is data generated by the researcher at the time of research, through '
        'instruments such as interviews, questionnaires or experiments. No primary survey was '
        'conducted for this study. The case company is a listed issuer whose obligations require '
        'it to publish the information needed for the stated objectives, and an unverified '
        'interview would have weakened rather than strengthened the evidence base.',
        'Secondary data is data already collected, recorded and published by others. The study '
        'rests entirely on secondary data drawn from primary-source documents, which is the '
        'strongest available category of secondary evidence: the issuer’s own prospectus, its '
        'audited and limited-reviewed results, its KPI data books, its shareholder letters and '
        'press releases, the regulator’s published payment statistics, the national payments '
        'operator’s product statistics and the exchange’s own quote page.')
    d.o(66)
    d.sub('1.8.4 Tools and techniques of analysis')
    d.o(67)
    d.b([
        'Trend and growth analysis: year-on-year growth and compound annual growth rate (CAGR) '
        'on revenue, profit, cash flow and operating indicators.',
        'Common-size and segment analysis: segment revenue as a share of total revenue, and '
        'international revenue as a share of total revenue.',
        'Ratio analysis: profitability, liquidity, leverage, efficiency and return ratios, each '
        'accompanied by the formula used and the caveat attaching to it.',
        'DuPont decomposition: three-factor separation of return on equity into net profit '
        'margin, asset turnover and the equity multiplier.',
        'Monetisation diagnostics: a revenue-to-GTV proxy expressed in basis points, used as a '
        'direction-of-travel indicator rather than as a contractual take rate.',
        'Qualitative strategic frameworks: PESTLE, Porter’s Five Forces, SWOT and a '
        'likelihood–impact risk register.',
        'Dated relative valuation: price-to-earnings, price-to-sales and price-to-book on a '
        'single stated market date, with sensitivity tables that make the assumptions visible.',
    ])
    d.sub('1.8.5 Treatment of company-defined measures')
    d.p('Company-defined measures such as contribution margin and adjusted EBITDA are reported in '
        'this study because they are the measures management uses to explain performance, but they '
        'are never substituted for audited figures. Wherever such a measure is used, the table '
        'states that it is company-defined, and the accompanying interpretation states what the '
        'measure excludes. Where the company’s own reconciliation is available, it is described '
        'rather than reproduced in full.')

    d.sec('1.9', 'Limitations and data discipline')
    d.o(69, 74)
    d.p('These limitations are not boilerplate. They determine the form of several conclusions in '
        'this report: they are the reason no discounted-cash-flow valuation is attempted, the reason '
        'the technical-analysis section is confined to a dated price observation, and the reason the '
        'cash-conversion proposition is recorded as unresolved. A fuller statement of limitations is '
        'given in Chapter 7.')

    d.sec('1.10', 'Review of relevant literature and analytical frameworks')
    d.o(76, 78)
    d.p('Three strands of literature inform the study. The first is the regulator’s own reporting on '
        'payment-system growth, which supplies system-level evidence against which company claims can '
        'be sized. The second is the industrial-organisation tradition, through which the structural '
        'attractiveness of the industry is assessed rather than assumed. The third is the corporate '
        'finance tradition of return decomposition and relative valuation, which supplies the '
        'arithmetic used in Chapter 5 and the discipline of stating the assumptions behind every '
        'multiple.',
        'The literature review is deliberately framework-led rather than survey-led. For a single-'
        'company case study of a recently listed issuer, the binding constraint is not the absence of '
        'academic theory but the absence of a long disclosure history. The frameworks are therefore '
        'used as instruments of interrogation, and the issuer’s own documents supply the evidence.')

    d.sec('1.11', 'Structure of the report')
    d.cap('Chapter plan of the report')
    d.tbl([
        ['Chapter', 'Title', 'What it contains'],
        ['1', 'Introduction and Research Design',
         'Need, objectives, scope, research questions, concepts, methodology, limitations, '
         'literature and structure.'],
        ['2', 'Organisational Background and Job Description',
         'Rosy Blue Securities Pvt. Ltd., services, departments, dealer and analyst duties, '
         'trading terminals, market infrastructure and skills developed.'],
        ['3', 'Theoretical Framework: Indian Fintech and Digital Payments',
         'Industry structure, value chain, system scale, economics, PESTLE, Five Forces, '
         'technology, regulation and consumer protection.'],
        ['4', 'Company Profile and Business Model: Pine Labs Limited',
         'Identification sheet, history, platforms, products, segments, geography, '
         'monetisation, customer journeys, SWOT and governance.'],
        ['5', 'Analysis and Interpretation of Financial and Operating Data',
         'Income statement, balance sheet, cash flow, ratios, DuPont, KPIs, peer context, '
         'valuation, market snapshot, risk and ESG.'],
        ['6', 'Findings, Suggestions and Conclusion',
         'Major findings, investment thesis, researcher’s view, recommendations and conclusion.'],
        ['7', 'Limitations of the Study',
         'Data, period, method, scope and interpretation limitations.'],
        ['—', 'References and Annexures A to F',
         'Source list, compact data sheet, formula sheet, glossary, abbreviations, quarterly '
         'data book and submission checklist.'],
    ], widths=[900, 3200, 5836])
    d.src('Author’s plan. Section numbers are continuous within each chapter so that every table '
          'and figure can be located from the index.')
    d.o(89)

    # ======================================================================
    # CHAPTER 2 - ORGANISATIONAL BACKGROUND AND JOB DESCRIPTION
    # ======================================================================
    d.chapter(2, 'Organisational Background and Job Description',
              'The internship host, the dealing desk, the analyst function and the '
              'institutions around a securities transaction')

    d.sec('2.1', 'Organisational introduction')
    d.o(494, 496)
    d.ip('The host organisation is an intermediary, not a principal. Its economic function is to '
         'convert a client instruction into an exchange order and to see that order through to '
         'confirmation and settlement. That distinction matters for this report, because the case '
         'company studied in Chapters 4 and 5 performs an analogous intermediation role in the '
         'payments chain: it carries value and instructions between merchants, banks and networks '
         'without owning the underlying funds. Working on the broking side made that parallel, and '
         'its limits, directly observable.')

    d.sec('2.2', 'Services of the firm')
    d.o(498)
    d.cap('Service lines of Rosy Blue Securities Pvt. Ltd.')
    d.o(500)
    d.src('Compiled from the firm’s public service profile. My own work was concentrated on the '
          'cash and F&O segments.')
    d.ip('The service list shows a firm operating across two regulatory logics at once. Exchange '
         'broking in the cash, derivative and currency segments is an execution service governed by '
         'exchange and clearing rules; mutual-fund distribution is a product-distribution activity '
         'governed by a different framework and carrying a different grievance route. The firm’s '
         'own public disclosures keep the two separate, and Section 2.8 explains why that '
         'separation matters when describing any intermediary.')

    d.sec('2.3', 'Departments and my roles')
    d.o(502)
    d.p('The two roles were deliberately sequenced. Time on the dealing desk came first, because '
        'order handling teaches the mechanics of the market — segments, order types, margins, '
        'settlement timetables and the consequences of an error. Analyst work followed, because a '
        'view on a security is only useful if the person forming it understands how that security '
        'is actually traded, what it costs to transact, and how quickly a position can be exited.')

    d.sec('2.4', 'Job description')
    d.sub('Dealer')
    d.o(505, 510)
    d.sub('Analyst')
    d.o(512, 514)

    d.sec('2.5', 'Trading terminals and markets')
    d.o(516, 517)
    d.cap('Cash market and F&O market compared')
    d.o(519)
    d.src('Compiled from desk practice and exchange segment descriptions.')
    d.ip('The comparison explains why the same client can hold very different risk in the two '
         'segments. A cash-market position is funded in full and its worst outcome is a fall in the '
         'price of an owned asset. An F&O position is funded by margin, carries an expiry date and, '
         'for a written option, can lose more than the premium received. On the desk this showed up '
         'as a difference in supervision intensity rather than a difference in order mechanics: the '
         'same screen, the same order ticket, a materially different consequence of being wrong.')

    d.sec('2.6', 'Dealing-desk workflow')
    d.o(521)
    d.o(522, 526)
    d.p('Two controls run through every step. The first is confirmation: an instruction is repeated '
        'back before it is entered, because an order cannot be recalled once it is matched. The '
        'second is record-keeping: the status of each order is reported to the client, so that the '
        'client always knows the executed quantity and price. Both controls are forms of the same '
        'discipline used in the research part of this report — state the source, state the date, and '
        'do not present an inference as a fact.')

    d.sec('2.7', 'The EIC framework in analysis')
    d.o(528)
    d.cap('EIC framework and its use in this report')
    d.o(530)
    d.src('Author’s mapping of the top-down method taught on the analyst desk to the chapters of '
          'this report.')
    d.ip('The EIC method is the organising logic of the whole report, not a decorative framework. '
         'The economy and industry layers are discharged in Chapter 3, where system-level payment '
         'statistics and the structure of the value chain are examined before any company figure is '
         'quoted. The company layer is discharged in Chapters 4 and 5. Following the sequence '
         'prevents the most common error in student company analysis, which is to treat a company’s '
         'growth rate as evidence of its quality without first establishing how fast its industry '
         'was growing anyway.')

    d.sec('2.8', 'Institutions around a securities transaction')
    d.o(547, 549)
    d.cap('Market-infrastructure roles')
    d.o(551)
    d.o(552)
    d.ip('The table is a safeguard against a frequent reporting error: describing an intermediary '
         'as though it performed the function of the institution it connects to. A broker routes '
         'orders but does not operate a trading venue; a depository participant maintains securities '
         'records but does not clear trades; a distributor sells a fund but is not the fund. The same '
         'discipline is applied to the case company in Chapter 4, where technology and processing '
         'services are distinguished from the licensed banking and issuing functions performed by '
         'its partners.')

    d.sec('2.9', 'Pine Labs and a securities broker: complementary, not identical models')
    d.o(538, 540)
    d.cap('Conceptual business-model contrast')
    d.o(542)
    d.o(543)
    d.ip('The two businesses rhyme without matching. Both depend on reliable digital workflows, '
         'regulated counterparties and accurate settlement, and both are measured publicly by an '
         'activity number that is not revenue — traded volume for the broker, gross transaction '
         'value for the platform. The difference is where the economics sit. A broker’s income is '
         'tied to the act of transacting; a payments platform earns through a mixture of '
         'subscription, processing and service fees that are only loosely related to the value '
         'carried. Treating either activity measure as turnover would overstate both businesses by '
         'orders of magnitude.')

    d.sec('2.10', 'Skills developed during the internship')
    d.cap('Skills developed during the internship')
    d.o(533)
    d.src('Author’s record of the internship period, 12 May 2026 to 13 August 2026.')
    d.o(534)
    d.ip('The skills divide into two groups that this report uses differently. The execution skills '
         '— terminal operation, order monitoring, client confirmation and quick decision-making '
         'under live market conditions — inform Chapter 2 and the market-infrastructure discussion. '
         'The analytical skills — the EIC sequence, company analysis and business analysis — are '
         'what Chapters 3 to 5 actually apply. The internship is therefore evidenced in this report '
         'by method rather than only by description.')

    d.sec('2.11', 'Learning outcomes evidenced by this research')
    d.o(371)
    d.o(372)
    d.cap('Learning outcomes evidenced by this research')
    d.o(374)
    d.src('Author’s mapping of internship learning to the analytical content of this report.')
    d.ip('The two organisations are kept distinct throughout. Rosy Blue Securities Pvt. Ltd. is the '
         'internship host and is described from its public service profile; Pine Labs Limited is '
         'the research case and is analysed from its own filings. No financial information about '
         'the host is presented, and no client, account or confidential desk information appears '
         'anywhere in this report.')

    d.sec('2.12', 'Internship particulars')
    d.o(376)
    d.cap('Internship summary')
    d.o(378)
    d.src('Internship record. Client identities, account details and confidential data are not '
          'disclosed in this report.')
    d.ip('The internship ran from 12 May 2026 to 13 August 2026 across two roles and two market '
         'segments, using the NEAT PLUS and CTCL terminals. The duties recorded — order placement '
         'and monitoring, client communication and EIC-based company and business analysis — map '
         'directly onto the two halves of this report: the market-infrastructure material in '
         'Chapter 2 and the company analysis in Chapters 4 and 5.')

    # ======================================================================
    # CHAPTER 3 - THEORETICAL FRAMEWORK
    # ======================================================================
    d.chapter(3, 'Theoretical Framework: Indian Fintech and Digital Payments',
              'Industry structure, system scale, value-chain economics, external '
              'conditions, competitive forces and the rules that govern them')

    d.sec('3.1', 'Introduction to the framework')
    d.p('This chapter builds the industry and conceptual framework against which the case company '
        'is assessed. It proceeds from structure to scale, from scale to economics, and from '
        'economics to the external and competitive forces that determine how much of the value '
        'created in the chain any single participant can retain. The chapter closes with the '
        'technology, regulatory and consumer-protection conditions that constrain every firm in the '
        'industry, including the internship host.',
        'The framework matters because digital payments is an industry in which volume growth and '
        'profit growth are only loosely connected. A participant can process a very large and '
        'rapidly rising value of transactions while earning a small and falling fee on each one. '
        'Establishing that proposition at the industry level, before examining any company figure, '
        'is what allows Chapter 5 to interpret the case company’s numbers rather than merely report '
        'them.')

    d.sec('3.2', 'Industry structure and the payments value chain')
    d.o(94)
    d.cap('Simplified digital-payments value chain')
    d.o(96)
    d.o(97)
    d.ip('The value chain shows where economic power sits. Rules and rails are set by public '
         'institutions and networks and are not a source of competitive advantage for any technology '
         'provider. Issuing and acquiring are licensed activities that require a balance sheet and '
         'regulatory permission. The technology and orchestration layer, where the case company '
         'operates, is the least capital-intensive and the most contestable: entry is possible with '
         'software, but durable advantage requires integration depth, reliability and switching '
         'costs rather than price. The merchant layer holds the customer relationship and can '
         'therefore bargain.')

    d.sec('3.3', 'Market scale and current system indicators')
    d.o(99, 100)
    d.cap('Industry indicators and interpretation')
    d.o(102)
    d.o(103)
    d.ip('Three readings follow from the table. First, the system is very large and still '
         'compounding, which supports the view that the addressable opportunity is not the '
         'constraint on any individual firm. Second, the measures are not additive and not directly '
         'comparable: regulator, network and company figures count different things over different '
         'periods, so no market share is calculated here. Third, the company’s own platform activity '
         'is substantial in absolute terms, which is precisely why the revenue earned on that '
         'activity, examined in Section 5.21, is the more informative number.')

    d.sec('3.4', 'System scale and interpretation in detail')
    d.o(555, 557)
    d.cap('Public payment-system indicators')
    d.o(559)
    d.o(560)
    d.ip('The average-value-per-transaction arithmetic is the most useful discipline in this table. '
         'A payment system whose average ticket size is falling is a system in which low-value, '
         'high-frequency transactions are growing fastest. For a fee-earning participant that is a '
         'mixed signal: transaction counts rise, but the revenue opportunity per transaction '
         'typically falls, and the cost of processing does not fall proportionately. This is the '
         'industry-level explanation for the declining revenue-to-GTV proxy observed for the case '
         'company in Section 5.21.')

    d.sec('3.5', 'Industry economics and value creation')
    d.o(105, 109)
    d.p('Taken together these five propositions define the economic test applied to the case company '
        'in Chapter 5. A platform in this industry creates durable value only if it converts '
        'transaction scale into recurring, contracted revenue; if the mix of that revenue is '
        'defensible against fee compression; if the services attached to the transaction increase '
        'retention; if the cost of serving the installed base grows more slowly than the revenue it '
        'generates; and if regulatory and operational trust is maintained throughout. Failure on any '
        'one of the five can be masked for several quarters by volume growth.')

    d.sec('3.6', 'Opportunity areas and headwinds')
    d.o(111, 113)
    d.ip('Every row of the table pairs an opportunity with the headwind that limits it, which is the '
         'honest way to present an industry scan. Small-merchant digitisation widens reach but brings '
         'the most price-sensitive customers. Embedded credit raises revenue per merchant but '
         'introduces consumer-protection and credit-quality exposure that sits with a partner bank. '
         'Cross-border expansion diversifies revenue but multiplies licensing and settlement '
         'complexity. The strategic question for any participant is not which opportunities exist, '
         'but which of them it can pursue without importing a risk it cannot manage.')

    d.sec('3.7', 'Competitive landscape')
    d.o(115)
    d.cap('Selected peer and adjacent-company context')
    d.o(117)
    d.o(118)
    d.ip('The competitive set is unusually heterogeneous. Competition arrives from banks that own '
         'the customer relationship, from software companies that own the checkout, from consumer '
         'applications that own the payer, and from global processors that own scale. No single '
         'competitor faces the case company across all of its product lines, which reduces the risk '
         'of head-to-head price war in any one line but also means the company must defend several '
         'fronts at once. This is why the Five Forces assessment in Section 3.9 rates rivalry and '
         'substitution as high even though no dominant direct rival exists.')

    d.sec('3.8', 'PESTLE analysis')
    d.o(172, 174)
    d.ip('The PESTLE scan shows an industry in which the binding external factors are legal and '
         'technological rather than political or social. Policy support for digital payments is '
         'settled and broadly favourable; social acceptance is high and rising. The live exposures '
         'are the regulatory perimeter around stored value, data and cross-border processing, and '
         'the pace of technological change in authentication, tokenisation and artificial '
         'intelligence. A firm in this industry therefore spends disproportionately on compliance '
         'and engineering relative to its marketing spend.')

    d.sec('3.9', 'Porter’s Five Forces')
    d.o(176, 178)
    d.ip('Four of the five forces are assessed as high or moderate-to-high, which describes a '
         'structurally demanding industry. Buyers are concentrated and sophisticated; suppliers '
         'include the banks and networks on whose rails the service runs; substitutes include the '
         'merchant simply accepting a bank QR code directly; and rivalry is intense because software '
         'differentiation is visible and copyable. Only the threat of new entrants is moderated, and '
         'that is by scale, certification and integration effort rather than by any legal barrier. '
         'The structural conclusion is that industry growth will not by itself produce attractive '
         'margins; firm-specific execution has to.')

    d.sec('3.10', 'Strategic implication of the industry analysis')
    d.o(180)
    d.p('The implication for the case study is methodological as well as strategic. Because the '
        'industry allows very rapid volume growth on thin and contested economics, no single '
        'operating indicator is sufficient evidence of success. Chapter 5 therefore never presents '
        'a growth rate without the margin and cash-conversion figures that qualify it, and never '
        'presents a company-defined measure without naming what it excludes.')

    d.sec('3.11', 'Payments technology: reliability, cybersecurity and AI controls')
    d.o(655, 657)
    d.cap('Generic threat-to-control lens')
    d.o(659)
    d.o(660)
    d.ip('Technology risk in payments is a financial risk, not merely an operational one. An outage '
         'during peak trading hours removes revenue that is never recovered, because the transaction '
         'is completed on a competing rail. A data or fraud incident imposes remediation cost, '
         'regulatory attention and merchant attrition at the same time. The control objectives in '
         'the table are therefore the minimum a reader should expect to see evidenced in disclosure; '
         'where a company reports uptime, incident counts and recovery testing, that disclosure is '
         'itself a quality signal.')

    d.sec('3.12', 'Regulatory perimeter: different activities, different rules')
    d.o(664, 666)
    d.cap('Activity-to-rule mapping (high level)')
    d.o(668)
    d.o(669)
    d.ip('The mapping enforces a boundary that this report observes throughout: an activity is '
         'described by what the documents say the firm does, not by what the firm’s brand implies. '
         'Supplying processing technology to a bank is not the same as holding a banking licence; '
         'distributing a prepaid programme is not the same as issuing stored value; facilitating an '
         'affordability offer is not the same as lending. Each of those distinctions changes who '
         'carries the credit, custody and conduct obligation, and therefore changes the risk that '
         'should be attributed to the company in Section 5.31.')

    d.sec('3.13', 'Trust, suitability and fair treatment')
    d.o(673, 675)
    d.cap('Customer-protection questions')
    d.o(677)
    d.o(678)
    d.ip('Consumer protection is a commercial variable in both businesses examined in this report. '
         'For the broker, suitability and clear communication determine whether a client relationship '
         'survives a losing position. For the payments platform, transparent consent, correct lender '
         'identification and reliable grievance handling determine whether merchants and end users '
         'continue to use a credit-linked product. Conduct failures in either business are rarely '
         'confined to the affected customers; they attract regulatory attention that raises the cost '
         'of the entire product line.')

    d.sec('3.14', 'Responsible fintech: stakeholders, benefits and trade-offs')
    d.o(682, 684)
    d.cap('Stakeholder and responsibility matrix')
    d.o(686)
    d.o(687)
    d.ip('The matrix sets out the trade-offs that a purely financial reading would miss. Wider '
         'acceptance benefits small merchants but transfers fee and settlement-timing risk to the '
         'least resilient participants. Embedded credit widens access but can harm users who do not '
         'understand the lender’s identity or the consequence of default. Device-led distribution '
         'creates reach and an electronic-waste obligation at the same time. These trade-offs are '
         'carried into the ESG assessment in Section 5.33 rather than treated as a separate '
         'narrative.')

    d.sec('3.15', 'The economy layer: macro drivers of merchant payments')
    d.p('The EIC method requires the economy to be considered before the industry. For a '
        'merchant-payments platform the relevant macro transmission is indirect but strong: the '
        'platform earns on transactions, transactions arise from retail and commercial spending, '
        'and spending responds to income growth, credit availability, inflation and consumer '
        'confidence. A platform therefore carries cyclical exposure even though it holds no '
        'inventory and extends no credit of its own.',
        'Four macro channels matter in particular. Consumption growth determines the number and '
        'size of transactions presented at the checkout. Credit conditions determine the viability '
        'of affordability and equated-instalment offers, which are among the higher-value product '
        'lines. Formalisation and digitisation of small business determine how quickly the '
        'addressable merchant base widens. Interest rates affect both the cost of funding working '
        'capital in the settlement cycle and the discount rate the market applies to a '
        'long-duration growth company, which is why the valuation discussion in Section 5.26 is '
        'framed around an assumed cost of equity.')
    d.cap('Macro channels and their transmission to platform revenue')
    d.tbl([
        ['Macro variable', 'Transmission channel', 'Observable platform effect'],
        ['Household consumption', 'Number and value of retail transactions presented',
         'Gross transaction value and transaction count'],
        ['Credit conditions', 'Availability and pricing of affordability and instalment offers',
         'Affordability volume and associated service revenue'],
        ['Small-business formalisation', 'Size of the addressable merchant base',
         'Merchant and digital-checkout-point additions'],
        ['Interest rates', 'Working-capital cost in settlement, and the discount rate applied to '
         'growth equities', 'Finance cost and the valuation multiple'],
        ['Inflation', 'Average ticket size and merchant cost sensitivity',
         'Revenue per transaction and fee negotiation pressure'],
        ['Foreign-exchange movement', 'Translation of international revenue and cross-border cost',
         'Reported overseas revenue share'],
    ], widths=[2300, 4300, 3336])
    d.src('Author’s framework. The channels are stated qualitatively; this study does not model '
          'macro sensitivities, which is recorded as a limitation in Section 7.3.')
    d.ip('The macro layer explains why a payments platform can be simultaneously described as a '
         'technology company and treated by the market as a consumption-linked one. Its revenue is '
         'contractual, but the volume on which much of that revenue is earned is cyclical. For this '
         'report the practical consequence is modest but real: a single strong or weak quarter '
         'should not be attributed entirely to company execution, because part of the movement is '
         'the spending cycle passing through the checkout.')

    d.sec('3.16', 'Summary of the theoretical framework')
    d.cap('Framework conclusions carried into the analysis')
    d.tbl([
        ['Framework element', 'Conclusion reached', 'Where it is tested'],
        ['Value chain', 'Technology and orchestration is the most contestable layer',
         'Sections 5.19 to 5.22'],
        ['System scale', 'Volume is abundant; monetisation per transaction is the constraint',
         'Section 5.21'],
        ['Industry economics', 'Scale must convert into recurring, contracted revenue',
         'Sections 5.2 to 5.7'],
        ['PESTLE', 'Legal and technological factors bind hardest',
         'Sections 5.31 to 5.33'],
        ['Five Forces', 'Structurally demanding; growth alone will not create margin',
         'Sections 5.3 and 5.15'],
        ['Regulatory perimeter', 'Attribute risk to the entity that carries the obligation',
         'Section 5.31'],
        ['Responsible fintech', 'Access, reliability and inclusion carry measurable trade-offs',
         'Section 5.33'],
    ], widths=[2400, 4600, 2936])
    d.src('Author’s synthesis of Chapter 3. Each conclusion is carried forward as a testable '
          'proposition rather than as an assumption.')

    # ======================================================================
    # CHAPTER 4 - COMPANY PROFILE AND BUSINESS MODEL
    # ======================================================================
    d.chapter(4, 'Company Profile and Business Model: Pine Labs Limited',
              'Identification, history, platform architecture, products, segments, '
              'geography, monetisation, governance and ownership')

    d.sec('4.1', 'Company identification sheet')
    d.cap('Company identification')
    d.o(83)
    d.o(84)
    d.ip('Three fields on the identification sheet shape the whole analysis. The company was '
         'incorporated in 1998, so it is not a start-up; it is a mature business that listed late. '
         'It describes itself as technology infrastructure for digital payments rather than as a '
         'financial institution, which determines where regulated obligations sit. And it reports '
         'through two platforms rather than one, which is why segment analysis in Sections 4.6 and '
         '5.6 is necessary rather than optional. Administrative fields should be re-verified '
         'against the latest official filing before final submission.')

    d.sec('4.2', 'Research question addressed in this chapter')
    d.p('The question this chapter answers is deliberately narrow: how does Pine Labs Limited '
        'actually make money, from whom, and with what obligations attached? Until that question is '
        'settled, no financial figure in Chapter 5 can be interpreted. A reader who believes the '
        'company earns a percentage of the value it routes will reach a very different conclusion '
        'from a reader who understands that most of the value routed never belongs to the company '
        'at any point.')

    d.sec('4.3', 'History and milestones')
    d.cap('Selected corporate milestones')
    d.o(124)
    d.o(125)
    d.ip('The milestone record describes a company that grew by adding capability rather than by '
         'deepening a single product. Merchant acceptance software came first, followed by regional '
         'expansion, then gift-card and prepaid issuance through acquisition, then an online '
         'gateway, then a corporate reorganisation ahead of listing. The analytical consequence is '
         'that the consolidated financial statements aggregate businesses with different economics '
         'and different acquisition dates, and that the pre-listing comparatives are restated rather '
         'than originally reported. Both facts are carried into the reading of the FY23 to FY25 '
         'series in Section 5.2.')

    d.sec('4.4', 'Two-platform architecture')
    d.o(127)
    d.fig('rId12', 5943600, 2421598,
          'Conceptual Pine Labs platform and value flow',
          'Author diagram based on the company’s platform and monetisation descriptions. '
          'It is not a legal-entity or funds-flow map. [1,5]', pic_id=11)
    d.p('The architecture is best read as two customer-facing propositions sharing one technology '
        'estate. The Digital Infrastructure and Transaction Platform faces merchants and the '
        'businesses that serve them: acceptance in store and online, affordability offers at the '
        'point of sale, and the application programming interfaces through which other fintechs '
        'embed payment capability. The Issuing and Acquiring Platform faces institutions: banks, '
        'brands and programme sponsors that need card issuance, prepaid and gift-programme '
        'processing, and distribution. The shared estate is what makes cross-sell possible; the '
        'separate customer bases are what make segment reporting meaningful.')

    d.sec('4.5', 'Products and services')
    d.cap('Products and service economics')
    d.o(156)
    d.o(157)
    d.ip('Reading the table by column rather than by row is the more useful exercise. The customer '
         'column shows that the company sells to four distinct buyer types — merchants, institutions, '
         'brands and other fintechs — each with a different purchasing process and a different '
         'willingness to pay. The revenue column shows that no single monetisation mechanism '
         'dominates: subscription, transaction-linked, value-linked and distribution fees all appear. '
         'That diversity is a defence against fee compression in any one line, and it is also the '
         'reason a single blended take-rate figure would be misleading.')

    d.sec('4.6', 'Revenue by operating segment')
    d.cap('Revenue mix by platform (₹ crore except share)')
    d.o(133)
    d.o(134)
    d.fig('rId13', 5943600, 2580830, 'Annual revenue by segment',
          'Company-reported segment revenue; annual FY24–FY26 only. Small ₹0.01 rounding '
          'differences may occur against the statutory total. [1,3]', pic_id=12)
    d.ip('The segment table records a deliberate and sustained mix shift. The Issuing and Acquiring '
         'Platform rose from 27.9 per cent of revenue in FY24 to 32.2 per cent in FY26 and 32.3 per '
         'cent in Q1 FY27, because it grew faster than the larger merchant-facing platform in every '
         'period shown. Two readings are available and the evidence does not yet separate them. The '
         'favourable reading is diversification away from dependence on in-store acceptance. The '
         'cautious reading is that the faster-growing segment may carry a different cost structure, '
         'which would help explain the contribution-margin decline analysed in Section 5.3. Segment '
         'revenue alone cannot settle the question because segment profitability is not disclosed.')

    d.sec('4.7', 'How the company makes money')
    d.cap('Disclosed revenue streams by activity')
    d.o(140)
    d.o(141)
    d.ip('This is the single most important table in the chapter. It establishes that recognised '
         'revenue arises from contracted subscription, processing, service and distribution fees — '
         'not from a share of the value routed across the platform. The analytical consequence is '
         'stated plainly: gross transaction value is an activity indicator, and any calculation that '
         'divides revenue by GTV produces a diagnostic ratio, not a price. Sections 5.19 to 5.22 '
         'apply that discipline to the published series.')

    d.sec('4.8', 'Geographic footprint, customer base and strategy')
    d.o(143, 145)
    d.ip('The strategic logic is land-and-expand, and it is measurable. The company reports a large '
         'installed base of merchants and digital checkout points, and a rising share of revenue from '
         'outside India. If the strategy is working, revenue per merchant and revenue per checkout '
         'point should hold or improve as the base grows, and international revenue should grow '
         'without a disproportionate increase in compliance and operating cost. Section 5.19 tests '
         'the first of those conditions; the second is not fully testable on public disclosure and is '
         'listed in Chapter 7 as a limitation.')

    d.sec('4.9', 'Illustrative merchant journey')
    d.o(159)
    d.p('Three points in that journey determine the economics. The first is the instrument the '
        'consumer chooses, because card, unified-payments-interface and affordability transactions '
        'carry different pricing and different direct costs. The second is whether the merchant has '
        'bought services beyond acceptance — reconciliation, loyalty, billing or data — because those '
        'are the recurring elements of the relationship. The third is settlement timing, which '
        'determines the working-capital profile examined in Section 5.11 rather than the revenue '
        'recognised.')

    d.sec('4.10', 'Illustrative prepaid and issuing journey')
    d.o(161)
    d.ip('The prepaid journey illustrates why balance-sheet size is a poor proxy for financial '
         'strength in this business. Programme balances held for brands and end users appear as both '
         'an asset and an obligation; they are not shareholder funds and they are not freely '
         'distributable. The company’s role is to supply programme software, issuance interfaces, '
         'processing and distribution, and to earn fees for doing so. Section 5.9 therefore reads the '
         'liquidity ratios with explicit reference to prepaid-card liabilities and other bank '
         'balances rather than treating cash-like items as available resources.')

    d.sec('4.11', 'Product evaluation framework')
    d.cap('Questions to assess each product line')
    d.o(164)
    d.o(165)
    d.ip('The framework exists to stop a product list being read as a performance record. For each '
         'line the analyst must establish reach, the billing mechanism, the unit economics, where '
         'risk sits and whether adoption improves retention. Applying it to the disclosed data, '
         'reach is well evidenced, the billing mechanism is described qualitatively, risk '
         'allocation is stated for credit-linked products, and unit economics and retention are '
         'not disclosed at all. Two of the five dimensions therefore remain unanswered on public '
         'information, which is recorded in Chapter 7.')

    d.sec('4.12', 'Innovation claims and the evidence standard applied')
    d.o(167)
    d.p('The standard applied in this report is therefore explicit. A product announcement is '
        'recorded as an announcement. A pilot is recorded as a pilot. A revenue contribution is '
        'recorded only where the company discloses one. Where a capability is strategically '
        'significant but not yet financially material, it is treated as optionality and is not '
        'included in any valuation arithmetic in Chapter 5.')

    d.sec('4.13', 'Recent initiatives and corporate actions')
    d.o(147, 150)
    d.ip('The corporate actions matter for per-share work as much as for strategy. The conversion of '
         'approximately 57.95 crore compulsorily convertible preference shares into equity on a '
         'one-for-one basis in December 2025 changes the share count used in any per-share '
         'calculation, and the Agya and Shopflo transactions change the composition of the '
         'consolidated group between periods. Section 5.25 therefore states the share count it uses, '
         'the date of that count, and the fact that it excludes potential dilution.')

    d.sec('4.14', 'SWOT analysis')
    d.cap('SWOT matrix')
    d.o(186)
    d.o(187)
    d.ip('The SWOT is internally consistent with the financial evidence in Chapter 5 rather than '
         'aspirational. The strengths are verifiable from the operating data: a large merchant and '
         'checkout base and a broad institutional footprint. The weaknesses are verifiable from the '
         'statements: a short listed record, a loss history through FY25 and volatile operating cash '
         'flow. The opportunities are real but unproven, and are treated as optionality. The threats '
         '— fee compression, regulatory change, concentration and execution risk on acquisitions — '
         'are precisely the items carried into the risk register in Section 5.31.')

    d.sec('4.15', 'Management, governance and ownership')
    d.o(189)
    d.cap('Governance and ownership review points')
    d.o(191)
    d.o(192)
    d.ip('The absence of an identifiable promoter at the offer stage changes the governance question '
         'rather than removing it. There is no promoter-pledge risk and no single controlling '
         'shareholder, but accountability then rests entirely on board independence, audit-committee '
         'effectiveness, related-party discipline and the quality of disclosure. For a reader, the '
         'practical tests are whether non-generally-accepted measures are reconciled consistently to '
         'audited figures, whether acquisition outcomes are reported after the deal rather than only '
         'at announcement, and whether customer-concentration disclosure is refreshed. Each of those '
         'tests is listed in Section 4.16.')

    d.sec('4.16', 'Governance questions for investors and students')
    d.o(194, 198)

    d.sec('4.17', 'Chapter summary')
    d.cap('Business-model conclusions carried into Chapter 5')
    d.tbl([
        ['Question', 'Conclusion from Chapter 4', 'Consequence for the analysis'],
        ['What does the company sell?',
         'Acceptance, affordability, issuing, prepaid and infrastructure software and processing',
         'Revenue must be read by segment and product, not in total'],
        ['Who pays?',
         'Merchants, banks, brands, programme sponsors and other fintechs',
         'Customer concentration and renewal risk are material'],
        ['How is revenue earned?',
         'Subscription, processing, value-linked, service and distribution fees',
         'GTV is an activity measure, never a revenue proxy'],
        ['Who carries the regulated obligation?',
         'Partner banks and licensed entities for credit, custody and stored value',
         'Risk must be attributed to the obligated entity'],
        ['What has changed recently?',
         'Listing, preference-share conversion, Agya and Shopflo transactions',
         'Share count and group composition differ between periods'],
        ['Where is the governance focus?',
         'No identifiable promoter; board, audit and disclosure quality',
         'Non-GAAP reconciliation and related-party clarity are the key tests'],
    ], widths=[2300, 4300, 3336])
    d.src('Author’s synthesis of Chapter 4.')
