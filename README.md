# Inbox for [Todoist](https://en.todoist.com/tour) #
## An Übersicht widget for your Todoist Inbox ##
---
## About ##
Inbox for [Todoist](https://en.todoist.com/tour) is a simple Übersicht widget designed to present your todoist inbox on your Desktop. It is in no way affiliated with the Brand Todoist or Doist in any way nor is it addiliated with [Übersicht](http://tracesof.net/uebersicht/) or [Felix Hageloh](https://github.com/felixhageloh)


Below is a preview of what Inbox for Todoist can look like:
![Screenshot](Screenshot.jpg)

## Installation ##
Clone this repository to your Übersicht folder:
`~/Library/Application Support/Übersicht/widgets/``

### Setting up your own Todoist Token ###
On the second line of the `todoistinbox.py` file, replace
`___YOUR TODOIST TOKEN HERE:___` (keep the ' ' for it to work) with your very own todoist API token.


You todoist token can be found on [Todoist](https://todoist.com) inside of `settings` and then `Integrations`. It will be labelled as `API Token`.

## Preferences ##
### Refresh Rate ###
By default, Inbox for Todoist refreshes every second. To reduce CPU & Memory Usage, you may go to line 5 of `index.coffee` and adjust this:
-   Removing the first `#` will make the widget refresh every `minute`.
-   Removing the second `#` will make the widget refresh every `5 minutes`.
-   Removing the third `#` will make the widget refresh every `10 minutes`.
-   Removing the fourth `#` will make the widget refresh every `20 minutes`.
-   Removing the fifth `#` will make the widget refresh every `hour`.
-   Removing the sixth `#` will make the widget refresh every `12 hours`.

## Possible Eventual Improvements ##
-   Priority Color coding
-   Due Date Sorting
-   Todoist Markdown Support
