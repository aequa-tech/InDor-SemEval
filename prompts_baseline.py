# Task A: detect the span of text that triggers the problematic content
# Task A1: explain the reason of its problematic nature

#zero-shot prompting 
baseline_zero_A = (
    lambda instance: f"""
Identify the portions of text (Span) that misrepresent events and persons involved in the news (Extract of News). 
If no spans are found, write "No". If more than one span if found, separate them with a comma.

- Extract from News: {instance}
- Spans: 
""".strip()
)

baseline_zero_A1 = (
    lambda instance, spans: f"""
Explain why the portions of text (Span) misrepresent events and persons involved in the news (Extract of News).

- Extract from News: {instance}
- Spans: {spans}
- Explanation: 
""".strip()
)

#few-shot prompting Task-A and Task-A1
baseline_few_A = (
    lambda instance: f"""
Looking at the examples below, identify the portions of text (Span) that misrepresent events and persons involved in the news (Extract of News). 
If no spans are found, write "No". If more than one span if found, separate them with a comma.

- Extract from News: TITLE: Watchdogs Slam President’s Perez Power Play SENTENCE 1: "While the politicization of federal agencies is running critique of the Obama administration, the Justice Department is the one agency that should remain above the fray of politics, and Perez has demonstrated that he is incapable of serving as a neutral arbiter of the law. SENTENCE 2: If Perez is allowed to operate the Department of Justice the way he has run the Labor Department, he will consistently put the priorities of the president’s key political backers ahead of the rights of regular Americans, he said. SENTENCE 3: Perez played a part in one of the first controversies that ensnared Holder when the Civil Rights division dropped voter intimidation charges against two members of the New Black Panther Party who brandished weapons outside of a Philadelphia polling place in 2008.
- Spans: Slam, Power Play

- Extract from News: TITLE: State parks seek input to enhance Gulf State Park Pier fishing experience. SENTENCE 1: Everyone from avid fishermen to occasional anglers is encouraged to take the survey so that Alabama State Parks can better provide a quality fishing experience at the state’s only public pier on the Gulf. SENTENCE 2: The data collected through this survey will help us accomplish that goal and assist us in meeting the needs of our park visitors.” The current Gulf State Park Pier was opened in 2009 after the original pier was destroyed by Hurricane Ivan. SENTENCE 3: In an effort to continually provide quality outdoor experiences, Alabama State Parks is launching an online survey to learn more about the experiences of anglers who utilize the pier.
- Spans: No

- Extract from News: {instance}
- Spans:
""".strip()
)

baseline_few_A1 = (
    lambda instance, spans: f"""
Looking at the example below, explain why the portions of text (Span) misrepresent events and persons involved in the news (Extract of News). 

- Extract from News: TITLE: Watchdogs Slam President’s Perez Power Play SENTENCE 1: "While the politicization of federal agencies is running critique of the Obama administration, the Justice Department is the one agency that should remain above the fray of politics, and Perez has demonstrated that he is incapable of serving as a neutral arbiter of the law. SENTENCE 2: If Perez is allowed to operate the Department of Justice the way he has run the Labor Department, he will consistently put the priorities of the president’s key political backers ahead of the rights of regular Americans, he said. SENTENCE 3: Perez played a part in one of the first controversies that ensnared Holder when the Civil Rights division dropped voter intimidation charges against two members of the New Black Panther Party who brandished weapons outside of a Philadelphia polling place in 2008.
- Spans: Slam, Power Play
- Explanation: Slam is emotive language, Describing actions as a "Power Play" is biased against the person, implying the only reason they did something if to gain more power

- Extract from News: {instance}
- Spans: {spans}
- Explanation:
""".strip()
)
