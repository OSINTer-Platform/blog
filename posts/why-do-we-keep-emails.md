---
title: Why (and how) do we handle email addresses?
date: 2022-08-01
author: Bertie
description: And explanation on how we store email addresses and why you would want to supply your's during signup.
---

**_TL;DR:_** We store your email using the same strong hashing algorithm as we
use for your password, and only uses it for account recovery.

---

### Why most websites require emails (and why we don't)

As you have probably noticed most modern websites that offers some kind of user authentication, requires you to enter your email address and verify it during the signup phase. The reasons for this can range from needing to identify users individually to limiting spam, but often times it boils down to one thing: verified emails are worth a lot more to advertisers.

But at OSINTer we don't need any of these. We neither have no need to identify users, nor do we sell your data, and furthermore we also recognize that a lot of our users not only strongly dislike spam in their inbox, but also would prefer to stay anonymous by not giving up any personally identifying information. Therefore email is an optional field during signup.

Because, instead of the aforementioned uses for verified email addresses, we use your email for a single purpose: account recovery should you forget your password. It often happens that people forget/losses their passwords, and unfortunately the only practical way for us to verify that you actually own an account when you're not able to provide the password is by using your email address. Do hovewer rest assured that if you choose to supply your email during signup, so that you have the option of account recovery later, we will never send you any kind of spam, we won't sell your information and due to the technical configuration of OSINTer, we don't even have access to your email.

---

### How do we handle your email?

After nearly a decade of data-leaks as a result of cyber-attacks, most of the modern websites have finally gotten a fairly solid grip on password-security. A plethora of mature and secure hashing algorithms with modern libraries implemented in nearly every widely adopted programming language, have certainly made the task of protecting passwords a lot more straighforward, but most websites out there still doesn't consider data like email addresses sensitive data, which is why they are often stored in plain-text, and therefore an easy target, should the website get hacked, and the database leaked.

But at OSINTer we (again) recognize that a lot of the users might not want their email leaked for a variety of reasons, and therefore we protect the email addresses supplied to us during signup with the same industry-standard Argon2 hashing algorithm used for password storage. Not only does this make it impossible for us to send you spam (as we don't even know your email address), but you can also rest assured, that even in the unlikely event that our database gets leaked, your email will (probably) still be safe.
