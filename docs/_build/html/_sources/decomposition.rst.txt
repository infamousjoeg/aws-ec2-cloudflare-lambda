#############
Decomposition
#############

Coming into this phase, I already knew I was doing something that took _way_ too long and  _way_ too many times 
repeatedly.  Immediately, that triggered my "Automation Senses" -- like Spidey Senses... but less cool... and not 
surprisingly dorkier.

Easily repeatable processes are the 🏅 **GOLDEN RULE 🏅** when it comes to easy automation.  All that was left was 
decomposing that easily repeatable process:

**🔁 My Easily Repeatable Process**

* When I start an AWS EC2 Instance, I do the following:
  * Copy the EC2 Instance's public IPv4 address to my clipboard.
  * Browse to <https://cloudflare.com>.
  * Login to my Cloudflare account.
  * Select `cybr.rocks` from the list of domains managed.
  * Select the IP address value of the A record named `cdemo.cybr.rocks` and update it with the public IPv4 address on my 
clipboard.
