---
title: The security of OSINTer
date: 2022-11-16
author: Bertmad
description: A walkthrough of the cyber-risks associated with an OSINTer instance, and how we handle those.
---


### Potential concerns

One of the main concerns that has been raised from multiple sources regarding OSINTer, is the security of the platform itself. OSINTer is a product that aims to be useful in an industry where it probably goes without saying that secure infrastructure is an absolute must, and it is for this reason that OSINTer has been built with security in mind. Specifically, when developing OSINTer and working with securing it, there's three areas that could potentially pose a threat that we keep in mind.

1. Leakage of sensitive data in attacks like SQL injections or social engineering.
2. Posing a threat to the infrastructure on which it is hosted, as commonly seen in RCE exploits, directory traversal and LFI.
3. Posing a threat to the infrastructure of the users of the platform, as commonly seen with stored XSS attacks or social engineering.

- - -

### Mitigation

The first challenge to deal with is the prevention of data leakage, and here it's central to recognize that OSINTer is a platform that stores minimal amounts of potentially sensitive data. The closest it comes to sensitive information is a password and username combination (with email being optional during signup), and all of this (except the username) is hashed using the industry standard Argon2id, making password retrieval even after a data leak near impossible. Furthermore these credentials are stored within a database with strong data access policies designed after the principle of least privilege, the frontend is configured with TLS as standard and should data leakage still be a concern, then the parameters for the Argon2id are customizable on an instance-to-instance basis, making cracking a leaked password or email virtually impossible.

- - -

The second challenge we have to tackle is ensuring that OSINTer is vulnerable to attacks that could somehow endanger the infrastructure on which it is hosted, as exemplified by a RCE vulnerability. This is a much more potent threat than the last one, as this has the potential of letting OSINTer act as an initial foothold into an organization for a hostile actor.

As such, this is of course a threat that we take rather seriously, and its something that is constantly taken into consideration when adding, changing or removing features from OSINTer. The only potential entrance for a hostile actor however is the API deployed with OSINTer, as this is the only exposed part of the application that processes untrusted input, and here we use libraries like Pydantic and Starlette along with rigorous data validation to ensure that no dangerous input could lead to unintended consequences. Besides this, it is also my strong recommendation to segment the network properly and isolate the running OSINTer application from the host machine using modern virtualization technologies to cripple the effectiveness of a potential vulnerability.

- - -

The last challenge is unfortunately a little more complicated as isolation of specific pieces of infrastructure isn't a suitable solution when it comes to protect the users of the platform against attacks like XSS attacks. While it would be possible to limit the access to the OSINTer instance to only a local network and thereby nearly eliminating any untrusted input, this isn't really a satisfactory solution to this specific challenge.

Instead, OSINTer aims to eliminate this kind of attacks by (as previously mentioned) rigorously validating any input and use modern Javascript frameworks and techniques for rendering the frontend. Combined with the security of modern browsers along with the only credentials for OSINTer being stored in a HTTPOnly and secure cookies with the Same-Site attribute set instead of localstorage eliminates a whole range of attacks from XSS to CRSF.

