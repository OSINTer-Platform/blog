---
title: About The Project
date: 2023-01-13
author: Bertmad
description: A short description of OSINTer as a project
image: /blog-images/progress-to-5.png
---

## What problem does OSINTer attempt to solve?

The process of gathering cyber threat intelligence is only as successful as the investigators ability to identify relevant intelligence sources. Identifying relevant and reliable sources could often be a time-consuming task, as the CTI personnel would have to first locate the intelligence source, then read it to identify its relevance and usefulness as well as identify its formatting, and finally mark down all relevant details for usage in their report. This is time consuming and can be hit and miss depending on the skill and experience of the CTI personnel, and while products to combat this repetitive and time-consuming task, like Recorded Future, exists, these are often not only expensive, but also closed in nature, as they rarely integrate well with thirdparty utilities.

The goal of OSINTer is to build an open-source and extensible platform for collecting and organizing open-source intelligence in a way that easily intergrates with thirdparty utilities and other pieces of open-source software. As such, it never was (and never will be) intended to compete with products like the aforementioned Recorded Future, since the core concept is very different and since OSINTer does not offer the needed analysis capabilities on its own.

### How does OSINTer Solve the Problem?

Firstly, to combat the time-consuming task of identifying relevant threat intelligence sources, OSINTer gathers information from known, reliable sources, automatically, and then displays these in its webservice interface in a list sorted by publish date. This provides the most current information first, and in a consistent format so that users can easily identify the relevant information sources for their CTI reports or other use cases.

Secondly, the content from the threat intelligence sources is archived and retrievable for the user, through a download functionality in OSINTer, which allows for download Markdown files containing this content, and formattet in a consisten fashion. These files, when imported into any markdown editor (preferably Obsidian), allows the user to analyze on all or parts of the collected information. Obsidian has tools to easily detect correlations between the information, providing a much-needed overview of the collected information.

---

## The current state of OSINTer

![The architecture of OSINTer](/blog-images/osinter-5-arch.png)

_OSINTer is a framework that is under constant and rapid development, and while that is great for the end-user, please keep in mind that, that might also mean that some of the following information is slightly inaccurate._

### The technical breakdown

OSINTer has over the span of it's one and a half year of development evolved into a mamoth of a framework which spans nearly every part of the tech-stack. The following list breaks this down into the 6 different layers composing OSINTer, going from the very backend with topics like deployment and database in mind, to the very frontend used to serve the information to the user in manageable and easily accessible manner:

- **Deployment:** For the process of preparing the host and deploying OSINTer (a process which is unfortunately far from trivial) Ansible is utilized. Ansible has been the framework of choice for deploying OSINTer since version 1.0, as it's wide support and reliability has made it an industry standard.
- **Database:** The current version of OSINTer has moved on from the initial solution of using a rudimentary setup for handling and indexing the collected data using a combination of an PostgresSQL DB and files on the disk, to using an Elasticsearch DB for the collected data and the Apache CouchDB for user-management.
- **Data-collection backend:** The backend written to collect the relevant news-information which drives OSINTer was written in Python. Most of the heavy-lifting is however done by the Selenium framework used for webscraping in combination with a series of custom Javascript programs written for manipulating and filtering the data before it was processed by the main Python-based engine. Furthermore, a custom DSL was created for this backend called "profiles" which was used for defining where OSINTer would locate the relevant information.
- **Machine-learning:** OSINTer currently uses a proprietary machine learning pipeline to better handle and organize the large information, which is based on a couple of SOTA deep learning models for everything from dimension reduction to data clustering. While it is a strong personal ambition of mine to open-source this along with (hopefully) the rest of the project at some point, it is currently being kept proprietary until a reliable and adequate source of funding for the project has been secured.
- **API:** To make all of the information stored by OSINTer easily available in a secure and scaleable manner, a simple REST API written in the FastAPI framework for Python is provided and deployed with the project. This not only provides a layer of abstraction upon the OSINTer internals, but also allows for user authentication using CouchDB for user management, the Argon2 hashing algorithm for storing sensitive information (passwords and emails) and JWT in HTTP-only and secure cookies with the same-site attribute set to strict. This API is also what is used by the frontend to retrieve data from OSINTer.
- **Frontend:** The frontend for OSINTer is a transitional MPA written using SvelteKit, Tailwind and plain HTML, which simplifies the workflow of the developer and allows OSINTer to ship nothing but HTML, CSS and old-fashioned Javascript to the client.

---

### The legal status

_Please mind that while the following section is a topic that has been thoroughly researched by me and large parts of it fact-checked by a lawyer, I personally am a developer and not a lawyer. Therefore, the following contents do not constitute legal advice, are not intended to be a substitute for legal advice and should not by relied upon as such. This section is merely meant to give an insight into the process behind the shifting licensing of the project, and for that reason, it is strongly recommended to seek legal advice or other professional advice in relation to any particular matters the reader, or the organisation which the reader represents, may have._

Due to the complicated nature of IP rights and the accompanying legislation, the legal state of software projects are something that the owner of the IP rights for a given project should be attentive of. This is especially true when it comes to open-source projects, as the source-available aspect of these often can result in unintended consequences for the developer, the user or possibly both if not handled with care, which is the reason for the rather complicated history of licensing for OSINTer.

The original OSINTw project was licensed under the GNU GPL v3 license, due to reasons tied directly to my personal beliefs. When creating software where a strong financial goal doesn't stand in the way of open-sourcing the project, I'm personally of the strong belief that open-source development using strong copy-left licenses like the GNU GPL will result in work from the developer and potential contributors which creates the greatest benefit for the general community, and as such OSINTw was created using this very model. When OSINTer 1.0 came along, and the project evolved into using a central server, I then moved it from the GPL to the AGPL v3 license, as this is much more targeted towards software designed to run on servers, but the general idea behind the license persisted. This happened once again with the move to SSPL on OSINTer 2.0, and while this technically isn't an open-source license, the general idea behind the license once again persisted with the SSPL license being much the same as the AGPL.

Unfortunately, locating financial support for the project proved to be harder than expected and after I finished the danish STX education, I realized that the development of OSINTer simply could not go on without funding from some source. Therefore, I removed the license from the current and all future releases of the project in the hopes that this move would encourage some of the industry leaders using OSINTer to contribute to the project financially. This means that while the current source code for OSINTer is completely available online, all rights are reserved, and it is therefore not actually possible for anyone but the owner of the project to use, modify or distribute the project for any purpose. This is something I would very much like to change in the future, but until a more sustainable way of developing OSINTer has been located, this is unfortunately the way things has to be.
