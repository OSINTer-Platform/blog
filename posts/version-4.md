---
title: Version 4.0 just released!
date: 2022-11-17
author: Bertmad
description: A look into the past and future of the project
image: /blog-images/timeline-4.png
---

Version of 4.0 of OSINTer just dropped, and while it on the surface doesn't bring along any major changes, it does bring a lot of structural changes to how the frontend retrieves and handles data. Not only does this optimize some parts significantly, but it also opens the door to further development in fields like machine learning, which will be discussed in greater detail in the following sections.

## The history of OSINTer

![A timeline of the development of OSINTer to version 4.0](/blog-images/timeline-4.png)
_While the following section will describe my thoughts on and the strategy for the future development of OSINTer, it may be subject to change, as new requirements and feature requests are added to the framework and the reader should therefore keep in mind that until a specific feature is implemented and released as a part of the framework, there's currently no guarantees for what future releases of OSINTer might contain._

The development of OSINTer has so far been a wild ride, and the platform has so far moved through a PoC and 4 following major versions. These versions brought along the following changes:

- **OSINTw:** Was the original PoC, which consisted of a simple script for being run locally by the user.
- **OSINTer 1.0:** A complete rewrite of OSINTw, enabling the use of a central server for persistent data storage and archival.
- **OSINTer 2.0:** A radical shift in the way OSINTer stores data, by shifting to using an Elasticsearch DB and thereby also allowing advanced search functionality.
- **OSINTer 3.0:** A modernization of the GUI for OSINTer which moved away from server-side rendering by using a single SPA.
- **OSINTer 4.0:** A lot of minor (but breaking) changes, like improved code quality, a simpler API schema and the possibility for integration with ML pipelines.

---

## The future of OSINTer

Now, as mentioned earlier, this newest version of OSINTer brings along some structural changes, that allows for expansion into some areas that have been determined to be of special interrest for the user base by the core team behind OSINTer. The main one of these which are to be the main focus of the next year of development for OSINTer are as follows:

