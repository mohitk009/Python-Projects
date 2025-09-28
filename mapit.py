import webbrowser, sys, pyperclip

# Check if command-line args were passed
if len(sys.argv) > 1:
    # Join all args as the address
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

# Open Google Maps with the address
webbrowser.open('https://www.google.com/maps/place/' + address)
