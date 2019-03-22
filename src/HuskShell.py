
def toLowerCase(sen):
    mod_sen = ""
    mode_lower = True
    char = ""
    for letter in sen:
        if letter in ["'", '"']:
            if mode_lower:
                char = letter
                mode_lower = False
            else:
                if letter == char:
                    char = ""
                    mode_letter = True

        if mode_lower: mod_sen += letter.lower()
        else: mod_sen += letter


def HuskCmd(cmd):
    cmd = toLowerCase(cmd)
    # perform checks here