- **A better ML pipeline:** Version 4.0 of OSINTer has enabled research within the use of SOTA ML models for better handling the large amounts of data collected by OSINTer, something that has so far shown extreme promise. The code for this has so far been kept proprietary to keep the door open to a potential freemium model should other attempts to obtain funding fail, but the results from a rudimentary version of this is already available on the development version of OSINTer, which is behind some of the new useful features at [dev.osinter.dk](https://dev.osinter.dk). To further improve those features, the development of the ML pipelines for OSINTer will play a central role in the general development of OSINTer in the future with the final goal of somehow making the code open-source.
- **A proper visual profile and design:** The truth about the development of the design and visual profile for OSINTer is that - while it has become rather decent over the latest iterations - I'm personally not a designer but instead mainly a developer. This results in a few shortcomings in the current design for OSINTer, like the lack of a proper visual profile with a logo and color scheme, or the fact that the frontend for OSINTer currently scales horribly on a mobile device, and therefore I'm currently looking into pulling in external talent to help with the process of designing the frontend for OSINTer, and this topic will be one of continued focus for the next versions of OSINTer.
- **Better data-visualization:** While the data collection capabilities of OSINTer and the data management capabilities of the associated ML pipeline has gotten quite sophisticated, the framework is still lacking when it comes to ways of visualize this data for the user. As such, there's currently an ongoing effort to come up with some new inovative and effective ways of visualizing the vast amount of information stored by OSINTer in an interactive manner, and like the other two topics, this is likely to justify a new major version once implemented.

As these topics of future development are rather complex, and none of them fall completly within my area of expertise, they are also one of the reasons that I'm currently looking into finding a source of funding for the project. While all of them have shown great promise with regards to at some point getting them to a production ready state, it would have a tremendous positive on the project if there were funds available for allocation to pulling in external talent for these tasks. With all of that said though, they're not the only changes planed for OSINTer.

### The legal direction for OSINTer moving forward

_Please mind that while the following section is a topic that has been thoroughly researched by me and large parts of it fact-checked by a lawyer, I personally am a developer and not a lawyer. Therefore, the following contents do not constitute legal advice, are not intended to be a substitute for legal advice and should not by relied upon as such. This section is merely meant to give an insight into the process behind the shifting licensing of the project, and for that reason, it is strongly recommended to seek legal advice or other professional advice in relation to any particular matters the reader, or the organisation which the reader represents, may have._

As described in the [_About The Project post_](/blog/about-the-project), OSINTer has through the time been under a few different licenses for a variety of reasons, but the current state is that the project is unfortunately unlicensed (and therefore all rights are reserved). We would prefer to change that, and as such, going forward the project will in all likelihood be put under a license which is non-commercial in nature.

In the optimal world we would like to put the project under a strong copy-left license which would actually qualify as open-source, but due the fact that OSINTer having evolved into more of a finished product in of itself, in contrast to many libraries and actual frameworks out there, we believe it would be near impossible to sustain the development of the project under that kind of license. Therefore, were currently looking into licensing the new version 4.0 of OSINTer under version 1.1 of the [MariaDB Buisness Source License](https://mariadb.com/bsl11/) (BSL for short).

BSL is an interresting license for a project like OSINTer for two reasons. First of, instead of prohibiting commercial activity, it simply prohibits use in a production enviroment which oftentimes means that it has the same limitations as a non-commercial license, but with a little more flexibility when it comes to internal testing. Secondly, after 4 years from the release of a specific version under the BSL license, that version will move from the BSL license to an open-source and GPL compatible license of choice from the developer (which in this case will be AGPL v3). This essentially means that buying a commercial license for a software product dual-licensed under the BSL will result in getting to use the software in production while it's still relevant and competitive, but old and outdated versions of that software will also be available for open-source development in a production enviroment by the community.

## The big picture: Building the next generation of CTI tools

Now what we have discussed so far is the concrete roadmap that the development of OSINTer will take in the comming months, but in the long run, we have also planed something which could have the potential to completly change how we work with and handle CTI.

The case at it stands today is that OSINTer is a tool that is really only designed to be used internally in companies, and while it is absolutely possible to allow access to an OSINTer instance for anyone, it really wouldn't make too much sense as it is tool designed specifically for CTI experts. Our proposal aims to change that, by changing OSINTer from a "read only" platform, to a platform where the users would be able to not only get the relevant information from, but also input intelligence collected from other sources and manually correlate different articles. This would transform OSINTer from a sophisticated news feed to the one-stop platform for collecting and distributing cybersecurity news and threat intelligence, allowing CTI personnel to not only work together, organize information and communicate with each other internally but also allowing potential clients direct access to the information.

What we proposed specifically is two changes to the fundamental concepts of how OSINTer works today. The first one is to change articles stored in OSINTer from read-only, to a data-object that can be changed and updated by specific users. This would allow CTI personnel to manually enrich articles after scraping with details like a MITRE ATT&CK mapping, to accompany the already identified IoC's and other information from the article.

The second one is to instead of having articles being the main data-object, create a new data-object that would be manually instantiated and would contain the contain the information related to specific incidents, and then be linked to all articles concerning that specific incident. This would not only create a central place to collect intelligence, avoiding big excel sheets and complicated shared documents, but also potentially allow for monetization of OSINTer, by selling access to this manually collected information. Furthermore, this approach would also allow for representing incidents and sources depicting these incidents on one big timeline, giving an overview of what is happening within cyberspace in a way not really seen before.

![Using incident-based dataobjects](/blog-images/ml-future.gif)

Now, this is something that would require quite a commitment from a company thats used to working with CTI. Not only would I need continuous input on how and what specific features are relevant along for the CTI personnel, but this approach would also require a fair bit of manual work from the CTI personnel at that company to collect and input the needed information for this to be of any value. We do believe that this is more than worth it however, as we believe that this rather novel approach to commercializing a platform like OSINTer might bring a large change in how we collect, organize and share threat intelligence. It is not something that will just be developed overnight, as the functionality needed is rather complex, but it is still absolutely possible to pull of and should this turn out to be something a CTI related company is willing to comit to, it would likely be possible to implement in 6-12 months.
