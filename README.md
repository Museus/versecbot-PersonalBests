# VerSecBot - Personal Bests

This plugin instructs VerSecBot to react to Personal Bests in the configured channel and optionally create a thread.

To use it, install the package and add the following block to your configuration, replacing values in <> with your desired values:

```
    [versecbot.plugins.personal_bests]
        enabled = true

    [[versecbot.plugins.personal_bests.handlers]]
        enabled = true
        channel_ids = [<channel ID>, ...]
        emoji_id = <emoji ID>
        create_thread = <true|false>
```
