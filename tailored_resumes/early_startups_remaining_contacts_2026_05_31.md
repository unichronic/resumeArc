# Early Startup Remaining Outreach Contacts

Scope: rows 11-27 of `early_startups_vibrium_onwards_2026-05-30.csv`.

Verification labels:
- Prospeo verified: Prospeo matched the person and revealed a verified professional email.
- Reoon safe: SMTP deliverable, non-catch-all, safe to send.
- Official fallback: email is published by the company, but not a founder mailbox.
- Catch-all/unknown: domain accepts broad mail or SMTP could not confirm the exact inbox.
- No usable email: tested or searched routes were not good enough to put directly in Apps Script.

| Row | Company | Founders / target people checked | Best contact(s) | Verification | Script recipient |
| --- | --- | --- | --- | --- | --- |
| 11 | Emergent | Madhav Jha, Mukund Jha | `mukund@emergent.sh`; `support@emergent.sh` | `mukund@emergent.sh` was Reoon safe. `support@emergent.sh` is a public company fallback. Prospeo found a masked verified Madhav address but it was not revealed. | `mukund@emergent.sh` |
| 12 | Vimag Labs | Manish Seth, Piyush Desai | No usable email found | `vimaglabs.com` has no MX. `manish@vimaglabs.com`, `piyush@vimaglabs.com`, and `hello@vimaglabs.com` were invalid/no-MX. Prospeo found no match. | blank |
| 13 | Dazzl | Komal Solanki, Ashish Bajpai | `care@dazzlnow.com` | Official contact page email. Domain has Google MX. Prospeo found no founder match. | `care@dazzlnow.com` |
| 14 | Escape Plan | Abhinav Pathak, Abhinav Zutshi | `abhinav@myescplan.com` | Prospeo SMTP verified. It returned the same mailbox for both Abhinav Pathak and Abhinav Zutshi matches, so use as a shared founder route. | `abhinav@myescplan.com` |
| 15 | Peeko | Chetan Sharma, Vivek Khetan, Abhijit Gairola | `chetan.sharma@peekonow.com`; `vivek.khetan@peekonow.com`; masked verified Abhijit email | Prospeo SMTP verified Chetan and Vivek. Prospeo search showed a masked verified Abhijit address but it was not revealed. | `chetan.sharma@peekonow.com` |
| 16 | PB Healthcare | Yashish Dahiya | No usable startup email found | Prospeo found no match for PB Healthcare/PB Fintech routes. Public sources confirm Yashish Dahiya as founder, but no direct company/founder email was found. | blank |
| 17 | CHINI KUM | Priyank Jain | `priyank@drinkchinikum.com`; `care@drinkchinikum.com` | Official about page publishes Priyank's founder contact and the care mailbox. Domain has Google MX. | `priyank@drinkchinikum.com` |
| 18 | CosMoss | Mohammad Jueitem | No usable email found | `shopcosmoss.com` has no MX. `mohammad@shopcosmoss.com`, `hello@shopcosmoss.com`, and `care@shopcosmoss.com` were invalid/no-MX. | blank |
| 19 | Filli & Me | Shikha Pahwa | `shikha@filliandme.com`; `hello@filliandme.com` | Prospeo SMTP verified Shikha's founder email. `hello@filliandme.com` is official fallback. | `shikha@filliandme.com` |
| 20 | HandyPanda | Abhishek Rao, Shaurya Goel, Shaurya Jindal | `contact@handypanda.in` | Official contact page email. Founder first-name guesses tested invalid, and `hello@handypanda.in` was disabled. Prospeo found no match. | `contact@handypanda.in` |
| 21 | Nester | Abhinav Singh | `support@nesterstore.com` | Official contact page email. `nesterstore.com` has Google MX. `.in` guesses were invalid/no-MX. | `support@nesterstore.com` |
| 22 | OZi | Amit Sah | `amit@ozi.in` | Prospeo SMTP verified Amit Sah. | `amit@ozi.in` |
| 23 | RARA Barefoot | Varun Mimani, Manas Tripathi | `care@rarabarefoot.in`; `care@rarabarefoot.com` | Official India contact page publishes `.in`; Crunchbase/terms pages also show `.com`. Use `.in` for India outreach. | `care@rarabarefoot.in` |
| 24 | Rotoris | Aakash Anand, Prerna Gupta | `support@rotoris.com`; tested `aakash@rotoris.com`, `prerna@rotoris.com`, `hello@rotoris.com` | Official contact page publishes support mailbox. Reoon returned unknown for founder/hello guesses, not safe. | `support@rotoris.com` |
| 25 | Tvissa | Mrinal Narain, Shrishti Agarwal | `customer.happiness@tvissa.com`; tested `mrinal@tvissa.com` | Official story/contact page publishes customer mailbox and founders. `mrinal@tvissa.com` was unknown, not safe. | `customer.happiness@tvissa.com` |
| 26 | Unbound | Kanika Mittal, Atul Arora | `hi@unbound-lifestyle.com` | Official about page publishes founders and contact email. Domain has Google MX. | `hi@unbound-lifestyle.com` |
| 27 | For Real | Anurag Sheth, Mohit Sheth | `anurag@for-real.in`; `support@for-real.com` | Public For Real/Velenca contact page publishes Anurag's email. Reoon returned catch-all/deliverable but not safe; official page makes it usable. Storefront support email is a company fallback. | `anurag@for-real.in` |

