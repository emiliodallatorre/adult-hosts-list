# Adult hosts list

This is a list of adult websites which you could eventually use to configure DNS filters or other tipe of blocking appliances on a connection level (or do anything you want with it).

The original list comes from [a Reddit post](https://www.reddit.com/r/NoFap/comments/6cplet/updated_may_2017_host_file_to_block_10848_porn/) I saw some time ago.

I am not the author of this list and I do not own any kind of right on this list.

## How to add it to Pi-Hole

In Pi-Hole V5 you can simply add this blocklist by accessing the ***Admin GUI > Group Management > Adlists*** and pasting the link of the raw list: https://raw.githubusercontent.com/emiliodallatorre/adult-hosts-list/main/list.txt.

After you are done adding the list, you have to update gravity using either the `pihole -g` command from the CLI, or ***Admin GUI > Tools > Update Gravity***.
