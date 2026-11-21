"""The day's stories, as printed on the page, with the reports each was checked against.

Day: Friday 20 November 2026. Every figure and name below appears in the cited
report(s) of that day; nothing is estimated or rounded beyond what they say.
"""

DATE_LINE = "FRIDAY 20 NOVEMBER 2026  ·  THE DAY'S TOP STORIES"
TAGLINE = ("One day. One page.", "The world on 20 Nov 2026")

# BBC "Russian missile hits Poland as Ukraine's allies hold military exercise, says Tusk"
#   https://www.bbc.co.uk/news/articles/cqx2x9dklxnro
# DW "Ukraine updates: Russian attack 'one of largest,' Zelenskyy says" (20 Nov 2026)
#   https://www.dw.com/en/ukraine-updates-russian-attack-one-of-largest-zelenskyy-says/live-79999822
LEAD = {
    "kicker": "Russia–Ukraine war  ·  NATO",
    "headline": "Russian missile crashes in Poland as huge air attack pounds Ukraine",
    "body": (
        "A Kh-101 cruise missile hits a field at Nowy Lipowiec, ~50 km from the "
        "Ukrainian border; no one hurt. Tusk: a “provocation”. NATO scrambles "
        "jets. At least 8 killed in Ukraine as Kyiv’s Dnipro bridges are hit."
    ),
    "stats": [
        ("~400", "drones launched at Ukraine"),
        ("110+", "missiles, 27 of them ballistic"),
        ("8+", "killed in Ukraine"),
    ],
    "stat_note": "Figures: Zelenskyy; BBC; DW",
}

# BBC "Tech stock sell-off drags markets down as Anthropic shares slide"
#   https://www.bbc.co.uk/news/articles/c6808ym10vzgo
MARKETS = {
    "kicker": "Markets  ·  Wall Street",
    "headline": "AI sell-off: Nasdaq plunges 5.3%",
    "bars": [("Nasdaq", 5.3), ("S&P 500", 3.7), ("Dow", 1.9)],
    "body": (
        "S&P 500 and Dow fall into correction. Nvidia −13.7%; "
        "Anthropic −8.5% on its 2nd day of trading."
    ),
}

# BBC "UK to explore even closer ties with EU after agreeing deal, says Burnham"
#   https://www.bbc.co.uk/news/articles/c6jreyqgw4e9o
# France 24 "UK and EU strike 'landmark' deal to rebuild ties after Brexit"
UKEU = {
    "kicker": "Europe  ·  Brussels summit",
    "headline": "UK and EU seal post-Brexit reset deal",
    "body": (
        "Most food-export checks scrapped from 2028; youth scheme for up to "
        "100,000 18–31s each way; carbon markets to link. PM Andy Burnham: "
        "a “good day”."
    ),
}

# Al Jazeera "Fossil fuel talks deadlock pushes COP31 climate summit into overtime"
#   https://www.aljazeera.com/news/2026/11/20/fossil-fuel-talks-deadlock-pushes-cop31-climate-summit-into-overtime
COP = {
    "kicker": "Climate  ·  COP31",
    "headline": "UN climate talks go into overtime",
    "body": (
        "Nearly 200 countries deadlock in Antalya, Türkiye, over a draft that "
        "drops every mention of fossil fuels. The EU warns of a “fossil summit”."
    ),
}

# BBC "Trump threatens ban on US firms building AI data centres overseas"
#   https://www.bbc.co.uk/news/articles/cmde1lw9y54ko
# CNBC "Trump vows to stop U.S. companies from building data centers abroad, threatens 'tremendous tax'"
DATACENTRES = {
    "kicker": "US  ·  Technology",
    "headline": "Trump threatens ‘tremendous tax’ on data centres abroad",
    "body": (
        "Back from talks with Xi and Putin, he says US firms won’t be "
        "allowed to build AI data centres overseas."
    ),
}

# BBC "In a year of AI solving maths problems, Anthropic may have just solved the biggest"
#   https://www.bbc.co.uk/news/articles/c6pqr2g7w059o
RIEMANN = {
    "kicker": "Science  ·  Mathematics",
    "headline": "AI-aided proof of Riemann hypothesis claimed",
    "body": (
        "Anthropic mathematician Levent Alpöge says Claude helped. The "
        "250,000-line Lean proof still awaits verification."
    ),
}

# BBC "Denmark accuses Russia of plotting to assassinate US-Ukrainian rapper"
#   https://www.bbc.co.uk/news/articles/cmde1lj4yjxno
# Al Jazeera "Overturned boat carrying mourners to funeral kills at least four in Nigeria"
#   https://www.aljazeera.com/news/2026/11/20/overturned-boat-carrying-mourners-to-funeral-kills-at-least-four-in-nigeria
# BBC video "Cost of living protests sweep across Europe" (20 Nov 2026)
ALSO = [
    "Denmark expels Russia’s defence attaché over alleged plot to kill rapper Kyivstoner",
    "Nigeria: boat taking mourners to a funeral capsizes in Bayelsa, at least 4 dead",
    "Cost-of-living protests across Europe",
]

SOURCES = "Sources: BBC, DW, Al Jazeera, France 24, CNBC reports of 20 November 2026."