## Apps Script Notes

Updated `tailored_resumes/early_startups_all_gmail_drafts_2026_05_31.gs` with the script recipients above. Vimag Labs, PB Healthcare, and CosMoss remain blank intentionally because I did not find a usable deliverable email route.

## Source URLs Used

- Emergent: https://emergent.sh ; https://www.ycombinator.com/companies/emergent ; https://www.crunchbase.com/organization/emergent-02ef ; https://www.business-standard.com/companies/start-ups/emergent-ceo-mukund-jha-emergent-went-from-zero-to-usd-50-million-7-months-126020401195_1.html
- Vimag Labs: https://vimaglabs.com/ ; https://www.linkedin.com/company/vimag-labs
- Dazzl: https://dazzlnow.com/contact-us ; https://dazzlnow.com
- Escape Plan: https://myescplan.com/pages/team ; https://myescplan.com
- Peeko: https://peekonow.com ; https://www.stellarisvp.com/portfolio/peeko ; https://app.dealroom.co/companies/peeko
- PB Healthcare: https://inc42.com/company/pb-healthcare/ ; https://www.gaebler.com/Funded-Company-446715B0-F469-4B5F-A0C7-AFE525547F5C-PB-Healthcare ; https://thekredible.com/company/pb-healthcare/people
- CHINI KUM: https://drinkchinikum.com/pages/about-us ; https://www.linkedin.com/company/chini-kum-guilt-free-drinks
- CosMoss: https://shopcosmoss.com/ ; https://www.linkedin.com/company/cosmoss-india ; https://inc42.com/company/cosmoss/
- Filli & Me: https://www.filliandme.com/policies/contact-information ; https://in.linkedin.com/company/filliandme
- HandyPanda: https://www.handypanda.in/contact ; https://www.ajuniorvc.com/portfolio-companies/handy-panda ; https://www.ynos.in/startup/handypanda-620492
- Nester: https://nesterstore.com/pages/contact ; https://inc42.com/company/nester/
- OZi: https://ozi.in ; https://www.linkedin.com/company/ozi/
- RARA Barefoot: https://www.rarabarefoot.in/pages/about-us ; https://www.rarabarefoot.in/pages/how-can-we-help ; https://www.ipoplatform.com/startup-business-funding/ap2gp-private-limited/100913
- Rotoris: https://www.rotoris.com/contact ; https://inc42.com/company/rotoris/ ; https://thehourmarkers.com/articles/rotoris-interview-with-founders
- Tvissa: https://tvissa.com/pages/tvissas-story-vision
- Unbound: https://unbound-lifestyle.com/pages/about-us ; https://app.dealroom.co/companies/unbound_lifestyle
- For Real: https://in.linkedin.com/company/forreall ; https://www.for-real.in ; https://outlet.for-real.in ; https://velenca.com/
