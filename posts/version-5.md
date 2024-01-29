---
title: Version 5.0 has finally arrived!
date: 2023-07-05
author: Bertmad
description: Getting OSINTer production-ready
---

After more than half a year of development, version 5.0 has finally passed the last development and testing phases, and is - at the time of writing - being released. If you, over the last year, has gotten used to the v4.0 interface you will find that although many of the core principles have stayed, the visual profile and design has gotten a complete overhaul along with a modernization of many core parts of OSINTer. This is done in an effort to ensure that the framework is truly production-ready, which means that we have been working hard to update and rework much of the OSINTer internals so that they're built by and kept up to high standards.

## The technical changes

![An overview of the version 5.0 architechture](/blog-images/osinter-5-arch.png)
Version 5.0 for OSINTer has brought along changes to the following areas:

- **Visual profile and design:** The GUI for OSINTer has gotten a major update. Besides the new look and logo, this includes features like dark-mode and proper scalability (horray for actual mobile-usability!)
- **Frontend**: Too assist the changes in both visual and data-visualization departments the inner workings of the frontend has been updated. Instead of building the GUI as a SPA using Svelte, OSINTer has been moved to SvelteKit (along with Tailwind for the visual part) to bring the end-user a client-hydrated SSR app with proper routing.
- **Backend**: To fit the more sophisticated frontend (and much larger peak-loads) the backend has too gotten an overhaul, updating the REST API endpoints and utilizing a separate databse (CouchDB) for user management, ensuring both a performant and reliable backend.

These changes have not only enabled OSINTer to scale in a true production-ready manner, but the more robust and flexible frontend do also enable us (the core team behind OSINTer) to utilize and implement a lot of new and exciting technologies to further simplify and automating the task of collecting and analyzing intelligence.

## Looking forward

We did already discuss much of the future for OSINTer [when version 4.0 released](/blog/version-4), and while much of that (like the unfortunate situation surrounding the licensing) is unchanged, getting version 5.0 of the roadmap and into the real world has given space for drawing up concrete plans for many of the much of the roadmap proposed in the v4.0 post. As 5.0 has more or less addressed the concerns raised there about the visual design and profile, version 6.0 will mostly focus on how we can use ML to augment and condense data using the following techniques:

- **Clustering:** Techniques like the Uniform Manifold Approximation and Projection are used for dimension reduction of data, and in conjunction with data-clustering algorithms they might prove useful to group related content.
- **Summarization:** Condensing information stored in text-form by abstractive summarization has long been a common but challenging task for Large Language Models (LLMs) but with the explosion of sophisticated LLMs following the GPT family from OpenAI LLMs might finally be applicable for use in a production context.
- **Filtering:** Advanced recommendation engines have for the last decade been the heart of modern social media along with a whole host of other platforms, and applying this technology to threat intelligence data might very well prove to be a significant time-saver.

Much of what is described here (especially applying a user-specific recommendation algorithm to the data held by OSINTer) is still in the very early phases of planing, but it is worth mentioning that specifically using existing techniques for clustering data has already been tested in the context of OSINTer and the data held within, and features such as "Articles like this one:" and clustering articles around specific topics are close to making their way into the testing versions of OSINTer.
