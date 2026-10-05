# -*- coding: utf-8 -*-
"""Chapters 5-7, References and Annexures A-F of the restructured report."""
import docxkit as K


def build(d):
    # ======================================================================
    # CHAPTER 5 - ANALYSIS AND INTERPRETATION
    # ======================================================================
    d.chapter(5, 'Analysis and Interpretation of Financial and Operating Data',
              'Income statement, balance sheet, cash flow, ratios, DuPont, platform '
              'KPIs, peer context, valuation, market snapshot, risk and ESG')

    d.sec('5.1', 'Introduction to the analysis')
    d.p('This chapter contains the analytical core of the report. It follows a fixed sequence so '
        'that each result rests on the one before it: reported income first, then the balance sheet '
        'and cash flow that the income statement implies, then the ratios that summarise both, then '
        'the operating indicators that explain them, then the peer and valuation context in which '
        'they are priced, and finally the risks and non-financial factors that could change the '
        'conclusion.',
        'Three conventions are applied without exception. Every table is followed by an explicit '
        'interpretation, in line with the requirement that no figure may be presented without being '
        'read. Every company-defined measure is labelled as such and its exclusions are stated. '
        'Every calculation performed by the author is labelled as an author calculation and its '
        'formula is reproduced in Annexure B.')
    d.cap('Structure of the analysis')
    d.tbl([
        ['Sections', 'Analytical block', 'Principal question'],
        ['5.2 to 5.7', 'Income statement and segment performance',
         'Is revenue growth being converted into profit?'],
        ['5.8 to 5.11', 'Balance sheet, funding and cash flow',
         'Is the reported profit supported by cash and a sound funding structure?'],
        ['5.12 to 5.18', 'Ratio analysis and DuPont decomposition',
         'What drives profitability, liquidity, leverage and return on equity?'],
        ['5.19 to 5.22', 'Operating KPIs and platform economics',
         'Does platform activity translate into recognised revenue?'],
        ['5.23 to 5.28', 'Peer context and valuation',
         'What is being paid for the business, and on what assumptions?'],
        ['5.29 to 5.30', 'Listed-market and technical observation',
         'What does the market price record on a stated date?'],
        ['5.31 to 5.34', 'Risk, ESG and evidence discipline',
         'What could change the conclusion, and how confident can it be?'],
    ], widths=[1500, 3600, 4836])
    d.src('Author’s plan for Chapter 5.')

    # --- income statement -------------------------------------------------
    d.sec('5.2', 'Income statement: four-year consolidated trend')
    d.cap('Selected income and company-defined measures')
    d.o(204)
    d.o(205)
    d.fig('rId14', 5943600, 2106503, 'Revenue growth and reported PAT',
          'Revenue and PAT in ₹ crore. FY23–FY25 restated; FY26 audited. [1,2]', pic_id=13)
    d.ip('The four-year record contains one genuine inflection and one qualification. The '
         'inflection is profit: a reported loss of ₹265.15 crore in FY23 widened to ₹341.90 crore in '
         'FY24, narrowed to ₹145.49 crore in FY25 and became a profit of ₹112.51 crore in FY26. The '
         'qualification is growth: revenue rose 10.8 per cent in FY24, accelerated to 28.5 per cent '
         'in FY25 and moderated to 19.2 per cent in FY26, so the growth path is not uniform. Reading '
         'the two together, FY26 is the first year in which the operating model covered its full '
         'cost base, and it did so in a year when revenue growth was slower than the year before — '
         'which points to cost discipline and operating leverage rather than to a growth surge.')

    d.sec('5.3', 'Growth and margin interpretation')
    d.o(210, 214)
    d.ip('The margin evidence points in two directions at once and must be reported that way. '
         'Company-defined adjusted EBITDA rose from ₹158.19 crore in FY24 to ₹558.87 crore in FY26 '
         'and its margin from 8.94 per cent to 20.62 per cent, which is strong operating leverage. '
         'Contribution margin, however, fell from 78.3 per cent of revenue in FY24 to 75.3 per cent '
         'in FY26 and 72.3 per cent in Q1 FY27. Falling contribution with rising adjusted EBITDA '
         'means the improvement is being delivered below the contribution line — by slower growth in '
         'indirect and overhead costs — rather than by better pricing on the revenue itself. That is '
         'a less durable source of margin than price or mix improvement, and it is the single most '
         'important caution in this chapter.')

    d.sec('5.4', 'Nine-quarter revenue and segment mix')
    d.o(563, 565)
    d.cap('Quarterly revenue by platform (₹ crore, rounded)')
    d.o(567)
    d.o(568)
    d.ip('The quarterly series shows seasonality that the annual table conceals. Revenue does not '
         'rise in a straight line from quarter to quarter; fourth quarters carry distribution and '
         'programme activity that first quarters do not. For analysis this has one firm consequence: '
         'a single quarter must never be multiplied by four to produce an annual figure. The series '
         'also shows that the Issuing and Acquiring Platform has grown its share in most quarters, '
         'confirming from a second angle the mix shift identified in Section 4.6.')

    d.sec('5.5', 'Contribution, adjusted EBITDA and PAT: reading the definitions')
    d.o(571, 573)
    d.cap('Quarterly margin and profit indicators')
    d.o(575)
    d.o(576)
    d.ip('This table is the clearest illustration in the report of why definitions must be read '
         'before numbers. The management profit-and-loss shows a loss in every FY25 quarter and a '
         'profit in each quarter thereafter, so the turn is visible at quarterly frequency and not '
         'only in the annual figure. At the same time, Q1 FY27 shows both contribution margin and '
         'adjusted EBITDA margin below the comparable prior-year quarter. Adjusted EBITDA excludes '
         'other income and adds back items including share-based payment, exceptional items and '
         'certain professional fees; those add-backs are recurring in a company that grants equity '
         'and acquires businesses. The audited profit figure, not the adjusted measure, is therefore '
         'the one used for the return and valuation work later in this chapter.')

    d.sec('5.6', 'Segment growth, mix shift and monetisation')
    d.o(216, 217)
    d.o(587, 589)
    d.cap('Annual and Q1 segment mix (₹ crore, rounded)')
    d.o(591)
    d.o(592)
    d.ip('Segment growth rates diverge consistently: in FY26 the merchant-facing platform grew about '
         '14.6 per cent while the issuing platform grew about 30.2 per cent, and Q1 FY27 repeated the '
         'pattern at roughly 15 per cent against 31 per cent. Diversification is therefore real and '
         'is accelerating. The limitation is equally clear: segment profitability is not disclosed, '
         'so it cannot be established whether the faster-growing segment is accretive or dilutive to '
         'group margin. Given the contribution-margin decline recorded in Section 5.3, the prudent '
         'working assumption is that mix is at least part of the explanation, and the question is '
         'listed as an open one in Chapter 6.')

    d.sec('5.7', 'Q1 FY27 interim update and year-on-year bridge')
    d.cap('Q1 FY27 performance snapshot (quarter ended 30 June 2026)')
    d.o(220)
    d.o(221)
    d.o(595, 597)
    d.cap('Q1 year-on-year bridge')
    d.o(599)
    d.o(600)
    d.ip('The bridge separates scale from quality. On scale, revenue rose 19.65 per cent year on '
         'year to ₹736.92 crore and profit after tax rose from ₹4.79 crore to ₹19.57 crore. On '
         'quality, contribution margin fell from 77.9 per cent to 72.3 per cent and adjusted EBITDA '
         'margin from 19.6 per cent to 17.1 per cent, while adjusted EBITDA in rupees rose only from '
         'about ₹121 crore to about ₹126 crore on nearly ₹121 crore of additional revenue. The '
         'profit increase is large in percentage terms because the prior-year base was very small. '
         'The correct reading is that the quarter confirms continued growth and continued '
         'profitability, but does not yet confirm margin durability.')
    d.sub('Questions carried forward from the income statement')
    d.o(223, 226)

    # --- balance sheet and cash flow -------------------------------------
    d.sec('5.8', 'Balance sheet: selected indicators')
    d.cap('Selected consolidated balance-sheet items (₹ crore)')
    d.o(232)
    d.o(233)
    d.o(234)
    d.ip('Total assets rose from ₹10,715.73 crore to ₹13,296.96 crore and total equity from '
         '₹3,506.14 crore to ₹5,895.41 crore, so the balance sheet grew and its equity funding grew '
         'faster. The composition is the more important point. Current assets of ₹10,884.33 crore '
         'and current liabilities of ₹7,184.12 crore both contain large settlement and prepaid '
         'programme balances that move with transaction activity. A reader who treats the resulting '
         'current ratio as a measure of distributable liquidity will overstate the company’s '
         'financial flexibility; the ratio is read with that caveat in Section 5.9.')

    d.sec('5.9', 'Funding and liquidity')
    d.o(236, 237)
    d.ip('The funding improvement is unambiguous and is one of the clearest positives in the report. '
         'Borrowings excluding leases fell by about ₹546.62 crore, from ₹829.49 crore to ₹282.87 '
         'crore, and the borrowings-to-equity ratio fell from roughly 0.24 times to about 0.05 times '
         'as equity rose after listing. Interest and refinancing risk are correspondingly lower. Two '
         'qualifications apply: lease liabilities are excluded from the borrowing figure, and the '
         'equity increase reflects a capital raise rather than retained earnings, so the lower '
         'leverage has not yet been earned through profit.')

    d.sec('5.10', 'Cash flow and funding movements')
    d.cap('Operating cash flow trend')
    d.o(240)
    d.o(241)
    d.fig('rId15', 5943600, 2534261,
          'Operating cash flow has improved but remains period-sensitive',
          'Net operating cash flow in ₹ crore. [1,2]', pic_id=14)
    d.cap('FY26 cash-flow statement summary (₹ crore)')
    d.o(246)
    d.o(247)
    d.ip('The operating-cash-flow series runs ₹(152.36) crore, ₹(229.01) crore, ₹49.72 crore and '
         '₹395.39 crore across FY23 to FY26 — a reversal of sign and a substantial improvement, but '
         'over only two positive years. The FY26 composition must be read carefully: investing '
         'outflow of ₹1,338.87 crore is dominated by deposit placement rather than by capital '
         'expenditure, and financing inflow of ₹1,972.17 crore reflects the listing. Stripping those '
         'out, the operating performance is genuinely better, but the series is too short and too '
         'settlement-sensitive to be called established.')

    d.sec('5.11', 'Working capital: profitability is not the same as cash flow')
    d.o(249, 250)
    d.o(603, 605)
    d.cap('Selected cash-flow and balance-sheet context (₹ crore)')
    d.o(607)
    d.o(608)
    d.ip('The Q1 FY27 figures make the point most sharply: operating cash flow is reported as '
         'positive ₹78 crore excluding early settlement and negative ₹159 crore including it. The '
         'same quarter is therefore cash-generative or cash-absorbing depending on the treatment of '
         'a single working-capital item. With cash equivalents of ₹1,393.08 crore, other bank '
         'balances of ₹6,832.84 crore and prepaid-card liabilities of ₹5,383.85 crore at 31 March '
         '2026, no reliable statement about free cash can be made without a restricted-cash bridge '
         'that the company does not currently publish. This is the principal unresolved question of '
         'the report.')

    # --- ratios -----------------------------------------------------------
    d.sec('5.12', 'Ratio analysis: formula sheet')
    d.p('Before any ratio is presented, the formula used to calculate it is stated. Where a ratio '
        'can be computed on more than one basis, the basis chosen is named. All averages are simple '
        'averages of opening and closing balance-sheet figures.')
    d.cap('Ratio formula sheet and what each ratio tells the reader')
    d.tbl([
        ['Ratio', 'Formula used in this report', 'What it is meant to show', 'Caveat applied here'],
        ['Revenue growth', '(Current revenue ÷ prior revenue) − 1',
         'Top-line momentum', 'Restated comparatives before FY26'],
        ['CAGR', '(Ending ÷ beginning)^(1/years) − 1',
         'Smoothed multi-year growth', 'Hides the uneven annual path'],
        ['Operating / adjusted EBITDA margin', 'Company-defined EBITDA ÷ revenue',
         'Operating leverage', 'Company-defined; excludes other income, adds back ESOP and '
         'exceptional items'],
        ['Contribution margin', 'Company-defined contribution ÷ revenue',
         'Revenue quality after direct cost', 'Not an accounting-standard gross margin'],
        ['Net profit (PAT) margin', 'PAT ÷ revenue from operations',
         'Profit per rupee of revenue', 'Very small base in FY26'],
        ['Current ratio', 'Current assets ÷ current liabilities',
         'Short-term liquidity', 'Contains settlement and prepaid balances'],
        ['Borrowings to equity', 'Borrowings excluding leases ÷ total equity',
         'Financial leverage', 'Excludes lease liabilities'],
        ['Return on equity', 'PAT ÷ average total equity',
         'Return on shareholder capital', 'Equity base inflated by recent issue'],
        ['Return on assets', 'PAT ÷ average total assets',
         'Return on the asset base', 'Assets include settlement balances'],
        ['Asset turnover', 'Revenue ÷ average total assets',
         'Asset efficiency', 'Depressed by payment-related balances'],
        ['Equity multiplier', 'Average total assets ÷ average total equity',
         'Balance-sheet gearing', 'Moves with programme liabilities, not only debt'],
        ['Cash conversion', 'Operating cash flow ÷ PAT',
         'Quality of reported earnings', 'Not meaningful when PAT is near zero or negative'],
        ['Revenue-to-GTV proxy', 'Revenue ÷ platform GTV, expressed in basis points',
         'Direction of monetisation', 'Diagnostic only; not a contractual take rate'],
    ], widths=[1900, 2900, 2500, 2636])
    d.src('Author’s formula sheet. Worked arithmetic for each line is reproduced in Annexure B.')

    d.sec('5.13', 'Ratio analysis: core dashboard')
    d.cap('Ratio dashboard (selected years)')
    d.o(256)
    d.o(257)
    d.ip('Read as a group, the dashboard describes a company that has fixed its balance sheet before '
         'it has fixed its returns. Leverage and liquidity have improved materially; profitability '
         'has only just turned positive; and returns on equity and assets remain low in absolute '
         'terms. That order of events is normal for a company that has recently raised equity, but '
         'it means the current ratios describe a transition rather than a steady state, and should '
         'not be annualised or extrapolated.')

    d.sec('5.14', 'Supporting annual ratio series')
    d.cap('Profitability, liquidity and leverage series')
    d.o(260)
    d.o(261)
    d.ip('The three-year series shows the direction of travel more reliably than any single year. '
         'Profitability moves from deeply negative to modestly positive; liquidity improves; leverage '
         'falls sharply. No ratio in the table is at a level that would be regarded as strong for a '
         'mature company, and that is the correct reading: the company has removed the most acute '
         'financial risks from its balance sheet without yet demonstrating a competitive return on '
         'the capital employed in it.')

    d.sec('5.15', 'Ratio interpretation')
    d.o(263, 267)
    d.ip('The five readings resolve into one judgement. Balance-sheet risk has fallen and is now '
         'low. Earnings risk remains high, because the profit base is small enough that a modest '
         'change in other income, employee share-based cost, acquisition expense or tax could move '
         'the company back towards break-even. Cash risk is unresolved. Any conclusion drawn from '
         'this chapter has to be conditional on the second and third of those statements.')

    d.sec('5.16', 'Ratio caveats')
    d.o(269)
    d.b([
        'Balance-sheet ratios use reported year-end classifications and are not adjusted for '
        'restricted, earmarked or customer-related balances.',
        'Average-based ratios use simple opening and closing averages, which understate the effect '
        'of capital raised part-way through a year.',
        'Company-defined measures are presented alongside audited measures but are never substituted '
        'for them in the return or valuation work.',
        'Ratios calculated on a small profit base are arithmetically unstable and are reported to '
        'one decimal place only.',
        'No ratio in this chapter is compared with a peer multiple, because the comparability tests '
        'in Section 5.23 are not satisfied by the available public data.',
    ])

    d.sec('5.17', 'DuPont analysis: method')
    d.o(297, 298)

    d.sec('5.18', 'DuPont analysis: results and interpretation')
    d.cap('DuPont decomposition')
    d.o(301)
    d.o(302)
    d.o(304, 305)
    d.ip('The decomposition isolates the cause of the improvement precisely. Asset turnover barely '
         'moved, from 0.186 times in FY24 to 0.223 times in FY25 and 0.226 times in FY26, so the '
         'company did not become materially more efficient in using its asset base. The equity '
         'multiplier fell from 2.89 times to 2.55 times, so leverage actually reduced the return '
         'rather than inflating it. Almost the entire movement in return on equity — from negative '
         '9.39 per cent to positive 2.39 per cent — is attributable to net profit margin turning '
         'from negative 19.32 per cent to positive 4.15 per cent. This is the highest-quality '
         'possible source of a return improvement, because it comes from the income statement rather '
         'than from gearing; but at 2.39 per cent the resulting return is still well below any '
         'reasonable cost of equity.')

    # --- operating KPIs ---------------------------------------------------
    d.sec('5.19', 'Operating KPIs: scale and activity indicators')
    d.cap('Scale and activity indicators')
    d.o(275)
    d.o(276)
    d.fig('rId16', 5943600, 2459869,
          'Platform GTV increased faster than recognised revenue',
          'GTV in ₹ lakh crore. Company-defined platform GTV; this is not revenue or market '
          'share. [1,3]', pic_id=15)
    d.o(579, 581)
    d.cap('Quarterly activity indicators')
    d.o(583)
    d.o(584)
    d.ip('The operating record is the strongest part of the company’s disclosure. Platform gross '
         'transaction value rose from about ₹4.40 lakh crore in FY23 to ₹17.15 lakh crore in FY26, '
         'roughly 3.9 times, while revenue rose about 1.7 times over the same period. Transactions '
         'rose from 112 crore in Q1 FY25 to 201 crore in Q1 FY27 and the installed base of digital '
         'checkout points and merchants expanded alongside. The network is unquestionably growing. '
         'The analytical question, addressed in Section 5.21, is what that network earns.')

    d.sec('5.20', 'Q1 FY27 operating snapshot')
    d.cap('Q1 FY27 operating metrics')
    d.o(282)
    d.o(283)
    d.ip('The quarterly snapshot repeats the annual pattern at higher frequency: ₹4.22 lakh crore of '
         'platform GTV, 201 crore transactions, 21.7 lakh digital checkout points and 11.5 lakh '
         'merchants, against ₹736.92 crore of revenue. Dividing one by the other is instructive only '
         'as a direction indicator, for the reasons set out in Section 5.21. The more useful '
         'quarterly discipline is to watch whether revenue per merchant and revenue per checkout '
         'point hold as the base expands, because a falling figure would indicate that growth is '
         'being bought at declining incremental value.')

    d.sec('5.21', 'Revenue-to-GTV proxy: a diagnostic, not a take rate')
    d.o(285, 286)
    d.o(611, 613)
    d.cap('Revenue to platform GTV proxy')
    d.o(615)
    d.o(616)
    d.ip('This is the central diagnostic of the report. The proxy falls from about 36.3 basis points '
         'in FY23 to 29.1 in FY24, 19.9 in FY25 and 15.8 in FY26 — a decline of more than half in '
         'three years. The decline does not prove that contractual pricing fell. Mix is a sufficient '
         'explanation on its own: the fastest-growing transaction types are the lowest-yielding, and '
         'subscription revenue does not scale with volume at all. But the direction is unambiguous '
         'and it is consistent with the contribution-margin decline in Section 5.3 and with the '
         'falling average ticket size at system level in Section 3.4. The practical implication is '
         'that future revenue growth must come increasingly from services attached to the '
         'transaction rather than from the transaction itself.')

    d.sec('5.22', 'KPI interpretation cautions and monitoring dashboard')
    d.o(288, 292)
    d.o(646, 648)
    d.cap('Suggested quarterly monitoring dashboard')
    d.o(650)
    d.o(651)
    d.ip('The dashboard is designed around consistency rather than around any single target. A '
         'quarter in which gross transaction value, revenue, contribution and operating cash flow all '
         'move in the same direction is evidence; a quarter in which volume rises while revenue '
         'yield and contribution fall is a warning that growth is being purchased. Applying the '
         'dashboard to the periods available, FY26 passes the consistency test and Q1 FY27 does not, '
         'because volume and revenue rose while both margin measures fell.')

    # --- peers and valuation ---------------------------------------------
    d.sec('5.23', 'Peer comparability: why one-line multiples can mislead')
    d.o(628, 630)
    d.cap('Peer-comparison readiness checklist')
    d.o(632)
    d.o(633)
    d.ip('The checklist is the reason this report publishes no peer multiple table. The candidate '
         'comparables differ in listing status, geography, licensing, revenue definition, '
         'gross-versus-net presentation and accounting period; several are private and do not '
         'publish the data required. Presenting a peer price-to-earnings column under those '
         'conditions would create a false impression of precision. A qualitative positioning table '
         'is given instead in Section 5.24, and the gap is recorded as a limitation in Chapter 7.')

    d.sec('5.24', 'Qualitative peer comparison')
    d.cap('Qualitative peer set')
    d.o(311)
    d.o(312)
    d.ip('The qualitative set places the company between two poles. Consumer-facing platforms share '
         'its merchant footprint but monetise a payer relationship it does not have. Global '
         'processors share its infrastructure role but operate under different licences, at '
         'different scale and in different markets. The closest listed Indian comparison is narrower '
         'in product scope. The practical conclusion is that the company is best assessed against '
         'its own disclosed trajectory rather than against a peer average, which is the approach '
         'taken throughout this chapter.')

    d.sec('5.25', 'Market snapshot and last-twelve-month valuation calculation')
    d.cap('Illustrative valuation snapshot as at 1 October 2026')
    d.o(315)
    d.o(316)
    d.o(317)
    d.ip('The arithmetic is transparent and the result is demanding. Last-twelve-month revenue of '
         '₹2,831.60 crore and profit of ₹127.29 crore, against an indicative equity value of about '
         '₹19,334 crore derived from the ₹167.55 close and roughly 115.39 crore shares, imply '
         'approximately 6.8 times sales and about 152 times earnings. A multiple of that order '
         'embeds an expectation of sustained high growth and a substantial future improvement in net '
         'margin. It is also arithmetically unstable: because the earnings denominator is small, the '
         'price-to-earnings ratio will fall very quickly if profit scales and rise very quickly if it '
         'does not.')

    d.sec('5.26', 'Price-to-book sensitivity: an illustrative expectation test')
    d.o(319)
    d.cap('Illustrative justified price-to-book sensitivity')
    d.o(321)
    d.o(322)
    d.ip('The sensitivity converts the market price into an implied expectation, which is a more '
         'useful exercise than asserting whether the share is cheap or dear. On a 12 per cent cost '
         'of equity and 4 per cent growth, a price-to-book of about 3.28 times corresponds to a '
         'sustainable return on equity of roughly 30 per cent. Reported FY26 return on equity was '
         'about 2.4 per cent. The gap between the two is the single clearest statement of what the '
         'market is paying for, and it is a gap that only sustained margin expansion on a growing '
         'revenue base can close.')

    d.sec('5.27', 'Revenue-growth and price-to-sales scenarios')
    d.o(619, 621)
    d.cap('Illustrative equity value and per-share sensitivity')
    d.o(623)
    d.o(624)
    d.ip('The scenario grid is deliberately crude, and its value lies in that crudeness: it shows '
         'that the multiple assumption moves the answer far more than the growth assumption does. '
         'Moving revenue growth from 15 per cent to 25 per cent changes implied equity value by '
         'roughly a fifth; moving the price-to-sales multiple from four times to eight times doubles '
         'it. Any valuation conclusion for this company is therefore principally a statement about '
         'the multiple the market is willing to pay, not about the forecast itself.')

    d.sec('5.28', 'Valuation interpretation and limits')
    d.o(324, 328)
    d.ip('Four limits bound every valuation statement in this report. The price date is 1 October '
         '2026 and the financial denominators are drawn from periods ending on different dates. The '
         'share count is approximate and excludes potential dilution. No enterprise-value multiple '
         'is published because settlement and customer-related balances prevent a reliable net-debt '
         'bridge. And no discounted-cash-flow valuation is attempted, because a forecast built on a '
         'two-year positive cash-flow history would be an assumption presented as an analysis.')

    # --- market snapshot --------------------------------------------------
    d.sec('5.29', 'Listed-market snapshot and price context')
    d.fig('rId17', 5943600, 1882534,
          'BSE price range and IPO issue-price reference',
          'BSE quote page: close ₹167.55 and 52-week range ₹134.75–₹283.70 on 1 October 2026; '
          'IPO issue price ₹221 from the prospectus. [1,11]', pic_id=16)
    d.cap('Listed-market reference points')
    d.o(337)
    d.o(338)
    d.o(637, 639)
    d.cap('Dated price and valuation observations')
    d.o(641)
    d.o(642)
    d.ip('The dated observations record three facts and no forecast. The close of ₹167.55 on 1 '
         'October 2026 sits roughly 24.2 per cent below the ₹221 issue price. The 52-week range of '
         '₹134.75 to ₹283.70 is wide, which indicates that the market has not settled on a valuation '
         'for a company with a short listed history. And the same price supports the multiples '
         'calculated in Section 5.25. Nothing in these observations constitutes a view on future '
         'returns; the price is used only as the denominator-date anchor for the valuation work.')

    d.sec('5.30', 'Scope of technical analysis')
    d.o(340, 341)
    d.cap('Technical indicators: status in this study')
    d.tbl([
        ['Indicator', 'Status in this report', 'Reason'],
        ['Price versus 50-day moving average', 'Not computed',
         'No validated adjusted daily price series was assembled'],
        ['Price versus 200-day moving average', 'Not computed',
         'Listed history is shorter than the window required for a stable reading'],
        ['Relative strength index', 'Not computed',
         'Requires a continuous daily close series'],
        ['Moving-average convergence divergence', 'Not computed',
         'Requires a continuous daily close series'],
        ['Support and resistance', 'Not asserted',
         'Would be a judgement on an incomplete series'],
        ['52-week range', 'Reported',
         '₹134.75 to ₹283.70 as displayed by the exchange on 1 October 2026'],
        ['Closing price', 'Reported',
         '₹167.55 on 1 October 2026, from the official exchange quote page'],
        ['Price versus issue price', 'Calculated',
         '−24.2 per cent against the ₹221 offer price'],
    ], widths=[2600, 2300, 5036])
    d.src('Author’s statement of technical scope. Indicators are recorded as not computed rather '
          'than estimated, so that the reader is not given a number without a series behind it.')
    d.ip('Declining to compute an indicator is itself a finding. A technical study of a security '
         'with roughly a year of listed history and no verified adjusted price series would produce '
         'numbers without information. The honest position is to report the two observations the '
         'exchange actually publishes — the close and the 52-week range — to date them, and to state '
         'that the remaining indicators require a data set this study did not assemble.')

    # --- risk -------------------------------------------------------------
    d.sec('5.31', 'Risk analysis: risk register')
    d.cap('Risk register (qualitative likelihood and impact ratings)')
    d.o(347)
    d.o(348)
    d.ip('Two risks dominate the register because they are rated high on both axes and because they '
         'are the two most capable of changing the investment thesis. The first is fee compression '
         'and monetisation yield: the revenue-to-GTV proxy in Section 5.21 has already halved, and a '
         'continuation would undermine the revenue growth on which the valuation in Section 5.25 '
         'depends. The second is cash conversion and settlement timing: the Q1 FY27 figures swing '
         'from positive to negative on the treatment of a single item, so the quality of earnings '
         'cannot yet be verified. The regulatory and cyber risks are rated high-impact but '
         'medium-likelihood, and are managed rather than removed.')

    d.sec('5.32', 'Early-warning dashboard')
    d.cap('Indicators to track each quarter')
    d.o(351)
    d.o(352)
    d.ip('The early-warning list converts the register into something a reader can actually monitor. '
         'Each indicator is published or derivable from published data, each is available quarterly, '
         'and each maps to a specific risk. The discipline is to decide in advance what movement '
         'would count as disconfirming evidence, rather than to re-interpret each quarter’s result '
         'to fit a view already held.')

    # --- ESG --------------------------------------------------------------
    d.sec('5.33', 'ESG and responsible fintech')
    d.sub('Environmental considerations')
    d.o(357)
    d.sub('Social considerations')
    d.o(359, 362)
    d.sub('Governance and trust')
    d.o(364)
    d.sub('Suggested ESG disclosures')
    d.cap('Potential metrics for future disclosure')
    d.o(367)
    d.o(368)
    d.ip('ESG is treated here as a financial-risk lens rather than as a reporting obligation. The '
         'environmental exposure is concrete: a very large installed base of payment terminals '
         'creates a device-lifecycle and electronic-waste obligation that will eventually carry '
         'cost. The social exposure sits in affordability and credit-linked products, where conduct '
         'failures attract regulatory attention that raises the cost of an entire product line. The '
         'governance exposure follows from the absence of an identifiable promoter, which places the '
         'full weight of accountability on the board and on disclosure quality. None of these is '
         'currently quantified in company reporting, which is why the suggested metrics table is '
         'framed as a disclosure recommendation.')

    d.sec('5.34', 'Separating facts, inferences, assumptions and judgments')
    d.o(691, 693)
    d.cap('Example evidence labels used in this report')
    d.o(695)
    d.o(696)
    d.ip('This classification is what allows a reader to audit the report. Audited revenue of '
         '₹2,710.59 crore for FY26 is a fact. The statement that mix explains part of the '
         'contribution-margin decline is an inference. A 12 per cent cost of equity is an '
         'assumption. The statement that the valuation is demanding relative to current returns is a '
         'judgement. Mixing the four categories is the most common failure in company research, and '
         'keeping them separate is the main reason this report reaches a conditional rather than a '
         'categorical conclusion.')

    d.sec('5.35', 'Common-size reading of the FY26 income statement')
    d.p('A common-size statement restates every line as a percentage of total income, so that the '
        'structure of the business can be compared across periods and against peers without the '
        'distortion of absolute size. The table below restates the FY26 statement of profit and '
        'loss on that basis using the totals disclosed in Section 5.2: total income of ₹2,847.15 '
        'crore, total expenses of ₹2,706.37 crore, profit before tax of ₹137.28 crore after share '
        'of loss of associates and joint ventures, tax expense of ₹24.77 crore and profit after '
        'tax of ₹112.51 crore.')
    d.cap('Common-size statement of profit and loss, FY26')
    d.tbl([
        ['Line item', '₹ crore', 'Per cent of total income'],
        ['Revenue from operations', '2,710.59', '95.20'],
        ['Other income', '136.56', '4.80'],
        ['Total income', '2,847.15', '100.00'],
        ['Total expenses', '2,706.37', '95.06'],
        ['Profit before tax and share of associates', '140.78', '4.94'],
        ['Profit before tax (after share of associates)', '137.28', '4.82'],
        ['Tax expense', '24.77', '0.87'],
        ['Profit after tax', '112.51', '3.95'],
    ], widths=[4736, 2600, 2600])
    d.src('Author’s calculation from the FY26 consolidated statement of profit and loss presented '
          'in Section 5.2. Percentages are computed on total income and are rounded to two '
          'decimal places, so components may not sum exactly.')
    d.ip('Three features of the structure are worth recording. First, other income contributes '
         '4.80 per cent of total income, which is larger than the 3.95 per cent net margin; the '
         'company would not have reported a profit for the year on operating revenue alone at the '
         'FY26 expense base. Second, total expenses absorb 95.06 per cent of total income, so the '
         'pre-tax cushion is 4.94 per cent and a cost movement of five percentage points would '
         'eliminate it. Third, the effective tax charge of ₹24.77 crore on pre-tax profit of '
         '₹137.28 crore is about 18.0 per cent, below the headline corporate rate, which is '
         'consistent with a company still carrying unabsorbed losses from earlier years. Each of '
         'these three features argues for treating the FY26 result as a first profitable year '
         'rather than as a normalised earnings base.')

    d.sec('5.36', 'Trend index analysis with FY23 as the base year')
    d.p('Trend index analysis rebases each series to 100 in the first year of the window, so that '
        'series measured in different units can be compared on a single scale. The two series that '
        'matter most for this report are revenue from operations and gross transaction value, '
        'because the relationship between them is the central diagnostic established in Section '
        '5.21.')
    d.cap('Trend indices for revenue and gross transaction value, FY23 = 100')
    d.tbl([
        ['Series', 'FY23', 'FY24', 'FY25', 'FY26'],
        ['Revenue from operations (₹ crore)', '1,597.66', '1,769.55', '2,274.27', '2,710.59'],
        ['Revenue index (FY23 = 100)', '100.0', '110.8', '142.3', '169.6'],
        ['Gross transaction value (₹ lakh crore)', '4.40', '6.08', '11.42', '17.15'],
        ['GTV index (FY23 = 100)', '100.0', '138.2', '259.5', '389.8'],
        ['Revenue index as a share of GTV index', '1.00', '0.80', '0.55', '0.44'],
    ], widths=[3936, 1500, 1500, 1500, 1500])
    d.src('Author’s calculation from the annual revenue and gross transaction value figures '
          'presented in Sections 5.2 and 5.20. Indices are rounded to one decimal place.')
    d.ip('The indices make the divergence unambiguous. Over three years gross transaction value '
         'multiplied by about 3.9 times while revenue multiplied by about 1.7 times, so the ratio '
         'of the two indices falls from 1.00 to 0.44. In plain terms, by FY26 each additional '
         'rupee of value routed through the platform was associated with less than half the '
         'revenue it would have produced at FY23 rates. The trend is monotonic across all three '
         'years, which rules out a single-year explanation such as one large merchant win or an '
         'accounting reclassification, and points instead to a sustained shift in mix, in pricing, '
         'or in both. Section 5.21 sets out why the available disclosure does not allow those two '
         'explanations to be separated, and Section 6.6 proposes the disclosure that would.')

    d.sec('5.37', 'Summary of the analysis')
    d.cap('Summary of analytical findings')
    d.tbl([
        ['Analytical block', 'Principal finding', 'Confidence'],
        ['Revenue and growth',
         'FY23–FY26 CAGR about 19.3%; FY26 growth 19.2%; Q1 FY27 growth 19.65%',
         'High — audited and reported'],
        ['Profitability',
         'First positive PAT year in FY26 at ₹112.51 crore; Q1 FY27 PAT ₹19.57 crore',
         'High — audited and limited-reviewed'],
        ['Margin quality',
         'Adjusted EBITDA margin up to 20.62% in FY26, but contribution margin down to 75.3% '
         'and 72.3% in Q1 FY27',
         'Medium — company-defined measures'],
        ['Funding',
         'Borrowings excluding leases down to ₹282.87 crore; borrowings/equity about 0.05×',
         'High — audited'],
        ['Cash conversion',
         'CFO positive in FY25 and FY26 but reverses sign in Q1 FY27 on settlement treatment',
         'Low — unresolved'],
        ['Returns',
         'FY26 ROE about 2.39%, driven almost entirely by margin, not leverage or turnover',
         'High — author calculation from audited data'],
        ['Monetisation',
         'Revenue-to-GTV proxy falls from about 36.3 bps to 15.8 bps across FY23–FY26',
         'Medium — diagnostic ratio, definitions differ'],
        ['Valuation',
         'About 6.8× LTM sales and 152× LTM PAT at the 1 October 2026 close',
         'Medium — dated, approximate share count'],
        ['Risk',
         'Fee compression and cash conversion are the two thesis-changing risks',
         'Qualitative judgement'],
    ], widths=[2200, 5200, 2536])
    d.src('Author’s synthesis of Chapter 5. Confidence refers to the strength of the underlying '
          'evidence, not to the attractiveness of the finding.')

    # ======================================================================
    # CHAPTER 6 - FINDINGS, SUGGESTIONS AND CONCLUSION
    # ======================================================================
    d.chapter(6, 'Findings, Suggestions and Conclusion',
              'Evidence-led synthesis, investment thesis, researcher’s view and '
              'practical recommendations')

    d.sec('6.1', 'Key findings at a glance')
    d.cap('Key findings at a glance')
    d.o(87)
    d.o(88)
    d.ip('The glance table is the one-page answer to the research question. It states the four '
         'movements that define the FY23–FY26 window — growth, the profitability inflection, '
         'deleveraging and the monetisation decline — together with the single unresolved item, '
         'cash conversion. Sections 6.2 and 6.3 set out the evidence behind each line, and Section '
         '6.4 converts the same five statements into a position.')

    d.sec('6.2', 'Major findings')
    d.o(383, 389)

    d.sec('6.3', 'Findings mapped to the research propositions')
    d.cap('Propositions tested and outcomes')
    d.tbl([
        ['Proposition from Section 1.5', 'Evidence', 'Outcome'],
        ['The platform monetises through contracted fees rather than a share of value routed',
         'Prospectus and segment disclosures; revenue stream mapping in Section 4.7',
         'Supported'],
        ['GTV growth translates one-for-one into revenue',
         'GTV up about 3.9× and revenue about 1.7× over FY23–FY26; proxy falls from 36.3 to '
         '15.8 bps',
         'Not supported'],
        ['The profitability inflection is durable',
         'FY26 PAT ₹112.51 crore and Q1 FY27 PAT ₹19.57 crore, but both margin measures lower '
         'year on year in Q1 FY27',
         'Partially supported'],
        ['The capital structure has improved',
         'Borrowings excluding leases down ₹546.62 crore; borrowings/equity 0.24× to 0.05×',
         'Supported'],
        ['Operating cash conversion has become predictable',
         'CFO reverses sign across the window and is treatment-dependent in Q1 FY27',
         'Not established'],
    ], widths=[3400, 4600, 1936])
    d.src('Author’s assessment. Two of five propositions are supported outright, one partially, one '
          'refuted and one unresolved.')
    d.ip('A mixed result is the honest result. The company has demonstrably strengthened its '
         'balance sheet and has reached profitability, so two propositions are supported. It has '
         'demonstrably not converted volume growth into proportionate revenue, so one is refuted. '
         'The durability of profit and the predictability of cash both require more periods of '
         'evidence than currently exist. A report that recorded five confirmations from four years '
         'of partly restated data would not be credible.')

    d.sec('6.4', 'Investment thesis and final recommendation')
    d.cap('Investment thesis worksheet')
    d.tbl([
        ['Question', 'Assessment based on the evidence in this report'],
        ['What is the strongest reason to own the business?',
         'A large and still-expanding merchant, checkout and institutional footprint, now '
         'operating at positive reported profit with materially lower borrowings and a '
         'diversifying revenue mix.'],
        ['What is the biggest reason not to own it?',
         'Monetisation yield on platform activity has fallen by more than half in three years '
         'while the market price embeds an expectation of roughly 30 per cent sustainable return '
         'on equity against a reported 2.4 per cent.'],
        ['What could drive earnings higher?',
         'Faster growth in the issuing and acquiring platform, higher attachment of recurring '
         'value-added services, operating leverage on the existing cost base, and successful '
         'integration of acquired capabilities.'],
        ['What could cause earnings to disappoint?',
         'Continued contribution-margin decline, fee compression on the fastest-growing payment '
         'types, higher share-based and acquisition-related costs, regulatory change, or a '
         'cyber or availability incident.'],
        ['Is the valuation attractive?',
         'Not on current evidence. About 6.8 times last-twelve-month sales and 152 times '
         'last-twelve-month profit require sustained growth and a substantial future margin '
         'improvement that the disclosed record does not yet evidence.'],
        ['What would change the view favourably?',
         'Two or three consecutive quarters of stable or rising contribution margin, a published '
         'restricted-cash and settlement bridge, and disclosed segment profitability.'],
        ['What would change the view unfavourably?',
         'A further fall in revenue per merchant or per checkout point, a return to negative '
         'operating cash flow on a like-for-like basis, or a material regulatory or security '
         'event.'],
        ['What is the single most important number to watch?',
         'Contribution margin as a percentage of revenue, reported quarterly.'],
        ['Overall research view',
         'Constructive on the business and the balance sheet; cautious on margin durability, cash '
         'conversion and valuation. Not a recommendation to buy, sell or hold.'],
    ], widths=[3000, 6936])
    d.src('Author’s worksheet. This is an academic research view prepared for a summer internship '
          'report. It is not investment advice, a target price or a recommendation.')
    d.ip('The thesis is deliberately two-sided. The operational and balance-sheet case is genuinely '
         'strong and has improved in every period examined. The valuation case is weak at the price '
         'observed, because the implied expectation is roughly twelve times the return the company '
         'currently earns. A reader who believes margin will expand materially will reach a '
         'favourable conclusion; a reader who weights the contribution-margin trend more heavily '
         'will not. The purpose of this report is to make both positions visible from the same '
         'evidence, not to conceal one of them.')

    d.sec('6.5', 'Researcher’s view')
    d.cap('Research view dashboard')
    d.o(410)
    d.o(411)
    d.o(412)
    d.ip('The dashboard is conditional by construction. Each dimension carries both an assessment '
         'and the reason behind it, so that a reader who disagrees with a reason can discard the '
         'assessment that rests on it. The view should be revisited after the next two audited years '
         'and after the company publishes segment profitability and a settlement-adjusted cash '
         'statement, because those two disclosures would resolve the largest remaining uncertainties '
         'in this report.')

    d.sec('6.6', 'Suggestions for Pine Labs Limited')
    d.o(391, 396)
    d.ip('The six recommendations share one purpose: to let an external reader verify the quality of '
         'growth rather than only its quantity. The first two would resolve the two unresolved '
         'findings of this report — the monetisation trend and cash conversion — at no commercial '
         'cost, because both are reconciliations of information the company already holds. The '
         'remaining four address disclosure of concentration, acquisition outcomes, operational '
         'resilience and environmental obligation, each of which is currently assessed by inference '
         'rather than from data.')

    d.sec('6.7', 'Suggestions for investors and future student researchers')
    d.o(398, 402)
    d.p('A seventh suggestion applies specifically to student work. Choose a company that publishes '
        'a key-performance-indicator data book, because the gap between company-defined measures and '
        'audited figures is where the genuine analysis lies. A report that simply restates audited '
        'totals demonstrates transcription; a report that reconciles the two demonstrates analysis.')

    d.sec('6.8', 'Learning outcomes of the project')
    d.b([
        'The ability to separate audited figures, company-defined measures, author calculations and '
        'personal judgement, and to label each explicitly in a written report.',
        'Practical command of growth, margin, liquidity, leverage, return and DuPont arithmetic '
        'applied to a real consolidated statement rather than to a textbook example.',
        'An understanding of why an activity measure such as gross transaction value or traded '
        'volume must never be presented as turnover, in either a payments business or a broking '
        'business.',
        'Experience of building a dated relative valuation and of stating the assumptions, the '
        'price date and the share count on which it depends.',
        'The discipline of reporting an unresolved question as unresolved, which was the outcome for '
        'cash conversion in this study.',
        'Direct market experience from the dealing desk — order entry, confirmation, status '
        'reporting and settlement — that informed the market-infrastructure discussion in Chapter 2.',
    ])

    d.sec('6.9', 'Conclusion')
    d.o(404, 405)
    d.p('The study therefore ends with a conditional conclusion rather than a categorical one, and '
        'that conclusion is the appropriate output of the evidence available. Pine Labs Limited has '
        'built a genuinely large platform, has repaired its balance sheet, and has crossed into '
        'reported profitability. It has not yet demonstrated that the profitability is durable, that '
        'cash conversion is predictable, or that monetisation yield can be stabilised. At the price '
        'observed on 1 October 2026 the market is paying for the resolution of all three questions in '
        'the company’s favour. The purpose of the next several quarters of disclosure, from a '
        'research point of view, is to establish whether that confidence is warranted.')

    # ======================================================================
    # CHAPTER 7 - LIMITATIONS
    # ======================================================================
    d.chapter(7, 'Limitations of the Study',
              'Data, period, method, scope and interpretation constraints on the '
              'conclusions reached')

    d.sec('7.1', 'Limitations arising from the data')
    d.o(69, 74)

    d.sec('7.2', 'Limitations arising from the period of study')
    d.b([
        'The company listed in 2025, so only one fully audited year exists as a listed issuer. '
        'FY23 to FY25 comparatives are prospectus-restated following a corporate reorganisation and '
        'are not identical to previously reported legal-entity accounts.',
        'The interim update covers a single quarter, Q1 FY27. One quarter cannot establish a trend '
        'and is not annualised anywhere in this report.',
        'The analysis cut-off is 3 October 2026 and the market observation is dated 1 October 2026. '
        'Any event after those dates is outside the study.',
        'Acquisitions completed during or after FY26 change the composition of the consolidated '
        'group between comparative periods.',
    ], bold=True)

    d.sec('7.3', 'Limitations arising from the method')
    d.b([
        'No primary data was collected. There were no interviews with management, merchants, banks '
        'or competitors, and no survey evidence.',
        'Segment profitability is not disclosed by the company, so the margin consequence of the '
        'mix shift identified in Sections 4.6 and 5.6 can be inferred but not measured.',
        'No discounted-cash-flow valuation is attempted. A forecast built on a two-year positive '
        'cash-flow history would be an assumption presented as an analysis.',
        'No quantitative peer multiple table is published, because the comparability conditions set '
        'out in Section 5.23 are not met by the available public data.',
        'Technical indicators were not computed because a validated adjusted daily price series was '
        'not assembled; the position is stated explicitly in Section 5.30.',
        'Ratios calculated on a small profit base are arithmetically unstable, and ratios using '
        'average balance-sheet figures understate the effect of capital raised during a year.',
    ], bold=True)

    d.sec('7.4', 'Limitations arising from the scope')
    d.b([
        'The study covers the consolidated group only. Individual subsidiaries, joint arrangements '
        'and overseas entities are not analysed separately.',
        'The financial performance of the internship host, Rosy Blue Securities Pvt. Ltd., is not '
        'analysed. The firm is described from its public service profile only, and no client, '
        'account or confidential information is disclosed.',
        'Taxation, transfer pricing, detailed accounting-policy analysis and legal interpretation of '
        'licence status are outside the scope of the report.',
        'The report does not provide an ESG score or any form of assurance; the ESG discussion in '
        'Section 5.33 is a risk lens, not an audited assessment.',
    ], bold=True)

    d.sec('7.5', 'Limitations arising from interpretation')
    d.b([
        'Qualitative ratings in the PESTLE, Five Forces, SWOT and risk-register tables are the '
        'author’s judgements. Another analyst could reasonably rate the same evidence differently.',
        'The revenue-to-GTV proxy is a diagnostic constructed by the author. It is not a company '
        'key performance indicator and it is not a contractual take rate.',
        'The price-to-book sensitivity uses an assumed 12 per cent cost of equity and 4 per cent '
        'growth. Both are assumptions, and the output is an illustration rather than a valuation.',
        'Conclusions drawn in Chapter 6 are conditional on the evidence available to 3 October 2026 '
        'and should be revisited as further audited periods are published.',
    ], bold=True)

    d.sec('7.6', 'Effect of the limitations on the conclusions')
    d.cap('How each limitation constrains a specific conclusion')
    d.tbl([
        ['Limitation', 'Conclusion it constrains', 'Effect'],
        ['Short listed record', 'Durability of the profitability inflection',
         'Reported as partially supported rather than supported'],
        ['No segment profitability', 'Margin consequence of the DITP/IAP mix shift',
         'Inferred, not measured'],
        ['Settlement-sensitive cash flow', 'Quality of earnings and cash conversion',
         'Recorded as not established'],
        ['No comparable peer data', 'Relative valuation',
         'No peer multiple table published'],
        ['No daily price series', 'Technical analysis',
         'Indicators recorded as not computed'],
        ['Secondary data only', 'Unit economics at merchant level',
         'Not attempted; listed as a direction for future research'],
    ], widths=[2600, 4000, 3336])
    d.src('Author’s assessment. Every limitation in this chapter is linked to the specific '
          'conclusion it affects, so that no finding is presented more strongly than its evidence '
          'allows.')
    d.ip('Read as a whole, the limitations constrain the precision of the conclusions without '
         'overturning their direction. The movements this report identifies — revenue growth, the '
         'first profitable year, the fall in borrowings and the decline in the revenue-to-GTV '
         'proxy — all rest on audited or limited-reviewed figures and would survive any reasonable '
         'change of method. What the limitations prevent is the next step: attributing those '
         'movements confidently to their causes, and pricing them. That is why the report ends '
         'with a conditional position rather than a target price.')

    d.sec('7.7', 'Directions for future research')
    d.p('The limitations above are not only constraints on this study; each of them also '
        'identifies work that a later researcher with better data, more time or direct access '
        'could carry out. The following directions are stated specifically enough to be actionable '
        'as dissertation or project topics.')
    d.cap('Directions for future research arising from this study')
    d.tbl([
        ['Direction', 'What it would require', 'Question it would answer'],
        ['Segment profitability analysis',
         'Segment-level cost allocation, either disclosed by the company or reconstructed from '
         'later filings',
         'Whether the shift towards issuing and acceptance improves or dilutes group margin'],
        ['Settlement-adjusted cash-flow study',
         'A consistent series of operating cash flow stated before and after settlement movements',
         'Whether cash conversion is structurally positive once float timing is neutralised'],
        ['Merchant-level unit economics',
         'Primary survey or interview access to merchants across size bands',
         'Revenue, cost to serve and retention per merchant, and the payback on a deployed '
         'checkout point'],
        ['Fee-realisation decomposition',
         'Transaction-mix data by product and by merchant category',
         'How much of the fall in the revenue-to-GTV proxy is mix and how much is price'],
        ['Post-listing price behaviour study',
         'A full daily price and volume series covering at least one year after listing',
         'Whether the technical picture deferred in Section 5.30 supports or contradicts the '
         'fundamental reading'],
        ['Peer-set construction',
         'Standardised definitions of GTV, take rate and contribution margin across listed '
         'payment companies',
         'Whether the valuation is demanding relative to genuinely comparable firms'],
        ['Regulatory-impact study',
         'A timeline of regulatory changes affecting acquiring, issuing and card-data storage',
         'How specific rule changes have affected platform economics in practice'],
    ], widths=[2600, 4000, 3336])
    d.src('Author’s compilation. Each direction is drawn from a limitation recorded in Sections '
          '7.1 to 7.5 and is framed so that the required data source is explicit.')
    d.ip('Two of these directions would materially change the conclusions of this report if they '
         'were completed. A settlement-adjusted cash-flow study would resolve the single largest '
         'open question in Chapter 5, and a fee-realisation decomposition would determine whether '
         'the monetisation decline is a deliberate consequence of mix or an involuntary '
         'consequence of pricing pressure. The remaining five would improve precision rather than '
         'change direction.')

    # ======================================================================
    # REFERENCES
    # ======================================================================
    d.part('References and Bibliography',
           'Primary company documents, regulatory and exchange sources, frameworks and websites',
           chap_label='')
    d.o(414)
    d.sub('A. Primary company documents')
    d.oo(415, 438)
    d.sub('B. Regulatory, exchange and industry sources')
    d.oo(439, 447)
    d.sub('C. Company investor-relations and document repositories')
    d.oo(448, 453)
    d.sub('D. Books, frameworks and academic references')
    d.oo(454, 459)
    d.sub('E. Organisational and market-infrastructure sources')
    d.b([
        '[16] Rosy Blue Securities Pvt. Ltd. Public service profile and website disclosures. '
        'Used for the organisational background in Chapter 2. Open source.',
        '[17] Securities and Exchange Board of India. Stock broker regulations and intermediary '
        'framework. Used for the regulatory-perimeter discussion in Section 3.12. Open source.',
        '[18] Securities and Exchange Board of India. Research analyst framework. Used for the '
        'activity-to-rule mapping in Section 3.12. Open source.',
        '[19] Securities and Exchange Board of India. Investor education and investor-protection '
        'materials. Used in Sections 2.8 and 3.13. Open source.',
        '[20] National Stock Exchange of India Limited. Market segment and trading-system pages. '
        'Used for the cash and F&O descriptions in Section 2.5. Open source.',
        '[21] National Stock Exchange of India Limited. Clearing and settlement information. Used '
        'for the market-infrastructure table in Section 2.8. Open source.',
        '[22] National Securities Depository Limited and Central Depository Services (India) '
        'Limited. Depository and depository-participant descriptions. Used in Section 2.8. '
        'Open source.',
    ])
    d.sub('F. Websites consulted')
    d.b([
        'www.pinelabs.com — company and investor-relations pages.',
        'www.bseindia.com — official quote page for the market snapshot.',
        'www.nseindia.com — market segment, clearing and settlement information.',
        'www.rbi.org.in — Payment Systems Report and related publications.',
        'www.npci.org.in — Unified Payments Interface product statistics.',
        'www.sebi.gov.in — intermediary framework and investor-education material.',
    ])

    # ======================================================================
    # ANNEXURES
    # ======================================================================
    d.annexure('A', 'Compact Data Sheet')
    d.o(461)
    d.cap('Core financial series (₹ crore unless stated)')
    d.o(463)
    d.o(464)
    d.cap('FY26 balance-sheet and cash-flow snapshot (₹ crore)')
    d.o(466)
    d.o(467)
    d.cap('Q1 FY27 interim snapshot')
    d.o(469)
    d.o(470)
    d.ip('This annexure is the single place from which every calculation in Chapter 5 can be '
         'reproduced. A reader who wishes to verify any ratio, index or growth rate in this report '
         'should begin here rather than with the narrative: all three tables are sourced from '
         'audited or limited-reviewed statements, and no figure appears elsewhere in the report '
         'that cannot be traced back to one of them, to the quarterly data book in Annexure E, or '
         'to a clearly labelled author calculation built on them.')

    d.annexure('B', 'Formulas and Worked Calculations')
    d.cap('Formula reference with worked illustrations')
    d.o(473)
    d.o(474)
    d.ip('Every ratio quoted in Chapter 5 is defined here and illustrated on the FY26 figures, so '
         'that a reader can confirm both the formula and the inputs used. Where a ratio can be '
         'computed on more than one basis — for example leverage on total liabilities or on '
         'borrowings alone, or returns on opening, closing or average balances — the basis adopted '
         'in this report is stated explicitly, because disclosing the basis matters more than the '
         'choice between equally defensible conventions.')

    d.annexure('C', 'Glossary of Terms')
    d.cap('Key terms used in this report')
    d.o(477)
    d.o(478)
    d.ip('The glossary is deliberately restricted to terms whose meaning affects a number in this '
         'report. Several of them — gross transaction value, take rate, contribution margin, '
         'adjusted EBITDA and digital checkout point — are company-defined or industry-defined '
         'rather than prescribed by accounting standards, which is precisely why they are listed. '
         'A reader comparing this report with another study of the same company should check these '
         'definitions first, because definitional differences, not analytical ones, are the most '
         'common source of apparently conflicting conclusions.')

    d.annexure('D', 'List of Abbreviations')
    d.cap('Abbreviations used in this report')
    d.tbl([
        ['Abbreviation', 'Expansion'],
        ['API', 'Application programming interface'],
        ['BSE', 'BSE Limited (formerly Bombay Stock Exchange)'],
        ['CAGR', 'Compound annual growth rate'],
        ['CCPS', 'Compulsorily convertible preference shares'],
        ['CFO / CFI / CFF', 'Cash flow from operating / investing / financing activities'],
        ['CTCL', 'Computer-to-computer link'],
        ['DCP', 'Digital checkout point'],
        ['DITP', 'Digital Infrastructure and Transaction Platform'],
        ['EBITDA', 'Earnings before interest, tax, depreciation and amortisation'],
        ['EIC', 'Economy–Industry–Company framework'],
        ['ESG', 'Environmental, social and governance'],
        ['ESOP', 'Employee stock option plan'],
        ['F&O', 'Futures and options'],
        ['FY', 'Financial year ended 31 March'],
        ['GTV', 'Gross transaction value'],
        ['IAP', 'Issuing and Acquiring Platform'],
        ['IPO', 'Initial public offering'],
        ['KPI', 'Key performance indicator'],
        ['LTM', 'Last twelve months'],
        ['MMS', 'Master of Management Studies'],
        ['NEAT', 'National Exchange for Automated Trading'],
        ['NPCI', 'National Payments Corporation of India'],
        ['NSE', 'National Stock Exchange of India Limited'],
        ['P/B', 'Price-to-book ratio'],
        ['P/E', 'Price-to-earnings ratio'],
        ['P/S', 'Price-to-sales ratio'],
        ['PAT', 'Profit after tax'],
        ['PBT', 'Profit before tax'],
        ['POS', 'Point of sale'],
        ['RBI', 'Reserve Bank of India'],
        ['ROA', 'Return on assets'],
        ['ROCE', 'Return on capital employed'],
        ['ROE', 'Return on equity'],
        ['SEBI', 'Securities and Exchange Board of India'],
        ['SME', 'Small and medium-sized enterprise'],
        ['UPI', 'Unified Payments Interface'],
        ['YoY', 'Year on year'],
    ], widths=[2200, 7736])
    d.src('Abbreviations are expanded at first use in the text; this table is a consolidated '
          'reference.')
    d.ip('Two pairs of abbreviations in this list are routinely confused and are worth separating '
         'here. DITP and IAP are the company’s two reporting platforms and are not '
         'interchangeable: the first covers digital infrastructure and transactions, the second '
         'covers issuing and acquiring, and the shift in mix between them is a finding of this '
         'report. GTV and revenue are likewise distinct: the first is value routed through the '
         'platform and the second is what the company earns for routing it, and the widening gap '
         'between the two is the central diagnostic of Chapter 5.')

    d.annexure('E', 'Quarterly Data Book and Supporting Exhibits')
    d.p('This annexure consolidates the quarterly series and supporting exhibits referenced in '
        'Chapter 5. All figures are as published by the company in its key-performance-indicator '
        'data books and results, rounded as presented in those documents. Annual figures and '
        'financial-statement totals take precedence where a rounded quarterly figure differs.')
    d.sub('E.1 Quarterly revenue by platform')
    d.cap('Quarterly revenue by platform (₹ crore, rounded)')
    d.o(567)
    d.src('Pine Labs KPI Data Book, Q1 FY27 [6]. Reproduced from Section 5.4 for reference.')
    d.sub('E.2 Quarterly margin and profit indicators')
    d.cap('Quarterly margin and profit indicators')
    d.o(575)
    d.src('Pine Labs KPI Data Book and management profit-and-loss, Q1 FY27 [6]. Reproduced from '
          'Section 5.5.')
    d.sub('E.3 Quarterly activity indicators')
    d.cap('Quarterly activity indicators')
    d.o(583)
    d.src('Pine Labs KPI Data Book, Q1 FY27 [6]. Reproduced from Section 5.19.')
    d.sub('E.4 Public payment-system indicators')
    d.cap('Public payment-system indicators')
    d.o(559)
    d.src('RBI Payment Systems Report, December 2025 [9]; NPCI UPI Product Statistics [10]. '
          'Reproduced from Section 3.4.')
    d.sub('E.5 Revenue to platform GTV proxy')
    d.cap('Revenue to platform GTV proxy')
    d.o(615)
    d.src('Author calculation from restated and audited revenue [1–3] and the company GTV series '
          '[3,6]. Reproduced from Section 5.21.')
    d.sub('E.6 Valuation sensitivity')
    d.cap('Illustrative equity value and per-share sensitivity')
    d.o(623)
    d.src('Author scenario arithmetic. Reproduced from Section 5.27. No forecast or target is '
          'implied.')
    d.ip('The exhibits are reproduced here so that the quarterly evidence can be read as a '
         'continuous series rather than in the fragments in which it appears in Chapter 5. Read '
         'together, E.1 to E.3 show growth in every quarter of the window alongside a falling '
         'contribution margin, E.5 shows the monetisation proxy declining across all four years, '
         'and E.6 shows how sensitive the implied value is to assumptions that this study does not '
         'attempt to resolve. Nothing in this annexure is new information; its purpose is '
         'verification.')

    d.annexure('F', 'Final Submission Checklist')
    d.o(480)
    d.o(481, 490)
    d.b([
        '☐ Confirm that the report is organised in seven chapters followed by references and '
        'Annexures A to F, and that the index page numbers match the final paginated document.',
        '☐ Check that every table and figure carries a caption, a source note and an '
        'interpretation, as required by the research-report template.',
        '☐ Verify that all cross-references to chapters, sections, tables and annexures resolve '
        'correctly after any further editing.',
        '☐ Before printing or converting to PDF, select the whole document (Ctrl+A) and press F9 '
        'to update fields, so that the page numbers in the index, the list of tables and the list '
        'of figures are recalculated against the final pagination.',
    ])
