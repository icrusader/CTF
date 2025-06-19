# ✈️ Where Did I Go?: An OSINT Luggage Tag Adventure!

The Where Did I Go? challenge was a super cool OSINT (Open-Source Intelligence) puzzle. We were given an image of a luggage tag, and the goal was to follow the trail of digital breadcrumbs to figure out the flight details.

## 🕵️he Investigation: Step-by-Step

### Step 1️⃣: Scan That Barcode!!

The first and most obvious clue was the barcode on the luggage tag. I used an online barcode scanner to see what information it held. The scanner spit out a number: `6006015722`.

### Step 2️⃣: Cracking the Airline Codee💻

Just having a long number wasn't enough, so I Googled "how to read luggage tag" to understand what the different parts of the number meant. I found this awesome website that broke it all down:

[How Baggage Tags Work](https://www.security-label.de/en-gb/inspiration/how-baggage-tags-work)

From that article, I learned that the three digits follow the first single digit of the baggage tag number (`006`) represent the airline's unique IATA code. A quick search for "airline code 006" confirmed it: this was a Delta Air Lines bag!

### Step 3️⃣: The Baggage Claim Hunt 🛄

With the airline identified, I headed over to the Delta Air Lines website and found their luggage tracking page. The page required a baggage tag number and the passenger's last name:
- We have tag numbers already.
- As for the customer last name, quick search of the challenge creator give out his last name `Elliots`   

I plugged all the information to delta tracking luggage page. Just like that I would have the flight number, the IATA code of destination and arrival. At the time of writting this, the page no longer give out the information so I can't have the screenshot. 

## ✅ Conclusion

This challenge was a fantastic real-world OSINT scenario! It showed how a tiny piece of information, like a barcode on a luggage tag, can be unraveled with a few smart searches to reveal a ton of information. It's a great reminder to always be curious and dig into the data you're given!

