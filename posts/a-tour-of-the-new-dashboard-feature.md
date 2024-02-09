---
title: A tour of the new dashboard feature!
date: 2024-02-09
author: David
description: A post to show off the new exciting dashboad feature!
---

## A quick tour of the dashboard!

![Dashboard](/blog-images/dashboard-jan24.png)

As we have previously posted, the dashboard has been a feature that Bertram and David have been working on together for the last few years. Bertram did most of the heavy lifting with the development work, with David providing the vision and knowledge of the industry to ensure the right data was included.

You would think displaying the data in such a way would be straight forward, but it has taken a long time to get the data setup correctly ready to be displayed in such a cool way with the dashboard feature.

But I hear you ask, "how do we use this and get the most out of it?". As with a number of the features in OSINTer, the dashboard is in beta mode. So it is likely to change slightly over the next period, but that doesn't mean we are going to leave you in the dark over how to use it!

## Common CVE's

![CVEs1](/blog-images/dashboard-common-cves1.png)

This one is probably one of the most requested items we have had so far from our 30000 large monthly user base. Something that looks so simple, but took a lot of hard work.

This section of the dashboard tracks the most recent mentioned CVE's in our article database. It is ordered based on how often the CVE's are mentioned. From here you can click on the specific CVE of interest and it will bring up the articles where this CVE is mentioned. This can be incredibly valuable if you have knowledge that your infrastructure is vulnerable to a specific CVE and you want to know about recent attacks or recent blog posts where that CVE is mentioned.

We have used it a lot ourselves when consulting with companies and helping them understand how severe is a CVE, where we can include not just the CVSS score but real open source intelligence.

![CVEs2](/blog-images/dashboard-common-cves2.png)

From here you can then look at the articles and understand much more about the attacks featuring the specific CVE.

## Emmerging topics

![Emmerging1](/blog-images/dashboard-emerging-topics1.png)

This section does exactly what it says on the tin. Since we track all incoming articles and cluster them based on our ML models. We are then able to display the most recently talked about subjects. This could include news about new CVE's, or recent cyber attacks. This section is really exciting as it is based on OSINTer's own engine creating the clustering. Definitely worth keeping an eye on to track subjects as they hit breaking news.

You can interact with the subjects and it will then bring up all of the articles associated with that subject.

![Emmerging2](/blog-images/dashboard-emerging-topics2.png)

## Common article tags - Word cloud

With the word cloud, what you see first is a visual representation of all of the articles within OSINTer. The word cloud has taken all 3500+ articles and displays the most prevalent words within those articles. To date Ransomware is the most talked about term and so this is the biggest word in the cloud.

![Wordcloud1](/blog-images/dashboard-wordcloud1.png)

You can interact with the word cloud, when you select a word by clicking on it. It will be added to the "tag" field and it will then filter the cloud to include all words associated with that "tag". So in this instance, I clicked on the Ransomware word.

![Wordcloud2](/blog-images/dashboard-wordcloud2.png)

It then filtered based on the tag, and I am given a new word cloud which shows all of the terms associated with Ransomware. You can see that the number of articles has also reduced from 35000 to now 4400+ articles. You can further interact with the words and it will continue to filter down to the next results. For example next I will click on Lockbit.

![Wordcloud3](/blog-images/dashboard-wordcloud3.png)

This then shows me all of the terms associated with both "Ransomware" and "Lockbit". I could keep filtering and it will further shrink the word cloud. Again I will now click on "Mandiant" as this could be interesting.

![Wordcloud4](/blog-images/dashboard-wordcloud4.png)

Now I get a much stripped down word cloud which only includes 5+ articles, but this could prove to be very useful as it names a number of malware variants and threat actor names like "Unc2165".

When I am down filtering, I can simply click on the "X"'s next to the tags in the top left of the cloud. This will then remove the terms, and with all the tags removed it will return to the original word cloud. Ready to be filtered again based on your wishes of tags.
