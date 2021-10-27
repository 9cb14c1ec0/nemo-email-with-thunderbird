# Introduction

This nemo action script adds an "Email with Thunderbird" item to the context menu in the nemo file manager.

# Installation

To install, copy the `email_with_thunderbird.nemo_action` and `email_with_thunderbird.py` to the `~\.local/share/nemo/actions` folder on your computer.

# Customization

You can customize both the binary location and your thunderbird profile location.  To get started, navigate to your home directory, adjust display settings to show hidden files, and then open the `.config` folder.  In the `.config` folder, create a new folder named `nemo-email-with-thunderbird`.  Open the `nemo-email-with-thunderbird` folder.  To customize the thunderbird binary path, create a file named `thunderbird_path.txt` and enter the binary as the only line in the text file.  Similarly, you can customize the thunderbird profile path by creating a file named `profile.txt` and entering the profile there.
